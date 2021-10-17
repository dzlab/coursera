# Lab: Optimizing your BigQuery Queries for Performance

## Overview
Performance tuning of BigQuery is usually carried out because we wish to reduce query execution times or cost. In this lab, we will look at a number of performance optimizations that might work for your use case. Performance tuning should be carried out only at the end of the development stage, and only if it is observed that typical queries take too long. It is far better to have flexible table schemas and elegant, readable, and maintainable queries than to obfuscate table layouts and queries in search of a tiny bit of performance. However, there will be instances where you do need to improve the performance of your queries, perhaps because they are carried out so often that small improvements are meaningful. Another aspect is that knowledge of performance tradeoffs can help you in deciding between alternative designs.

## Objectives
In this lab, you learn about the following techniques for reducing BigQuery execution times and costs:

- Minimizing I/O
- Caching results of previous queries
- Performing efficient joins
- Avoid over-whelming single workers
- Using approximate aggregation functions

## Minimize I/O
A query that computes the sum of three columns will be slower than a query that computes the sum of two columns, but most of the performance difference will be due to reading more data, not the extra addition. Therefore, a query that computes the mean of a column will be nearly as fast as a query whose aggregation method is to compute the variance of the data (even though computing variance requires BigQuery to keep track of both the sum and the sum of the squares) because most of the overhead of simple queries is caused by I/O, not by computation.

### Be purposeful in SELECT
Because BigQuery uses columnar file formats, the fewer the columns that are read in a SELECT, the less the amount of data that needs to be read. In particular, doing a SELECT * reads every column of every row in the table, making it quite slow and expensive. The exception is when you use a SELECT * in a subquery, then only reference a few fields in an outer query; the BigQuery optimizer will be smart enough to only read the columns that are absolutely required.

1. Execute the following query in the [BigQuery EDITOR window](https://console.cloud.google.com/bigquery):
```
SELECT
  bike_id,
  duration
FROM
  `bigquery-public-data`.london_bicycles.cycle_hire
ORDER BY
  duration DESC
LIMIT
  1
```
In the **Query results** window notice that the query completed in ~1.2s and processed ~372MB of data.

2. Execute the following query in the BigQuery EDITOR window:
```
SELECT
  *
FROM
  `bigquery-public-data`.london_bicycles.cycle_hire
ORDER BY
  duration DESC
LIMIT
  1
```
In the **Query results** window notice that this query completed in ~4.5s and consumed ~2.6GB of data. Much longer!

If you require nearly all the columns in a table, consider using `SELECT * EXCEPT` so as to not read the ones you don’t require.

> BigQuery will cache query results to speed up repeat queries. Turn off this cache to see actual query processing performance by clicking **More -> Query settings** and un-checking **Use cached results**

### Reduce data being read
When tuning a query, it is important to start with the data that is being read and consider whether it is possible to reduce this. Suppose we wish to find the typical duration of the most common one-way rentals.

1. Execute the following query into the BigQuery editor window:
```sql
SELECT
  MIN(start_station_name) AS start_station_name,
  MIN(end_station_name) AS end_station_name,
  APPROX_QUANTILES(duration, 10)[OFFSET (5)] AS typical_duration,
  COUNT(duration) AS num_trips
FROM
  `bigquery-public-data`.london_bicycles.cycle_hire
WHERE
  start_station_id != end_station_id
GROUP BY
  start_station_id,
  end_station_id
ORDER BY
  num_trips DESC
LIMIT
  10
```

The output of your query should look similar to the following:

![image](https://user-images.githubusercontent.com/1645304/137640889-ad399348-5dfe-4ded-a993-594e477dd4b0.png)

2. Click on the **Execution details** tab of the **Query results** window.

![image](https://user-images.githubusercontent.com/1645304/137640901-5aa13abb-96ad-423f-bf7c-e095e8476a6d.png)

The details of the query indicate that the sorting (for the approximate quantiles for every station pair) required a repartition of the outputs of the input stage but most of the time is spent during computation.

3. We can reduce the I/O overhead of the query if we do the filtering and grouping using the station name rather than the station id since we will need to read fewer columns. Execute the following query:
```sql
SELECT
  start_station_name,
  end_station_name,
  APPROX_QUANTILES(duration, 10)[OFFSET(5)] AS typical_duration,
  COUNT(duration) AS num_trips
FROM
  `bigquery-public-data`.london_bicycles.cycle_hire
WHERE
  start_station_name != end_station_name
GROUP BY
  start_station_name,
  end_station_name
ORDER BY
  num_trips DESC
LIMIT
  10
```
The above query avoids the need to read the two id columns and finishes in 10.8 seconds. This speedup is caused by the downstream effects of reading less data.

![image](https://user-images.githubusercontent.com/1645304/137640946-50bfb1a9-20e0-4d5d-bbfb-3fc93ec26a36.png)

The query result remains the same since there is a 1:1 relationship between the station name and the station id.

### Reduce number of expensive computations
Suppose we wish to find the total distance traveled by each bicycle in our dataset.

1. A naive way to do this would be to find the distance traveled in each trip undertaken by each bicycle and sum them up:
```sql
WITH
  trip_distance AS (
SELECT
  bike_id,
  ST_Distance(ST_GeogPoint(s.longitude,
      s.latitude),
    ST_GeogPoint(e.longitude,
      e.latitude)) AS distance
FROM
  `bigquery-public-data`.london_bicycles.cycle_hire,
  `bigquery-public-data`.london_bicycles.cycle_stations s,
  `bigquery-public-data`.london_bicycles.cycle_stations e
WHERE
  start_station_id = s.id
  AND end_station_id = e.id )
SELECT
  bike_id,
  SUM(distance)/1000 AS total_distance
FROM
  trip_distance
GROUP BY
  bike_id
ORDER BY
  total_distance DESC
LIMIT
  5
```
![image](https://user-images.githubusercontent.com/1645304/137640973-e6284c59-37d9-4c59-bb60-e681c4c9420a.png)


The above query takes 9.8 seconds (55 seconds of slot time) and shuffles 1.22 MB. The result is that some bicycles have been ridden nearly 6000 kilometers.

2. Computing the distance is a pretty expensive operation and we can avoid joining the `cycle_stations` table against the `cycle_hire table` if we precompute the distances between all pairs of stations:
```sql
WITH
  stations AS (
SELECT
  s.id AS start_id,
  e.id AS end_id,
  ST_Distance(ST_GeogPoint(s.longitude,
      s.latitude),
    ST_GeogPoint(e.longitude,
      e.latitude)) AS distance
FROM
  `bigquery-public-data`.london_bicycles.cycle_stations s,
  `bigquery-public-data`.london_bicycles.cycle_stations e ),
trip_distance AS (
SELECT
  bike_id,
  distance
FROM
  `bigquery-public-data`.london_bicycles.cycle_hire,
  stations
WHERE
  start_station_id = start_id
  AND end_station_id = end_id )
SELECT
  bike_id,
  SUM(distance)/1000 AS total_distance
FROM
  trip_distance
GROUP BY
  bike_id
ORDER BY
  total_distance DESC
LIMIT
  5
```
This query only makes 600k geo-distance calculations vs. 24M previously. Now it takes 31.5 seconds of slot time (a 30% speedup), despite shuffling 33.05MB of data.

## Cache results of previous queries
The BigQuery service automatically caches query results in a temporary table. If the identical query is submitted within approximately 24 hours, the results are served from this temporary table without any recomputation. Cached results are extremely fast and do not incur charges.

There are, however, a few caveats to be aware of. Query caching is based on exact string comparison. So even whitespaces can cause a cache miss. Queries are never cached if they exhibit non-deterministic behavior (for example, they use CURRENT_TIMESTAMP or RAND), if the table or view being queried has changed (even if the columns/rows of interest to the query are unchanged), if the table is associated with a streaming buffer (even if there are no new rows), if the query uses DML statements, or queries external data sources.

### Cache intermediate results
It is possible to improve overall performance at the expense of increased I/O by taking advantage of temporary tables and materialized views.

1. For example, suppose you have a number of queries that start out by finding the typical duration of trips between a pair of stations. The WITH clause (also called a Common Table Expression) improves readability but does not improve query speed or cost since results are not cached. The same holds for views and subqueries as well. If you find yourself using a WITH clause, view, or a subquery often, one way to potentially improve performance is to store the result into a table (or materialized view).

First you will need to create a dataset named `mydataset` in the `EU` region (where the bicycle data resides) under your project in BigQuery.

- In the left pane in the **Explorer** section, click on the **View action** icon (three dots) near your BigQuery project (`qwiklabs-gcp-xxxx`) and select **Create dataset**.

![image](https://user-images.githubusercontent.com/1645304/137641089-95eaff69-3993-41c8-9072-f53056bf0351.png)


In the **Create dataset** dialog:

- Set the Dataset ID to mydataset.
- Set the Data location to European Union (EU).
- Leave all other options at their default values.
- To finish, click the blue CREATE DATASET button.

![image](https://user-images.githubusercontent.com/1645304/137641104-7584714a-6387-4cdd-be40-4c5d39a3bf8c.png)

Now you may execute the following query:
```sql
CREATE OR REPLACE TABLE
  mydataset.typical_trip AS
SELECT
  start_station_name,
  end_station_name,
  APPROX_QUANTILES(duration, 10)[OFFSET (5)] AS typical_duration,
  COUNT(duration) AS num_trips
FROM
  `bigquery-public-data`.london_bicycles.cycle_hire
GROUP BY
  start_station_name,
  end_station_name
```

2. Use the table created to find days when bicycle trips are much longer than usual:
```
SELECT
  EXTRACT (DATE
  FROM
    start_date) AS trip_date,
  APPROX_QUANTILES(duration / typical_duration, 10)[OFFSET(5)] AS ratio,
  COUNT(*) AS num_trips_on_day
FROM
  `bigquery-public-data`.london_bicycles.cycle_hire AS hire
JOIN
  mydataset.typical_trip AS trip
ON
  hire.start_station_name = trip.start_station_name
  AND hire.end_station_name = trip.end_station_name
  AND num_trips > 10
GROUP BY
  trip_date
HAVING
  num_trips_on_day > 10
ORDER BY
  ratio DESC
LIMIT
  10
```
![image](https://user-images.githubusercontent.com/1645304/137641123-7644d2f7-94e8-413d-8f5c-9c173c5958fb.png)

3. Use the WITH clause to find days when bicycle trips are much longer than usual:
```
WITH
typical_trip AS (
SELECT
  start_station_name,
  end_station_name,
  APPROX_QUANTILES(duration, 10)[OFFSET (5)] AS typical_duration,
  COUNT(duration) AS num_trips
FROM
  `bigquery-public-data`.london_bicycles.cycle_hire
GROUP BY
  start_station_name,
  end_station_name )
SELECT
  EXTRACT (DATE
  FROM
    start_date) AS trip_date,
  APPROX_QUANTILES(duration / typical_duration, 10)[
OFFSET
  (5)] AS ratio,
  COUNT(*) AS num_trips_on_day
FROM
  `bigquery-public-data`.london_bicycles.cycle_hire AS hire
JOIN
  typical_trip AS trip
ON
  hire.start_station_name = trip.start_station_name
  AND hire.end_station_name = trip.end_station_name
  AND num_trips > 10
GROUP BY
  trip_date
HAVING
  num_trips_on_day > 10
ORDER BY
  ratio DESC
LIMIT
10
```

![image](https://user-images.githubusercontent.com/1645304/137641128-92cc4f0e-ae39-43ae-a9bb-013603833fc8.png)

Notice the ~50% speedup since the average trip duration computation is avoided. Both queries return the same result, that trips on Christmas take longer than usual. Note, the table `mydataset.typical_trip` is not refreshed when new data is added to the `cycle_hire` table. One way to solve this problem of stale data is to use a materialized view or to schedule queries to update the table periodically. You should measure the cost of such updates to see whether the improvement in query performance makes up for the extra cost of maintaining the table or materialized view up-to-date.

### Accelerate queries with BI Engine
If there are tables that you access frequently in Business Intelligence (BI) settings such as dashboards with aggregations and filters, one way to speed up your queries is to employ **BI Engine**. It will automatically store relevant pieces of data in memory (either actual columns from the table or derived results), and will use a specialized query processor tuned for working with mostly in-memory data. You can reserve the amount of memory (up to a current maximum of 10 GB) that BigQuery should use for its cache from the BigQuery Admin Console, under BI Engine.

Make sure to reserve this memory in the same region as the dataset you are querying. Then, BigQuery will start to cache tables, parts of tables, and aggregations in memory and serve results faster.

A primary use case for BI Engine is for tables that are accessed from dashboard tools such as Google Data Studio. By providing memory allocation for a BI Engine reservation, we can make dashboards that rely on a BigQuery backend much more responsive.


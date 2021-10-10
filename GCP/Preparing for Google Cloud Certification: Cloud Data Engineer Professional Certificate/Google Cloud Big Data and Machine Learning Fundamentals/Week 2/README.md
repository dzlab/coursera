# Week 2

## Real-time IoT Dashboards with Pub/Sub, Dataflow, and Data Studio

### Lab: Creating a Streaming Data Pipeline with Dataflow
In this lab, you own a fleet of New York City taxi cabs and are looking to monitor how well your business is doing in real-time. You will build a streaming data pipeline to capture taxi revenue, passenger count, ride status, and much more and visualize the results in a management dashboard. Specifically you will:

- Connect to a streaming data Topic in Cloud Pub/sub
- Ingest streaming data with Cloud Dataflow
- Load streaming data into BigQuery
- Analyze and visualize the results 

#### Task 1. Create a Pub/Sub topic and BigQuery dataset
```
bq mk taxirides
```

```
bq mk \
--time_partitioning_field timestamp \
--schema ride_id:string,point_idx:integer,latitude:float,longitude:float,\
timestamp:timestamp,meter_reading:float,meter_increment:float,ride_status:string,\
passenger_count:integer -t taxirides.realtime
```

#### Task 3. Set up a Dataflow Pipeline
[Dataflow](https://cloud.google.com/dataflow/) is a serverless way to carry out data analysis. In this lab, you set up a streaming data pipeline to read sensor data from Pub/Sub, compute the maximum temperature within a time window, and write this out to BigQuery.

1. In the Cloud Console, go to Navigation menu > Dataflow.
2. In the top menu bar, click CREATE JOB FROM TEMPLATE.
3. Enter streaming-taxi-pipeline as the Job name for your Dataflow job.
4. Under Dataflow template, select the Pub/Sub Topic to BigQuery template.
5. Under Input Pub/Sub topic, enter projects/pubsub-public-data/topics/taxirides-realtime
6. Under BigQuery output table, enter `<myprojectid>:taxirides.realtime`

#### Task 4. Analyze the taxi data using BigQuery
To analyze the data as it is streaming:

1. In the Cloud Console, select Navigation menu > BigQuery.
2. Enter the following query in the query EDITOR and click RUN:

```
SELECT * FROM taxirides.realtime LIMIT 10
```
3. If no records are returned, wait another minute and re-run the above query (Dataflow takes 3-5 minutes to setup the stream). You will receive a similar output:

#### Task 5. Perform aggregations on the stream for reporting
1. Copy and paste the below query and click RUN.
```
WITH streaming_data AS (
SELECT
  timestamp,
  TIMESTAMP_TRUNC(timestamp, HOUR, 'UTC') AS hour,
  TIMESTAMP_TRUNC(timestamp, MINUTE, 'UTC') AS minute,
  TIMESTAMP_TRUNC(timestamp, SECOND, 'UTC') AS second,
  ride_id,
  latitude,
  longitude,
  meter_reading,
  ride_status,
  passenger_count
FROM
  taxirides.realtime
WHERE ride_status = 'dropoff'
ORDER BY timestamp DESC
LIMIT 100000
)
# calculate aggregations on stream for reporting:
SELECT
 ROW_NUMBER() OVER() AS dashboard_sort,
 minute,
 COUNT(DISTINCT ride_id) AS total_rides,
 SUM(meter_reading) AS total_revenue,
 SUM(passenger_count) AS total_passengers
FROM streaming_data
GROUP BY minute, timestamp
```
The result shows key metrics by the minute for every taxi drop-off.

#### Task 6. Create a real-time dashboard
1. Open this [Google Data Studio](https://datastudio.google.com/) link in a new incognito browser tab.
2. On the Reports page, in the Start with a Template section, click the [+] Blank Report template.
3. If prompted with the Welcome to Google Studio window, click Get started.
4. Check the checkbox to acknowledge the Google Data Studio Additional Terms, and click Continue.
5. Select No to all the questions, then click Continue.
6. Switch back to the BigQuery Console.
7. Click EXPLORE DATA > Explore with Data Studio in BigQuery page.
8. Click GET STARTED, then click AUTHORIZE.
9. Specify the below settings:
  - Chart type: Combo chart
  - Date range Dimension: dashboard_sort
  - Dimension: dashboard_sort
  - Drill Down: dashboard_sort (Make sure that Drill down option is turned ON)
  - Metric: SUM() total_rides, SUM() total_passengers, SUM() total_revenue
  - Sort: dashboard_sort, Ascending (latest rides first)

#### Task 7. Create a time series dashboard
1. Click this [Google Data Studio](https://datastudio.google.com/) link to open Data Studio in a new browser tab.
2. On the Reports page, in the Start with a Template section, click the [+] Blank Report template.
3. A new, empty report opens with Add data to report.
4. From the list of Google Connectors, select the BigQuery tile.
5. Under CUSTOM QUERY, click qwiklabs-gcp-xxxxxxx > Enter Custom Query, add the following query.
```
SELECT
  *
FROM
  taxirides.realtime
WHERE
  ride_status='dropoff'
```
6. Click Add > ADD TO REPORT.

Create a time series chart
1. In the Data panel, scroll down to the bottom right and click ADD A FIELD. Click All Fields on the left corner.
2. Change the field timestamp type to Date & Time > Date Hour Minute (YYYYMMDDhhmm).
3. Click DONE.
4. Click Add a chart.
5. Choose Time series chart.
6. Position the chart in the bottom left corner - in the blank space.
7. In the Data panel on the right, change the following:
- Dimension: timestamp
- Metric: meter_reading(SUM)

Your time series chart should look similar to this:

### Quiz: Module Review
**1. Question 1**

Relational databases are a good choice when you need:

- [ ] Streaming, high-throughput writes
- [ ] Fast queries on terabytes of data
- [ ] Aggregations on unstructured data
- [x] Transactional updates on relatively small datasets

**2. Question 2**

Cloud SQL and Cloud Dataproc offer familiar tools (MySQL and Hadoop/Pig/Hive/Spark). What is the value-add provided by Google Cloud Platform?

(Select all of the correct options)

- [ ] It’s the same API, but Google implements it better
- [ ] Google-proprietary extensions and bug fixes to MySQL, Hadoop, and so on
- [x] Fully-managed versions of the software offer no-ops
- [x] Running it on Google infrastructure offers reliability and cost savings

### Reading: Module Resources
- [Pub/Sub documentation](https://cloud.google.com/pubsub/docs/) + [blog](https://cloud.google.com/pubsub/docs/release-notes)
- [Dataflow documentation](https://cloud.google.com/dataflow/docs/) + [blog](https://cloud.google.com/blog/products/data-analytics/) + [templates](https://github.com/GoogleCloudPlatform/DataflowTemplates/)
- [Data Studio documentation](https://developers.google.com/datastudio/) + [templates](https://datastudiogallery.appspot.com/gallery)

## Deriving Insights from Unstructured Data using Machine Learning
### Lab: Classifying Images of Clouds in the Cloud with AutoML Vision


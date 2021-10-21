# Week 2

## Building a Data Warehouse

### Lab: Loading Data into BigQuery
#### Overview
BigQuery is Google's fully managed, NoOps, low cost analytics database. With BigQuery you can query terabytes and terabytes of data without having any infrastructure to manage or needing a database administrator. BigQuery uses SQL and can take advantage of the pay-as-you-go model. BigQuery allows you to focus on analyzing data to find meaningful insights.

In this lab you will ingest subsets of the NYC taxi trips data into tables inside of BigQuery.

What you'll learn
- Loading data into BigQuery from various sources
- Loading data into BigQuery using the CLI and Console
- Using DDL to create tables

#### Create a new dataset to store tables
In the BigQuery console, click on the name of your project, then click Create Dataset.
Set the Dataset ID to nyctaxi. Leave the other fields at their default values.

Click Create dataset.

You'll now see the nyctaxi dataset under your project name.

#### Ingest a new Dataset from a CSV
In this section, you will load a local CSV into a BigQuery table.

1. Download a subset of the NYC taxi 2018 trips data locally onto your computer from [here](https://storage.googleapis.com/cloud-training/OCBL013/nyc_tlc_yellow_trips_2018_subset_1.csv):
2. In the BigQuery Console, Select the nyctaxi dataset then click Create Table

**Specify the below table options:**

Source:
- Create table from: Upload
- Choose File: select the file you downloaded locally earlier
- File format: CSV

Destination:
- Table name: 2018trips Leave all other setting at default.

Schema:
- Check Auto Detect (tip: Not seeing the checkbox? Ensure the file format is CSV and not Avro)

Advanced Options
- Leave at default values

Click Create Table.

You should now see the 2018trips table below the nyctaxi dataset.

Select Preview and confirm all columns have been loaded (sampled below):
You have successfully loaded in a CSV file into a new BigQuery table.

Running SQL Queries
Next, practice with a basic query on the 2018trips table.

In the Query Editor, write a query to list the top 5 most expensive trips of the year:
```sql
#standardSQL
SELECT
  *
FROM
  nyctaxi.2018trips
ORDER BY
  fare_amount DESC
LIMIT  5
```

#### Ingest a new Dataset from Google Cloud Storage
Now, lets try load another subset of the same 2018 trip data that is available on Cloud Storage. And this time, let's use the CLI tool to do it.

1. In your Cloud Shell, run the following command :
```
$ bq load \
--source_format=CSV \
--autodetect \
--noreplace  \
nyctaxi.2018trips \
gs://cloud-training/OCBL013/nyc_tlc_yellow_trips_2018_subset_2.csv
Waiting on bqjob_r37cdd21ac1c6c28d_0000017c6ba4594e_1 ... (2s) Current status: DONE 
```

Note: With the above load job, you are specifying that this subset is to be appended to the existing 2018trips table that you created above.

2. When the load job is complete, you will get a confirmation on the screen.
3. Back on your BigQuery console, select the 2018trips table and view details. Confirm that the row count has now almost doubled.
4. You may want to run the same query like earlier to see if the top 5 most expensive trips have changed.

#### Create tables from other tables with DDL
The 2018trips table now has trips from throughout the year. What if you were only interested in January trips? For the purpose of this lab, we will keep it simple and focus only on pickup date and time. Let's use DDL to extract this data and store it in another table

1. In the Query Editor, run the following CREATE TABLE command :
```sql
#standardSQL
CREATE TABLE
  nyctaxi.january_trips AS
SELECT
  *
FROM
  nyctaxi.2018trips
WHERE
  EXTRACT(Month
  FROM
    pickup_datetime)=1;
```
2. Now run the below query in your Query Editor find the longest distance traveled in the month of January:
```sql
#standardSQL
SELECT
  *
FROM
  nyctaxi.january_trips
ORDER BY
  trip_distance DESC
LIMIT
  1
```


### Lab: Working with JSON and Array Data in BigQuery
#### Overview
BigQuery is Google's fully managed, NoOps, low cost analytics database. With BigQuery you can query terabytes and terabytes of data without having any infrastructure to manage or needing a database administrator. BigQuery uses SQL and can take advantage of the pay-as-you-go model. BigQuery allows you to focus on analyzing data to find meaningful insights.

This lab is an in-depth walkthrough of working with semi-structured data (ingesting JSON, Array data types) inside of BigQuery. Denormalizing your schema into a single table with nested and repeated fields can yield performance improvements, but the SQL syntax for working with array data can be tricky. You will practice loading, querying, troubleshooting, and unnesting various semi-structured datasets.

Objectives
In this lab, you learn about the following:

- Loading semi-structured JSON into BigQuery
- Creating and querying arrays
- Creating and querying structs
- Querying nested and repeated fields

#### Create a new dataset to store our tables
1. To create a dataset, click on the View actions icon next to your Project ID and then select Create dataset.
2. Name the new dataset **fruit_store**. Leave the other options at their default values (Data Location, Default Expiration). Click **Create dataset**.

#### Practice working with Arrays in SQL
Normally in SQL you will have a single value for each row like this list of fruits below:

What if you wanted a list of fruit items for each person at the store? It could look something like this:

In traditional relational database SQL, you would look at the repetition of names and immediately think to split the above table into two separate tables: Fruit Items and People. That process is called [normalization](https://en.wikipedia.org/wiki/Database_normalization) (going from one table to many). This is a common approach for transactional databases like mySQL.

For data warehousing, data analysts often go the reverse direction (denormalization) and bring many separate tables into one large reporting table.

What are some potential issues if you stored all your data in one giant table?
- [x] The table row size could be too large for traditional reporting databases
- [ ] Any changes to a value (like customer email) could impact many other rows (like all their orders)
- [ ] Data at differing levels of granularity could lead to reporting issues because less granular fields would be repeated.
- [ ] All of the above

Now, you're going to learn a different approach that stores data at different levels of granularity all in one table using repeated fields:

What looks strange about the previous table?

- It's only two rows.
- There are multiple field values for Fruit in a single row.
- The people are associated with all of the field values.

What the key insight? The `array` data type!

An easier way to interpret the Fruit array:


|Row|Fruit (array)|Person|
|-|-|-|
|1|[raspberry, blackberry, strawberry, cherry]|sally
|2|[orange, apple]|frederick

Both of these tables are exactly the same. There are two key learnings here:
- An array is simply a list of items in brackets [ ]
- BigQuery visually displays arrays as flattened. It simply lists the value in the array vertically (note that all of those values still belong to a single row)

1. Try it yourself. Enter the following in the BigQuery Query Editor:
```sql
#standardSQL
SELECT
['raspberry', 'blackberry', 'strawberry', 'cherry'] AS fruit_array
```

2. Click Run.
3. Now try executing this one:
```sql
 #standardSQL
SELECT
['raspberry', 'blackberry', 'strawberry', 'cherry', 1234567] AS fruit_array
```

You should get an error that looks like the following:

```
Error: Array elements of types {INT64, STRING} do not have a common supertype at [3:1]
```

Why did we get this error?

- [ ] Data in an array must only be strings
- [ ] Data in an array cannot exceed 4 elements
- [x] Data in an array `[ ]` must all be the same type

Arrays can only share one data type (all strings, all numbers).

4. Here's the final table to query against:
```sql
#standardSQL
SELECT person, fruit_array, total_cost FROM `data-to-insights.advanced.fruit_store`;
```

5. Click Run.
6. After viewing the results, click the JSON tab to view the nested structure of the results.


Loading semi-structured JSON into BigQuery
What if you had a JSON file that you needed to ingest into BigQuery?

1. Create a new table in the fruit_store dataset.
2. To create a table, click on the View actions icon next to the `fruit_store` dataset and select Open.
3. Now, click + CREATE TABLE.
4. Add the following details for the table:
  - Source: Choose Google Cloud Storage in the Create table from dropdown.
  - Select file from GCS bucket: `gs://data-insights-course/labs/optimizing-for-performance/shopping_cart.json` File format: JSONL (Newline delimited JSON)
  - Schema: Check Auto detect (Schema and input parameters).
5. Call the new table "fruit_details".
6. Click Create table.

In the schema, note that `fruit_array` is marked as REPEATED which means it's an array.


Recap

- BigQuery natively supports arrays
- Array values must share a data type
- Arrays are called REPEATED fields in BigQuery

#### Creating your own arrays with ARRAY_AGG()
Don't have arrays in your tables already? You can create them!
1. Copy and Paste the below query to explore this public dataset
```sql
SELECT
  fullVisitorId,
  date,
  v2ProductName,
  pageTitle
  FROM `data-to-insights.ecommerce.all_sessions`
WHERE visitId = 1501570398
ORDER BY date
```
2. Click Run and view the results
3. Now, we will use the ARRAY_AGG() function to aggregate our string values into an array. Copy and paste the below query to explore this public dataset:
```sql
SELECT
  fullVisitorId,
  date,
  ARRAY_AGG(v2ProductName) AS products_viewed,
  ARRAY_AGG(pageTitle) AS pages_viewed
  FROM `data-to-insights.ecommerce.all_sessions`
WHERE visitId = 1501570398
GROUP BY fullVisitorId, date
ORDER BY date
```
4. Click Run and view the results

5. Next, we will use the ARRAY_LENGTH() function to count the number of pages and products that were viewed.
```sql
SELECT
  fullVisitorId,
  date,
  ARRAY_AGG(v2ProductName) AS products_viewed,
  ARRAY_LENGTH(ARRAY_AGG(v2ProductName)) AS num_products_viewed,
  ARRAY_AGG(pageTitle) AS pages_viewed,
  ARRAY_LENGTH(ARRAY_AGG(pageTitle)) AS num_pages_viewed
  FROM `data-to-insights.ecommerce.all_sessions`
WHERE visitId = 1501570398
GROUP BY fullVisitorId, date
ORDER BY date
```
6. Next, lets deduplicate the pages and products so we can see how many unique products were viewed. We'll simply add DISTINCT to our ARRAY_AGG()
```sql
SELECT
  fullVisitorId,
  date,
  ARRAY_AGG(DISTINCT v2ProductName) AS products_viewed,
  ARRAY_LENGTH(ARRAY_AGG(DISTINCT v2ProductName)) AS distinct_products_viewed,
  ARRAY_AGG(DISTINCT pageTitle) AS pages_viewed,
  ARRAY_LENGTH(ARRAY_AGG(DISTINCT pageTitle)) AS distinct_pages_viewed
  FROM `data-to-insights.ecommerce.all_sessions`
WHERE visitId = 1501570398
GROUP BY fullVisitorId, date
ORDER BY date
```

##### Recap

You can do some pretty useful things with arrays like:

- finding the number of elements with `ARRAY_LENGTH(<array>)`
- deduplicating elements with `ARRAY_AGG(DISTINCT <field>)`
- ordering elements with `ARRAY_AGG(<field> ORDER BY <field>)`
- limiting `ARRAY_AGG(<field> LIMIT 5)`

#### Querying datasets that already have ARRAYs
The BigQuery Public Dataset for Google Analytics bigquery-public-data.google_analytics_sample has many more fields and rows than our course dataset data-to-insights.ecommerce.all_sessions. More importantly, it already stores field values like products, pages, and transactions natively as ARRAYs.

1. Copy and Paste the below query to explore the available data and see if you can find fields with repeated values (arrays)
```sql
SELECT
  *
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_20170801`
WHERE visitId = 1501570398
```
2. Run the query.
3. Scroll right in the results until you see the hits.product.v2ProductName field (we will discuss the multiple field aliases shortly).

You will notice a lot of seemingly 'empty' cells in the results as you scroll. These cells are grayed out and not marked as null. Why do you think that is?
- [ ] BigQuery is still in the process of loading values for the grayed out cells
- [ ] The entire dataset has no data values for the grayed out cells
- [x] The grayed out cells are visual placeholders to make it possible to show each item in an array type column on its own row within the context of a row in the result set

4. The amount of fields available in the Google Analytics schema can be overwhelming for our analysis. Let's try to query just the visit and page name fields like we did before.
```sql
SELECT
  visitId,
  hits.page.pageTitle
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_20170801`
WHERE visitId = 1501570398
```
You will get an error: `Cannot access field page on a value with type ARRAY<STRUCT<hitNumber INT64, time INT64, hour INT64, ...>> at [3:8]`

Before we can query REPEATED fields (arrays) normally, you must first break the arrays back into rows.

For example, the array for `hits.page.pageTitle` is stored currently as a single row like:
```
['homepage','product page','checkout']
```
and we need it to be
```
['homepage',
'product page',
'checkout']
```
5. How do we do that with SQL? Answer: Use the UNNEST() function on your array field:
```sql
SELECT DISTINCT
  visitId,
  h.page.pageTitle
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_20170801`,
UNNEST(hits) AS h
WHERE visitId = 1501570398
LIMIT 10
```
We'll cover `UNNEST()` more in detail later but for now just know that:

- You need to `UNNEST()` arrays to bring the array elements back into rows
- `UNNEST()` always follows the table name in your FROM clause (think of it conceptually like a pre-joined table)


#### Introduction to STRUCTs
You may have wondered why the field alias `hit.page.pageTitle` looks like three fields in one separated by periods. Just as ARRAY values give you the flexibility to go deep into the granularity of your fields, another data type allows you to go wide in your schema by grouping related fields together. That SQL data type is the [STRUCT](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct-type) data type.

The easiest way to think about a STRUCT is to consider it conceptually like a separate table that is already pre-joined into your main table.

A STRUCT can have:

one or many fields in it
- the same or different data types for each field
- it's own alias
- Sounds just like a table right?

Let's explore a dataset with STRUCTs
1. Under Explorer find the bigquery-public-data dataset (if it's not present already, use this [link](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_analytics_sample&t=ga_sessions_20170801&page=table) to pin the dataset)
2. Click bigquery-public-data
3. Find and open google_analytics_sample
4. Click the ga_sessions table
5. Start scrolling through the schema and answer the following question by using the find feature of your browser (i.e. CTRL + F)

6. As you can imagine, there is an incredible amount of website session data stored for a modern ecommerce website. The main advantage of having 32 STRUCTs in a single table is it allows you to run queries like this one without having to do any JOINs:
```sql
SELECT
  visitId,
  totals.*,
  device.*
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_20170801`
WHERE visitId = 1501570398
LIMIT 10
```

Note: The `.*` syntax tells BigQuery to return all fields for that STRUCT (much like it would if totals.* was a separate table we joined against)

Storing your large reporting tables as STRUCTs (pre-joined "tables") and ARRAYs (deep granularity) allows you to:

- gain significant performance advantages by avoiding 32 table JOINs
- get granular data from ARRAYs when you need it but not be punished if you don't (BigQuery stores each column individually on disk)
- have all the business context in one table as opposed to worrying about JOIN keys and which tables have the data you need

#### Practice with STRUCTs and ARRAYs
The next dataset will be lap times of runners around the track. Each lap will be called a "split".
1. With this query, try out the STRUCT syntax and note the different field types within the struct container:
```sql
#standardSQL
SELECT STRUCT("Rudisha" as name, 23.4 as split) as runner
```


|Row|runner.name|runner.split
|-|-|-
|1|Rudisha|23.4

What do you notice about the field aliases? Since there are fields nested within the struct (name and split are a subset of runner) you end up with a dot notation.

What if the runner has multiple split times for a single race (like time per lap)?

How could you have multiple split times within a single record? Hint: the splits all have the same numeric datatype.

- [x] Store each split time as an element in an ARRAY of splits
- [ ] Use a SQL UNION to join the race and split details
- [ ] Store each split time in a separate STRING field with STRING_AGG()
- [ ] Store each split time in a separate table called race_splits

2. With an array of course! Run the below query to confirm:
```sql
#standardSQL
SELECT STRUCT("Rudisha" as name, [23.4, 26.3, 26.4, 26.1] as splits) AS runner
```

To recap:

- Structs are containers that can have multiple field names and data types nested inside.
- An array can be one of the field types inside of a Struct (as shown above with the splits field).

Practice ingesting JSON data
1. Create a new dataset titled racing.
2. Create a new table titled race_results.
3. Ingest this Google Cloud Storage JSON file:
```
gs://data-insights-course/labs/optimizing-for-performance/race_results.json
```
  - Source: Google Cloud Storage under Create table from dropdown.
  - Select file from GCS bucket: gs://data-insights-course/labs/optimizing-for-performance/race_results.json
  - File format: JSONL (Newline delimited JSON)
  - Under Schema move the Edit as text slider and add the following:
```json
[
    {
        "name": "race",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "participants",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "splits",
                "type": "FLOAT",
                "mode": "REPEATED"
            }
        ]
    }
]
```
4. Click Create table.
5. After the load job is successful, preview the schema for the newly created table:

Which field is the STRUCT? How do you know?

The participants field is the STRUCT because it is of type RECORD

Which field is the ARRAY?

The `participants.splits` field is an array of floats inside of the parent participants struct. It has a REPEATED Mode which indicates an array. Values of that array are called nested values since they are multiple values inside of a single field.

##### Practice querying nested and repeated fields
1. Let's see all of our racers for the 800 Meter race.
```sql
#standardSQL
SELECT * FROM racing.race_results
```
How many rows were returned?

Answer: 1

2. What if you wanted to list the name of each runner and the type of race?
Run the below schema and see what happens:
```sql
#standardSQL
SELECT race, participants.name
FROM racing.race_results
```

```
Error: Cannot access field name on a value with type ARRAY<STRUCT<name STRING, splits ARRAY<FLOAT64>>> at [2:27]
```

Much like forgetting to GROUP BY when you use aggregation functions, here there are two different levels of granularity. One row for the race and three rows for the participants' names. So how do you change this...
 
 
In traditional relational SQL, if you had a races table and a participants table what would you do to get information from both tables? You would JOIN them together. Here the participant STRUCT (which is conceptually very similar to a table) is already part of your races table but is not yet correlated correctly with your non-STRUCT field "race".

Can you think of what two word SQL command you would use to correlate the 800M race with each of the racers in the first table?

Answer: CROSS JOIN

3. Great! Now try running this:
```sql
#standardSQL
SELECT race, participants.name
FROM racing.race_results
CROSS JOIN
participants  # this is the STRUCT (it's like a table within a table)
```

```
Error: Table name "participants" missing dataset while no default dataset is set in the request.
```

Even though the participants STRUCT is like a table, it is still technically a field in the `racing.race_results` table.

4. Add the dataset name to the query:
```sql
#standardSQL
SELECT race, participants.name
FROM racing.race_results
CROSS JOIN
race_results.participants # full STRUCT name
```
5. Click Run.
Wow! You've successfully listed all of the racers for each race!

You can simplify the last query by:

- Adding an alias for the original table
- Replacing the words "CROSS JOIN" with a comma (a comma implicitly cross joins)

This will give you the same query result:
```sql
#standardSQL
SELECT race, participants.name
FROM racing.race_results AS r, r.participants
```

If you have more than one race type (800M, 100M, 200M), wouldn't a CROSS JOIN just associate every racer name with every possible race like a cartesian product?

**Answer**: No. This is a correlated cross join which only unpacks the elements associated with a single row. For a greater discussion, see [working with ARRAYs and STRUCTs](https://cloud.google.com/bigquery/docs/reference/standard-sql/arrays#flattening-arrays)

Recap of STRUCTs:

- A SQL [STRUCT](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct-type) is simply a container of other data fields which can be of different data types. The word struct means data structure. Recall the example from earlier:
- `__STRUCT(__"Rudisha" as name, [23.4, 26.3, 26.4, 26.1] as splits__)__AS runner`
- STRUCTs are given an alias (like runner above) and can conceptually be thought of as a table inside of your main table.
- STRUCTs (and ARRAYs) must be unpacked before you can operate over their elements. Wrap an UNNEST() around the name of the struct itself or the struct field that is an array in order to unpack and flatten it.


#### Lab Question: STRUCT()
Answer the below questions using the racing.race_results table you created previously.

Task: Write a query to COUNT how many racers were there in total.

To start, use the below partially written query:
```sql
#standardSQL
SELECT COUNT(participants.name) AS racer_count
FROM racing.race_results
```
Hint: Remember you will need to cross join in your struct name as an additional data source after the FROM.

Possible Solution:
```sql
#standardSQL
SELECT COUNT(p.name) AS racer_count
FROM racing.race_results AS r, UNNEST(r.participants) AS p
```
Answer: There were 8 racers who ran the race.


#### Lab Question: Unpacking ARRAYs with UNNEST( )
Write a query that will list the total race time for racers whose names begin with R. Order the results with the fastest total time first. Use the UNNEST() operator and start with the partially written query below.

Complete the query:
```sql
#standardSQL
SELECT
  p.name,
  SUM(split_times) as total_race_time
FROM racing.race_results AS r
, r.participants AS p
, p.splits AS split_times
WHERE
GROUP BY
ORDER BY
;
```
Hint:

- You will need to unpack both the struct and the array within the struct as data sources after your FROM clause
- Be sure to use aliases where appropriate

Possible Solution:
```sql
#standardSQL
SELECT
  p.name,
  SUM(split_times) as total_race_time
FROM racing.race_results AS r
, UNNEST(r.participants) AS p
, UNNEST(p.splits) AS split_times
WHERE p.name LIKE 'R%'
GROUP BY p.name
ORDER BY total_race_time ASC;
```

#### Lab Question: Filtering within ARRAY values
You happened to see that the fastest lap time recorded for the 800 M race was 23.2 seconds, but you did not see which runner ran that particular lap. Create a query that returns that result.

Task: Complete the partially written query:
```sql
#standardSQL
SELECT
  p.name,
  split_time
FROM racing.race_results AS r
, r.participants AS p
, p.splits AS split_time
WHERE split_time = ;
```

Possible Solution:
```sql
#standardSQL
SELECT
  p.name,
  split_time
FROM racing.race_results AS r
, UNNEST(r.participants) AS p
, UNNEST(p.splits) AS split_time
WHERE split_time = 23.2;
```

Next Steps / Learn More
- For additional reading, refer to [Working with Arrays](https://cloud.google.com/bigquery/docs/reference/standard-sql/arrays).

### Quiz
**1. Question 1**

Which of the following statements on BigQuery are true?

- [x] Data is run length-encoded and dictionary-encoded
- [x] Data on BigQuery is physically stored in a redundant way separate from the compute cluster
- [x] A BigQuery slot is a combination of CPU, memory, and networking resources
- [ ] The number of slots allotted to a query is independent of query complexity


**2. Question 2**

True or False:  ARRAYS can be part of regular fields or STRUCTS in BigQuery?

- [x] True
- [ ] False



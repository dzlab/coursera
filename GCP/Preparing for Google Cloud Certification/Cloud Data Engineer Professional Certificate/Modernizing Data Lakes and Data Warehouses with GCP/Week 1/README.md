# Week 1

## Introduction to Data Engineering

### Quiz
**1. Question 1**

Which of the following are the jobs of a data engineer? 

- [x] Get the data to where it can be useful
- [x] Get the data into a usable condition
- [x] Add new value to the data
- [x] Manage the data
- [x] Productionize data processes


**2. Question 2**

Which statements are true?


- [x] Clod SQL is optimized for high-throughput writes
- [x] BigQuery is optimized for high-read data
- [ ] BigQuery is a row-based storage
- [ ] Cloud SQL is optimized for high-read data

## Building a Data Lake
### Lab: Loading Taxi Data into Cloud SQL

#### Preparing your Environment
Create environment variables that will be used later in the lab for your project ID and the storage bucket that will contain your data:
```
export PROJECT_ID=$(gcloud info --format='value(config.project)')
export BUCKET=${PROJECT_ID}-ml
```

#### Create a Cloud SQL instance
Enter the following commands to create a Cloud SQL instance:
```
gcloud sql instances create taxi \
    --tier=db-n1-standard-1 --activation-policy=ALWAYS
```
This will take a few minutes to complete.

Set a root password for the Cloud SQL instance:
```
gcloud sql users set-password root --host % --instance taxi \
 --password Passw0rd
```
When prompted for the password type `Passw0rd` and press enter this will update root password.

Now create an environment variable with the IP address of the Cloud Shell:
```
export ADDRESS=$(wget -qO - http://ipecho.net/plain)/32
```
Whitelist the Cloud Shell instance for management access to your SQL instance.
```
gcloud sql instances patch taxi --authorized-networks $ADDRESS
```
When prompted press **Y** to accept the change.

Get the IP address of your Cloud SQL instance by running:
```
MYSQLIP=$(gcloud sql instances describe \
taxi --format="value(ipAddresses.ipAddress)")
```
Check the variable MYSQLIP:
```
echo $MYSQLIP
```
you should get an IP address as an output.

Create the taxi trips table by logging into the `mysql` command line interface.
```
mysql --host=$MYSQLIP --user=root \
      --password --verbose
```

When prompted for a password enter `Passw0rd`. Paste the following content into the command line to create the schema for the `trips` table:
```sql
create database if not exists bts;
use bts;
drop table if exists trips;
create table trips (
  vendor_id VARCHAR(16),		
  pickup_datetime DATETIME,
  dropoff_datetime DATETIME,
  passenger_count INT,
  trip_distance FLOAT,
  rate_code VARCHAR(16),
  store_and_fwd_flag VARCHAR(16),
  payment_type VARCHAR(16),
  fare_amount FLOAT,
  extra FLOAT,
  mta_tax FLOAT,
  tip_amount FLOAT,
  tolls_amount FLOAT,
  imp_surcharge FLOAT,
  total_amount FLOAT,
  pickup_location_id VARCHAR(16),
  dropoff_location_id VARCHAR(16)
);
```
In the `mysql` command line interface check the import by entering the following commands:
```
describe trips;
```

Query the `trips` table:
```
select distinct(pickup_location_id) from trips;
```
This will return an empty set as there is no data in the database yet.

Exit the `mysql` interactive console:
```
exit
```

#### Add data to Cloud SQL instance
Now you'll copy the New York City taxi trips CSV files stored on Cloud Storage locally. To keep resource usage low, you'll only be working with a subset of the data (~20,000 rows).

Run the following in the command line:
```
gsutil cp gs://cloud-training/OCBL013/nyc_tlc_yellow_trips_2018_subset_1.csv trips.csv-1
gsutil cp gs://cloud-training/OCBL013/nyc_tlc_yellow_trips_2018_subset_2.csv trips.csv-2
```
Import the CSV file data into Cloud SQL using `mysql`:
```
mysqlimport --local --host=$MYSQLIP --user=root --password \
--ignore-lines=1 --fields-terminated-by=',' bts trips.csv-*
```
When prompted for a password enter `Passw0rd`.

Connect to the `mysql` interactive console:
```
mysql --host=$MYSQLIP --user=root  --password
```
When prompted for a password enter `Passw0rd`.

#### Checking for data integrity
Whenever data is imported from a source it's always important to check for data integrity. Roughly, this means making sure the data meets your expectations.

In the `mysql` interactive console select the database:
```
use bts;
```
Query the `trips` table for unique pickup location regions:
```
select distinct(pickup_location_id) from trips;
```

This should return 159 unique ids. Let's start by digging into the `trip_distance` column. Enter the following query into the console:
```
select
  max(trip_distance),
  min(trip_distance)
from
  trips;
```
One would expect the trip distance to be greater than 0 and less than, say 1000 miles. The maximum trip distance returned of 85 miles seems reasonable but the minimum trip distance of 0 seems buggy. How many trips in the dataset have a trip distance of 0?

```
select count(*) from trips where trip_distance = 0;
```

There are 155 such trips in the database. These trips warrant further exploration. You'll find that these trips have non-zero payment amounts associated with them. Perhaps these are fraudulent transactions? Let's see if we can find more data that doesn't meet our expectations. We expect the `fare_amount` column to be positive. Enter the following query to see if this is true in the database:

```
select count(*) from trips where fare_amount < 0;
```

There should be 14 such trips returned. Again, these trips warrant further exploration. There may be a reasonable explanation for why the fares take on negative numbers. However, it's up to the data engineer to ensure there are no bugs in the data pipeline that would cause such a result.

Finally, let's investigate the `payment_type` column.

```
select
  payment_type,
  count(*)
from
  trips
group by
  payment_type;
```

The results of the query indicate that there are four different payment types, with:

- payment type = 1 has 13863 rows
- payment type = 2 has 6016 rows
- payment type = 3 has 113 rows
- payment type = 4 has 32 rows

Digging into [the documentation](https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf), a payment type of 1 refers to credit card use, payment type of 2 is cash, and a payment type of 4 refers to a dispute. The figures make sense.

Exit the 'mysql' interactive console:
```
exit
```


### Quiz
**1. Question 1**

Which statement best describes a data lake?


- [x] The place where you capure every aspect of your business operations. Data is stored in its natural, raw format.
- [ ] Data storage intended for analytics.
- [ ] Storage optimized for high-throughput writes.
- [ ] Storage for current/historical data intened for reporting.

**2. Question 2**

Which of the following statements on Cloud Storage are true?


- [x] Cloud Storage simulates a file system
- [x] Cloud Storage allows you to set retention policies on all objects in a bucket
- [x] Cloud Storage implements both Cloud IAM policy and Access Control Lists
- [ ] Data in Cloud Storage is not encrypted




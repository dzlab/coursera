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
$ gcloud sql instances create taxi \
    --tier=db-n1-standard-1 --activation-policy=ALWAYS
WARNING: Starting with release 233.0.0, you will need to specify either a region or a zone to create an instance.
Creating Cloud SQL instance...working   
Creating Cloud SQL instance...done.    
Created [https://sqladmin.googleapis.com/sql/v1beta4/projects/qwiklabs-gcp-00-6dc7000c66b4/instances/taxi].
NAME: taxi
DATABASE_VERSION: MYSQL_5_7
LOCATION: us-central1-c
TIER: db-n1-standard-1
PRIMARY_ADDRESS: 34.134.212.213
PRIVATE_ADDRESS: -
STATUS: RUNNABLE
```
This will take a few minutes to complete.

Set a root password for the Cloud SQL instance:
```
$ gcloud sql users set-password root --host % --instance taxi --password Passw0rd
Updating Cloud SQL user...done.  
```
When prompted for the password type `Passw0rd` and press enter this will update root password.

Now create an environment variable with the IP address of the Cloud Shell:
```
export ADDRESS=$(wget -qO - http://ipecho.net/plain)/32
```
Whitelist the Cloud Shell instance for management access to your SQL instance.
```
$ gcloud sql instances patch taxi --authorized-networks $ADDRESS
When adding a new IP address to authorized networks, make sure to also
 include any IP addresses that have already been authorized.
Otherwise, they will be overwritten and de-authorized.

Do you want to continue (Y/n)?  Y

The following message will be used for the patch API method.
{"name": "taxi", "project": "qwiklabs-gcp-00-6dc7000c66b4", "settings": {"ipConfiguration": {"authorizedNetworks": [{"value": "34.82.190.146/32"}]}}}
Patching Cloud SQL instance...done.     
Updated [https://sqladmin.googleapis.com/sql/v1beta4/projects/qwiklabs-gcp-00-6dc7000c66b4/instances/taxi].
```
When prompted press **Y** to accept the change.

Get the IP address of your Cloud SQL instance by running:
```
$ MYSQLIP=$(gcloud sql instances describe taxi --format="value(ipAddresses.ipAddress)")
```
Check the variable MYSQLIP:
```
echo $MYSQLIP
```
you should get an IP address as an output.

Create the taxi trips table by logging into the `mysql` command line interface.
```
$ mysql --host=$MYSQLIP --user=root --password --verbose
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 59
Server version: 5.7.34-google (Google)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Reading history-file /home/student_02_f57edb69be5d/.mysql_history
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
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
mysql> describe trips;
--------------
describe trips
--------------

+---------------------+-------------+------+-----+---------+-------+
| Field               | Type        | Null | Key | Default | Extra |
+---------------------+-------------+------+-----+---------+-------+
| vendor_id           | varchar(16) | YES  |     | NULL    |       |
| pickup_datetime     | datetime    | YES  |     | NULL    |       |
| dropoff_datetime    | datetime    | YES  |     | NULL    |       |
| passenger_count     | int(11)     | YES  |     | NULL    |       |
| trip_distance       | float       | YES  |     | NULL    |       |
| rate_code           | varchar(16) | YES  |     | NULL    |       |
| store_and_fwd_flag  | varchar(16) | YES  |     | NULL    |       |
| payment_type        | varchar(16) | YES  |     | NULL    |       |
| fare_amount         | float       | YES  |     | NULL    |       |
| extra               | float       | YES  |     | NULL    |       |
| mta_tax             | float       | YES  |     | NULL    |       |
| tip_amount          | float       | YES  |     | NULL    |       |
| tolls_amount        | float       | YES  |     | NULL    |       |
| imp_surcharge       | float       | YES  |     | NULL    |       |
| total_amount        | float       | YES  |     | NULL    |       |
| pickup_location_id  | varchar(16) | YES  |     | NULL    |       |
| dropoff_location_id | varchar(16) | YES  |     | NULL    |       |
+---------------------+-------------+------+-----+---------+-------+
17 rows in set (0.04 sec)
```

Query the `trips` table:
```
mysql> select distinct(pickup_location_id) from trips;
```
This will return an empty set as there is no data in the database yet.

Exit the `mysql` interactive console:
```
mysql> exit
```

#### Add data to Cloud SQL instance
Now you'll copy the New York City taxi trips CSV files stored on Cloud Storage locally. To keep resource usage low, you'll only be working with a subset of the data (~20,000 rows).

Run the following in the command line:
```
$ gsutil cp gs://cloud-training/OCBL013/nyc_tlc_yellow_trips_2018_subset_1.csv trips.csv-1
Copying gs://cloud-training/OCBL013/nyc_tlc_yellow_trips_2018_subset_1.csv...
/ [1 files][850.3 KiB/850.3 KiB]
Operation completed over 1 objects/850.3 KiB.

$ gsutil cp gs://cloud-training/OCBL013/nyc_tlc_yellow_trips_2018_subset_2.csv trips.csv-2
Copying gs://cloud-training/OCBL013/nyc_tlc_yellow_trips_2018_subset_2.csv...
/ [1 files][849.8 KiB/849.8 KiB]
Operation completed over 1 objects/849.8 KiB.
```
Import the CSV file data into Cloud SQL using `mysql`:
```
$ mysqlimport --local --host=$MYSQLIP --user=root --password --ignore-lines=1 --fields-terminated-by=',' bts trips.csv-*
Enter password:
bts.trips: Records: 10018  Deleted: 0  Skipped: 0  Warnings: 0
bts.trips: Records: 10006  Deleted: 0  Skipped: 0  Warnings: 0
```
When prompted for a password enter `Passw0rd`.

Connect to the `mysql` interactive console:
```
$ mysql --host=$MYSQLIP --user=root  --password
```
When prompted for a password enter `Passw0rd`.

#### Checking for data integrity
Whenever data is imported from a source it's always important to check for data integrity. Roughly, this means making sure the data meets your expectations.

In the `mysql` interactive console select the database:
```
mysql> use bts;
```
Query the `trips` table for unique pickup location regions:
```
mysql> select distinct(pickup_location_id) from trips;
159 rows in set (0.06 sec)
```

This should return 159 unique ids. Let's start by digging into the `trip_distance` column. Enter the following query into the console:
```
mysql> select
  max(trip_distance),
  min(trip_distance)
from
  trips;
+--------------------+--------------------+
| max(trip_distance) | min(trip_distance) |
+--------------------+--------------------+
|                 85 |                  0 |
+--------------------+--------------------+
1 row in set (0.05 sec)
```
One would expect the trip distance to be greater than 0 and less than, say 1000 miles. The maximum trip distance returned of 85 miles seems reasonable but the minimum trip distance of 0 seems buggy. How many trips in the dataset have a trip distance of 0?

```
mysql> select count(*) from trips where trip_distance = 0;
+----------+
| count(*) |
+----------+
|      155 |
+----------+
1 row in set (0.05 sec)
```

There are 155 such trips in the database. These trips warrant further exploration. You'll find that these trips have non-zero payment amounts associated with them. Perhaps these are fraudulent transactions? Let's see if we can find more data that doesn't meet our expectations. We expect the `fare_amount` column to be positive. Enter the following query to see if this is true in the database:

```
mysql> select count(*) from trips where fare_amount < 0;
+----------+
| count(*) |
+----------+
|       14 |
+----------+
1 row in set (0.05 sec)
```

There should be 14 such trips returned. Again, these trips warrant further exploration. There may be a reasonable explanation for why the fares take on negative numbers. However, it's up to the data engineer to ensure there are no bugs in the data pipeline that would cause such a result.

Finally, let's investigate the `payment_type` column.

```
mysql> select
  payment_type,
  count(*)
from
  trips
group by
  payment_type;
+--------------+----------+
| payment_type | count(*) |
+--------------+----------+
| 1            |    13863 |
| 2            |     6016 |
| 3            |      113 |
| 4            |       32 |
+--------------+----------+
4 rows in set (0.05 sec)
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




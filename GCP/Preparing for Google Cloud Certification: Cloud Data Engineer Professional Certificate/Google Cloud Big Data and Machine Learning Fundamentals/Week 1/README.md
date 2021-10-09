# Week 1

### Lab: Exploring a BigQuery Public Dataset
In this lab, you will explore publicly available datasets using BigQuery for big data analysis. Specifically you will:

- Query a public dataset
- Create a custom table
- Load data into a table
- Query a table


#### Reading: Google Cloud Public Datasets program
Google Cloud hosts over 150+ public datasets in BigQuery for exploration and use in applications

Take 5-10 minutes and read about the [program here](https://services.google.com/fh/files/misc/public_datasets_one_pager.pdf) and then continue with your first lab which will be exploring a public dataset in BigQuery

Additional Resources:

- [BigQuery use cases](https://cloud.google.com/bigquery/#bigquery-solutions-and-use-cases)
- [Google Cloud customers who use Big Data tools](https://cloud.google.com/customers/#/products=Big_Data_Analytics)

### Quiz: Module Review
**1. Question 1**

What are the common big data challenges that you will be building solutions for in this course? (check all that apply)

- [ ] Migrating existing on-premise workloads to the cloud
- [x] Analyzing large datasets at scale
- [ ] Building containerized applications for web development
- [ ] Building streaming data pipelines
- [x] Applying machine learning to your datasets


**2. Question 2**

You have a large enterprise that will likely have many teams using their own Google Cloud Platform projects and resources. What should you be sure to have to help manage and administer these resources? (check all that apply)

- [x] A defined Organization
- [x] Foldersfor teams and/or products
- [x] A defined access control policy with Cloud IAM
- [ ] A Kubernetes or Hadoop cluster for each project


**3. Question 3**

Which of the following is **NOT** one of the advantages of Google Cloud security

- [x] Google Cloud will automatically manage and curate your content and access policies to be safe for the public
- [ ] Google Cloud will secure the physical hardware that is running your applications and infrastructure
- [ ] Google Cloud has tools like Cloud IAM that help you administer and set company-wide security policies
- [ ] Google Cloud will manage audit logging of access and use of resources in your account


**4. Question 4**

If you don't have a large dataset of your own but still want to practice writing queries and building pipelines on Google Cloud Platform, what should you do?

- [x] Practice with the datasets in the Google Cloud Public Datasets program
- [x] Find other public datasets online and upload them into BigQuery
- [x] Work to create your own dataset and then upload it into BigQuery for analysis


**5. Question 5**

As you saw in the demo, Compute Engine nodes on GCP are:

- [x] Allocated on demand, and you pay for the time that they are up.
- [ ] Expensive to create and teardown
- [ ] One of ~50 choices in terms of CPU and memory
- [ ] Pre-installed with all the software packages you might ever need.

### Reading Module Resources
The cloud is a constantly changing environment and Google Cloud is continually evolving and releasing new products and features. It's a good idea to bookmark the below links to stay ahead of updates:
- [Google Cloud blog](https://cloud.google.com/blog/products)
- [Google Cloud big data product list](https://cloud.google.com/products/big-data/)
- [Google Cloud customers and case studies](https://cloud.google.com/customers/#/)

Need to practice SQL a bit more?
- [BigQuery standard SQL guide](https://cloud.google.com/bigquery/docs/reference/standard-sql/)
- [Qwiklabs BigQuery quest for Data Analysts](https://www.qwiklabs.com/quests/69)

Learn more about big data infrastructure:

- Compute Engine: https://cloud.google.com/compute/
- Storage: https://cloud.google.com/storage/
- Pricing: https://cloud.google.com/pricing/

We'll keep the module resources links up-to-date with the latest news and tips. Found a great blog post? Share it in the forums so everyone can benefit.

## Recommendation Systems

### Lab: Recommending Products Using Cloud SQL and Spark
In this lab, you populate rentals data in Cloud SQL for the rentals recommendation engine to use. The recommendations engine itself will run on Dataproc using Spark ML.

- Create Cloud SQL instance
- Create database tables by importing .sql files from Cloud Storage
- Populate the tables by importing .csv files from Cloud Storage
- Allow access to Cloud SQL
- Explore the rentals data using SQL statements from CloudShell

```
echo "Authorizing Cloud Dataproc to connect with Cloud SQL"
CLUSTER=rentals
CLOUDSQL=rentals
ZONE=us-central1-f
NWORKERS=2
machines="$CLUSTER-m"
for w in `seq 0 $(($NWORKERS - 1))`; do
   machines="$machines $CLUSTER-w-$w"
done
echo "Machines to authorize: $machines in $ZONE ... finding their IP addresses"
ips=""
for machine in $machines; do
    IP_ADDRESS=$(gcloud compute instances describe $machine --zone=$ZONE --format='value(networkInterfaces.accessConfigs[].natIP)' | sed "s/\['//g" | sed "s/'\]//g" )/32
    echo "IP address of $machine is $IP_ADDRESS"
    if [ -z  $ips ]; then
       ips=$IP_ADDRESS
    else
       ips="$ips,$IP_ADDRESS"
    fi
done
echo "Authorizing [$ips] to access cloudsql=$CLOUDSQL"
gcloud sql instances patch $CLOUDSQL --authorized-networks $ips
```

PySpark training job
```python
#!/usr/bin/env python
"""
Copyright Google Inc. 2016
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import os
import sys
import pickle
import itertools
from math import sqrt
from operator import add
from os.path import join, isfile, dirname
from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark.sql.types import StructType, StructField, StringType, FloatType

# MAKE EDITS HERE
CLOUDSQL_INSTANCE_IP = 'xxx.xxx.xxx.xxx'   # <---- CHANGE (database server IP)
CLOUDSQL_DB_NAME = 'recommendation_spark' # <--- leave as-is
CLOUDSQL_USER = 'root'  # <--- leave as-is
CLOUDSQL_PWD  = 'root'  # <---- CHANGE

# DO NOT MAKE EDITS BELOW
conf = SparkConf().setAppName("train_model")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

jdbcDriver = 'com.mysql.jdbc.Driver'
jdbcUrl    = 'jdbc:mysql://%s:3306/%s?user=%s&password=%s' % (CLOUDSQL_INSTANCE_IP, CLOUDSQL_DB_NAME, CLOUDSQL_USER, CLOUDSQL_PWD)

# checkpointing helps prevent stack overflow errors
sc.setCheckpointDir('checkpoint/')

# Read the ratings and accommodations data from Cloud SQL
dfRates = sqlContext.read.format('jdbc').options(driver=jdbcDriver, url=jdbcUrl, dbtable='Rating', useSSL='false').load()
dfAccos = sqlContext.read.format('jdbc').options(driver=jdbcDriver, url=jdbcUrl, dbtable='Accommodation', useSSL='false').load()
print("read ...")

# train the model
model = ALS.train(dfRates.rdd, 20, 20) # you could tune these numbers, but these are reasonable choices
print("trained ...")

# use this model to predict what the user would rate accommodations that she has not rated
allPredictions = None
for USER_ID in range(0, 100):
  dfUserRatings = dfRates.filter(dfRates.userId == USER_ID).rdd.map(lambda r: r.accoId).collect()
  rddPotential  = dfAccos.rdd.filter(lambda x: x[0] not in dfUserRatings)
  pairsPotential = rddPotential.map(lambda x: (USER_ID, x[0]))
  predictions = model.predictAll(pairsPotential).map(lambda p: (str(p[0]), str(p[1]), float(p[2])))
  predictions = predictions.takeOrdered(5, key=lambda x: -x[2]) # top 5
  print("predicted for user={0}".format(USER_ID))
  if (allPredictions == None):
    allPredictions = predictions
  else:
    allPredictions.extend(predictions)

# write them
schema = StructType([StructField("userId", StringType(), True), StructField("accoId", StringType(), True), StructField("prediction", FloatType(), True)])
dfToSave = sqlContext.createDataFrame(allPredictions, schema)
```

### Quiz: Module Review

**1. Question 1**

Complete the following:

You should feed your machine learning model your _______ and not your _______. It will learn those for itself!

- [ ] if/then statements, data
- [x] data, rules
- [ ] rules, data

**2. Question 2**

True or False: Cloud SQL is a big data analytics warehouse

- [ ] True
- [x] False

**3. Question 3**

True or False: If you are migrating your Hadoop workload to the cloud, you must first rewrite all your Spark jobs to be compliant with the cloud.

- [ ] True
- [x] False


**4. Question 4**

You are thinking about migrating your Hadoop workloads to the cloud and you have a few workloads that are fault-tolerant (they can handle interruptions of individual VMs gracefully). What are some architecture considerations you should explore in the cloud? Choose all that apply


- [x] Use PVMs or Preemptible Virtual Machines
- [x] Migrate your storage from on-cluster HDFS to off-cluster Google Cloud Storage (GCS)
- [x] Consider having multiple Cloud Dataproc instances for each priority workload and then turning them down when not in use


**5. Question 5**

Google Cloud Storage is a good option for storing data that:

(Select the2 correct options below).

- [ ] Is ingested in real-time from sensors and other devices and supports SQL-based queries
- [x] May be required to be read at some later time (i.e. load a CSV file into BigQuery)
- [x] May be imported from a bucket into a Hadoop cluster for analysis
- [ ] Will be accessed frequently and updated constantly with new transactions from a front-end and needs to be stored in a relational database


**6. Question 6**

Relational databases are a good choice when you need:

- [ ] Fast queries on terabytes of data
- [ ] Streaming, high-throughput writes
- [x] Transactional updates on relatively small datasets
- [ ] Aggregations on unstructured data


**7. Question 7**
Cloud SQL and Cloud Dataproc offer familiar tools (MySQL and Hadoop/Pig/Hive/Spark). What is the value-add provided by Google Cloud Platform?

(Select the 2 correct options below )


- [ ] Google-proprietary extensions and bug fixes to MySQL, Hadoop, and so on
- [x] Fully-managed versions of the software offer no-ops
- [x] Running it on Google infrastructure offers reliability and cost savings
- [ ] It’s the same API, but Google implements it better




### Reading: Module Resources

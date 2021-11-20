# Required Reading for Google Data Engineer Exam
Before taking the Google Professional Data Engineer exam, I recommend reading the documentation at the following links.

## Storage

### BigQuery

#### BigQuery

- Moving BigQuery data between locations https://cloud.google.com/bigquery/docs/locations#moving-data
- https://cloud.google.com/bigquery/docs/partitioned-tables
- https://cloud.google.com/bigquery/docs/clustered-tables
- https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions
- https://cloud.google.com/bigquery/docs/gis-intro
- Accessing historical data using time travel https://cloud.google.com/bigquery/docs/time-travel
- How to manage BigQuery flat-rate slots within a project https://cloud.google.com/blog/products/data-analytics/how-to-manage-bigquery-flat-rate-slots-within-a-project
- SQL MERGE examples https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#merge_statement
- Bigquery. Know what a federated table is. While you are at it, learn also about clustered tables.
https://cloud.google.com/bigquery/external-data-sources
- BigQuery + GCS. Know how to link tables between GCS and BigQuery as permanent tables and temporary tables.
https://cloud.google.com/bigquery/external-data-cloud-storage
- BigQuery query plan. BigQuery allows you to see the query plan and execution profile for queries that you run. Know the phases, difference between average and max time, why there can be skew in the plan, and how to optimize for it.
https://cloud.google.com/bigquery/query-plan-explanation
- table date range for bq. Accessing tables with dates and partitioned tables with functions like TABLE_DATE_RANGE, _TABLE_SUFFIX, TABLE_QUERY. https://stackoverflow.com/questions/22641894/bigquery-wildcard-using-table-date-range
- Syntax for wildcards in big query names. And in legacy SQL?
https://cloud.google.com/bigquery/docs/querying-wildcard-tables
- partitioning tables. Based on what are they partitioned — ingestion time, timestamp, date. How are they named? How are they then accessed in queries? Using _PARTITIONTIME. https://cloud.google.com/bigquery/docs/partitioned-tables

#### Security
- Basic roles for datasets https://cloud.google.com/bigquery/docs/access-control-basic-roles#dataset-basic-roles
- access at Table level.
https://cloud.google.com/blog/products/data-analytics/introducing-table-level-access-controls-in-bigquery

#### BigQuery Data Transfer Service

- https://cloud.google.com/bigquery/transfer/

#### BigQuery ML

- https://cloud.google.com/bigquery-ml/docs/bigqueryml-web-ui-start
- https://cloud.google.com/blog/products/data-analytics/simplified-data-transformations-for-machine-learning-in-bigquery

### Cloud Spanner

- https://cloud.google.com/spanner/docs/secondary-indexes
- https://cloud.google.com/spanner/docs/transactions#introduction (only read the Introduction)
- Schema design best practices https://cloud.google.com/spanner/docs/schema-design
- secondary index for cloud spanner. How indexes are created for you and how you can create secondary indexes.
https://cloud.google.com/spanner/docs/secondary-indexes

### Cloud Bigtable

- https://cloud.google.com/bigtable/docs/keyvis-overview
- row key scheme. What are the recommended ways for creating the row key? How do you avoid hotspotting? Should you use timestamp, and where? https://cloud.google.com/bigtable/docs/schema-design
- ways to optimize https://cloud.google.com/bigtable/docs/performance

### Cloud Datastore

- multiple indexes for datastore. Default indexes. Syntax for creating custom, composite indexes. https://cloud.google.com/datastore/docs/concepts/indexes
- https://cloud.google.com/datastore/docs/concepts/indexes
- https://cloud.google.com/datastore/docs/export-import-entities

## Other

### Cloud Composer

- https://cloud.google.com/composer/docs/concepts/overview

### Cloud AutoML

- AutoML Vision Beginner's guide https://cloud.google.com/automl/docs/

### Cloud Data Loss Prevention (DLP) 

- Supported cryptographic methods in Cloud DLP (only read this section) https://cloud.google.com/dlp/docs/pseudonymization#supported-methods

### Data Catalog

- https://cloud.google.com/data-catalog/docs/concepts/overview


### Kubeflow
- https://www.kubeflow.org/docs/about/kubeflow/

### Cloud Dataprep

- https://cloud.google.com/dataprep/docs/quickstarts/quickstart-dataprep
- Dataprep: jobs. How are Dataprep jobs created and run? What permissions do you need? A term I saw was that this is a more ‘casual’ way of data cleaning. Dataproc/Dataflow would be more programmatic and therefore ‘intense’, I suppose.
https://cloud.google.com/dataprep/docs/html/Jobs-Page_57344842

### Data Studio
- DataStudio: visualisation. What are the causes of stale data? And how do you get the latest? What caching options do you need to set?
- BigQuery+DataStudio — caching/pre-fetch cache. Learn how you connect DataStudio to storage solutions. Learn the difference between default caching (which cannot be disabled) and pre-fetch caching (which can be disabled). What is the difference between doing that with Viewer credentials and Owner credentials.
https://support.google.com/datastudio/answer/7020039?hl=en

### Pub/Sub

- https://cloud.google.com/pubsub/docs/monitoring
- At-Least-Once delivery https://cloud.google.com/pubsub/docs/subscriber#at-least-once-delivery
- https://cloud.google.com/pubsub/docs/pull#dupes
- https://cloud.google.com/pubsub/docs/replay-overview

### Cloud Dataflow

- Side inputs https://beam.apache.org/documentation/programming-guide/#side-inputs
- https://cloud.google.com/dataflow/docs/guides/templates/overview
- Dataflow developer mode. https://cloud.google.com/dataflow/docs/concepts/access-control


### Cloud Dataproc
- usage of gcs instead of existing file system. It is a best practice to use Google Cloud Storage instead of using HDFS. You can destroy the compute nodes after data crunching and save cost on them.
- https://cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage
- Dataproc: how to control scaling? Configure autoscaling?
https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling

### Edge TPU

- https://cloud.google.com/edge-tpu

### IAM
- Key Management Service. Using KMS with non-GCP products. Note that there is a default key management where Google manages all the keys, then there is a customer managed encryption keys, and also a customer supplied encryption keys.
https://cloud.google.com/kms/docs/

### Machine Learning
- feature crosses. Learn what these are and what issues it solves.
https://developers.google.com/machine-learning/crash-course/feature-crosses/video-lecture
- Go through the Coursera course on machine learning.
https://www.coursera.org/learn/serverless-machine-learning-gcp/home/welcome
- Dealing with overfitting.
https://developers.google.com/machine-learning/crash-course/generalization/peril-of-overfitting
- Regularization. What does it mean to increase or decrease regularization?
https://www.coursera.org/lecture/deep-neural-network/why-regularization-reduces-overfitting-T6OJj


### Other

- Avro file format. This is a compressed format that bigquery/dataflow can work with it directly.
https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro
- https://cloud.google.com/storage/docs/gsutil/commands/rsync
- https://cloud.google.com/logging/docs/export/aggregated_sinks

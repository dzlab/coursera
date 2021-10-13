# Week 2: Manage Data Pipelines with Cloud Data Fusion and Cloud Composer


## Cloud Data Fusion

### Lab: Building and executing a pipeline graph in Cloud Data Fusion
#### Overview
This tutorial shows you how to use the Wrangler and Data Pipeline features in Cloud Data Fusion to clean, transform, and process taxi trip data for further analysis.

What you learn
In this lab, you will:

- Connect Cloud Data Fusion to a couple of data sources
- Apply basic transformations
- Join two data sources
- Write data to a sink

#### Introduction
Often times, data needs go through a number of pre-processing steps before analysts can leverage the data to glean insights. For example, data types may need to be adjusted, anomalies removed, and vague identifiers may need to be converted to more meaningful entries. Cloud Data Fusion is a service for efficiently building ETL/ELT data pipelines. Cloud Data Fusion uses Cloud Dataproc cluster to perform all transforms in the pipeline.

The use of Cloud Data Fusion will be exemplified in this tutorial by using a subset of the NYC TLC Taxi Trips dataset on BigQuery.

#### Task 1: Creating a Cloud Data Fusion instance
Thorough directions for creating a Cloud Data Fusion instance can be found [here](https://cloud.google.com/data-fusion/docs/how-to/create-instance`). The essential steps are as follows:

1. To ensure the training environment is properly configured you must first stop and restart the Cloud Data Fusion API. Run the command below in the Cloud Shell. It will take a few minutes to complete.
```
$ gcloud services disable datafusion.googleapis.com
Operation "operations/acf.p17-444613618410-dc120640-8e4b-43ad-8eb7-144254d47a86" finished successfully.
```
2. Next, restart the connection to the Cloud Data Fusion API.
In the Google Cloud Console, enter Cloud Data Fusion API in the top search bar. Click on the result for Cloud Data Fusion API.

3. On the page that loads click Enable.
4. When the API has been enabled again, the page will refresh and show the option to disable the API along with other details on the API usage and performance.
5. On the Navigation menu, select Data Fusion.
6. To create a Cloud Data Fusion instance, click Create an Instance.
7. Enter a name for your instance.
8. Select Basic for the Edition type.
9. Under Authorization section, click Grant Permission.
10. Leave all other fields as their defaults and click Create.

> Note: Creation of the instance can take around 15 minutes.

11. Once the instance is created, you need one additional step to grant the service account associated with the instance permissions on your project. Navigate to the instance details page by clicking the instance name.

12. Copy the service account to your clipboard. e.g. `cloud-datafusion-management-sa@w515881f454fae40d-tp.iam.gserviceaccount.com`
13. In the GCP Console navigate to the IAM & Admin > IAM.
14. On the IAM Permissions page, add the service account you copied earlier as a new member and grant the Cloud Data Fusion API Service Agent role, by clicking the Add button.
15. Click Save.

#### Task 2: Loading the data
Once the Cloud Data Fusion instance is up and running, you can start using Cloud Data Fusion. However, before Cloud Data Fusion can start ingesting data you have to take some preliminary steps.

1. In this example, Cloud Data Fusion will read data out of a storage bucket. Open a [cloud shell console](https://cloud.google.com/shell/docs/starting-cloud-shell) and execute the following commands to create a new bucket and copy the relevant data into it:
```
export BUCKET=$GOOGLE_CLOUD_PROJECT
gsutil mb gs://$BUCKET
gsutil cp gs://cloud-training/OCBL017/ny-taxi-2018-sample.csv gs://$BUCKET
```
> Note: The created bucket name is your project id.

2. In the command line, execute the following command to create a bucket for temporary storage items that Cloud data Fusion will create.
```
gsutil mb gs://$BUCKET-temp
```
> Note: The created bucket name is your project id followed by "-temp".

3. Click the View Instance link on the Cloud Data Fusion instances page, or the details page of an instance. If prompted to take a tour of the service click on No, Thanks. You should now be in the Cloud Data Fusion UI.
> Note: You may need to reload or refresh the Cloud Fusion UI pages to allow prompt loading of the page.

4. Wrangler is an interactive, visual tool that lets you see the effects of transformations on a small subset of your data before dispatching large, parallel-processing jobs on the entire dataset. On the Cloud Data Fusion UI, choose Wrangler. On the left side, there is a panel with the pre-configured connections to your data, including the Cloud Storage connection.
5. Under Google Cloud Storage, select Cloud Storage Default.
6. Click on the bucket corresponding to your project name.
7. Select ny-taxi-2018-sample.csv. The data is loaded into the Wrangler screen in row/column form.

#### Task 3: Cleaning the data
Now, you will perform some transformations to parse and clean the taxi data.

1. To the left of the body column, click the Down arrow.
2. Click Parse > CSV, select Set first row as header and then click Apply. The data splits into multiple columns.
3. Because the body column isn't needed anymore, click the Down arrow next to the body column and choose Delete column.
4. You'll notice that all of the column types have been loaded in as String. Click the Down arrow next to the trip_distance column, select Change data type and then click on Float. Repeat for the total_amount column.
5. If you look at the data closely, you may find some anomalies, such as negative trip distances. You can avoid those negative values by filtering out in Wrangler. Click the Down arrow next to the trip_distance column and select Filter. Click if Custom condition and input >0.0
6. Click on Apply.

#### Task 4: Creating the pipeline
Basic data cleansing is now complete and you've run transformations on a subset of your data. You can now create a batch pipeline to run transformations on all your data.

Cloud Data Fusion translates your visually built pipeline into an Apache Spark or MapReduce program that executes transformations on an ephemeral Cloud Dataproc cluster in parallel. This enables you to easily execute complex transformations over vast quantities of data in a scalable, reliable manner, without having to wrestle with infrastructure and technology.

1. On the upper-right side of the Google Cloud Fusion UI, click Create a Pipeline.
2. In the dialog that appears, select Batch pipeline.
3. In the Data Pipelines UI, you will see a GCSFile source node connected to a Wrangler node. The Wrangler node contains all the transformations you applied in the Wrangler view captured as directive grammar. Hover over the Wrangler node and select Properties.
4. At this stage, you can apply more transformations by clicking the Wrangle button. Delete the extra column by pressing the red trashcan icon beside its name. To close the Wrangler tool click the X button in the top right corner.

#### Task 5: Adding a data source
The taxi data contains several cryptic columns such as `pickup_location_id`, that aren't immediately transparent to an analyst. You are going to add a data source to the pipeline that maps the `pickup_location_id` column to a relevant location name. The mapping information will be stored in a BigQuery table.

1. In a separate tab, [open the BigQuery UI in the GCP Console](https://console.cloud.google.com/bigquery). Click Done on the 'Welcome to BigQuery in the Cloud Console' launch page.
2. In the Explorer section of the BigQuery UI, click the three dots beside your GCP Project ID (it will start with qwiklabs).
3. On the menu that appears click the Create dataset link.
4. In the Dataset ID field type in trips.
5. Click on Create dataset.
6. To create the desired table in the newly created dataset, navigate to More > Query Settings. This process will ensure you can access your table from Cloud Data Fusion.
7. Select the item for Set a destination table for query results. Also, under Table name input zone_id_mapping. Click Save.
8. Enter the following query in the Query Editor and then click Run:
```sql
SELECT
  zone_id,
  zone_name,
  borough
FROM
  `bigquery-public-data.new_york_taxi_trips.taxi_zone_geom`
```
You can see that this table contains the mapping from zone_id to its name and borough.
9. Now, you will add a source in your pipeline to access this BigQuery table. Return to tab where you have Cloud Data Fusion open, from the Plugin palette on the left, select BigQuery from the Source section. A BigQuery source node appears on the canvas with the two other nodes.
10. Hover over the new BigQuery source node and click Properties.
11. To configure the Reference Name, enter zone_mapping, which is used to identify this data source for lineage purposes. The BigQuery Dataset and Table configurations are the Dataset and Table you setup in BigQuery a few steps earlier: trips and zone_id_mapping. For Temporary Bucket Name input the name of your project followed by "-temp", which corresponds to the bucket you created in Task 2.
12. To populate the schema of this table from BigQuery, click Get Schema. The fields will appear on the right side of the wizard.
13. To close the BigQuery Properties window click the X button in the top right corner.

#### Task 6: Joining two sources
Now you can join the two data sources—taxi trip data and zone names—to generate more meaningful output.

1. Under the Analytics section in the Plugin Palette, choose Joiner. A Joiner node appears on the canvas.
2. To connect the Wrangler node and the BigQuery node to the Joiner node: Drag a connection arrow > on the right edge of the source node and drop on the destination node.
3. To configure the Joiner node, which is similar to a SQL JOIN syntax:
- Click Properties of Joiner.
- Leave the label as Joiner.
- Change the Join Type to Inner
- Set the Join Condition to join the pickup_location_id column in the Wrangler node to the zone_id column in the BigQuery node.
- To generate the schema of the resultant join, click Get Schema.
- In the Output Schema table on the right, remove the zone_id and pickup_location_id fields by hitting the red garbage can icon.
- Close the window by clicking the X button in the top right corner.

#### Task 7: Storing the output to BigQuery
You will store the result of the pipeline into a BigQuery table. Where you store your data is called a sink.

1. In the Sink section of the Plugin Palette, choose BigQuery.
2. Connect the Joiner node to the BigQuery node. Drag a connection arrow > on the right edge of the source node and drop on the destination node.
3. Open the BigQuery node by hovering on it and then clicking Properties. You will next configure the node as shown below. You will use a configuration that's similar to the existing BigQuery source. Provide bq_insert for the Reference Name field and then use trips for the Dataset and the name of your project followed by "-temp" as Temporary Bucket Name. You will write to a new table that will be created for this pipeline execution. In Table field, enter trips_pickup_name.
4. Close the window by clicking the X button in the top right corner.

#### Task 8: Deploying and running the pipeline
At this point you have created your first pipeline and can deploy and run the pipeline.

1. Name your pipeline in the upper left corner of the Data Fusion UI and click Save.
2. Now you will deploy the pipeline. In the upper-right corner of the page, click Deploy.
3. On the next screen click Run to start processing data.
4. When you run a pipeline, Cloud Data Fusion provisions an ephemeral Cloud Dataproc cluster, runs the pipeline, and then tears down the cluster. This could take a few minutes. You can observe the status of the pipeline transition from Provisioning to Starting and from Starting to Running to Succeeded during this time.

![image](https://user-images.githubusercontent.com/1645304/137187341-b649e549-9ceb-4345-8a48-e9548b443b93.png)

![datafusion](https://user-images.githubusercontent.com/1645304/137188900-0208a7e7-8813-4636-9ab6-785cd9dc6a58.gif)


> Note: The pipeline can take 10-15 minutes to get succeeded.

#### Task 9: Viewing the results
To view the results after the pipeline runs:

1. Return to the tab where you have BigQuery open. Run the query below to see the values in the trips_pickup_name table.
```sql
SELECT
  *
FROM
  `trips.trips_pickup_name`
```

BQ RESULTS





### Quiz
**1. Question 1**

Cloud Data Fusion is the ideal solution when you need


- [ ] low-latency and high throughput processing of streaming data
- [x] to build visual pipelines
- [ ] a data warehousing solution
- [ ] to resuse spark pipelines

## Data Processing with Cloud Dataflow

### Quiz
**1. Question 1**

Which of the following statements are true?

 
(Select all  2 correct responses)

- [x] Dataflow executes Apache Beam pipelines
- [ ] Side-inputs in Dataflow are a way to export data from one pipeline to share with another pipeline
- [ ] Map operations in a MapReduce can be performed by Combine transforms in Dataflow
- [x] Dataflow transforms support both batch and streaming pipelines


**2. Question 2**
Match each of the Dataflow terms with what they do in the life of a dataflow job:

|Term|Definition
|-|-|
|__ 1. Transform|A. Output endpoint for your pipeline
|__ 2. PCollection|B. A data processing operation or step in your pipeline
|__ 3. Sink|C. A set of data in your pipeline

- [x] 
  1. B
  2. C
  3. A
- [ ] 
  1. C
  2. B
  3. A
- [ ] 
  1. A
  2. C
  3. B
- [ ] 
  1. B
  2. A
  3. C



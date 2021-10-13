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



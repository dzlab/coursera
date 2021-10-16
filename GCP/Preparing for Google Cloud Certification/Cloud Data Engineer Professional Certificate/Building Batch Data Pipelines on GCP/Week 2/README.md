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


## Cloud Composer
### Lab: An Introduction to Cloud Composer
Resource:
- [Flexible, Easy Data Pipelines on Google Cloud with Cloud Compooser (NEXT'18)](https://www.youtube.com/watch?v=GeNFEtt-D4k)


#### Overview
Workflows are a common theme in data analytics - they involve ingesting, transforming, and analyzing data to figure out the meaningful information within. In Google Cloud Platform (GCP), the tool for hosting workflows is Cloud Composer which is a hosted version of the popular open source workflow tool Apache Airflow.

In this lab, you use the GCP Console to set up a Cloud Composer environment. You then use Cloud Composer to go through a simple workflow that verifies the existence of a data file, creates a Cloud Dataproc cluster, runs an Apache Hadoop wordcount job on the Cloud Dataproc cluster, and deletes the Cloud Dataproc cluster afterwards.

What you'll do
- Use GCP Console to create the Cloud Composer environment
- View and run the DAG (Directed Acyclic Graph) in the Airflow web interface
- View the results of the wordcount job in storage.

#### Ensure that the Kubernetes Engine API is successfully enabled
To ensure access to the necessary APIs, restart the connection to the Kubernetes Engine API.

1. In the Google Cloud Console, enter Kubernetes Engine API in the top search bar. Click on the result for Kubernetes Engine API.
2. Click Manage.
3. Click Disable API.

If asked to confirm, click Disable.

Again, when prompted Do you want to disable Kubernetes Engine API and its dependent APIs?, Click Disable.

4. Click Enable.

When the API has been enabled again, the page will show the option to disable.

#### Ensure that the Cloud Composer API is successfully enabled
Restart the connection to the Cloud Composer API. In the prior step, restarting the Kubernetes Engine API forced the Cloud Composer API to be disabled.

1. In the Google Cloud Console, enter Cloud Composer API in the top search bar. Click on the result for Cloud Composer API.
2. Click Enable.

When the API has been enabled again, the page will show the option to disable.

#### Create Cloud Composer environment
In this section, you create a Cloud Composer environment.

> Before proceeding further, make sure that you have performed earlier tasks to ensure that the required APIs are successfully enabled. If not, then please perform those tasks otherwise Cloud Composer environment creation will fail.

1. Go to Navigation menu > Composer:
2. Click CREATE ENVIRONMENT and set the following for your environment:

|Property|	Value|
|-|-|
|Name|	highcpu|
|Location|	us-central1|
|Zone|	us-central1-a|
|Machine type||	n1-highcpu-4|

Leave all other settings as default.

3. Click Create.

The environment creation process is completed when the green checkmark displays to the left of the environment name on the Environments page in the GCP Console.

It can take 10-20 minutes for the environment to complete the setup process. Continue with the lab while the environment spins up.

##### Create a Cloud Storage bucket
Create a Cloud Storage bucket in your project. This buckets will be used as output for the Hadoop job from Dataproc.

1. Go to Navigation menu > Cloud Storage > Browser and then click Create bucket.
2. Give your bucket a universally unique name, then click Create.

Remember the Cloud Storage bucket name as you'll use it as an Airflow variable later in the lab.

#### Airflow and core concepts
While waiting for your Composer environment to get created, review some terms that are used with Airflow.

[Airflow](https://airflow.apache.org/) is a platform to programmatically author, schedule and monitor workflows.

Use Airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The airflow scheduler executes your tasks on an array of workers while following the specified dependencies.

##### Core concepts
[DAG](https://airflow.apache.org/concepts.html#dags)

A Directed Acyclic Graph is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies.

[Operator](https://airflow.apache.org/concepts.html#operators)

The description of a single task, it is usually atomic. For example, the BashOperator is used to execute bash command.

[Task](https://airflow.apache.org/concepts.html#tasks)

A parameterised instance of an Operator; a node in the DAG.

[Task Instance](https://airflow.apache.org/concepts.html#task-instances)

A specific run of a task; characterized as: a DAG, a Task, and a point in time. It has an indicative state: running, success, failed, skipped, ...

You can read more about the concepts [here](https://airflow.apache.org/concepts.html#).

#### Defining the workflow
Now let's discuss the workflow you'll be using. Cloud Composer workflows are comprised of [DAGs (Directed Acyclic Graphs)](https://airflow.incubator.apache.org/concepts.html#dags). DAGs are defined in standard Python files that are placed in Airflow's DAG_FOLDER. Airflow will execute the code in each file to dynamically build the DAG objects. You can have as many DAGs as you want, each describing an arbitrary number of tasks. In general, each one should correspond to a single logical workflow.

Below is the `hadoop_tutorial.py` workflow code, also referred to as the DAG:

```python
"""Example Airflow DAG that creates a Cloud Dataproc cluster, runs the Hadoop
wordcount example, and deletes the cluster.
This DAG relies on three Airflow variables
https://airflow.apache.org/concepts.html#variables
* gcp_project - Google Cloud Project to use for the Cloud Dataproc cluster.
* gce_zone - Google Compute Engine zone where Cloud Dataproc cluster should be
  created.
* gcs_bucket - Google Cloud Storage bucket to used as output for the Hadoop jobs from Dataproc.
  See https://cloud.google.com/storage/docs/creating-buckets for creating a
  bucket.
"""
import datetime
import os
from airflow import models
from airflow.contrib.operators import dataproc_operator
from airflow.utils import trigger_rule
# Output file for Cloud Dataproc job.
output_file = os.path.join(
    models.Variable.get('gcs_bucket'), 'wordcount',
    datetime.datetime.now().strftime('%Y%m%d-%H%M%S')) + os.sep
# Path to Hadoop wordcount example available on every Dataproc cluster.
WORDCOUNT_JAR = (
    'file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'
)
# Arguments to pass to Cloud Dataproc job.
wordcount_args = ['wordcount', 'gs://pub/shakespeare/rose.txt', output_file]
yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time())
default_dag_args = {
    # Setting start date as yesterday starts the DAG immediately when it is
    # detected in the Cloud Storage bucket.
    'start_date': yesterday,
    # To email on failure or retry set 'email' arg to your email and enable
    # emailing here.
    'email_on_failure': False,
    'email_on_retry': False,
    # If a task fails, retry it once after waiting at least 5 minutes
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
    'project_id': models.Variable.get('gcp_project')
}
with models.DAG(
        'composer_sample_quickstart',
        # Continue to run DAG once per day
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args) as dag:
    # Create a Cloud Dataproc cluster.
    create_dataproc_cluster = dataproc_operator.DataprocClusterCreateOperator(
        task_id='create_dataproc_cluster',
        # Give the cluster a unique name by appending the date scheduled.
        # See https://airflow.apache.org/code.html#default-variables
        cluster_name='composer-hadoop-tutorial-cluster-{{ ds_nodash }}',
        num_workers=2,
        region='us-central1',
        zone=models.Variable.get('gce_zone'),
        image_version='2.0',
        master_machine_type='n1-standard-2',
        worker_machine_type='n1-standard-2')
    # Run the Hadoop wordcount example installed on the Cloud Dataproc cluster
    # master node.
    run_dataproc_hadoop = dataproc_operator.DataProcHadoopOperator(
        task_id='run_dataproc_hadoop',
        region='us-central1',
        main_jar=WORDCOUNT_JAR,
        cluster_name='composer-hadoop-tutorial-cluster-{{ ds_nodash }}',
        arguments=wordcount_args)
    # Delete Cloud Dataproc cluster.
    delete_dataproc_cluster = dataproc_operator.DataprocClusterDeleteOperator(
        task_id='delete_dataproc_cluster',
        region='us-central1',
        cluster_name='composer-hadoop-tutorial-cluster-{{ ds_nodash }}',
        # Setting trigger_rule to ALL_DONE causes the cluster to be deleted
        # even if the Dataproc job fails.
        trigger_rule=trigger_rule.TriggerRule.ALL_DONE)
    # Define DAG dependencies.
    create_dataproc_cluster >> run_dataproc_hadoop >> delete_dataproc_cluster
```

To orchestrate the three workflow tasks, the DAG imports the following operators:

1. `DataprocClusterCreateOperator`: Creates a Cloud Dataproc cluster.
2. `DataProcHadoopOperator`: Submits a Hadoop wordcount job and writes results to a Cloud Storage bucket.
3. `DataprocClusterDeleteOperator`: Deletes the cluster to avoid incurring ongoing Compute Engine charges.

The tasks run sequentially, which you can see in this section of the file:
```
# Define DAG dependencies.
create_dataproc_cluster >> run_dataproc_hadoop >> delete_dataproc_cluster
```

The name of the DAG is `quickstart`, and the DAG runs once each day.

```python
with models.DAG(
        'composer_sample_quickstart',
        # Continue to run DAG once per day
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args) as dag:
```

Because the `start_date` that is passed in to `default_dag_args` is set to `yesterday`, Cloud Composer schedules the workflow to start immediately after the DAG uploads.

#### Viewing environment information
1. Go back to Composer to check the status of your environment.

2. Once your environment has been created, click the name of the environment (highcpu) to see its details.

On the Environment details you'll see information such as the Airflow web interface URL, Kubernetes Engine cluster ID, and a link to the DAGs folder, which is stored in your bucket.

> Note: Cloud Composer only schedules the workflows in the /dags folder.


#### Using the Airflow UI
To access the Airflow web interface using the GCP Console:

1. Go back to the Environments page.
2. In the Airflow webserver column for the environment, click Airflow.
3. Click on your lab credentials.
4. The Airflow web interface opens in a new browser window.

#### Setting Airflow variables
Airflow variables are an Airflow-specific concept that is distinct from [environment variables](https://cloud.google.com/composer/docs/how-to/managing/environment-variables).

1. Select Admin > Variables from the Airflow menu bar, then Create.
2. Create the following Airflow variables, gcp_project, gcs_bucket, and gce_zone:

|KEY|	VALUE|	Details|
|-|-|-|
|gcp_project|	<your project-id>|	The Google Cloud Platform project you're using for this quickstart.|
|gcs_bucket|	gs://<my-bucket>|	Replace <my-bucket> with the name of the Cloud Storage bucket you made earlier. This bucket stores the output from the Hadoop jobs from Dataproc.|
|gce_zone|	us-central1-a|	This is the Compute Engine zone where your Cloud Dataproc cluster will be created. To chose a different zone, see [Available regions & zones](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available).|

Click Save and Add Another after adding first two variable and click Save for the third variable. Your Variables table should look like this when you're finished:
![image](https://user-images.githubusercontent.com/1645304/137205558-1cc7e174-a3c5-41c7-8e52-d4ac455ab3a3.png)

#### Uploading the DAG to Cloud Storage
To upload the DAG:

1. In Cloud Shell, upload a copy of the hadoop_tutorial.py file to the Cloud Storage bucket that was automatically created when you created the environment.

Replace <DAGs_folder_path> in the following command:
  
```
gsutil cp gs://cloud-training/datawarehousing/lab_assets/hadoop_tutorial.py <DAGs_folder_path>
```
  
with the path to the DAGs folder. You can get the path by going to Composer. Click on the environment you created earlier and then click on the Environment Configuration tab to see the details of the environment. Find DAGs folder and copy the path.  
  
The revised command to upload the file will look similar to the one below:  
```
gsutil cp gs://cloud-training/datawarehousing/lab_assets/hadoop_tutorial.py gs://us-central1-highcpu-0682d8c0-bucket/dags
```
Once the file has been successfully uploaded to the DAGs directory, open dags folder in the bucket and you will see the file in the Objects tab of the Bucket details.

![image](https://user-images.githubusercontent.com/1645304/137205822-2e22997c-1b9b-4d4d-9eac-bfb71891117c.png)  

When a DAG file is added to the DAGs folder, Cloud Composer adds the DAG to Airflow and schedules it automatically. DAG changes occur within 3-5 minutes.

You can see the task status of the composer_hadoop_tutorial DAG in the Airflow web interface.

##### Exploring DAG runs
When you upload your DAG file to the dags folder in Cloud Storage, Cloud Composer parses the file. If no errors are found, the name of the workflow appears in the DAG listing, and the workflow is queued to run immediately.

Make sure that you're on the DAGs tab in the Airflow web interface. It takes several minutes for this process to complete. Refresh your browser to make sure you're looking at the latest information.

![image](https://user-images.githubusercontent.com/1645304/137206029-706bf821-77a8-49c7-9270-987f73b74275.png)

1. In Airflow, click composer_hadoop_tutorial to open the DAG details page. This page includes several representations of the workflow tasks and dependencies.
![image](https://user-images.githubusercontent.com/1645304/137206090-5c915e26-f2dc-464b-960d-25e8157eb0fa.png)

2. In the toolbar, click Graph View. Mouseover the graphic for each task to see its status. Note that the border around each task also indicates the status (green border = running; red = failed, etc.).
![image](https://user-images.githubusercontent.com/1645304/137206155-b6e6848e-300e-49e5-ae68-0d91aeb115c4.png)

3. Click the "Refresh" link to make sure you're looking at the most recent information. The borders of the processes change colors as the state of the process changes

> Note: If your Dataproc cluster already exists, you can run the workflow again to reach the success state by clicking create_dataproc_cluster graphic and then click Clear to reset the three tasks and click OK to confirm.

4. Once the status for create_dataproc_cluster has changed to "running", go to Navigation menu > Dataproc, then click on:

  - Clusters to monitor cluster creation and deletion. The cluster created by the workflow is ephemeral: it only exists for the duration of the workflow and is deleted as part of the last workflow task.

  - Jobs to monitor the Apache Hadoop wordcount job. Click the Job ID to see job log output.  
5. Once Dataproc gets to a state of "Running", return to Airflow and click Refresh to see that the cluster is complete.

When the run_dataproc_hadoop process is complete, go to Navigation menu > Cloud Storage > Browser and click on the name of your bucket to see the results of the wordcount in the wordcount folder.

6. Once all the steps are complete in the DAG, each step has a dark green border. Additionally the Dataproc cluster that was created is now deleted.

![image](https://user-images.githubusercontent.com/1645304/137207603-104d7e2c-6af6-4ea6-95e4-d22b4139880d.png)

#### Next steps
- Check out when Cloud Composer was presented at NEXT 18 in San Francisco: https://www.youtube.com/watch?v=GeNFEtt-D4k
- To see the value of a variable, run the Airflow CLI sub-command [variables](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#variables) with the get argument or use the [Airflow web interface](https://cloud.google.com/composer/docs/quickstart#variables-ui).
- For information about the Airflow web interface, see [Accessing the web interface](https://cloud.google.com/composer/docs/how-to/accessing/airflow-web-interface#accessing_the_web_interface).  
  
### Quiz: Cloud Data Fusion and Cloud Composer
**1. Question 1**

Cloud Data Fusion is the ideal solution when you need


- [ ] low-latency and high throughput processing of streaming data
- [x] to build visual pipelines
- [ ] a data warehousing solution
- [ ] to resuse spark pipelines

## Running batch processing pipelines on Cloud Dataflow

### Quiz: Data Processing with Cloud Dataflow

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



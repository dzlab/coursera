# Lab Serverless Data Analysis with Dataflow: Side Inputs (Python)

## Overview
In this lab, you learn how to load data into BigQuery and run complex queries. Next, you will execute a Dataflow pipeline that can carry out Map and Reduce operations, use side inputs and stream into BigQuery.

## Objective
In this lab, you learn how to use BigQuery as a data source into Dataflow, and how to use the results of a pipeline as a side input to another pipeline.

- Read data from BigQuery into Dataflow
- Use the output of a pipeline as a side-input to another pipeline

## Task 1. Preparation
For this lab, you will need the training-data-analyst files.

### Verify that the repository files are in Cloud Shell
1. Clone the repository from the Cloud Shell command line:
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

2. You should see the training-data-analyst directory.

### Verify that you have a Cloud Storage bucket
If you don't have a bucket, you can follow these instructions to create a bucket.

3. In the Console, on the Navigation menu (7a91d354499ac9f1.png), click Home.
4. Select and copy the Project ID. For simplicity, you will use the Qwiklabs Project ID, which is already globally unique, as the bucket name.
5. In the Console, on the Navigation menu (7a91d354499ac9f1.png), click Cloud Storage > Browser.
6. Click Create Bucket.
7. Specify the following, and leave the remaining settings as their defaults:

|Property|	Value (type value or select option as specified)|
|-|-|
|Name|	`<your unique bucket name (Project ID)>`|
Default storage class|	Multi-Regional|
Location|	`<Your location>`|

8. Click Create.

9. Record the name of your bucket. You will need it in subsequent tasks.

10. In Cloud Shell enter the following to create an environment variable named "BUCKET" and verify that it exists with the echo command.
```
BUCKET=$(gcloud config get-value project)
echo $BUCKET
```
You can use $BUCKET in Cloud Shell commands. And if you need to enter the bucket name `<your-bucket>` in a text field in Console, you can quickly retrieve the name with echo $BUCKET.

### Verify environment variable for your Project ID
1. Cloud Shell creates a default environment variable that contains the current Project ID.
```
echo $DEVSHELL_PROJECT_ID
```

### Verify that Apache Beam is installed on Cloud Shell
2. Return to Cloud Shell. Verify that Apache Beam is installed on Cloud Shell. If the Cloud Shell has timed out and was reconnected, it may have lost the in-memory components of Apache Beam. There is no harm in reinstalling. It will take the necessary steps.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
sudo ./install_packages.sh
```

## Task 2. Try using BigQuery query
1. In the console, on the Navigation menu, click BigQuery.

2. If prompted click Done.

3. Click Compose new query and type the following query.
```
SELECT
  content
FROM
  `fh-bigquery.github_extracts.contents_java_2016`
LIMIT
  10
```
4. Click on Run.

What is being returned?

The BigQuery table `fh-bigquery.github_extracts.contents_java_2016` contains the content (and some metadata) of all the Java files present in GitHub in 2016.

To find out how many Java files this table has, type the following query and click Run:
```
SELECT
  COUNT(*)
FROM
  `fh-bigquery.github_extracts.contents_java_2016`
```

Why do you think zero bytes of data were processed to return the result?

- [ ] There were 0 records returned in the result.
- [x] BigQuery stores common metadata about the table (like row count). Querying metadata processes 0 bytes.
- [ ] This dataset is not properly setup for billing.
- [ ] Cache is enabled so all queries process 0 bytes.

How many files are there in this dataset?

Is this a dataset you want to process locally or on the cloud?

## Task 3. Explore the pipeline code
1. In Cloud Shell editor, or in Cloud Shell, navigate to the lab directory:
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
```
2. View the pipeline code using Cloud Shell editor or nano. Do not make any changes to the code.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
nano JavaProjectsThatNeedHelp.py
```

Refer to this diagram as you read the code. The pipeline looks like this:

![image](https://user-images.githubusercontent.com/1645304/137598135-461b48a3-bc01-4ff0-ad09-4f5c2312a8c3.png)


Answer the following questions:

- Looking at the class documentation at the very top, what is the purpose of this pipeline?
- Where does the content come from?
- What does the left side of the pipeline do?
- What does the right side of the pipeline do?
- What does ToLines do? (Hint: look at the content field of the BigQuery result)
- Why is the result of ReadFromBQ stored in a named PCollection instead of being directly passed to another step?
- What are the two actions carried out on the PCollection generated from ReadFromBQ?
- If a file has 3 FIXMEs and 2 TODOs in its content (on different lines), how many calls for help are associated with it?
- If a file is in the package com.google.devtools.build, what are the packages that it is associated with?
- popular_packages and help_packages are both named PCollections and both used in the Scores (side inputs) step of the pipeline. Which one is the main input and which is the side input?
- What is the method used in the Scores step?
- What Python data type is the side input converted into in the Scores step?

> The Java version of this program is slightly different from the Python version. The Java SDK supports AsMap and the Python SDK doesn't. It supports AsDict instead. In Java, the PCollection is converted into a View as a preparatory step before it is used. In Python, the PCollection conversion occurs in the step where it is used.

## Task 4. Execute the pipeline
1. Change into the directory:
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
```

2. The program requires BUCKET and PROJECT values and choosing whether to run the pipeline locally using `--DirectRunner` or on the cloud using `--DataFlowRunner`

3. Execute the pipeline locally by typing the following into Cloud Shell.
```
python3 JavaProjectsThatNeedHelp.py --bucket $BUCKET --project $DEVSHELL_PROJECT_ID --DirectRunner
```

> Note: Please ignore the warning if any and move forward.

4. Once the pipeline has finished executing, On the Navigation menu (7a91d354499ac9f1.png), click Cloud Storage > Browser and click on your bucket. You will find the results in the javahelp folder. Click on the Result object to examine the output.

5. Execute the pipeline on the cloud by typing the following into Cloud Shell.
```
$ python3 JavaProjectsThatNeedHelp.py --bucket $BUCKET --project $DEVSHELL_PROJECT_ID --DataFlowRunner
JavaProjectsThatNeedHelp.py:163: BeamDeprecationWarning: BigQuerySource is deprecated since 2.25.0. Use ReadFromBigQuery instead.
  bigqcollection = p | 'ReadFromBQ' >> beam.io.Read(beam.io.BigQuerySource(project=project,query=get_java_query))
/usr/local/lib/python3.7/dist-packages/apache_beam/io/gcp/bigquery.py:1881: BeamDeprecationWarning: options is deprecated since First stable release. References to <pipeline>.options will not be supported
  temp_location = pcoll.pipeline.options.view_as(
WARNING:apache_beam.io.gcp.bigquery_tools:Dataset qwiklabs-gcp-00-4844b6de667d:temp_dataset_098da2cd13584b6b8b00e6af09cb40aa does not exist so we will create it as temporary with location=US
```

> Note: Please ignore the warning if any and move forward.

6. Return to the browser tab for Console. On the Navigation menu, click **Dataflow** and click on your job to monitor progress.
7. Once the pipeline has finished executing, On the Navigation menu click **Cloud Storage** > **Browser** and click on your bucket. You will find the results in the javahelp folder. Click on the **Result** object to examine the output.


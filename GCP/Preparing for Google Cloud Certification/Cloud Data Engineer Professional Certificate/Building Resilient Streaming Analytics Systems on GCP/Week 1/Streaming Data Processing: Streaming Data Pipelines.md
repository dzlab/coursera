# Lab: Streaming Data Processing: Streaming Data Pipelines

## Overview
In this lab, you will use Dataflow to collect traffic events from simulated traffic sensor data made available through Google Cloud PubSub, process them into an actionable average, and store the raw data in BigQuery for later analysis. You will learn how to start a Dataflow pipeline, monitor it, and, lastly, optimize it.

> At the time of this writing, streaming pipelines are not available in the DataFlow Python SDK. So the streaming labs are written in Java.

## Objectives
In this lab, you will perform the following tasks:

- Launch Dataflow and run a Dataflow job
- Understand how data elements flow through the transformations of a Dataflow pipeline
- Connect Dataflow to Pub/Sub and BigQuery
- Observe and understand how Dataflow autoscaling adjusts compute resources to process input data optimally
- Learn where to find logging information created by Dataflow
- Explore metrics and create alerts and dashboards with Cloud Monitoring

## Task 1: Preparation
You will be running a sensor simulator from the training VM. In Lab 1 you manually setup the Pub/Sub components. In this lab several of those processes are automated.

### Open the SSH terminal and connect to the training VM
1. In the Console, on the Navigation menu ( 7a91d354499ac9f1.png), click Compute Engine > VM instances.

2. Locate the line with the instance called training-vm.

3. On the far right, under Connect, click on SSH to open a terminal window.

4. In this lab, you will enter CLI commands on the training-vm.

### Verify initialization is complete
5. The training-vm is installing some software in the background. Verify that setup is complete by checking the contents of the new directory.
```
ls /training
```

The setup is complete when the result of your list (ls) command output appears as in the image below. If the full listing does not appear, wait a few minutes and try again. Note: It may take 2 to 3 minutes for all background actions to complete.

![image](https://user-images.githubusercontent.com/1645304/137612957-04bef39b-cd7a-473c-80db-77e142ddb231.png)

### Download Code Repository
6. Next you will download a code repository for use in this lab.
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

### Set environment variables
7. On the training-vm SSH terminal enter the following:
```
source /training/project_env.sh
```
This script sets the `DEVSHELL_PROJECT_ID` and `BUCKET` environment variables.

## Task 2: Create a BigQuery Dataset and Cloud Storage Bucket
The Dataflow pipeline will be created later and will write into a table in the BigQuery dataset.

## Create a BigQuery Dataset
### Open BigQuery Console
In the Google Cloud Console, select Navigation menu > Big Data > BigQuery:

![image](https://user-images.githubusercontent.com/1645304/137613105-c8a9f628-a7bc-4dad-add6-e0892929ff9b.png)

The Welcome to BigQuery in the Cloud Console message box opens. This message box provides a link to the quickstart guide and lists UI updates.

Click Done.

1. To create a dataset, click on the View actions icon next to your project ID and select Create dataset
CD.png

![image](https://user-images.githubusercontent.com/1645304/137613122-1c1ff078-65a1-46a8-8c3d-f0eae61eeb3e.png)

2. Next, name your Dataset ID **demos** and leave all other options at their default values, and then click Create dataset.

![image](https://user-images.githubusercontent.com/1645304/137613133-d2e3b345-e6aa-4ef0-9a4d-6a192b598cbb.png)

### Verify the Cloud Storage Bucket
A bucket should already exist that has the same name as the Project ID.

3. In the Console, on the Navigation menu, click **Cloud Storage > Browser**.

4. Observe the following values:

|Property|Value (type value or select option as specified)|
|-|-|
|Name|`<Same as the Project ID>`|
|Default storage class|Regional|
|Location|us-central1|

## Task 3: Simulate traffic sensor data into Pub/Sub
1/ In the training-vm SSH terminal, start the sensor simulator. The script reads sample data from a CSV file and publishes it to Pub/Sub.
```
/training/sensor_magic.sh
```
This command will send 1 hour of data in 1 minute. Let the script continue to run in the current terminal.

### Open a second SSH terminal and connect to the training VM
In the upper right corner of the training-vm SSH terminal, click on the gear-shaped button ( 9649d58acf1c4e06.png) and select New Connection to training-vm from the drop-down menu. A new terminal window will open.

![image](https://user-images.githubusercontent.com/1645304/137613217-a40acfc7-c955-49a1-87cf-25c5a99916d7.png)


3. The new terminal session will not have the required environment variables. Run the following command to set them.

4. In the new training-vm SSH terminal enter the following:
```
source /training/project_env.sh
```

## Task 4: Launch Dataflow Pipeline
### Verify that Google Cloud Dataflow API is enabled for this project
1. Return to the browser tab for Console. In the top search bar, enter Dataflow API. This will take you to the page, Navigation menu > APIs & Services > Dashboard > Dataflow API. It will either show status information or it will give you the option to Enable the API.

2. If necessary, Enable the API.

3. Return to the second training-vm SSH terminal. Change into the directory for this lab.
```
cd ~/training-data-analyst/courses/streaming/process/sandiego
```

4. Identify the script that creates and runs the Dataflow pipeline.
```
cat run_oncloud.sh
```

5. Copy-and-paste the following URL into a new browser tab to view the source code on Github.
```
https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/streaming/process/sandiego/run_oncloud.sh
```

6. The script requires three arguments: project id, bucket name, classname

A 4th optional argument is options. The options argument discussed later in this lab.

|||
|-|-|
|project id|`<your Project ID>`|
|bucket name|`<your Bucket Name>`|
|classname|`<java file that runs aggregations>`|
|options|`<options>`|

There are 4 java files that you can choose from for classname. Each reads the traffic data from Pub/Sub and runs different aggregations/computations.

7. Go into the java directory. Identify the source file AverageSpeeds.java.
```
cd ~/training-data-analyst/courses/streaming/process/sandiego/src/main/java/com/google/cloud/training/dataanalyst/sandiego
cat AverageSpeeds.java
```
What does the script do?

Close the file to continue. You will want to refer to this source code while running the application. So for easy access you will open a new browser tab and view the file AverageSpeeds.java on Github.

8. Copy-and-paste the following URL into a browser tab to view the source code on Github.
```
https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/streaming/process/sandiego/src/main/java/com/google/cloud/training/dataanalyst/sandiego/AverageSpeeds.java
```
Leave this browser tab open. You will be referring back to the source code in a later step in this lab.

9. Return to the training-vm SSH terminal. Run the Dataflow pipeline to read from PubSub and write into BigQuery.
```
cd ~/training-data-analyst/courses/streaming/process/sandiego
./run_oncloud.sh $DEVSHELL_PROJECT_ID $BUCKET AverageSpeeds
```

This script uses maven to build a Dataflow streaming pipeline in Java.

Example successful completion:
```
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 45.542 s
[INFO] Finished at: 2018-06-08T16:51:30+00:00
[INFO] Final Memory: 56M/216M
[INFO] ------------------------------------------------------------------------
```


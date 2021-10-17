# Lab: Streaming Data Processing: Streaming Analytics and Dashboards

## Overview
Data visualization tools can help you make sense of your BigQuery data and help you analyze the data interactively. You can use visualization tools to help you identify trends, respond to them, and make predictions using your data. In this lab, you use Google Data Studio to visualize data in the BigQuery table populated by your Dataflow pipeline in the previous exercise.

> At the time of this writing, streaming pipelines are not available in the DataFlow Python SDK. So the streaming labs are written in Java.

## Objectives
In this lab, you will perform the following tasks:

- Connect to a BigQuery data source
- Create reports and charts to visualize BigQuery data

This lab uses Google Data Studio to visualize data in BigQuery using the BigQuery connector. In subsequent tasks, you will create a data source, a report, and charts that visualize data in the sample table.

## Task 1: Preparation
You will be running a sensor simulator from the training VM. There are several files and some setup of the environment required.

### Open the SSH terminal and connect to the training VM
1. In the Console, on the Navigation menu (7a91d354499ac9f1.png), click Compute Engine > VM instances.

2. Locate the line with the instance called training-vm.

3. On the right, under 'Connect' column, click on SSH to open a terminal window.

4. In this lab, you will enter CLI commands on the training-vm.

### Verify initialization is complete
5. The training-vm is installing some software in the background. Verify that setup is complete by checking the contents of the new directory.
```
ls /training
```

The setup is complete when the result of your list (ls) command output appears as in the image below. If the full listing does not appear, wait a few minutes and try again. Note: It may take 2 to 3 minutes for all background actions to complete.

![image](https://user-images.githubusercontent.com/1645304/137638213-4c500494-68ee-465d-800b-e4e084ebf7fc.png)

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
This script sets the `$DEVSHELL_PROJECT_ID` and `$BUCKET` environment variables.


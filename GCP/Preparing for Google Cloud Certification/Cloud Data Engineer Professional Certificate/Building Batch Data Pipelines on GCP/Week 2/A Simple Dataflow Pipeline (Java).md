# Lab: Serverless Data Analysis with Dataflow: A Simple Dataflow Pipeline (Java)

## Overview
In this lab, you will open a Dataflow project, use pipeline filtering, and execute the pipeline locally and on the cloud.

## Objective
In this lab, you will learn how to write a simple Dataflow pipeline and run it both locally and on the cloud.

- Setup a Java Dataflow project using Maven
- Write a simple pipeline in Java
- Execute the query on the local machine
- Execute the query on the cloud

## Task 1. Preparation
For this lab, you will need the training-data-analyst files and a Cloud Storage bucket.

### Verify that the repository files are in Cloud Shell Editor
1. Clone the repository from the Cloud Shell command line:
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```
2. You should see the training-data-analyst directory.

### Verify that you have a Cloud Storage bucket
If you don't have a bucket, you can follow these instructions to create a bucket.

3. In the Console, on the Navigation menu (7a91d354499ac9f1.png), click Home.
4. Select and copy the Project ID. For simplicity you will use the Qwiklabs Project ID, which is already globally unique, as the bucket name.
5. In the Console, on the Navigation menu (7a91d354499ac9f1.png), click Storage > Browser.
6. Click Create Bucket.
7. Specify the following, and leave the remaining settings as their defaults:

|Property|	Value (type value or select option as specified)|
|-|-|
|Name|	`<your unique bucket name (Project ID)>`|
|Default| storage class	Multi-Regional|
|Location|	`<Your location>`|

8. Click Create.

9. Record the name of your bucket. You will need it in subsequent tasks.

10. In Cloud Shell enter the following to create an environment variable named "BUCKET" and verify that it exists with the echo command.
```
BUCKET="<your unique bucket name (Project ID)>"
echo $BUCKET
```
You can use $BUCKET in Cloud Shell commands. And if you need to enter the bucket name <your-bucket> in a text field in Console, you can quickly retrieve the name with echo $BUCKET.

### Verify that Dataflow API is enabled for this project
1. Return to the browser tab for Console. In the top search bar, enter Dataflow API. This will take you to the page, Navigation menu > APIs & Services > Dashboard > Dataflow API.
It will either show a status information or it will give you the option to Enable the API.

2. If necessary, Enable the API.


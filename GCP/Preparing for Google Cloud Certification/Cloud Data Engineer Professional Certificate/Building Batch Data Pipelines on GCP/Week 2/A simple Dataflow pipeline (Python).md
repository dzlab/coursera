# Lab: A simple Dataflow pipeline (Python)

## Overview
In this lab, you will open a Dataflow project, use pipeline filtering, and execute the pipeline locally and on the cloud.

- Open Dataflow project
- Pipeline filtering
- Execute the pipeline locally and on the cloud

## Objective
In this lab, you learn how to write a simple Dataflow pipeline and run it both locally and on the cloud.

- Setup a Python Dataflow project using Apache Beam
- Write a simple pipeline in Python
- Execute the query on the local machine
- Execute the query on the cloud

## Ensure that the Dataflow API is successfully enabled
To ensure access to the necessary API, restart the connection to the Dataflow API.

1. In the Cloud Console, enter Dataflow API in the top search bar. Click on the result for Dataflow API.
2. Click Manage.
3. Click Disable API.

If asked to confirm, click Disable.

4. Click Enable.

  
## Task 1. Preparation
For this lab, you will need the training-data-analyst files and a Cloud Storage bucket.

### Verify that the repository files are in Cloud Shell Editor
1. Clone the repository from the Cloud Shell command line:
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

2. Click on refresh explorer icon. You should see the training-data-analyst directory.

### Verify that you have a Cloud Storage bucket
If you don't have a bucket, you can follow these instructions to create a bucket.

3. In the Console, on the Navigation menu , click Home.
4. Select and copy the Project ID. For simplicity you will use the Qwiklabs Project ID, which is already globally unique, as the bucket name.
5. In the Console, on the Navigation menu, click Cloud Storage > Browser.
6.  Click Create Bucket.
7.  Specify the following, and leave the remaining settings as their defaults:

|Property|	Value (type value or select option as specified)|
|-|-|
|Name|	`<your unique bucket name (Project ID)>`|
|Location| type	Multi-Region|
|Location|	`<Your location>`|

8.  Click Create.

9. Record the name of your bucket. You will need it in subsequent tasks.

10. In Cloud Shell enter the following to create an environment variable named "BUCKET" and verify that it exists with the echo command.
```
BUCKET="<your unique bucket name (Project ID)>"
echo $BUCKET
```

You can use `$BUCKET` in Cloud Shell commands. And if you need to enter the bucket name `<your-bucket>` in a text field in Console, you can quickly retrieve the name with `echo $BUCKET`.

## Task 2. Open Dataflow project
The goal of this lab is to become familiar with the structure of a Dataflow project and learn how to execute a Dataflow pipeline. You will need to update some files to install Apache Beam. Apache Beam is an open source platform for executing data processing workflows.

1. Return to the browser tab containing Cloud Shell. In Cloud Shell navigate to the directory for this lab:
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
```
2. Install the necessary dependencies for Python dataflow:
```
sudo ./install_packages.sh
```
3. Verify that you have the right version of pip. (It should be > 8.0):
```
pip3 -V
```
If not, open a new Cloud Shell tab and it should pick up the updated version of pip.

Use refresh explorer icon in Cloud Shell editor to view the local copy of the repository.
If at any time during the DataFlow labs you are logged out of Cloud Shell due to inactivity, when you login the in-memory elements of Apache Beam will be lost. So you will need to reissue these commands before proceeding:

```
cd ~/training-data-analyst/courses/data_analysis/lab2/python

sudo ./install_packages.sh
```

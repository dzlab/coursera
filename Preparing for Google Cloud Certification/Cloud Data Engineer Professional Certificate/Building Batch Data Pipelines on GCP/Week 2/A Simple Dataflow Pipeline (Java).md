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
You can use $BUCKET in Cloud Shell commands. And if you need to enter the bucket name `<your-bucket>` in a text field in Console, you can quickly retrieve the name with echo $BUCKET.

### Verify that Dataflow API is enabled for this project
1. Return to the browser tab for Console. In the top search bar, enter Dataflow API. This will take you to the page, Navigation menu > APIs & Services > Dashboard > Dataflow API.
It will either show a status information or it will give you the option to Enable the API.

2. If necessary, Enable the API.

![image](https://user-images.githubusercontent.com/1645304/137596466-7cb23235-533e-44c7-851c-4ca074e6d98b.png)

## Task 2. Create a new Dataflow project
The goal of this lab is to become familiar with the structure of a Dataflow project and learn how to execute a Dataflow pipeline. You will use the powerful build tool [Maven](https://maven.apache.org/) to create a new Dataflow project.

1. Return to the browser tab containing Cloud Shell. In Cloud Shell navigate to the directory for this lab:
```
cd ~/training-data-analyst/courses/data_analysis/lab2
```
2. Copy and paste the following Maven command:
```
mvn archetype:generate \
  -DarchetypeArtifactId=google-cloud-dataflow-java-archetypes-starter \
  -DarchetypeGroupId=com.google.cloud.dataflow \
  -DgroupId=com.example.pipelinesrus.newidea \
  -DartifactId=newidea \
  -Dversion="[1.0.0,2.0.0]" \
  -DinteractiveMode=false
```

<details>
  <summary>Click to expand!</summary>

```
[INFO] ----------------------------------------------------------------------------
[INFO] Using following parameters for creating project from Archetype: google-cloud-dataflow-java-archetypes-starter:2.5.0
[INFO] ----------------------------------------------------------------------------
[INFO] Parameter: groupId, Value: com.example.pipelinesrus.newidea
[INFO] Parameter: artifactId, Value: newidea
[INFO] Parameter: version, Value: [1.0.0,2.0.0]
[INFO] Parameter: package, Value: com.example.pipelinesrus.newidea
[INFO] Parameter: packageInPathFormat, Value: com/example/pipelinesrus/newidea
[INFO] Parameter: package, Value: com.example.pipelinesrus.newidea
[INFO] Parameter: groupId, Value: com.example.pipelinesrus.newidea
[INFO] Parameter: artifactId, Value: newidea
[INFO] Parameter: targetPlatform, Value: 1.8
[INFO] Parameter: version, Value: [1.0.0,2.0.0]
[INFO] Project created from Archetype in dir: /home/student_01_bcf3a15a5352/training-data-analyst/courses/data_analysis/lab2/newidea
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  22.500 s
[INFO] Finished at: 2021-10-16T17:20:33Z
[INFO] ------------------------------------------------------------------------
```
</details>

- What directory has been created?
- What package has been created inside the src directory?

3. Examine the Maven command that was used to create the lab code:
```
cat ~/training-data-analyst/courses/data_analysis/lab2/create_mvn.sh
```
- What directory will get created?
- What package will get created inside the src directory?

## Task 3. Pipeline filtering
In the Cloud Shell code editor navigate to the directory `/training-data-analyst/courses/data_analysis/lab2`.

Then select the path `javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp/` and view the file `Grep.java`.

Alternatively, you could view the file with nano editor. Do not make any changes to the code.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp/
nano Grep.java
```

  
Can you answer these questions about the file Grep.java?

- What files are being read?
- What is the search term?
- Where does the output go?

There are three apply statements in the pipeline:

- What does the first apply() do?
- What does the second apply() do?
- Where does its input come from?
- What does it do with this input?
- What does it write to its output?
- Where does the output go to?
- What does the third apply() do?

## Task 4. Execute the pipeline locally
1. In Cloud Shell, paste the following Maven command:
```
cd ~/training-data-analyst/courses/data_analysis/lab2
export PATH=/usr/lib/jvm/java-8-openjdk-amd64/bin/:$PATH
cd ~/training-data-analyst/courses/data_analysis/lab2/javahelp
mvn compile -e exec:java \
 -Dexec.mainClass=com.google.cloud.training.dataanalyst.javahelp.Grep
```

2. The output file will be output.txt. If the output is large enough, it will be sharded into separate parts with names like: output-00000-of-00001. If necessary, you can locate the correct file by examining the file's time.
```
$ ls -al /tmp
total 32
drwxrwxrwt 1 root                    root                    4096 Oct 16 17:30 .
drwxr-xr-x 1 root                    root                    4096 Oct 16 17:13 ..
drwxr-xr-x 2 student_01_bcf3a15a5352 student_01_bcf3a15a5352 4096 Oct 16 17:30 hsperfdata_student_01_bcf3a15a5352
-rw-r--r-- 1 student_01_bcf3a15a5352 student_01_bcf3a15a5352 5332 Oct 16 17:13 minikube_delete_03cfb299ba8559e96af59cf45cb4362fc8de3fba_0.log
-rw-r--r-- 1 student_01_bcf3a15a5352 student_01_bcf3a15a5352 2897 Oct 16 17:30 output.txt
drwx------ 4 student_01_bcf3a15a5352 student_01_bcf3a15a5352 4096 Oct 16 17:13 tmp.KYKuIhKRQV
-rw------- 1 root                    root                       0 Oct 16 17:13 tmp.xgADuqzyAR
drwx------ 2 student_01_bcf3a15a5352 student_01_bcf3a15a5352 4096 Oct 16 17:13 tmux-1000
```

3. Examine the output file. Replace "-*" below with the appropriate suffix.
```
cat /tmp/output-*
```

Does the output seem logical?

## Task 5. Execute the pipeline on the cloud
1. Copy some Java files to the cloud.
```
gsutil cp ../javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp/*.java gs://$BUCKET/javahelp
```

2. Edit the Dataflow pipeline in `Grep.java`. In the Cloud Shell code editor navigate to the directory `/training-data-analyst/courses/data_analysis/lab2/javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp` and edit the file `Grep.java`.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp
```

3. Replace Input and Output variables with your Bucket name. These must be the actual value, not the environment variable. Recall your Bucket name:
```
echo $BUCKET
```
Replace the variables.
```
String input = "gs://<YOUR-BUCKET-NAME>/javahelp/*.java";
String outputPrefix = "gs://<YOUR-BUCKET-NAME>/javahelp/output";
```
Make sure that you changed the input and outputPrefix strings that are already present in the source code (do not copy-and-paste the entire line above because you will then end up with two variables named input).

Example lines before:
```
String input = "src/main/java/com/google/cloud/training/dataanalyst/javahelp/*.java";
String outputPrefix = "/tmp/output";
```
Example lines after edit (use your values):
```
String input = "gs://qwiklabs-gcp-your-value/javahelp/*.java";
String outputPrefix = "gs://qwiklabs-gcp-your-value/javahelp/output";
```

4. Examine the script to submit the Dataflow to the cloud:
```
$ cd ~/training-data-analyst/courses/data_analysis/lab2/javahelp
$ cat run_oncloud1.sh
#!/bin/bash

if [ "$#" -ne 3 ]; then
   echo "Usage:   ./run_oncloud.sh project-name  bucket-name  mainclass-basename"
   echo "Example: ./run_oncloud.sh cloud-training-demos  cloud-training-demos  JavaProjectsThatNeedHelp"
   exit
fi

PROJECT=$1
BUCKET=$2
MAIN=com.google.cloud.training.dataanalyst.javahelp.$3

echo "project=$PROJECT  bucket=$BUCKET  main=$MAIN"

export PATH=/usr/lib/jvm/java-8-openjdk-amd64/bin/:$PATH
mvn compile -e exec:java \
 -Dexec.mainClass=$MAIN \
      -Dexec.args="--project=$PROJECT \
      --stagingLocation=gs://$BUCKET/staging/ \
      --tempLocation=gs://$BUCKET/staging/ \
      --runner=DataflowRunner"
```
What is the difference between this Maven command and the one to run locally?

5. Submit the Dataflow job to the cloud.
```
bash run_oncloud1.sh $DEVSHELL_PROJECT_ID $BUCKET Grep
```
Because this is such a small job, running on the cloud will take significantly longer than running it locally (on the order of 2-3 minutes).

Example completion of command line (do not copy):
```
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 01:50 min
[INFO] Finished at: 2018-02-06T15:11:23-05:00
[INFO] Final Memory: 39M/206M
[INFO] ------------------------------------------------------------------------
```

6. Return to the browser tab for Console. On the Navigation menu (7a91d354499ac9f1.png), click Dataflow and click on your job to monitor progress.
Example:

![image](https://user-images.githubusercontent.com/1645304/137597029-17f47486-e68e-4524-bfa8-a6492e4a1d2f.png)


7. Wait for the job status to turn to Succeeded. At this point, your Cloud Shell will display a command-line prompt.

> If Dataflow job fails the first time, then re-run the previous command to submit a fresh Dataflow job to the cloud

8. Examine the output in the Cloud Storage bucket. On the Navigation menu (7a91d354499ac9f1.png), click Storage > Browser and click on your bucket.

9. Click the javahelp directory. This job will generate the file output.txt. If the file is large enough it will be sharded into multiple parts with names like: output-0000x-of-000y. You can identify the most recent file by name or by the Last modified field. Click on the file to view it.

Alternatively, you could download the file in Cloud Shell and view it:
```
gsutil cp gs://$BUCKET/javahelp/output* .
cat output*
```

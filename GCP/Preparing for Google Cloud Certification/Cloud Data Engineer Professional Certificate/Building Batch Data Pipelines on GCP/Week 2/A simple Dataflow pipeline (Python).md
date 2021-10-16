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

## Setup

### Ensure that the Dataflow API is successfully enabled
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

## Task 3. Pipeline filtering
1. In the Cloud Shell code editor navigate to the directory `/training-data-analyst/courses/data_analysis/lab2/python` and view the file `grep.py`. Do not make any changes to the code.

Alternatively, you could view the file with nano. Do not make any changes to the code. If you use nano, press Ctrl + X to exit.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
nano grep.py
```

Can you answer these questions about the file `grep.py`?

- What files are being read?
- What is the search term?
- Where does the output go?

There are three transforms in the pipeline:

- What does the transform do?
- What does the second transform do?
- Where does its input come from?
- What does it do with this input?
- What does it write to its output?
- Where does the output go to?
- What does the third transform do?

## Task 4. Execute the pipeline locally
1. In the Cloud Shell command line, locally execute grep.py.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
python3 grep.py
```

> Note: if you see an error that says "No handlers could be found for logger "oauth2client.contrib.multistore_file", you may ignore it. The error is simply saying that logging from the oauth2 library will go to stderr.

2. The output file will be `output.txt`. If the output is large enough, it will be sharded into separate parts with names like: `output-00000-of-00001`. If necessary, you can locate the correct file by examining the file's time.
```
$ ls -al /tmp
total 28
drwxrwxrwt 1 root                    root                    4096 Oct 16 07:18 .
drwxr-xr-x 1 root                    root                    4096 Oct 16 07:07 ..
-rw-r--r-- 1 student_03_3509181180f9 student_03_3509181180f9 5332 Oct 16 07:08 minikube_delete_bd0b4b4d2844917f65da52d909545164bb919ae2_0.log
-rw-r--r-- 1 student_03_3509181180f9 student_03_3509181180f9 2570 Oct 16 07:18 output-00000-of-00001
-rw------- 1 root                    root                       0 Oct 16 07:07 tmp.hPZlYCclHj
drwx------ 4 student_03_3509181180f9 student_03_3509181180f9 4096 Oct 16 07:08 tmp.jo6v2sveOh
drwx------ 2 student_03_3509181180f9 student_03_3509181180f9 4096 Oct 16 07:08 tmux-1000
```
3. Examine the output file. Replace "-*" below with the appropriate suffix.
```
cat /tmp/output-*
```

<details>
  <summary>CExample output</summary>
  
```
$ cat /tmp/output-00000-of-00001
import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
import org.apache.beam.sdk.options.Default;
import org.apache.beam.sdk.options.Description;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.DoFn;
import org.apache.beam.sdk.transforms.ParDo;
import org.apache.beam.sdk.transforms.Sum;
import org.apache.beam.sdk.transforms.windowing.SlidingWindows;
import org.apache.beam.sdk.transforms.windowing.Window;
import org.joda.time.Duration;
import com.google.api.services.bigquery.model.TableFieldSchema;
import com.google.api.services.bigquery.model.TableRow;
import com.google.api.services.bigquery.model.TableSchema;
import java.util.ArrayList;
import java.util.List;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.TextIO;
import org.apache.beam.sdk.options.Default;
import org.apache.beam.sdk.options.Description;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.DoFn;
import org.apache.beam.sdk.transforms.ParDo;
import org.apache.beam.sdk.transforms.Sum;
import org.apache.beam.sdk.transforms.Top;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.TextIO;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.DoFn;
import org.apache.beam.sdk.transforms.ParDo;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import com.google.api.services.bigquery.model.TableRow;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
import org.apache.beam.sdk.io.TextIO;
import org.apache.beam.sdk.options.Default;
import org.apache.beam.sdk.options.Description;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.DoFn;
import org.apache.beam.sdk.transforms.ParDo;
import org.apache.beam.sdk.transforms.Sum;
import org.apache.beam.sdk.transforms.Top;
import org.apache.beam.sdk.transforms.View;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.PCollectionView;
```
</details>

Does the output seem logical?

## Task 5. Execute the pipeline on the cloud
Copy some Java files to the cloud.
```
$ gsutil cp ../javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp/*.java gs://$BUCKET/javahelp
Copying file://../javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp/Grep.java [Content-Type=text/x-java]...
Copying file://../javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp/IsPopular.java [Content-Type=text/x-java]...
Copying file://../javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp/JavaProjectsThatNeedHelp.java [Content-Type=text/x-java]...
Copying file://../javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp/StreamDemoConsumer.java [Content-Type=text/x-java]...
- [4 files][ 16.7 KiB/ 16.7 KiB]
Operation completed over 4 objects/16.7 KiB.
```

![image](https://user-images.githubusercontent.com/1645304/137578316-bad5d300-30f5-485a-b6f2-3bd5e2c827fb.png)


2. Edit the Dataflow pipeline in `grepc.py`. In the Cloud Shell code editor navigate to the directory `/training-data-analyst/courses/data_analysis/lab2/python` in and edit the file `grepc.py`.

```
$ vi ~/training-data-analyst/courses/data_analysis/lab2/python/grepc.py
```

3. Replace PROJECT and BUCKET with your Project ID and Bucket name. Here are easy ways to retrieve the values:
```
echo $DEVSHELL_PROJECT_ID
echo $BUCKET
```
Example strings before:
```
PROJECT='cloud-training-demos'
BUCKET='cloud-training-demos'
```
Example strings after edit (use your values):
```
PROJECT='qwiklabs-gcp-your-value'
BUCKET='qwiklabs-gcp-your-value'
```
4. Submit the Dataflow job to the cloud:
```
python3 grepc.py
```

Because this is such a small job, running on the cloud will take significantly longer than running it locally (on the order of 2-3 minutes).

5. Return to the browser tab for Console. On the Navigation menu, click Dataflow and click on your job to monitor progress.
Example:

![image](https://user-images.githubusercontent.com/1645304/137578112-0785ce30-e642-4998-a06b-cf993084e957.png)

6. Wait for the job status to turn to Succeeded. At this point, your Cloud Shell will display a command-line prompt.

7. Examine the output in the Cloud Storage bucket. On the Navigation menu, click Cloud Storage > Browser and click on your bucket. Click the javahelp directory. This job will generate the file output.txt. If the file is large enough it will be sharded into multiple parts with names like: `output-0000x-of-000y`. You can identify the most recent file by name or by the Last modified field. Click on the file to view it.

Alternatively, you could download the file in Cloud Shell and view it:
```
gsutil cp gs://$BUCKET/javahelp/output* .
cat output*
```

# PDE Prep : Cloud Dataproc Cluster Operations and Maintenance

## Overview
This is a Challenge lab where you must complete a series of tasks within a limited time period. Instead of following step-by-step instructions, you are presented with general objectives. An automated scoring system (shown on this page) will provide feedback on whether you have completed each task correctly.

To score 100% the challenge, you must complete all tasks within the time period!

This lab does not teach GCP concepts. Instead, it is a test of your Data Engineering skills. This lab is only recommended for students who have Cloud Dataproc skills.

#### Topics tested
- Create a cluster with access to a Cloud Storage staging bucket.
- Run PySpark jobs with input arguments.
- Upgrade the master node configuration on an existing cluster.
- Resolve a cluster capacity performance issue.
- Upgrade the number of worker nodes on an existing cluster.

## Your Challenge: Scenario
You work as a Data Engineer for MJTelco. (Congratulations on the new job!)

MJTelco's Data Scientist team plans to port an existing predictive machine learning application to a Cloud Dataproc cluster. The application is written in Python and runs on Spark. The application takes a long time to run, even with sample data. So the Data Scientists have established a benchmark by running a program in their data center. They have attempted to run the benchmark on a Cloud Dataproc cluster, but it is taking longer than they would like. Your job is to run the benchmark program on Cloud Dataproc and make adjustments to the cluster configuration to meet their requirements.

> Note: The benchmark program is a PySpark application. It calculates the value of PI. The input value determines how many iterations are used in the calculation.

### Requirements
If the benchmark program is given an input value of 220, and the job completes in under 75 seconds, the requirements will be met.

At this time, when the benchmark program is submitted with the input value of 20, the job completes in under 75 seconds. When it is submitted with the required input value of 220, the job takes about 2 minutes to run, which does not met the requirement.

## Objective 1
Your first job is to duplicate the cluster that the Data Scientists are using and then run the benchmark job.

### Task 1: Stage the benchmark PySpark application
Create a Cloud Storage bucket for use by your Cloud Dataproc cluster. Give the bucket the same name as your project. Copy the benchmark Python Spark application to the bucket in your project.

The benchmark application has been shared with you from a Cloud Storage bucket: `gs://cloud-training/preppde/benchmark.py`

```
$ gsutil cp gs://cloud-training/preppde/benchmark.py gs://qwiklabs-gcp-01-d740b3fbec6d/
Copying gs://cloud-training/preppde/benchmark.py [Content-Type=text/x-python-script]...
/ [1 files][  1.4 KiB/  1.4 KiB]
Operation completed over 1 objects/1.4 KiB.
```

### Task 2: Create a Cloud Dataproc Cluster that matches the Data Analyst's configuration
The Data Scientists are using a minimal Cloud Dataproc cluster consisting of one master node and two worker nodes. All the instances are of type **n1-standard-2**.

Create a Cloud Dataproc cluster named **mjtelco** using version **2.0 (Debian 10, Hadoop 3.2, Spark 3.1)** with a master node of **n1-standard-2** and two worker nodes of **n1-standard-2** in **us-central1** region and **us-central1-a** zone. Use the default settings on everything else. Remember to set advanced options to give the cluster access to your Cloud Storage staging bucket.

### Task 3: Demonstrate the successful benchmark job without the required input value
Submit the python job to the cluster, and give the job the name mjtelco-test-1. Give the job the input argument of 20. For Max restarts per hour, enter 1.

The job should take under 75 seconds to run and should succeed.

### Task 4: Demonstrate the slower benchmark job with the required input value
Submit the python job to the cluster, and give the job the name mjtelco-test-2. Give the job the input argument of 220. For Max restarts per hour, enter 1.

The job should take between 1 minute and 45 seconds and 3 minutes to run and should succeed.

## Objective 2
Your second job is to improve the performance of the cluster and to reduce the time it takes to run the benchmark job.

### Task 5: Upgrade the master node
Upgrade the master node to a 4-CPU instance, **n1-standard-4**.

![datafusion](https://user-images.githubusercontent.com/1645304/137842107-68987a23-0867-4a5f-a58e-03e63f6cd6cb.gif)


### Task 6: Demonstrate that the benchmark job completes in less time
After the upgraded master node is running, submit the python job again to the cluster. Give the job the name **mjtelco-test-3**. Give the job the input argument of 220. For Max restarts per hour, enter 1.

The job should take about 2 minutes to run and should succeed.

![datafusion](https://user-images.githubusercontent.com/1645304/137842343-88a4b2ef-0a65-4baa-8a63-0b16542aecea.gif)

### Task 7: Grow the cluster
You are getting closer but the job still does not complete in under the required time (under 75 seconds) when given the input value of **220**.

Upgrade the cluster by adding three more **n1-standard-2** worker nodes for a total of five workers.

![datafusion](https://user-images.githubusercontent.com/1645304/137842662-271dabfa-e8d8-4df0-a0f8-57d7773aaefe.gif)


### Task 8: Submit the job and verify improved performance
After the additional nodes are running, submit the job again. Submit the python job to the cluster, and give the job the name **mjtelco-test-4**. Give the job the input argument of 220. For Max restarts per hour, enter 1.

The benchmark job should now complete within the required time (under 75 seconds).

![datafusion](https://user-images.githubusercontent.com/1645304/137842888-6823627c-7561-4d52-9b28-b7d86ad77f63.gif)


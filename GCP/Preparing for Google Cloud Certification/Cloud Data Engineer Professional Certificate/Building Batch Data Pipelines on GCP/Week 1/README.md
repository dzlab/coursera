# Week 1
## Introduction to Batch Data Pipelines
### Quiz: EL, ELT, ETL

**1. Question 1**

Which of the following is the ideal use case for Extract and Load (EL)

- [ ] When the raw data needs to be quality-controlled, transformed, or enriched before being loaded into BigQuery
- [ ] When the data loading has to happen continuously
- [x] Scheduled periodic loads of log files (e.g. once a day)
- [ ] When you want to integrate with continuous integration / continuous delivery (CI/CD) systems and perform unit testing on all components.

## Executing Spark on Cloud Dataproc

### Lab: Running Apache Spark jobs on Cloud Dataproc
#### Overview
In this lab you will learn how to migrate Apache Spark code to Cloud Dataproc. You will follow a sequence of steps progressively moving more of the job components over to GCP services:

Run original Spark code on Cloud Dataproc (Lift and Shift)

Replace HDFS with Cloud Storage (cloud-native)

Automate everything so it runs on job-specific clusters (cloud-optimized)

#### Objectives
In this lab you will learn how to:

- Migrate existing Spark jobs to Cloud Dataproc
- Modify Spark jobs to use Cloud Storage instead of HDFS
- Optimize Spark jobs to run on Job specific clusters

What will you use?
- Cloud Dataproc
- Apache Spark

#### Scenario
You are migrating an existing Spark workload to Cloud Dataproc and then progressively modifying the Spark code to make use of GCP native features and services.

#### Part 1: Lift and Shift
Migrate existing Spark jobs to Cloud Dataproc

You will create a new Cloud Dataproc cluster and then run an imported Jupyter notebook that uses the cluster's default local Hadoop Distributed File system (HDFS) to store source data and then process that data just as you would on any Hadoop cluster using Spark. This demonstrates how many existing analytics workloads such as Jupyter notebooks containing Spark code require no changes when they are migrated to a Cloud Dataproc environment.

Configure and start a Cloud Dataproc cluster

1. In the GCP Console, on the Navigation menu, in the Big Data section, click Dataproc.
2. Click Create Cluster.
3. Enter `sparktodp` for Cluster Name.
4. In the Versioning section, click Change and select 2.0 (Debian 10, Hadoop 3.2, Spark 3.1).

This version includes Python3 which is required for the sample code used in this lab.
5. Click Select.
6. In the Components > Component gateway section, select Enable component gateway.
7. Under Optional components, Select Jupyter Notebook.
8. Click Create.

The cluster should start in a couple of minutes. You can proceed to the next step without waiting for the Cloud Dataproc Cluster to fully deploy.

#### Clone the source repository for the lab
In the Cloud Shell you clone the Git repository for the lab and copy the required notebook files to the Cloud Storage bucket used by Cloud Dataproc as the home directory for Jupyter notebooks.

1. To clone the Git repository for the lab enter the following command in Cloud Shell:
```
git -C ~ clone https://github.com/GoogleCloudPlatform/training-data-analyst
```
2. To locate the default Cloud Storage bucket used by Cloud Dataproc enter the following command in Cloud Shell:

```
export DP_STORAGE="gs://$(gcloud dataproc clusters describe sparktodp --region=us-central1 --format=json | jq -r '.config.configBucket')"
```

3. To copy the sample notebooks into the Jupyter working folder enter the following command in Cloud Shell:

```
gsutil -m cp ~/training-data-analyst/quests/sparktobq/*.ipynb $DP_STORAGE/notebooks/jupyter
```

#### Log in to the Jupyter Notebook
As soon as the cluster has fully started up you can connect to the Web interfaces. Click the refresh button to check as it may be deployed fully by the time you reach this stage.

1. On the Dataproc Clusters page wait for the cluster to finish starting and then click the name of your cluster to open the Cluster details page.
2. Click Web Interfaces.
3. Click the Jupyter link to open a new Jupyter tab in your browser.

This opens the Jupyter home page. Here you can see the contents of the `/notebooks/jupyter` directory in Cloud Storage that now includes the sample Jupyter notebooks used in this lab.

4. Under the Files tab, click the GCS folder and then click 01_spark.ipynb notebook to open it.
5. Click Cell and then Run All to run all of the cells in the notebook.
6. Page back up to the top of the notebook and follow as the notebook completes runs each cell and outputs the results below them.

You can now step down through the cells and examine the code as it is processed so that you can see what the notebook is doing. In particular pay attention to where the data is saved and processed from.

The first code cell fetches the source data file, which is an extract from the KDD Cup competition from the Knowledge, Discovery, and Data (KDD) conference in 1999. The data relates to computer intrusion detection events.

```
!wget https://archive.ics.uci.edu/ml/machine-learning-databases/kddcup99-mld/kddcup.data_10_percent.gz
```

In the second code cell, the source data is copied to the default (local) Hadoop file system.
```
!hadoop fs -put kddcup* /
```

In the third code cell, the command lists contents of the default directory in the cluster's HDFS file system.
```
!hadoop fs -ls /
```

#### Reading in data

### Quiz

**1. Question 1**

Which of the following statements are true about Cloud Dataproc?

(Select all  2 correct answers)

- [x] Lets you run Spark and Hadoop clusters with minimal administration
- [ ] Streamlined API for Spark and Hadoop programming
- [x] Helps you create job-specific clusters without HDFS

**2. Question 2**

Match each of the terms with what they do when setting up clusters in Cloud Dataproc:

|Term|Definition
|-|-
|__ 1. Zone|A. Costs less but may not be available always
|__ 2. Standard Cluster mode|B. Determines the Google data center where compute nodes will be
|__ 3. Preemptible |C. Provides 1 master and N workers

- [ ] 
  1. A
  2. B
  3. C
- [x] 
  1. B
  2. C
  3. A
- [ ] 
  1. C
  2. A
  3. B
- [ ] 
  1. C
  2. B
  3. A


**3. Question 3**

Cloud Dataproc provides the ability for Spark programs to separate compute & storage by:

- [x] Reading and writing data directory from/to Cloud Storage
- [ ] Pre-copying data from Cloud Storage to persistent disk on cluster startup
- [ ] Mirroring data on both Cloud Storage and HDFS
- [ ] Setting individual zones for compute and storage



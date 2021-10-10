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



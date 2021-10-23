# Week 6: Resources and next steps

## Practice exam quiz

### Reading: Instructions of GRADED and UNGRADED Practice Exam Quizzes
There are two versions of the Practice Exam Quiz. The first version is UNGRADED Practice Exam Quiz and provides information about the answers you select and feedback to help you understand what you might need to study. You can try the ungraded version multiple times until you get everything right.

A good way to study is to look up every correct and incorrect answer and make sure you not only know which answer is correct, but also why it is correct.

The second version is the GRADED Practice Exam Quiz. This version is more like the actual exam. Because it offers limited feedback -- just a total score at the end. When you are ready, proceed to the GRADED Practice Exam Quiz which will give you credit towards completing this course. You may only attempt the GRADED Practice Exam Quiz three times in 8 hours.

Good luck!

### Quiz: Ungraded Practice Exam
**1. Question 1**

Storage of JSON files with occasionally changing schema, for ANSI SQL queries.

- [ ] Store in BigQuery. Provide format files for data load and update them as needed.
- [ ] Store in BigQuery. Select "Automatically detect" in the Schema section.
> **Correct:** This is correct because of the requirement to support occasionally (schema) changing JSON files and aggregate ANSI SQL queries: you need to use BigQuery, and it is quickest to use 'Automatically detect' for schema changes.
- [ ] Store in Cloud Storage. Link data as temporary tables in BigQuery and turn on the "Automatically detect" option in the Schema section of BigQuery.
> **Incorrect**: This is not correct because you should not use Cloud Storage for this scenario: it is cumbersome and doesn't add value.
- [ ] Store in Cloud Storage. Link data as permanent tables in BigQuery and turn on the "Automatically detect" option in the Schema section of BigQuery.

**2. Question 2**

Low-cost one-way one-time migration of two 100-TB file servers to Google Cloud; data will be frequently accessed and only from Germany.

- [ ] Use Transfer Appliance. Transfer to a Cloud Storage Standard bucket.
- [ ] Use Transfer Appliance. Transfer to a Cloud Storage Nearline bucket.
> **Incorrect:** This is not correct because you should not use a  Nearline storage bucket for frequently accessed data. 
- [ ] Use Storage Transfer Service. Transfer to a Cloud Storage Standard bucket.
- [ ] Use Storage Transfer Service. Transfer to a Cloud Storage Coldline bucket.


**3. Question 3**

Cost-effective backup to Google Cloud of multi-TB databases from another cloud including monthly DR drills.

- [ ] Use Transfer Appliance. Transfer to Cloud Storage Nearline bucket.
- [ ] Use Transfer Appliance. Transfer to Cloud Storage Coldline bucket.
- [ ] Use Storage Transfer Service. Transfer to Cloud Storage Nearline bucket.
> **Correct:** This is correct because you will need to access your backup data monthly to test your disaster recovery process, so you should use a Nearline bucket; also because you will be performing ongoing, regular data transfers, so you should use Storage Transfer Service.
- [ ] Use Storage Transfer Service. Transfer to Cloud Storage Coldline bucket.
> **Incorrect:** This is not correct because you should not use Coldline if you want to access the files monthly.

**4. Question 4**

250,000 devices produce a JSON device status every 10 seconds. How do you capture event data for outlier time series analysis? 

- [ ] Capture data in BigQuery. Develop a BigQuery API custom application to query the dataset and display device outlier data.
- [ ] Capture data in BigQuery. Use the BigQuery console to query the dataset and display device outlier data.
> **Incorrect:** This is not correct because you do not need to use BigQuery for the query pattern in this scenario. The focus is on a single action (identify outliers), not interactive analysis. And the speed of the data is more suited to Cloud Bigtable.
- [x] Capture data in Cloud Bigtable. Use the Cloud Bigtable cbt tool to display device outlier data.
> **Correct:** This is correct because the data type, volume, and query pattern best fit Cloud Bigtable capabilities.
- [ ] Capture data in Cloud Bigtable. Install and use the HBase shell for Cloud Bigtable to query the table for device outlier data.


**5. Question 5**

Event data in CSV format to be queried for individual values over time windows. Which storage and schema to minimize query costs?

- [x] Use Cloud Storage. Write a Dataprep job to split the data into partitioned tables.
> **Correct:** This is correct because it is a recommended best practice. Use Cloud Bigtable and this schema for this scenario. Cloud Storage would have cheaper STORAGE costs than Cloud Bigtable, but we want to **minimize QUERY costs**.
- [ ] Use Cloud Bigtable. Design short and wide tables, and use a new column for each single event version.
- [ ] Use Cloud Bigtable. Design tall and narrow tables, and use a new row for each single event version.
- [ ] Use Cloud Storage. Join the raw file data with a BigQuery log table.


**6. Question 6**

Customer wants to maintain investment in an existing Apache Spark code data pipeline.

- [ ] BigQuery
- [ ] Dataflow
- [x] Dataproc
> **Correct:** This is correct because Dataproc is a managed Hadoop service and runs Apache Spark applications.
- [ ] Dataprep


**7. Question 7**

Host a deep neural network machine learning model on Google Cloud. Run and monitor jobs that could occasionally fail.

- [ ] Use AI Platform to host your model. Monitor the status of the Operation object for 'error' results.
- [x] Use AI Platform to host your model. Monitor the status of the Jobs object for 'failed' job states.
> **Correct:** This is correct because of the requirement to host an ML DNN. AI Platform for Tensorflow can handle DNNs. Google recommends monitoring Jobs, not Operations.
- [ ] Use a Google Kubernetes Engine cluster to host your model. Monitor the status of the Jobs object for 'failed' job states.
- [ ] Use a Google Kubernetes Engine cluster to host your model. Monitor the status of the Operation object for 'error' results.


**8. Question 8**

Cost-effective way to run non-critical Apache Spark jobs on Dataproc?

- [ ] Set up a cluster in high availability mode with high-memory machine types. Add 10 additional local SSDs.
- [ ] Set up a cluster in high availability mode with default machine types. Add 10 additional preemptible worker nodes.
- [x] Set up a cluster in standard mode with high-memory machine types. Add 10 additional preemptible worker nodes.
> **Correct:** This is correct because Spark and high-memory machines only need the standard mode. Also, use preemptible nodes because you want to save money and this is not mission-critical.
- [ ] Set up a cluster in standard mode with the default machine types. Add 10 additional local SSDs.


**9. Question 9**

Promote a Cloud Bigtable solution with a lot of data from development to production and optimize for performance.


- [ ] Change your Cloud Bigtable instance type from Development to Production, and set the number of nodes to at least 3. Verify that the storage type is HDD.
- [ ] Change your Cloud Bigtable instance type from Development to Production, and set the number of nodes to at least 3. Verify that the storage type is SSD.
> **Correct:** This is correct because Cloud Bigtable allows you to 'scale in place,' which meets your requirements for this scenario.
- [ ] Export the data from your current Cloud Bigtable instance to Cloud Storage. Create a new Cloud Bigtable Production instance type with at least 3 nodes. Select the HDD storage type. Import the data into the new instance from Cloud Storage.
- [x] Export the data from your current Cloud Bigtable instance to Cloud Storage. Create a new Cloud Bigtable Production instance type with at least 3 nodes. Select the SSD storage type. Import the data into the new instance from Cloud Storage.

> **Incorrect:** This is not correct because creating a new Cloud Bigtable instance is extraneous and not needed to export; you can upgrade in place for nodes, but the storage type cannot be changed.

**10. Question 10**

As part of your backup plan, you want to be able to restore snapshots of Compute Engine instances using the fewest steps. 

- [ ] Export the snapshots to Cloud Storage. Create disks from the exported snapshot files. Create images from the new disks.
- [ ] Export the snapshots to Cloud Storage. Create images from the exported snapshot files.
> **Incorrect:** This is not correct because you don't need to export the snapshot to use it.
- [ ] Use the snapshots to create replacement disks. Use the disks to create instances as needed.
- [x] Use the snapshots to create replacement instances as needed.

> **Correct:** This is correct because the scenario asks how to recreate instances. You can create an instance directly from a snapshot without restoring to disk first.

**11. Question 11**

You want to minimize costs to run Google Data Studio reports on BigQuery queries by using prefetch caching.

- [ ] Set up the report to use the Owner's credentials to access the underlying data in BigQuery, and direct the users to view the report only once per business day (24-hour period).
- [x] Set up the report to use the Owner's credentials to access the underlying data in BigQuery, and verify that the 'Enable cache' checkbox is selected for the report.
> **Correct:** This is correct because you must set Owner credentials to use the 'enable cache' option in BigQuery. It is also a Google best practice to use the ‘enable cache’ option when the business scenario calls for using prefetch caching. 1) Report must use Owner's Credentials. 2) You don't need to tell the users not to use the report, you need to tell the system to use Query and Pre-fetch caching to cut down on BigQuery jobs.

- [ ] Set up the report to use the Viewer's credentials to access the underlying data in BigQuery, and also set it up to be a 'view-only' report.
> **Incorrect:** This is not correct because a cache auto-expires every 12 hours; a prefetch cache is only for data sources that use the Owner's credentials (not the Viewer's credentials).
- [ ] Set up the report to use the Viewer's credentials to access the underlying data in BigQuery, and verify that the 'Enable cache' checkbox is not selected for the report.


**12. Question 12**

A Data Analyst is concerned that a BigQuery query could be too expensive.

- [ ] Use the LIMIT clause to limit the number of values in the results.
- [ ] Use the SELECT clause to limit the amount of data in the query. Partition data by date so the query can be more focused.
- [x] Set the Maximum Bytes Billed, which will limit the number of bytes processed but still run the query if the number of bytes requested goes over the limit.
> **Incorrect:** This is not correct because if the query contains too many bytes, the job will fail and not be run.
- [ ] Use GROUP BY so the results will be grouped into fewer output values.


**13. Question 13**

BigQuery data is stored in external CSV files in Cloud Storage; as the data has increased, the query performance has dropped.

- [ ] Import the data into BigQuery for better performance.
- [x] Request more slots for greater capacity to improve performance.
> **Incorrect:** This is incorrect because a slot is a measure of processing power, and the bottleneck is in the data access, not the data processing.
- [ ] Divide the data into partitions based on date.
- [ ] Time to move to Cloud Bigtable; it is faster in all cases.


**14. Question 14**

Source data is streamed in bursts and must be transformed before use.

- [ ] Use Cloud Bigtable for fast input and cbt for ETL.
- [ ] Ingest data to Cloud Storage. Use Dataproc for ETL.
- [ ] Use Pub/Sub to buffer the data, and then use BigQuery for ETL.
- [x] Use Pub/Sub to buffer the data, and then use Dataflow for ETL.
> **Correct:** This is correct because the unpredictable data requires a buffer

**15. Question 15**

Calculate a running average on streaming data that can arrive late and out of order.

- [x] Use Pub/Sub and Dataflow with Sliding Time Windows.
> **Correct:** This is correct because together, Pub/Sub and Dataflow can provide a solution.
- [ ] Use Pub/Sub and Google Data Studio.
- [ ] Pub/Sub can guarantee timely arrival and order.
- [ ] Use Dataflow's built-in timestamps for ordering and filtering.


**16. Question 16**

Testing a Machine Learning model with validation data returns 100% correct answers.

- [x] The model is working extremely well, indicating the hyperparameters are set correctly.
> **Incorrect:** This is not correct because the 100% accuracy is an indicator of an overfit model. It may mean your validation data has gotten mixed in with your training data.

- [ ] The model is overfit. There is a problem.
- [ ] The model is underfit. There is a problem.
- [ ] The model is perfectly fit. You do not need to continue training.

**17. Question 17**

A client is using Cloud SQL database to serve infrequently changing lookup tables that host data used by applications. The applications will not modify the tables. As they expand into other geographic regions they want to ensure good performance. What do you recommend?

- [x] Migrate to Cloud Spanner
> **Incorrect:** This is not correct because there is no mention of a scale issue requiring a larger database or globally consistent transactions.
- [ ] Read replicas
- [ ] Instance high availability configuration
- [ ] Replicate from an external server


**18. Question 18**

A client wants to store files from one location and retrieve them from another location. Security requirements are that no one should be able to access the contents of the file while it is hosted in the cloud. What is the best option?

- [ ] Default encryption should be sufficient
- [ ] Client-side encryption
- [x] Customer-Supplied Encryption Keys (CSEK)
> **Incorrect:** The specific requirement is that the file cannot be decrypted in the cloud. This feature simply makes decryption more private and secure. So it is not the best solution because it does not satisfy the business requirements stated in the question.
- [ ] Customer Managed Encryption Keys (CMEK)


**19. Question 19**

Three Google Cloud services commonly used together in data engineering solutions. (Described in this course).

- [ ] Dataproc, Cloud SQL, BigQuery
- [x] Pub/Sub, Dataflow, BigQuery
> **Correct:** Correct. Pub/Sub provides messaging, Dataflow is used for ETL and data transformation, and BigQuery is used for interactive queries.
- [ ] Pub/Sub,Google Kubernetes Engine, Spanner
- [ ] Bigtable, Dataproc, Cloud Spanner


**20. Question 20**

What is AVRO used for?

- [x] Serialization and de-serialization of data so that it can be transmitted and stored while maintaining an object structure.
> **Correct:** This is correct. AVRO is a serialization / de-serialization standard.
- [ ] AVRO is an encryption method. AVRO-256 is a 256-bit key standard.
- [ ] AVRO is a file type usually specified with `*.avr` and a common format for spreadsheets.
- [ ] AVRO is a numerical type in SQL that stores a 38 digit value with 9 digit decimal representation. It avoids rounding errors in financial calculations.


**21. Question 21**

A company has a new IoT pipeline. Which services will make this design work?

Select the services that should be used to replace the icons with the number "1" and number "2" in the diagram.

![image](https://user-images.githubusercontent.com/1645304/138025700-a4c47c1a-eef8-4482-b133-87310e70fc2c.png)


- [ ] IoT Core, Datastore
- [x] Pub/Sub, Storage
> **Incorrect:** This is not correct because Pub/Sub does not do device management.
- [ ] IoT Core, Pub/Sub
> **Correct:** This is correct because device data captured by IoT Core gets published to Pub/Sub.
- [ ] App Engine, IoT Core


**22. Question 22**

A company wants to connect cloud applications to an Oracle database in its data center. Requirements are a maximum of 9 Gbps of data and a Service Level Agreement (SLA) of 99%.

- [ ] Implement a high-throughput Cloud VPN connection
- [ ] Cloud Router with VPN
- [x] Dedicated Interconnect
> **Incorrect:** This is not correct. Direct Interconnect is useful for data from 10 Gbps to 80 Gbps. An ISP could offer a 99% SLA, but the max 9 Gbps requirement means this solution would not be optimal.
- [ ] Partner Interconnect
> **Correct:** This is correct. Partner Interconnect is useful for data up to 10 Gbps and is offered by ISPs with SLAs.

**23. Question 23**

A client has been developing a pipeline based on PCollections using local programming techniques and is ready to scale up to production. What should they do?

- [x] They should use the Dataflow Cloud Runner.
> **Correct:** This is correct. The PCollection indicates it is a Dataflow pipeline. And the Cloud Runner will enable the pipeline to scale to production levels.
- [ ] They should upload the pipeline to Dataproc.
- [ ] They should use the local version of runner.
- [ ] Import the pipeline into BigQuery.


**24. Question 24**

A company has migrated their Hadoop cluster to the cloud and is now using  Dataproc with the same settings and same methods as in the data center. What would you advise them to do to make better use of the cloud environment?

- [ ] Upgrade to the latest version of HDFS. Change the settings in Hadoop components to optimize for the different kinds of work in the mix.
- [ ] Find more jobs to run so the cluster utilizations will cost-justify the expense.
- [x] Store persistent data off-cluster. Start a cluster for one kind of work then shut it down when it is not processing data.
> **Correct:** This is correct. Storing persistent data off the cluster allows the cluster to be shut down when not processing data. And it allows separate clusters to be started per job or per kind of work, so tuning is less important.
- [ ] Migrate from Dataproc to an open source Hadoop Cluster hosted on Compute Engine, because this is the only way to get all the Hadoop customizations needed for efficiency.


**25. Question 25**

An application has the following data requirements. 1. It requires strongly consistent transactions. 2. Total data will be less than 500 GB. 3. The data does not need to be streaming or real time. Which data technology would fit these requirements?

- [ ] BigQuery
- [ ] Cloud Bigtable
- [x] Cloud SQL
> **Correct:** This is correct. Cloud SQL supports strongly consistent transactions. And the size requirements will fit with a Cloud SQL instance.
- [ ] Memorystore

## Resources
### Reading: Exam Tips #7
#### Review of tips
TIP 1: Create your own custom preparation plan using the resources in this course.

TIP 2: Use the Exam Guide outline to help identify what to study.

TIP 3: Product and technology knowledge.

TIP 4: This course has touchstone concepts for self-evaluation, not technical training. Seek training if needed.

TIP 5: Problem solving is the key skill.

TIP 6: Practice evaluating your confidence in your answers.

TIP 7: Practice case evaluation and creating proposed solutions.

Tip 8: Use what you know and what you don't know to identify correct and incorrect answers.

Tip 9: Review or rehearse labs to refresh your experience

Tip 10: Prepare!

Good luck!!




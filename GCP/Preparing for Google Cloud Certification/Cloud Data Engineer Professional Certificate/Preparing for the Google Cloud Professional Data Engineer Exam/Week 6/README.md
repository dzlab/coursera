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
- [x] Store in Cloud Storage. Link data as temporary tables in BigQuery and turn on the "Automatically detect" option in the Schema section of BigQuery.
- [ ] Store in Cloud Storage. Link data as permanent tables in BigQuery and turn on the "Automatically detect" option in the Schema section of BigQuery.

**2. Question 2**

Low-cost one-way one-time migration of two 100-TB file servers to Google Cloud; data will be frequently accessed and only from Germany.

- [ ] Use Transfer Appliance. Transfer to a Cloud Storage Standard bucket.
- [x] Use Transfer Appliance. Transfer to a Cloud Storage Nearline bucket.
- [ ] Use Storage Transfer Service. Transfer to a Cloud Storage Standard bucket.
- [ ] Use Storage Transfer Service. Transfer to a Cloud Storage Coldline bucket.


**3. Question 3**

Cost-effective backup to Google Cloud of multi-TB databases from another cloud including monthly DR drills.

- [ ] Use Transfer Appliance. Transfer to Cloud Storage Nearline bucket.
- [ ] Use Transfer Appliance. Transfer to Cloud Storage Coldline bucket.
- [ ] Use Storage Transfer Service. Transfer to Cloud Storage Nearline bucket.
- [x] Use Storage Transfer Service. Transfer to Cloud Storage Coldline bucket.


**4. Question 4**

250,000 devices produce a JSON device status every 10 seconds. How do you capture event data for outlier time series analysis? 

- [ ] Capture data in BigQuery. Develop a BigQuery API custom application to query the dataset and display device outlier data.
- [ ] Capture data in BigQuery. Use the BigQuery console to query the dataset and display device outlier data.
- [x] Capture data in Cloud Bigtable. Use the Cloud Bigtable cbt tool to display device outlier data.
- [ ] Capture data in Cloud Bigtable. Install and use the HBase shell for Cloud Bigtable to query the table for device outlier data.


**5. Question 5**

Event data in CSV format to be queried for individual values over time windows. Which storage and schema to minimize query costs?

- [ ] Use Cloud Storage. Write a Dataprep job to split the data into partitioned tables.
- [ ] Use Cloud Bigtable. Design short and wide tables, and use a new column for each single event version.
- [x] Use Cloud Bigtable. Design tall and narrow tables, and use a new row for each single event version.
- [ ] Use Cloud Storage. Join the raw file data with a BigQuery log table.


**6. Question 6**

Customer wants to maintain investment in an existing Apache Spark code data pipeline.

- [ ] BigQuery
- [ ] Dataflow
- [x] Dataproc
- [ ] Dataprep


**7. Question 7**

Host a deep neural network machine learning model on Google Cloud. Run and monitor jobs that could occasionally fail.

- [ ] Use AI Platform to host your model. Monitor the status of the Operation object for 'error' results.
- [x] Use AI Platform to host your model. Monitor the status of the Jobs object for 'failed' job states.
- [ ] Use a Google Kubernetes Engine cluster to host your model. Monitor the status of the Jobs object for 'failed' job states.
- [ ] Use a Google Kubernetes Engine cluster to host your model. Monitor the status of the Operation object for 'error' results.


**8. Question 8**

Cost-effective way to run non-critical Apache Spark jobs on Dataproc?

- [ ] Set up a cluster in high availability mode with high-memory machine types. Add 10 additional local SSDs.
- [ ] Set up a cluster in high availability mode with default machine types. Add 10 additional preemptible worker nodes.
- [x] Set up a cluster in standard mode with high-memory machine types. Add 10 additional preemptible worker nodes.
- [ ] Set up a cluster in standard mode with the default machine types. Add 10 additional local SSDs.


**9. Question 9**

Promote a Cloud Bigtable solution with a lot of data from development to production and optimize for performance.


- [ ] Change your Cloud Bigtable instance type from Development to Production, and set the number of nodes to at least 3. Verify that the storage type is HDD.
- [ ] Change your Cloud Bigtable instance type from Development to Production, and set the number of nodes to at least 3. Verify that the storage type is SSD.
- [ ] Export the data from your current Cloud Bigtable instance to Cloud Storage. Create a new Cloud Bigtable Production instance type with at least 3 nodes. Select the HDD storage type. Import the data into the new instance from Cloud Storage.
- [x] Export the data from your current Cloud Bigtable instance to Cloud Storage. Create a new Cloud Bigtable Production instance type with at least 3 nodes. Select the SSD storage type. Import the data into the new instance from Cloud Storage.


**10. Question 10**

As part of your backup plan, you want to be able to restore snapshots of Compute Engine instances using the fewest steps. 

- [ ] Export the snapshots to Cloud Storage. Create disks from the exported snapshot files. Create images from the new disks.
- [ ] Export the snapshots to Cloud Storage. Create images from the exported snapshot files.
- [ ] Use the snapshots to create replacement disks. Use the disks to create instances as needed.
- [x] Use the snapshots to create replacement instances as needed.


**11. Question 11**

You want to minimize costs to run Google Data Studio reports on BigQuery queries by using prefetch caching.

- [ ] Set up the report to use the Owner's credentials to access the underlying data in BigQuery, and direct the users to view the report only once per business day (24-hour period).
- [x] Set up the report to use the Owner's credentials to access the underlying data in BigQuery, and verify that the 'Enable cache' checkbox is selected for the report.
- [ ] Set up the report to use the Viewer's credentials to access the underlying data in BigQuery, and also set it up to be a 'view-only' report.
- [ ] Set up the report to use the Viewer's credentials to access the underlying data in BigQuery, and verify that the 'Enable cache' checkbox is not selected for the report.


**12. Question 12**

A Data Analyst is concerned that a BigQuery query could be too expensive.

- [ ] Use the LIMIT clause to limit the number of values in the results.
- [ ] Use the SELECT clause to limit the amount of data in the query. Partition data by date so the query can be more focused.
- [x] Set the Maximum Bytes Billed, which will limit the number of bytes processed but still run the query if the number of bytes requested goes over the limit.
- [ ] Use GROUP BY so the results will be grouped into fewer output values.


**13. Question 13**

BigQuery data is stored in external CSV files in Cloud Storage; as the data has increased, the query performance has dropped.

- [ ] Import the data into BigQuery for better performance.
- [x] Request more slots for greater capacity to improve performance.
- [ ] Divide the data into partitions based on date.
- [ ] Time to move to Cloud Bigtable; it is faster in all cases.


**14. Question 14**

Source data is streamed in bursts and must be transformed before use.

- [ ] Use Cloud Bigtable for fast input and cbt for ETL.
- [ ] Ingest data to Cloud Storage. Use Dataproc for ETL.
- [ ] Use Pub/Sub to buffer the data, and then use BigQuery for ETL.
- [x] Use Pub/Sub to buffer the data, and then use Dataflow for ETL.


**15. Question 15**

Calculate a running average on streaming data that can arrive late and out of order.

- [x] Use Pub/Sub and Dataflow with Sliding Time Windows.
- [ ] Use Pub/Sub and Google Data Studio.
- [ ] Pub/Sub can guarantee timely arrival and order.
- [ ] Use Dataflow's built-in timestamps for ordering and filtering.


**16. Question 16**

Testing a Machine Learning model with validation data returns 100% correct answers.

- [x] The model is working extremely well, indicating the hyperparameters are set correctly.
- [ ] The model is overfit. There is a problem.
- [ ] The model is underfit. There is a problem.
- [ ] The model is perfectly fit. You do not need to continue training.

**17. Question 17**

A client is using Cloud SQL database to serve infrequently changing lookup tables that host data used by applications. The applications will not modify the tables. As they expand into other geographic regions they want to ensure good performance. What do you recommend?

- [x] Migrate to Cloud Spanner
- [ ] Read replicas
- [ ] Instance high availability configuration
- [ ] Replicate from an external server


**18. Question 18**

A client wants to store files from one location and retrieve them from another location. Security requirements are that no one should be able to access the contents of the file while it is hosted in the cloud. What is the best option?

- [ ] Default encryption should be sufficient
- [ ] Client-side encryption
- [x] Customer-Supplied Encryption Keys (CSEK)
- [ ] Customer Managed Encryption Keys (CMEK)


**19. Question 19**

Three Google Cloud services commonly used together in data engineering solutions. (Described in this course).

- [ ] Dataproc, Cloud SQL, BigQuery
- [x] Pub/Sub, Dataflow, BigQuery
- [ ] Pub/Sub,Google Kubernetes Engine, Spanner
- [ ] Bigtable, Dataproc, Cloud Spanner


**20. Question 20**

What is AVRO used for?

- [x] Serialization and de-serialization of data so that it can be transmitted and stored while maintaining an object structure.
- [ ] AVRO is an encryption method. AVRO-256 is a 256-bit key standard.
- [ ] AVRO is a file type usually specified with `*.avr` and a common format for spreadsheets.
- [ ] AVRO is a numerical type in SQL that stores a 38 digit value with 9 digit decimal representation. It avoids rounding errors in financial calculations.


**21. Question 21**

A company has a new IoT pipeline. Which services will make this design work?

Select the services that should be used to replace the icons with the number "1" and number "2" in the diagram.

![image](https://user-images.githubusercontent.com/1645304/138025700-a4c47c1a-eef8-4482-b133-87310e70fc2c.png)


- [ ] IoT Core, Datastore
- [x] Pub/Sub, Storage
- [ ] IoT Core, Pub/Sub
- [ ] App Engine, IoT Core


**22. Question 22**

A company wants to connect cloud applications to an Oracle database in its data center. Requirements are a maximum of 9 Gbps of data and a Service Level Agreement (SLA) of 99%.

- [ ] Implement a high-throughput Cloud VPN connection
- [ ] Cloud Router with VPN
- [x] Dedicated Interconnect
- [ ] Partner Interconnect

**23. Question 23**

A client has been developing a pipeline based on PCollections using local programming techniques and is ready to scale up to production. What should they do?

- [x] They should use the Dataflow Cloud Runner.
- [ ] They should upload the pipeline to Dataproc.
- [ ] They should use the local version of runner.
- [ ] Import the pipeline into BigQuery.


**24. Question 24**

A company has migrated their Hadoop cluster to the cloud and is now using  Dataproc with the same settings and same methods as in the data center. What would you advise them to do to make better use of the cloud environment?

- [ ] Upgrade to the latest version of HDFS. Change the settings in Hadoop components to optimize for the different kinds of work in the mix.
- [ ] Find more jobs to run so the cluster utilizations will cost-justify the expense.
- [x] Store persistent data off-cluster. Start a cluster for one kind of work then shut it down when it is not processing data.
- [ ] Migrate from Dataproc to an open source Hadoop Cluster hosted on Compute Engine, because this is the only way to get all the Hadoop customizations needed for efficiency.


**25. Question 25**

An application has the following data requirements. 1. It requires strongly consistent transactions. 2. Total data will be less than 500 GB. 3. The data does not need to be streaming or real time. Which data technology would fit these requirements?

- [ ] BigQuery
- [ ] Cloud Bigtable
- [x] Cloud SQL
- [ ] Memorystore



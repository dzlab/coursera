# Exam A
**QUESTION 1**
You are deploying 10,000 new Internet of Things devices to collect temperature data in your warehouses globally. You need to process, store and analyze these very large datasets in real time. What should you do?
- [ ] A. Send the data to Google Cloud Datastore and then export to BigQuery.
- [ ] B. Send the data to Google Cloud Pub/Sub, stream Cloud Pub/Sub to Google Cloud Dataflow, and store the data in Google BigQuery.
- [ ] C. Send the data to Cloud Storage and then spin up an Apache Hadoop cluster as needed in Google Cloud Dataproc whenever analysis is required.
- [ ] D. Export logs in batch to Google Cloud Storage and then spin up a Google Cloud SQL instance, import the data from Cloud Storage, and run an analysis as needed.

```diff
+ Correct Answer: B Section: (none) Explanation
```

**QUESTION 2**

You have spent a few days loading data from comma-separated values (CSV) files into the Google BigQuery table CLICK_STREAM. The column DT stores the epoch time of click events. For convenience, you chose a simple schema where every field is treated as the STRING type. Now, you want to compute web session durations of users who visit your site, and you want to change its data type to the TIMESTAMP. You want to minimize the migration effort without making future queries computationally expensive. What should you do?
- [ ] A. Delete the table CLICK_STREAM, and then re-create it such that the column DT is of the TIMESTAMP type. Reload the data.
- [ ] B. Add a column TS of the TIMESTAMP type to the table CLICK_STREAM, and populate the numeric values from the column TS for each row. Reference the column TS instead of the column DT from now on.
- [ ] C. Create a view CLICK_STREAM_V, where strings from the column DT are cast into TIMESTAMP values. Reference the view CLICK_STREAM_V instead of the table CLICK_STREAM from now on.
- [ ] D. Add two columns to the table CLICK STREAM: TS of the TIMESTAMP type and IS_NEW of the BOOLEAN type. Reload all data in append mode. For each  appended row, set the value of IS_NEW to true. For future queries, reference the column TS instead of the column DT, with the WHERE clause ensuring that the value of IS_NEW must be true.
- [ ] E. Construct a query to return every row of the table CLICK_STREAM, while using the built-in function to cast strings from the column DT into TIMESTAMP values. Run the query into a destination table NEW_CLICK_STREAM, in which the column TS is the TIMESTAMP type. Reference the table NEW_CLICK_STREAM instead of the table CLICK_STREAM from now on. In the future, new data is loaded into the table NEW_CLICK_STREAM.

```diff
+ Correct Answer: D Section: (none) Explanation
Explanation/Reference:
```

**QUESTION 3**

You want to use Google Stackdriver Logging to monitor Google BigQuery usage. You need an instant notification to be sent to your monitoring tool when new data is appended to a certain table using an insert job, but you do not want to receive notifications for other tables. What should you do?
- [ ] A. Make a call to the Stackdriver API to list all logs, and apply an advanced filter.
- [ ] B. In the Stackdriver logging admin interface, and enable a log sink export to BigQuery.
- [ ] C. In the Stackdriver logging admin interface, enable a log sink export to Google Cloud Pub/Sub, and subscribe to the topic from your monitoring tool.
- [ ] D. Using the Stackdriver API, create a project sink with advanced log filter to export to Pub/Sub, and subscribe to the topic from your monitoring tool.

```diff
+ Correct Answer: B Section: (none) Explanation
Explanation/Reference:
```

**QUESTION 4**

You are working on a sensitive project involving private user data. You have set up a project on Google Cloud Platform to house your work internally. An external consultant is going to assist with coding a complex transformation in a Google Cloud Dataflow pipeline for your project. How should you maintain users’ privacy?
- [ ] A. Grant the consultant the Viewer role on the project.
- [ ] B. Grant the consultant the Cloud Dataflow Developer role on the project.
- [ ] C. Create a service account and allow the consultant to log on with it.
- [ ] D. Create an anonymized sample of the data for the consultant to work with in a different project.

```diff
+ Correct Answer: C
 Section: (none) Explanation
Explanation/Reference:
```

**QUESTION 5**

You are building a model to predict whether or not it will rain on a given day. You have thousands of input features and want to see if you can improve training speed by removing some features while having a minimum effect on model accuracy. What can you do?
- [ ] A. Eliminate features that are highly correlated to the output labels.
- [ ] B. Combine highly co-dependent features into one representative feature.
- [ ] C. Instead of feeding in each feature individually, average their values in batches of 3.
- [ ] D. Remove the features that have null values for more than 50% of the training records.

```diff
+ Correct Answer: B Section: (none) Explanation
Explanation/Reference:
```

**QUESTION 6**

Your company is performing data preprocessing for a learning algorithm in Google Cloud Dataflow. Numerous data logs are being are being generated during this step, and the team wants to analyze them. Due to the dynamic nature of the campaign, the data is growing exponentially every hour.
The data scientists have written the following code to read the data for a new key features in the logs.

```
BigQueryIO.Read
.named(“ReadLogData”) .from(“clouddataflow-readonly:samples.log_data”)
```

You want to improve the performance of this data read. What should you do?
- [ ] A. Specify the TableReference object in the code.
- [ ] B. Use .fromQuery operation to read specific fields from the table.
- [ ] C. Use of both the Google BigQuery TableSchema and TableFieldSchema classes.
- [ ] D. Call a transform that returns TableRow objects, where each element in the PCollection represents a single row in the table.

```diff
Correct Answer: D Section: (none)
 Explanation Explanation/Reference:
```

**QUESTION 7**

Your company is streaming real-time sensor data from their factory floor into Bigtable and they have noticed extremely poor performance. How should the row key be redesigned to improve Bigtable performance on queries that populate real-time dashboards?
- [ ] A. Use a row key of the form `<timestamp>`.
- [ ] B. Use a row key of the form `<sensorid>`.
- [ ] C. Use a row key of the form `<timestamp>#<sensorid>`.
- [ ] D. Use a row key of the form `#<sensorid>#<timestamp>`.

```diff
Correct Answer: D Section: (none) Explanation
Explanation/Reference:
```

**QUESTION 8**

Your company’s customer and order databases are often under heavy load. This makes performing analytics against them difficult without harming operations. The databases are in a MySQL cluster, with nightly backups taken using mysqldump. You want to perform analytics with minimal impact on operations. What should you do?
- [ ] A. Add a node to the MySQL cluster and build an OLAP cube there.
- [ ] B. Use an ETL tool to load the data from MySQL into Google BigQuery.
- [ ] C. Connect an on-premises Apache Hadoop cluster to MySQL and perform ETL.
- [ ] D. Mount the backups to Google Cloud SQL, and then process the data using Google Cloud Dataproc.

```diff
Correct Answer: C Section: (none) Explanation
Explanation/Reference:
```

**QUESTION 9**

You have Google Cloud Dataflow streaming pipeline running with a Google Cloud Pub/Sub subscription as the source. You need to make an update to the code that https://www.gratisexam.com/
will make the new Cloud Dataflow pipeline incompatible with the current version. You do not want to lose any data when making this update. What should you do?
- [ ] A. Update the current pipeline and use the drain flag.
- [ ] B. Update the current pipeline and provide the transform mapping JSON object.
- [ ] C. Create a new pipeline that has the same Cloud Pub/Sub subscription and cancel the old pipeline.
- [ ] D. Create a new pipeline that has a new Cloud Pub/Sub subscription and cancel the old pipeline.

```diff
Correct Answer: D Section: (none) Explanation
Explanation/Reference:
```

**QUESTION 10**

Your company is running their first dynamic campaign, serving different offers by analyzing real-time data during the holiday season. The data scientists are collecting terabytes of data that rapidly grows every hour during their 30-day campaign. They are using Google Cloud Dataflow to preprocess the data and collect the feature (signals) data that is needed for the machine learning model in Google Cloud Bigtable. The team is observing suboptimal performance with reads and writes of their initial load of 10 TB of data. They want to improve this performance while minimizing cost. What should they do?
- [ ] A. Redefine the schema by evenly distributing reads and writes across the row space of the table.
- [ ] B. The performance issue should be resolved over time as the site of the BigDate cluster is increased.
- [ ] C. Redesign the schema to use a single row key to identify values that need to be updated frequently in the cluster.
- [ ] D. Redesign the schema to use row keys based on numeric IDs that increase sequentially per user viewing the offers.

Correct Answer: A Section: (none) Explanation
Explanation/Reference:

**QUESTION 11**

Your software uses a simple JSON format for all messages. These messages are published to Google Cloud Pub/Sub, then processed with Google Cloud Dataflow to create a real-time dashboard for the CFO. During testing, you notice that some messages are missing in the dashboard. You check the logs, and all messages are being published to Cloud Pub/Sub successfully. What should you do next?
- [ ] A. Check the dashboard application to see if it is not displaying correctly.
- [ ] B. Run a fixed dataset through the Cloud Dataflow pipeline and analyze the output.
- [ ] C. Use Google Stackdriver Monitoring on Cloud Pub/Sub to find the missing messages.
- [ ] D. Switch Cloud Dataflow to pull messages from Cloud Pub/Sub instead of Cloud Pub/Sub pushing messages to Cloud Dataflow.

```diff
Correct Answer: B Section: (none) Explanation
Explanation/Reference:
```

## QUESTION 12

**Flowlogistic Case Study**

**Company Overview**

Flowlogistic is a leading logistics and supply chain provider. They help businesses throughout the world manage their resources and transport them to their final destination. The company has grown rapidly, expanding their offerings to include rail, truck, aircraft, and oceanic shipping.

**Company Background**
The company started as a regional trucking company, and then expanded into other logistics market. Because they have not updated their infrastructure, managing and tracking orders and shipments has become a bottleneck. To improve operations, Flowlogistic developed proprietary technology for tracking shipments in real time at the parcel level. However, they are unable to deploy it because their technology stack, based on Apache Kafka, cannot support the processing volume. In addition, Flowlogistic wants to further analyze their orders and shipments to determine how best to deploy their resources.

**Solution Concept**

Flowlogistic wants to implement two concepts using the cloud:
- Use their proprietary technology in a real-time inventory-tracking system that indicates the location of their loads
- Perform analytics on all their orders and shipment logs, which contain both structured and unstructured data, to determine how best to deploy resources, which markets to expand info. They also want to use predictive analytics to learn earlier when a shipment will be delayed.

**Existing Technical Environment**
Flowlogistic architecture resides in a single data center:

Databases
- 8 physical servers in 2 clusters
  - SQL Server – user data, inventory, static data 3 physical servers
  - Cassandra – metadata, tracking messages

- 10 Kafka servers – tracking message aggregation and batch insert

Application servers – customer front end, middleware for order/customs
- 60 virtual machines across 20 physical servers
  - Tomcat – Java services
  - Nginx – static content
  - Batch servers
- Storage appliances
  - iSCSI for virtual machine (VM) hosts
  - Fibre Channel storage area network (FC SAN) – SQL server storage
  - Network-attached storage (NAS) image storage, logs, backups
- 10 Apache Hadoop /Spark servers
  - Core Data Lake
  - Data analysis workloads
- 20 miscellaneous servers
  - Jenkins, monitoring, bastion hosts,

**Business Requirements**
- Build a reliable and reproducible environment with scaled panty of production.
- Aggregate data in a centralized Data Lake for analysis
- Use historical data to perform predictive analytics on future shipments
- Accurately track every shipment worldwide using proprietary technology
- Improve business agility and speed of innovation through rapid provisioning of new resources Analyze and optimize architecture for performance in the cloud
- Migrate fully to the cloud if all other requirements are met

**Technical Requirements**
- Handle both streaming and batch data
- Migrate existing Hadoop workloads
- Ensure architecture is scalable and elastic to meet the changing demands of the company. Use managed services whenever possible
- Encrypt data flight and at rest'
- Connect a VPN between the production data center and cloud environment

**SEO Statement**
We have grown so quickly that our inability to upgrade our infrastructure is really hampering further growth and efficiency. We are efficient at moving shipments around the world, but we are inefficient at moving data around.
We need to organize our information so we can more easily understand where our customers are and what they are shipping.

**CTO Statement**



# Professional Cloud Developer Sample Questions

## 1
Your team has developed a mobile web application where global users vote on popular topics. For each topic, you expect a very high volume of votes during each individual 30-minute voting window. You need to capture and count all votes within 24 hours and then store the votes for future analysis and reporting. What should you do?

- [ ] A. Save the votes to Memorystore, and use Cloud Functions to insert the data into BigQuery. Display the results in Google Data Studio.
- [x] B. Publish the votes to Pub/Sub, and use a Datafow pipeline to insert the data into BigQuery. Display the results in Google Data Studio.
- [ ] C. Publish the votes to Pub/Sub, and use Cloud Functions to insert the data into Cloud Storage. Display the results in Google Data Studio.
- [ ] D. Use Firebase to authenticate the mobile users, and publish the data directly to the database. Export the data to a CSV file, and import it into Sheets for reporting.

**Feedback**
```diff
- A. Incorrect. Memorystore is an in-memory database not suitable for data analysis.
+ B. Correct. Pub/Sub supports the ingestion of millions of records per second and guarantees the delivery of the messages. BigQuery should be used for analysis.
- C. Incorrect. Cloud Functions is event-driven and is not meant for long-running tasks. Also storing analytics in a blob store vs BigQuery is not optimal.
- D. Incorrect. Given the high number of votes, writing the votes to Pub/Sub is a better choice. Additionally, exporting the data would be a one-time action vs being able to analyze data in BigQuery over time.
```
- https://cloud.google.com/pubsub/docs/publisher
- https://cloud.google.com/sql/docs/mysql/create-instance
- https://cloud.google.com/memorystore/ 
- https://cloud.google.com/bigquery/docs/visualize-data-studio


## 2
![image](https://user-images.githubusercontent.com/1645304/163494343-f3617bc3-df9c-4b23-9832-530bdf2b84ee.png)
- [ ] A. Migrate the database to Cloud SQL. Then import the session data into Cloud Bigtable.
- [ ] B. Migrate the database to BigQuery. Then import the session data into Firestore in Native mode.
- [x] C. Migrate the database to Cloud SQL. Then import the session data into Firestore in Native mode.
- [ ] D. Create a Compute Engine virtual machine instance in Google Cloud, and install PostgreSQL and MongoDB Server software. Migrate the database to the new PostgreSQL, and then migrate the session data to MongoDB.

**Feedback**
```diff
- A is incorrect. Bigtable is a bit of an overkill for this test - this NoSQL DB is more performant and stores data in a unique way which can help with time-series data (such as Financial market data).
- B is incorrect. BigQuery is a data warehouse. It has limited update/delete capabilities for inserted rows and hence is a bad choice for user session data, which changes as the session with the user progresses.
+ C is correct. Cloud SQL is the managed PostgreSQL database and migration will not require any schema changes. Firestore in Native mode is recommended for storing user-session information and is a natural choice for this test.
- D is incorrect. This doesn’t use any managed service and will increase testing time since it will require database server management.
```
- https://cloud.google.com/bigtable/docs/overview
- https://cloud.google.com/solutions/building-scalable-web-apps-with-cloud-datastore
- https://cloud.google.com/bigquery/docs/loading-data-cloud-firestore
- https://cloud.google.com/sql/docs/postgres/import-export/importing
- https://cloud.google.com/solutions/migrating-postgresql-to-gcp


## 3
Your development team uses GitHub to manage their code. You need to perform debugging tasks to resolve an error that was recently reported by the QA team. What should you do?
- [ ] A. Ask a reviewer to analyze the code in the GitHub pull request.
- [x] B. Set up Cloud Debugger, create a snapshot, and set log points.
- [ ] C. Pull your code from GitHub, and troubleshoot with Cloud Trace.
- [ ] D. Set up Cloud Profiler, pull your code from GitHub, and create snapshots.

**Feedback**
```diff
- A is not correct because this is a manual process and does not actually perform debugging
+ B is correct because Cloud Debugger allows you to:
+ - take debug snapshots, which lets you view the state of local variables and the call stack in your app at specific points in your code
+ - add log-points to your code, which lets you inject logging into a running service without restarting it or interfering with its normal function.
- C is not correct because Cloud Trace does not natively provide debugging capabilities but it’s used for tracking down performance issues.
- D is not correct because Cloud Profiler does not perform debugging, but analyzes running services.
```
- https://cloud.google.com/source-repositories/docs/debug-overview
- https://cloud.google.com/source-repositories/docs/debug-snapshots
- https://cloud.google.com/debugger/docs/source-options#github


## 4
You have written a Cloud Function in Node.js with source code stored in a Git repository. You want any committed changes to the source to be automatically tested. You write a Cloud Build configuration that pushes the source to a uniquely named Cloud Function, then calls the function as a test, and then deletes the Cloud Function as cleanup. You discover that if the test fails, the Cloud Function is not deleted. What should you do?
- [ ] A. Change the order of the steps to delete the Cloud Function before performing the test, which can indicate a result failure.
- [ ] B. Include a waitFor option in the configuration for the Cloud Function deletion that identifies the test step as a required preceding step.
- [x] C. Have the test write its results to a file and return 0. Add a final step after the Cloud Function deletion that checks whether the file contains the expected results.
- [ ] D. Have the test set its outcome in an environment variable called result and return 0. Add a final step after the Cloud Function deletion that checks whether the result contains the expected results.

## 5
You have deployed a web application in a Google Kubernetes Engine (GKE) cluster. You are reviewing the Cloud Monitoring metrics and find that your cluster’s CPU load fluctuates throughout the day. To maximize performance while minimizing cost, you want the number of replicas to automatically adjust. What should you do?
- [ ] A. Modify the managed instance group (MIG) to enable Autoscaling to configure max and min amount of nodes based on CPU load.
- [x] B. Enable Cluster Autoscaler on the GKE cluster, and configure the Horizontal Pod Autoscaler (HPA) to autoscale the workload based on CPU load.
- [ ] C. Enable Cluster Autoscaler on the GKE cluster, and configure the HPA to autoscale the workloads based on a custom metric.
- [ ] D. Modify the MIG to enable Autoscaling to configure max and min amount of nodes based on CPU load, and configure the Vertical Pod Autoscaler (VPA) to scale workloads based on CPU load.

## 6
You have a Java application running on the App Engine flexible environment. Your application’s error messages do not appear in the Error Reporting console. What should you do?
- [ ] A. Ensure that Cloud Monitoring client libraries are bundled with the Java application.
- [ ] B. Verify that application logs are being written to the correct regional storage bucket.
- [x] C. Test the container locally, and verify that application errors are being written to stderr.
- [ ] D. Use API Explorer to create a Cloud Logging log record, and validate that it is recognized by Error Reporting.

## 7
> For this question, refer to the HipLocal case study: [goo.gl/NpR3y2](https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf)
Which database should HipLocal use for storing state while minimizing application changes?
- [ ] A. Firestore
- [ ] B. BigQuery
- [x] C. Cloud SQL
- [ ] D. Cloud Bigtable

## 8
> For this question, refer to the HipLocal case study: [goo.gl/NpR3y2](https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf)

HipLocal needs to implement a solution that meets their business requirement of supporting a large increase in concurrent users. What approach should they take?
- [x] A. Use a load testing tool to load-test the application.
- [ ] B. Use a code test coverage tool to verify the code coverage.
- [ ] C. Use a security analysis tool to perform static security code analyses.
- [ ] D. Use a CI/CD tool to introduce canary testing into the release pipeline.

## 9
> For this question, refer to the HipLocal case study: [goo.gl/NpR3y2](https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf)

How should HipLocal improve their software release velocity without significantly impacting reliability or increasing cost? (select two)
- [ ] A. Remove QA freezes and test in production after deployment.
- [x] B. Remove QA freezes and use canaries to evaluate releases instead.
- [ ] C. Assign additional DevOps engineers to test the software releases.
- [ ] D. Assign additional QA testers to shorten the duration of their QA freezes.
- [x] E. Automate the release of virtual machine (VM) images using CI/CD processes.

## 10
> For this question, refer to the HipLocal case study: [goo.gl/NpR3y2](https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf)

HipLocal is migrating the user state data to Cloud SQL. Cloud SQL will be deployed in the same region as the application. What connection strategy should they implement to meet the requirements while following Google-recommended best practices?
- [ ] A. Connect the application to the private IP address.
- [x] B. Deploy and configure the Cloud SQL proxy. Connect the application to the proxy.
- [ ] C. Run MySQL client along with the application. Configure the application to call the MySQL client to connect to the database.
- [ ] D. Configure a public IP address on Cloud SQL, and configure Cloud SQL to require SSL for connections. Connect the application to the public IP address.

## 11

> For this question, refer to the HipLocal case study: [goo.gl/NpR3y2](https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf)

Which architecture should HipLocal use for log analysis?
- [ ] A. Use Cloud Spanner to store each event.
- [ ] B. Start storing key metrics in Memorystore.
- [x] C. Use Cloud Logging with a BigQuery sink.
- [ ] D. Use Cloud Logging with a Cloud Storage sink.

## 12
You are analyzing your application’s performance. You observe that certain Cloud Bigtable tables in your cluster are used much more than others, causing inconsistent application performance for end users. You discover that some tablets have large sections of similarly named row keys and are heavily utilized, while other tablets are running idle. You discover that a user’s ZIP code is the first component of the row key, and your application is being heavily used by profiles originating from that ZIP code. You want to change how you generate row keys so that they are human readable and so that Cloud Bigtable demand is more evenly distributed within the cluster. What should you do?
- [ ] A. Use serially generated integer values.
- [x] B. Use a subset of the MD5 hash of the row contents.
- [ ] C. Use a concatenation of multiple human-readable attributes.
- [ ] D. Use UNIX epoch-styled timestamps represented in milliseconds.

## 13
Your company has a successful multi-player game that has become popular in the US. Now, it wants to expand to other regions. It is launching a new feature that allows users to trade points. This feature will work for users across the globe. Your company’s current MySQL backend is reaching the limit of the Compute Engine instance that hosts the game. Your company wants to migrate to a different database that will provide global consistency and high availability across the regions. Which database should they choose?
- [ ] A. BigQuery
- [ ] B. Cloud SQL
- [x] C. Cloud Spanner
- [ ] D. Cloud Bigtable

## 14
Your company plans to expand their analytics use cases. One of the new use cases requires your data analysts to analyze events using SQL on a near real–time basis. You expect rapid growth and want to use managed services as much as possible. What should you do?
- [x] A. Create a Pub/Sub topic and a subscription. Stream your events from the source into the Pub/Sub topic. Leverage Dataflow to ingest these events into BigQuery.
- [ ] B. Create a Pub/Sub topic and a subscription. Stream your events from the source into the Pub/Sub topic. Leverage Dataflow to ingest these events into Cloud Storage.
- [ ] C. Create a Pub/Sub topic and a subscription. Stream your events from the source into the Pub/Sub topic. Leverage Dataflow to ingest these events into Firestore in Datastore mode.
- [ ] D. Create a Kafka instance on a large Compute Engine instance. Stream your events from the source into a Kafka pipeline. Leverage Dataflow to ingest these events into Cloud Storage.

## 15
Your organization develops and tests multiple applications on Compute Engine virtual machine instances across 3 environments; Test, Staging, and Production. The separate development teams for each application require minimal access to Production but broad access in Test and Staging. You need to design the Resource Manager structure to support your organization in following least-privilege best practices. What should you do?
- [ ] A. Create one project per environment per application. Assign the application team members an IAM role at the project level.
- [ ] B. Create one project per environment. Assign the application team members an Identity Access Management (IAM) role at the project level.
- [ ] C. Create one project per environment. Group each application team member into a Google Group. Assign the application team’s Google Group an IAM role at the project level.
- [x] D. Create one project per environment per application. Group each application team member into a Google Group. Assign the application team’s Google Group an IAM role at the project level.

## 16
Your application that is deployed in the App Engine standard environment receives a large amount of traffic. You are concerned that deploying changes to the application could affect all users negatively. You want to avoid full-scale load testing due to cost concerns, but you still want to deploy new features as quickly as possible. Which approach should you take?
- [ ] A. Schedule weekly load tests against the production application.
- [ ] B. Use the local development environment to perform load testing outside Google Cloud.
- [ ] C. Before allowing users to access new features, deploy as a new version and perform smoke tests. Then enable all users to access the new features.
- [x] D. Use App Engine traffic splitting to have a smaller part of the users test out new features, and slowly adjust traffic splitting until all users get the new features.

## 17
You have two tables in Cloud SQL with identical columns that you need to quickly combine into a single table, removing duplicate rows from the result set. What should you do?
- [ ] A. Use the JOIN operator in SQL to combine the tables.
- [ ] B. Use nested WITH statements to combine the tables.
- [x] C. Use the UNION operator in SQL to combine the tables.
- [ ] D. Query the tables from a Linux shell, combine the results into a single CSV, and re-import the rows into the database. Use the UNION ALL operator in SQL to combine the tables.

## 18
Your website is deployed on Compute Engine. Your marketing team wants to test conversion rates between 3 different website designs. You are not able to make changes to your application code. What should you do?
- [x] A. Deploy website on App Engine and use traffic splitting.
- [ ] B. Deploy website on App Engine as three separate services.
- [ ] C. Deploy website on Cloud Functions as three separate functions.
- [ ] D. Deploy website on Cloud Functions and implement custom code to show different designs.


## 19
You are building a storage layer for an analytics Hadoop cluster in a region for your company. This cluster will run multiple jobs on a nightly basis, and you need to access the data frequently. You want to use Cloud Storage for this purpose. What is the most cost effective option?
- [ ] A. Regional Coldline storage
- [ ] B. Regional Nearline storage
- [x] C. Regional Standard storage
- [ ] D. Multi-regional Standard storage


## 20
You have an application that accepts inputs from users. The application needs to kick off different background tasks based on these inputs. You want to allow for automated asynchronous execution of these tasks as soon as input is submitted by the user. Which product should you use?
- [ ] A. Pub/Sub
- [x] B. Cloud Tasks
- [ ] C. Cloud Bigtable
- [ ] D. Cloud Composer


## 21
You have a data warehouse built on BigQuery that contains a table with array fields. To analyze the data for a specific use case using Standard SQL, you need to read all elements from the array and write them with all other non-array fields in a table. You don’t want to lose any records if they don’t match records in the array fields. What should you do?
- [ ] A. Perform SELECT * FROM tablename.
- [x] B. Perform UNNEST and JOIN with the table to get these results.
- [ ] C. Perform UNNEST and INNER JOIN with the table to get these results.
- [ ] D. Perform UNNEST and CROSS JOIN with the table to get these results.


## 22
You have deployed your website in a managed instance group. The managed instance group is configured to have a size of three instances and to perform an HTTP health check on port 80. When the managed instance group is created, three instances are created and started. When you connect to the instance using SSH, you confirm that the website is running and available on port 80. However, the managed instance group is re-creating the instances when they fail verification. What should you do?
- [ ] A. Change the type to an unmanaged instance group.
- [ ] B. Disable autoscaling on the managed instance group.
- [x] C. Increase the initial delay timeout to ensure that the instance is created.
- [ ] D. Check the firewall rules and ensure that the probes can access the instance.

## 23
Your team is using App Engine to write every Pub/Sub message to both a Cloud Storage object and a BigQuery table. You want to minimize operational overhead. Which architecture should you implement?

![image](https://user-images.githubusercontent.com/1645304/163509280-e87cbe93-3800-4ad7-9f62-d2377f73c197.png)

- [ ] A.
- [ ] B.
- [x] C.
- [ ] D.

## 24
As your organization has grown, new teams need access to manage network connectivity within and across projects. You are now seeing intermittent timeout errors in your application. You want to find the cause of the problem. What should you do?
- [x] A. Configure VPC flow logs for each of the subnets in your VPC.
- [ ] B. Configure firewall rules logging for each of the firewalls in your VPC.
- [ ] C. Set up wireshark on each Google Cloud Virtual Machine instance.
- [ ] D. Review the instance admin activity logs in Cloud Logging for the application instances.

## 25
Your application starts on the virtual machine (VM) as a systemd service. Your application outputs its log information to stdout. You want to review the application logs. What should you do?
- [ ] A. Review the application logs from the Compute Engine VM instance activity logs in Cloud Logging.
- [ ] B. Review the application logs from the Compute Engine VM instance data access logs in Cloud Logging.
- [x] C. Install Cloud Logging Agent. Review the application logs from the Compute Engine VM instance syslog logs in Cloud Logging.
- [ ] D. Install Cloud Logging Agent. Review the application logs from the Compute Engine VM instance system event logs in Cloud Logging.

## 26
You are capturing important audit activity in Cloud Logging. You need to read the information from Cloud Logging to perform real-time analysis of the logs. You will have multiple processes performing different types of analysis on the logging data. What should you do?
- [ ] A. Read the logs directly from the Cloud Logging API.
- [ ] B. Set up a Cloud Logging sync to Pub/Sub, and read the logs from a Pub/Sub topic.
- [x] C. Set up a Cloud Logging sync to BigQuery, and read the logs from the BigQuery table.
- [ ] D. Set up a Cloud Logging sync to Cloud Storage, and read the logs from a Cloud Storage bucket.

## 27
You want to upload files from an on-premises virtual machine to Cloud Storage as part of a data migration. These files will be consumed by a Dataproc Hadoop cluster in a Google Cloud environment. Which command should you use?
- [x] A. `gsutil cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/`
- [ ] B. `gcloud cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/`
- [ ] C. `hadoop fs cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/`
- [ ] D. `gcloud dataproc cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/`

## 28
You are writing an API endpoint to process orders from a web application and save the data into a Datastore collection. During application testing, you notice that when your application encounters an HTTP 5xx server error from the Datastore API, it catches this error and returns an HTTP 200 OK response code to the client, but does not store the data within Datastore. You want the consumers of your API endpoint to know that the write request was unsuccessful. What should you do?
- [ ] A. Return an HTTP 204 No Content response.
- [ ] B. Return an HTTP 406 Not Acceptable response.
- [x] C. Return an HTTP 500 Internal Server Error response.
- [ ] D. Retry the Datastore API with exponential backoff until Datastore returns a HTTP 2xx response.

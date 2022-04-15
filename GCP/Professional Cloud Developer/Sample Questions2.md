# Sample Questions

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

**Feedback**
```diff
- A is incorrect. This is the biggest red-herring but sounds good. While it might be nice to delete the function before performing the test, and hence be assured that we won't have the function at the end, if we delete the function before performing the test there will be no function to actually test. Technically, we could accomplish this, however functionally it won't work.
- B is incorrect. The Cloud Build waitFor is used to synchronize parallel steps. If a step identifies a previous step in a waitFor and the previous step fails then the Cloud Build as a whole will fail and no further execution will make progress.

+ C is correct. There is a persistent file system that is shared between steps in a Cloud Build. We change the story to be:
+ 1. Deploy the Cloud Function.
+ 2. Save the results of calling the Cloud Function to a file.
+ 3. Delete the Cloud Function.
+ 4. Test the content of the file.
+ Since step 2 can now never fail, step 3 is executed and step 4 defines the outcome of the build as a whole.

- D is incorrect. Environment variables exist locally in the container in which the step executes. When the step completes, the container is destroyed and takes its environment variables with it. These variables are thus not available in subsequent steps and hence can't be used as a communication between distinct steps.
```

- https://cloud.google.com/build/docs/configuring-builds/configure-build-step-order
- https://cloud.google.com/build/docs/configuring-builds/create-basic-configuration
- https://cloud.google.com/build/docs/build-config

## 5
You have deployed a web application in a Google Kubernetes Engine (GKE) cluster. You are reviewing the Cloud Monitoring metrics and find that your cluster’s CPU load fluctuates throughout the day. To maximize performance while minimizing cost, you want the number of replicas to automatically adjust. What should you do?
- [ ] A. Modify the managed instance group (MIG) to enable Autoscaling to configure max and min amount of nodes based on CPU load.
- [x] B. Enable Cluster Autoscaler on the GKE cluster, and configure the Horizontal Pod Autoscaler (HPA) to autoscale the workload based on CPU load.
- [ ] C. Enable Cluster Autoscaler on the GKE cluster, and configure the HPA to autoscale the workloads based on a custom metric.
- [ ] D. Modify the MIG to enable Autoscaling to configure max and min amount of nodes based on CPU load, and configure the Vertical Pod Autoscaler (VPA) to scale workloads based on CPU load.

**Feedback**
```diff
- A is not correct because you should not use Compute Engine's autoscaling feature on instance groups created by GKE.
+ B is the recommended approach to autoscale a Kubernetes Deployment.
- C is not correct because CPU metrics are enabled by default and custom metrics are unnecessary.
- D is not correct because you should not use Compute Engine's autoscaling feature on instance groups created by GKE.
```

- https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler
- https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler
- https://cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps


## 6
You have a Java application running on the App Engine flexible environment. Your application’s error messages do not appear in the Error Reporting console. What should you do?
- [ ] A. Ensure that Cloud Monitoring client libraries are bundled with the Java application.
- [ ] B. Verify that application logs are being written to the correct regional storage bucket.
- [x] C. Test the container locally, and verify that application errors are being written to stderr.
- [ ] D. Use API Explorer to create a Cloud Logging log record, and validate that it is recognized by Error Reporting.

**Feedback**
```diff
- A is not correct because no external libraries are required for error reporting in App Engine environments.
- B. is not correct because Error Reporting is a global service built on Cloud Logging, and it does not analyze logs stored in regional log buckets or logs routed to other projects.
+ C is correct because errors must be written to stderr in App Engine Flexible to be recognized by Error Reporting.
- D is not correct because API Explorer can be used for Logging API - not Error Reporting API.
```

- https://cloud.google.com/error-reporting/docs/troubleshooting

## 7
> For this question, refer to the HipLocal case study: [goo.gl/NpR3y2](https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf)
Which database should HipLocal use for storing state while minimizing application changes?
- [ ] A. Firestore
- [ ] B. BigQuery
- [x] C. Cloud SQL
- [ ] D. Cloud Bigtable

**Feedack**
```diff
- A is incorrect because it requires developing a new data model and changing the application data access code significantly.
- B is incorrect because BigQuery is an analytics database.
+ C is correct as it is a managed offering that will require the least application changes.
- D is incorrect because Bigtable is not designed as a key/value store for state.
```
- https://cloud.google.com/sql/docs/

## 8
> For this question, refer to the HipLocal case study: [goo.gl/NpR3y2](https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf)

HipLocal needs to implement a solution that meets their business requirement of supporting a large increase in concurrent users. What approach should they take?
- [x] A. Use a load testing tool to load-test the application.
- [ ] B. Use a code test coverage tool to verify the code coverage.
- [ ] C. Use a security analysis tool to perform static security code analyses.
- [ ] D. Use a CI/CD tool to introduce canary testing into the release pipeline.

**Feedback**
```diff
+ A is correct because with load testing you can ensure you are able to handle the increased usage.
- B is not correct because for Unit Coverage, overall it’s good practice but it doesn’t explicitly help with handling a larger workload.
- C is not correct because static code analysis won’t help with supporting 10x new users.
- D is not correct because this only helps with introducing new features, not with load testing.
```

- https://www.atlassian.com/software/clover
- https://jmeter.apache.org/
- https://snyk.io/blog/secure-code-review/
- https://cloud.google.com/solutions/application-deployment-and-testing-strategies#canary_test_pattern
- https://cloud.google.com/blog/products/application-development/release-with-confidence-how-testing-and-cicd-can-keep-bugs-out-of-production

## 9
> For this question, refer to the HipLocal case study: [goo.gl/NpR3y2](https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf)

How should HipLocal improve their software release velocity without significantly impacting reliability or increasing cost? (select two)
- [ ] A. Remove QA freezes and test in production after deployment.
- [x] B. Remove QA freezes and use canaries to evaluate releases instead.
- [ ] C. Assign additional DevOps engineers to test the software releases.
- [ ] D. Assign additional QA testers to shorten the duration of their QA freezes.
- [x] E. Automate the release of virtual machine (VM) images using CI/CD processes.

**Feedback**
```diff
- A. Incorrect because this will impact service reliability by introducing more bugs into production.
+ B. Correct because this will address their requirements as stated without impacting reliability or cost.
- C. Incorrect because this will increase cost.
- D. Incorrect because this will increase cost.
+ E. Correct because this will address their requirements directly.
```
- https://cloud.google.com/solutions/continuous-delivery/

## 10
> For this question, refer to the HipLocal case study: [goo.gl/NpR3y2](https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf)

HipLocal is migrating the user state data to Cloud SQL. Cloud SQL will be deployed in the same region as the application. What connection strategy should they implement to meet the requirements while following Google-recommended best practices?
- [ ] A. Connect the application to the private IP address.
- [x] B. Deploy and configure the Cloud SQL proxy. Connect the application to the proxy.
- [ ] C. Run MySQL client along with the application. Configure the application to call the MySQL client to connect to the database.
- [ ] D. Configure a public IP address on Cloud SQL, and configure Cloud SQL to require SSL for connections. Connect the application to the public IP address.

**Feedback**
```diff
- A is not correct because connecting to a private IP requires additional steps
+ B is correct because the proxy ensures secure communications to Cloud SQL.
- C is not correct because it requires developing the application to call the MySQL client.
- D is not correct because connections are secure but they require public access to the Cloud SQL instance when Cloud SQL is located near the existing application.
```
- https://cloud.google.com/sql/docs/mysql/external-connection-methods

## 11

> For this question, refer to the HipLocal case study: [goo.gl/NpR3y2](https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf)

Which architecture should HipLocal use for log analysis?
- [ ] A. Use Cloud Spanner to store each event.
- [ ] B. Start storing key metrics in Memorystore.
- [x] C. Use Cloud Logging with a BigQuery sink.
- [ ] D. Use Cloud Logging with a Cloud Storage sink.

**Feedback**
```diff
- A Is not correct because Cloud Spanner is not an analytics database.
- B is not correct because this is not a log analysis solution.
+ C is correct because it utilizes GCP’s scalable logging solution with an automated sink to BigQuery in order to provide analytics.
- D Is not correct because it does not allow easy analytics (post processing is required).
```
- https://cloud.google.com/logging/docs/export/configure_export_v2

## 12
You are analyzing your application’s performance. You observe that certain Cloud Bigtable tables in your cluster are used much more than others, causing inconsistent application performance for end users. You discover that some tablets have large sections of similarly named row keys and are heavily utilized, while other tablets are running idle. You discover that a user’s ZIP code is the first component of the row key, and your application is being heavily used by profiles originating from that ZIP code. You want to change how you generate row keys so that they are human readable and so that Cloud Bigtable demand is more evenly distributed within the cluster. What should you do?
- [ ] A. Use serially generated integer values.
- [x] B. Use a subset of the MD5 hash of the row contents.
- [ ] C. Use a concatenation of multiple human-readable attributes.
- [ ] D. Use UNIX epoch-styled timestamps represented in milliseconds.

**Feedback**
```diff
- A is not correct because, depending on the distribution of the underlying values, serially generated integer values may lead to hotspotting.
- B is not correct because this is no longer a recommended best practice: it makes it difficult to troubleshoot issues.
+ C is correct because using a sufficient number of delimited attributes can provide sufficient spreading.
- D Is not correct because timestamps are poor candidates for row keys, and in this case inadvertently lead to ID collisions if multiple updates happening in the same millisecond execute in close succession.
```

- https://cloud.google.com/bigtable/docs/schema-design#types_of_row_keys
- https://cloud.google.com/bigtable/docs/schema-design-time-series#ensure_that_your_row_key_avoids_hotspotting


## 13
Your company has a successful multi-player game that has become popular in the US. Now, it wants to expand to other regions. It is launching a new feature that allows users to trade points. This feature will work for users across the globe. Your company’s current MySQL backend is reaching the limit of the Compute Engine instance that hosts the game. Your company wants to migrate to a different database that will provide global consistency and high availability across the regions. Which database should they choose?
- [ ] A. BigQuery
- [ ] B. Cloud SQL
- [x] C. Cloud Spanner
- [ ] D. Cloud Bigtable

**Feedback**
```diff
- A is not correct because BigQuery can’t be used as a transactional database.
- B is not correct because Cloud SQL doesn’t provide high availability across regions.
+ C is correct because only Cloud Spanner provides global consistency and availability.
- D is not correct because Cloud Bigtable doesn’t provide global availability.
```

## 14
Your company plans to expand their analytics use cases. One of the new use cases requires your data analysts to analyze events using SQL on a near real–time basis. You expect rapid growth and want to use managed services as much as possible. What should you do?
- [x] A. Create a Pub/Sub topic and a subscription. Stream your events from the source into the Pub/Sub topic. Leverage Dataflow to ingest these events into BigQuery.
- [ ] B. Create a Pub/Sub topic and a subscription. Stream your events from the source into the Pub/Sub topic. Leverage Dataflow to ingest these events into Cloud Storage.
- [ ] C. Create a Pub/Sub topic and a subscription. Stream your events from the source into the Pub/Sub topic. Leverage Dataflow to ingest these events into Firestore in Datastore mode.
- [ ] D. Create a Kafka instance on a large Compute Engine instance. Stream your events from the source into a Kafka pipeline. Leverage Dataflow to ingest these events into Cloud Storage.

**Feedback**
```diff
+ A is correct because all three products involved can scale to significant volumes, and writing the data to BigQuery allows for immediate analysis via SQL.
- B is not correct because Cloud Storage is not ideal for inserting individual events and analyzing them via SQL.
- C Is not correct because Firestore in Datastore mode is not ideal for inserting individual events and analyzing them.
- D is not correct because this solution doesn’t provide a fully managed solution.
```

## 15
Your organization develops and tests multiple applications on Compute Engine virtual machine instances across 3 environments; Test, Staging, and Production. The separate development teams for each application require minimal access to Production but broad access in Test and Staging. You need to design the Resource Manager structure to support your organization in following least-privilege best practices. What should you do?
- [ ] A. Create one project per environment per application. Assign the application team members an IAM role at the project level.
- [ ] B. Create one project per environment. Assign the application team members an Identity Access Management (IAM) role at the project level.
- [ ] C. Create one project per environment. Group each application team member into a Google Group. Assign the application team’s Google Group an IAM role at the project level.
- [x] D. Create one project per environment per application. Group each application team member into a Google Group. Assign the application team’s Google Group an IAM role at the project level.

**Feedback**
```diff
- A is not correct because adding individual users as members in an IAM policy can become difficult to manage over time.
- B is not correct because each team requires permissions to just their application.
- C is not correct because each team requires permissions to just their application.
+ D is correct because a project provides good isolation for each application team, and managing membership via a group is easier to maintain over time.
```
- https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations

## 16
Your application that is deployed in the App Engine standard environment receives a large amount of traffic. You are concerned that deploying changes to the application could affect all users negatively. You want to avoid full-scale load testing due to cost concerns, but you still want to deploy new features as quickly as possible. Which approach should you take?
- [ ] A. Schedule weekly load tests against the production application.
- [ ] B. Use the local development environment to perform load testing outside Google Cloud.
- [ ] C. Before allowing users to access new features, deploy as a new version and perform smoke tests. Then enable all users to access the new features.
- [x] D. Use App Engine traffic splitting to have a smaller part of the users test out new features, and slowly adjust traffic splitting until all users get the new features.

**Feedback**
```diff
- A is incorrect because there are patterns to perform A/B testing and reduce the need for regular independent load tests.
- B is incorrect because it does not accurately simulate the production environment.
- C is incorrect because smoke tests are still exposing all users to new features immediately as described.
+ D is correct because traffic splitting allows real user testing without impacting all users and reduces load testing costs.
```
- https://cloud.google.com/appengine

## 17
You have two tables in Cloud SQL with identical columns that you need to quickly combine into a single table, removing duplicate rows from the result set. What should you do?
- [ ] A. Use the JOIN operator in SQL to combine the tables.
- [ ] B. Use nested WITH statements to combine the tables.
- [x] C. Use the UNION operator in SQL to combine the tables.
- [ ] D. Query the tables from a Linux shell, combine the results into a single CSV, and re-import the rows into the database. Use the UNION ALL operator in SQL to combine the tables.

**Feedback**
```diff
- A is not correct because there is no indication of a column to potentially join on.
- B is not correct because WITH statements simply define query results as an intra-statement table.
+ C is correct because the UNION operator combines result sets while removing duplicates.
- D is not correct because UNION ALL does not remove duplicates.
```

- https://www.techonthenet.com/sql/union.php
- https://cloud.google.com/sql

## 18
Your website is deployed on Compute Engine. Your marketing team wants to test conversion rates between 3 different website designs. You are not able to make changes to your application code. What should you do?
- [x] A. Deploy website on App Engine and use traffic splitting.
- [ ] B. Deploy website on App Engine as three separate services.
- [ ] C. Deploy website on Cloud Functions as three separate functions.
- [ ] D. Deploy website on Cloud Functions and implement custom code to show different designs.

**Feedback**
```diff
+ A is correct because it allows routing traffic to a single domain and split traffic based on IP or Cookie.
- B is not correct because the domain name will change based on the service.
- C and D are not correct because Cloud Functions cannot be used to deploy websites.
```
- https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration


## 19
You are building a storage layer for an analytics Hadoop cluster in a region for your company. This cluster will run multiple jobs on a nightly basis, and you need to access the data frequently. You want to use Cloud Storage for this purpose. What is the most cost effective option?
- [ ] A. Regional Coldline storage
- [ ] B. Regional Nearline storage
- [x] C. Regional Standard storage
- [ ] D. Multi-regional Standard storage

**Feedback**
```diff
- A is not correct because Coldline storage is used if you need to access data only once a year.A is not correct because Multi-regional storage can place data in a region away from a Hadoop cluster. This would add latency to the requests made by the cluster.
- B is not correct because Nearline storage is used if you need to access data only once a month.
+ C is correct because it’s the most cost effective based on requirements
- D is not correct because Multi-regional storage can place data in a region away from a Hadoop cluster. This would add latency to the requests made by the cluster.
```

- https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fcloud.google.com%2Fstorage%2Fdocs%2Fstorage-classes%23available_storage_classes
- https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fcloud.google.com%2Fstorage%2Fdocs%2Fstorage-classes%23standard-availability


## 20
You have an application that accepts inputs from users. The application needs to kick off different background tasks based on these inputs. You want to allow for automated asynchronous execution of these tasks as soon as input is submitted by the user. Which product should you use?
- [ ] A. Pub/Sub
- [x] B. Cloud Tasks
- [ ] C. Cloud Bigtable
- [ ] D. Cloud Composer

**Feedback**
```diff
- A is not correct because Pub/Sub is only a messaging system.
+ B is correct because this is the standard use case.
- C is not correct because Cloud Bigtable is only a database.
- D is not correct because Cloud Composer is not a good fit to receive input from users.
```

## 21
You have a data warehouse built on BigQuery that contains a table with array fields. To analyze the data for a specific use case using Standard SQL, you need to read all elements from the array and write them with all other non-array fields in a table. You don’t want to lose any records if they don’t match records in the array fields. What should you do?
- [ ] A. Perform SELECT * FROM tablename.
- [x] B. Perform UNNEST and JOIN with the table to get these results.
- [ ] C. Perform UNNEST and INNER JOIN with the table to get these results.
- [ ] D. Perform UNNEST and CROSS JOIN with the table to get these results.

**Feedback**
```diff
- A is not correct because it does not join the records.
- B is not correct because it might lose records.
- C is not correct because it might lose records.
+ D is correct because it does not lose records when the join is performed.
```
- https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#join-types

## 22
You have deployed your website in a managed instance group. The managed instance group is configured to have a size of three instances and to perform an HTTP health check on port 80. When the managed instance group is created, three instances are created and started. When you connect to the instance using SSH, you confirm that the website is running and available on port 80. However, the managed instance group is re-creating the instances when they fail verification. What should you do?
- [ ] A. Change the type to an unmanaged instance group.
- [ ] B. Disable autoscaling on the managed instance group.
- [x] C. Increase the initial delay timeout to ensure that the instance is created.
- [ ] D. Check the firewall rules and ensure that the probes can access the instance.

**Feedback**
```diff
- A is not correct because the instance group type is not listed as being a problem.
- B is not correct because the scenario does not mention autoscaling as being configured.
- C Is not correct because using SSH to connect to the instance confirms that the website is running.
+ D. is correct because the instance has been created and the website is being served, but the health check is failing verification.
```
- https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups

## 23
Your team is using App Engine to write every Pub/Sub message to both a Cloud Storage object and a BigQuery table. You want to minimize operational overhead. Which architecture should you implement?

![image](https://user-images.githubusercontent.com/1645304/163509280-e87cbe93-3800-4ad7-9f62-d2377f73c197.png)

- [ ] A.
- [ ] B.
- [x] C.
- [ ] D.

**Feedback**
```diff
- A is not correct because this will write half the messages to BigQuery and half to Cloud Storage, which doesn't meet the need.
+ B is correct because each App Engine service will get its own message to write and can retry/fail independently.
- C is not correct because a failure in processing the message to one system can cause duplicate writes to BigQuery or Google Cloud Storage.
- D is not correct because it duplicates the message send charges and requires that the message be sent twice to two different topics, which increases costs, the need to manage an additional topic and complexities on the client.
```

## 24
As your organization has grown, new teams need access to manage network connectivity within and across projects. You are now seeing intermittent timeout errors in your application. You want to find the cause of the problem. What should you do?
- [x] A. Configure VPC flow logs for each of the subnets in your VPC.
- [ ] B. Configure firewall rules logging for each of the firewalls in your VPC.
- [ ] C. Set up wireshark on each Google Cloud Virtual Machine instance.
- [ ] D. Review the instance admin activity logs in Cloud Logging for the application instances.

**Feedback**
```diff
+ A is correct because it uses the substrate specific logging to capture everything.
- B is not correct because the timeouts are intermittent, not permanent, so firewall rules are not the cause.
- C is not correct because it is impossible to manage at scale, particularly with autoscaling.
- D is not correct because logs have little to do with networking.
```

## 25
Your application starts on the virtual machine (VM) as a systemd service. Your application outputs its log information to stdout. You want to review the application logs. What should you do?
- [ ] A. Review the application logs from the Compute Engine VM instance activity logs in Cloud Logging.
- [ ] B. Review the application logs from the Compute Engine VM instance data access logs in Cloud Logging.
- [x] C. Install Cloud Logging Agent. Review the application logs from the Compute Engine VM instance syslog logs in Cloud Logging.
- [ ] D. Install Cloud Logging Agent. Review the application logs from the Compute Engine VM instance system event logs in Cloud Logging.

**Feedback**
```diff
- A is not correct because the admin activity logs show destroy, create, modify, etc. events for a VM instance. (https://cloud.google.com/logging/docs/audit/#admin-activity)
- B is not correct because the data access logs show read activities. (https://cloud.google.com/logging/docs/audit/#data-access)
+ C is correct: a service running in systemd that outputs to stdout will have logs in syslog and will be scraped by the logging agent. (https://cloud.google.com/logging/docs/agent/installation)(https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/tree/master/configs/config.d)
- D is not correct because system event logs tell you about live migration, etc. (https://cloud.google.com/logging/docs/agent/installation)(https://cloud.google.com/logging/docs/audit/#system-event)
```

## 26
You are capturing important audit activity in Cloud Logging. You need to read the information from Cloud Logging to perform real-time analysis of the logs. You will have multiple processes performing different types of analysis on the logging data. What should you do?
- [ ] A. Read the logs directly from the Cloud Logging API.
- [ ] B. Set up a Cloud Logging sync to Pub/Sub, and read the logs from a Pub/Sub topic.
- [x] C. Set up a Cloud Logging sync to BigQuery, and read the logs from the BigQuery table.
- [ ] D. Set up a Cloud Logging sync to Cloud Storage, and read the logs from a Cloud Storage bucket.

**Feedback**
```diff
- A is not correct because the API has read limits and is not a suitable solution if you have multiple readers. (https://cloud.google.com/logging/quotas)
+ B is correct because this solution is real time. (https://cloud.google.com/logging/docs/export/using_exported_logs#pubsub-availability)
- C is not correct because this solution is not real time. (https://cloud.google.com/logging/docs/export/using_exported_logs#bigquery-availability)
- D is not correct because this solution is not real time. (https://cloud.google.com/logging/docs/export/using_exported_logs#gcs-availability)
```

## 27
You want to upload files from an on-premises virtual machine to Cloud Storage as part of a data migration. These files will be consumed by a Dataproc Hadoop cluster in a Google Cloud environment. Which command should you use?
- [x] A. `gsutil cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/`
- [ ] B. `gcloud cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/`
- [ ] C. `hadoop fs cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/`
- [ ] D. `gcloud dataproc cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/`

**Feedback**
```diff
+ A is correct because the correct CLI tool is being used to interact with Cloud Storage
- B is not correct. The gsutil command is used to interact with Cloud Storage.
- C is not correct. The gsutil command is used to interact with Cloud Storage.
- D is not correct. The gsutil command is used to interact with Cloud Storage.
```

## 28
You are writing an API endpoint to process orders from a web application and save the data into a Datastore collection. During application testing, you notice that when your application encounters an HTTP 5xx server error from the Datastore API, it catches this error and returns an HTTP 200 OK response code to the client, but does not store the data within Datastore. You want the consumers of your API endpoint to know that the write request was unsuccessful. What should you do?
- [ ] A. Return an HTTP 204 No Content response.
- [ ] B. Return an HTTP 406 Not Acceptable response.
- [x] C. Return an HTTP 500 Internal Server Error response.
- [ ] D. Retry the Datastore API with exponential backoff until Datastore returns a HTTP 2xx response.

**Feedback**
```diff
- A is not correct because 2xx codes indicate a success from the server.
- B is not correct because 406 is sent specifically when a request’s accept header is unfulfillable by the server.
+ C is correct because a 500-class response clearly communicates to clients that the API call was unsuccessful, and the client can re-submit independently.
- D is not correct because it is unbounded as to when the Datastore API might respond with a non-500 class response.
```
- https://www.restapitutorial.com/httpstatuscodes.html

# Professional Cloud Developer Sample Questions

## 1
Your team has developed a mobile web application where global users vote on popular topics. For each topic, you expect a very high volume of votes during each individual 30-minute voting window. You need to capture and count all votes within 24 hours and then store the votes for future analysis and reporting. What should you do?

- [ ] A. Save the votes to Memorystore, and use Cloud Functions to insert the data into BigQuery. Display the results in Google Data Studio.
- [x] B. Publish the votes to Pub/Sub, and use a Datafow pipeline to insert the data into BigQuery. Display the results in Google Data Studio.
- [ ] C. Publish the votes to Pub/Sub, and use Cloud Functions to insert the data into Cloud Storage. Display the results in Google Data Studio.
- [ ] D. Use Firebase to authenticate the mobile users, and publish the data directly to the database. Export the data to a CSV file, and import it into Sheets for reporting.

## 2
![image](https://user-images.githubusercontent.com/1645304/163494343-f3617bc3-df9c-4b23-9832-530bdf2b84ee.png)
- [ ] A. Migrate the database to Cloud SQL. Then import the session data into Cloud Bigtable.
- [ ] B. Migrate the database to BigQuery. Then import the session data into Firestore in Native mode.
- [x] C. Migrate the database to Cloud SQL. Then import the session data into Firestore in Native mode.
- [ ] D. Create a Compute Engine virtual machine instance in Google Cloud, and install PostgreSQL and MongoDB Server software. Migrate the database to the new PostgreSQL, and then migrate the session data to MongoDB.

## 3
Your development team uses GitHub to manage their code. You need to perform debugging tasks to resolve an error that was recently reported by the QA team. What should you do?
- [ ] A. Ask a reviewer to analyze the code in the GitHub pull request.
- [x] B. Set up Cloud Debugger, create a snapshot, and set log points.
- [ ] C. Pull your code from GitHub, and troubleshoot with Cloud Trace.
- [ ] D. Set up Cloud Profiler, pull your code from GitHub, and create snapshots.

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
- [ ] B. Deploy and configure the Cloud SQL proxy. Connect the application to the proxy.
- [ ] C. Run MySQL client along with the application. Configure the application to call the MySQL client to connect to the database.
- [ ] D. Configure a public IP address on Cloud SQL, and configure Cloud SQL to require SSL for connections. Connect the application to the public IP address.


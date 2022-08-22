# Sample Questions.md

## 1
You are helping with the design of an e-commerce application. The web application receives web requests and  stores sales transactions in a database. A batch job runs every hour to trigger analysis of sales numbers, available inventory, and forecasted sales numbers. You want to identify minimal Service Level Indicators (SLIs) for the application to ensure that forecasted numbers are based on the latest sales numbers. Which SLIs should you set for the application?

- [ ] A.
  - Web Application - Quality 
  - Database - Availability
  - Batch Job - Coverage
- [ ] B.
  - Web Application - Latency
  - Database - Latency
  - Batch Job - Throughput
- [x] C.
  - Web Application - Availability
  - Database - Availability
  - Batch Job - Frenshness
- [ ] D.
  - Web Application - Availability, Quality
  - Database - Durability
  - Batch Job - Coverage

**Feedback**
```diff
- A is not correct because Web Application Quality and Batch Job Coverage SLIs don’t help in meeting the objective.
- B is not correct because the latency of the web application, although important to measure, doesn’t help with meeting the objective of the latest data available in the database.
+ C is the correct answer because these are the minimal set of SLIs to measure in order to meet the objective of using the latest data in a batch job.
- D is not correct because Web Application Quality and Batch Job Coverage SLIs don’t help in meeting the objective.
```
https://landing.google.com/sre/workbook/toc/


## 2
Your Site Reliability Engineering team does toil work to archive unused data in tables within your application’s relational database. This toil is required to ensure that your application has a low Latency Service Level Indicator (SLI) to meet your Service Level Objective (SLO). Toil is preventing your team from focusing on a high-priority engineering project that will improve the Availability SLI of your application. You want to: (1) reduce repetitive tasks to avoid burnout, (2) improve organizational efficiency, and (3) follow the Site Reliability Engineering recommended practices. What should you do?

- [ ] A. Identify repetitive tasks that contribute to toil and onboard additional team members for support.
- [x] B. Identify repetitive tasks that contribute to toil and automate them.
- [ ] C. Change the SLO of your Latency SLI to accommodate toil being done less often. Use this capacity to work on the Availability SLI engineering project.
- [ ] D. Assign the Availability SLI engineering project to the Software Engineering team.

**Feedback**
```diff
- A is incorrect because toil does not diminish on its own. It needs to be eliminated with action.
+ B is correct because the organizational culture should allow for openly expressing concerns in the benefit of service reliability.
- C is incorrect because changing the SLO will not eliminate toil.
- D is incorrect because the SRE team will still be overwhelmed with toil that will also block future projects.
```
https://sre.google/sre-book/eliminating-toil/

## 3

Your application runs in Google Kubernetes Engine (GKE). You want to use Spinnaker with the Kubernetes Provider to perform blue/green deployments and control which version of the application receives traffic. What should you do?
- [ ] A. Use a Kubernetes Replica Set and use Spinnaker to create a new service for each new version of the application to be deployed.
- [ ] B. Use a Kubernetes Replica Set and use Spinnaker to update the Replica Set for each new version of the application to be deployed.
- [x] C. Use a Kubernetes Deployment and use Spinnaker to update the deployment for each new version of the application to be deployed.
- [ ] D. Use a Kubernetes Deployment and use Spinnaker to create a new deployment object for each new version of the application to be deployed.

**Feedback**
```diff
- A is incorrect because Spinnaker needs to update and not create a new service for deployment.
+ B is correct because Spinnaker can update the replica set in place without conflicting with Kubernetes.
- C is incorrect because this would conflict with Kubernetes operations on the deployment.
- D is incorrect because Spinnaker does not manage deployment objects in this way.
```
https://www.spinnaker.io/guides/user/kubernetes-v2/traffic-management/#route-traffic-during-a-deployment-bluegreen


## 4

You are deploying an application to a Kubernetes cluster that requires a username and password to connect to another service. When you deploy the application, you want to ensure that the credentials are used securely in multiple environments with minimal code changes. What should you do?
- [ ] A. Bundle the credentials with the code inside the container and secure the container registry.
- [x] B. Store the credentials as a Kubernetes Secret and let the application access it via environment variables at runtime.
- [ ] C. Leverage a CI/CD pipeline to update the variables at build time and inject them into a templated Kubernetes application manifest.
- [ ] D. Store the credentials as a Kubernetes ConfigMap and let the application access it via environment variables at runtime.

**Feedback**
```diff
- A is incorrect because it would produce an insecure artifact, which anyone could run without going through proper RBAC channels.
+ B is correct because it enables secrets usage without needing to modify the code per environment, update build pipelines, or store secrets insecurely.
- C is incorrect because it requires modification of deployment code per environment, which will produce an insecure intermediary artifact.
- D is incorrect because it will expose the parameters in an insecure fashion and would require changing deployment code for every environment.
```

https://kubernetes.io/docs/concepts/configuration/secret/

## 5
Several teams in your company want to use Cloud Build to deploy to their own Google Kubernetes Engine (GKE) clusters. The clusters are in projects that are dedicated to each team. The teams only have access to their own projects. One team should not have access to the cluster of another team. You are in charge of designing the Cloud Build setup, and want to follow Google-recommended practices. What should you do?

- [ ] A. Limit each team member’s access so that they only have access to their team’s clusters. Ask each team member to install the gcloud CLI and to authenticate themselves by running “gcloud init”. Ask each team member to execute Cloud Build builds by using “gcloud builds submit”.
- [ ] B. Create a single project for Cloud Build that all the teams will use. List the service accounts in this project and identify the one used by Cloud Build. Grant the Kubernetes Engine Developer IAM role to that service account in each team’s project.
- [x] C. In each team’s project, list the service accounts and identify the one used by Cloud Build for each project. In each project, grant the Kubernetes Engine Developer IAM role to the service account used by Cloud Build. Ask each team to execute Cloud Build builds in their own project.
- [ ] D. In each team’s project, create a service account, download a JSON key for that service account, and grant the Kubernetes Engine Developer IAM role to that service account in that project. Create a single project for Cloud Build that all the teams will use. In that project, encrypt all the service account keys by using Cloud KMS. Grant the Cloud KMS CryptoKey Decrypter IAM role to Cloud Build’s service account. Ask each team to include in their “cloudbuild.yaml” files a step that decrypts the key of their service account, and use that key to connect to their cluster.

**Feedback**
```diff
- A is not correct because, even if you authenticated yourself with the gcloud CLI, Cloud Build runs with its own service account, and not your identity.
- B is not correct because this grants access to all the clusters, for all the teams.
+ C is correct because this ensures that each team cannot execute builds that touch another team’s cluster.
- D is not correct because this grants access to all the clusters, for all the teams.
```
https://cloud.google.com/cloud-build/docs/securing-builds/configure-access-control

## 6

You have an application deployed on Google Kubernetes Engine (GKE). The application logs are captured by Cloud Logging. You need to remove sensitive data before it reaches the Cloud Logging API. What should you do?

- [ ] A. Write the log information to the container file system. Execute a second process inside the container that will filter the sensitive information before writing to Standard Output.
- [x] B. Customize the GKE clusters’ Fluentd configuration with a filter rule. Update the Fluentd Config Map and Daemon Set in the GKE cluster.
- [ ] C. Configure a filter in the Cloud Logging UI to exclude the logs with sensitive data.
- [ ] D. Configure BigQuery as a sink for the logs from Cloud Logging, and then create a Data Loss Prevention job.

**Feedback**
```diff
- A is incorrect because you cannot modify the behavior of the logging.
+ B is correct because you can configure the Fluentd logging behavior.
- C is incorrect because this does not prevent the data from arriving in Cloud Logging.
- D is incorrect because this does not prevent the data from arriving in Cloud Logging.
```
https://cloud.google.com/solutions/customizing-stackdriver-logs-fluentd

## 7
You have a Compute Engine instance that uses the default Debian image. The application hosted on this instance recently suffered a series of crashes that you weren’t able to debug in real time: the application process died suddenly every time. The application usually consumes 50% of the instance’s memory, and normally never more than 70%, but you suspect that a memory leak was responsible for the crashes. You want to validate this hypothesis. What should you do?

- [ ] A. Go to Metrics Explorer and look for the “compute.googleapis.com/guest/system/problem_count” metric for that instance. Examine its value for when the application crashed in the past.
- [ ] B. In Cloud Monitoring, create an uptime check for your application. Create an alert policy for that uptime check to be notified when your application crashes. When you receive an alert, use your usual debugging tools to investigate the behavior of the application in real time.
- [x] C. Install the Cloud Monitoring agent on the instance. Go to Metrics Explorer and look for the “agent.googleapis.com/memory/percent_used” metric for that instance. Examine its value for when the application crashed in the past.
- [ ] D. Install the Cloud Monitoring agent on the instance. Create an alert policy on the “agent.googleapis.com/memory/percent_used” metric for that instance to be alerted when the memory used is higher than 75%. When you receive an alert, use your usual debugging tools to investigate the behavior of the application in real time.

Correct answer
- [x] D. Install the Cloud Monitoring agent on the instance. Create an alert policy on the “agent.googleapis.com/memory/percent_used” metric for that instance to be alerted when the memory used is higher than 75%. When you receive an alert, use your usual debugging tools to investigate the behavior of the application in real time.

**Feedback**
```diff
- A is not correct because this metric doesn’t help you debug the issue.
- B is not correct because it doesn’t allow you to investigate the issue in real time.
- C is not correct because the agent won’t retroactively send monitoring data.
+ D is correct because it allows you to investigate the issue in real time.
```
- https://cloud.google.com/monitoring/uptime-checks/
- https://cloud.google.com/monitoring/api/metrics_agent
- https://cloud.google.com/monitoring/api/metrics_gcp


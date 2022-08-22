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

## 8
You are running a production application on Compute Engine. You want to monitor the key metrics of CPU, Memory, and Disk I/O time. You want to ensure that the metrics are visible by the team and will be explorable if an issue occurs. What should you do? (Choose 2)
- [ ] A. Set up logs-based metrics based on your application logs to identify errors.
- [ ] B. Export key metrics to a Google Cloud Function and then analyze them for outliers.
- [x] C. Set up alerts in Cloud Monitoring for key metrics breaching defined thresholds.
- [x] D. Create a Dashboard with key metrics and indicators that can be viewed by the team.
- [ ] E. Export key metrics to BigQuery and then run hourly queries on the metrics to identify outliers.

**Feedback**
```diff
- A is incorrect because this will not identify all issues; instead, it will identify a specific issue.
- B is incorrect because this will introduce significant overhead.
+ C is correct because alerts allow reaction to issues that have not been previously identified.
+ D is correct because dashboards are a powerful tool to identify issues early.
- E is incorrect because this will introduce significant delay.
```

- https://cloud.google.com/blog/products/management-tools/stackdriver-tips-and-tricks-understanding-metrics-and-building-charts
- https://cloud.google.com/monitoring/charts/dashboards
- https://cloud.google.com/monitoring/alerts/

## 9
You support a Python application running in production on Compute Engine. You want to debug some of the application code by inspecting the value of a specific variable. What should you do?
- [ ] A. Create a Cloud Debugger logpoint with the variable at a specific line location in your application's source code, and view the value in the Logs Viewer.
- [ ] B. Use your local development environment and code editor to set up a breakpoint in the source code, run the application locally, and then inspect the value of the variable.
- [ ] C. Modify the source code of the application to log the value of the variable, deploy to the development environment, and then run the application to capture the value in Cloud Logging.
- [x] D. Create a Cloud Debugger snapshot at a specific line location in your application's source code, and view the value of the variable in the Google Cloud Console.

**Feedback**
```diff
- A is not correct because, although it is a good option, it requires the additional step of viewing the logs in Logs Viewer.
- B is not correct because the state of the local application might be very different from the state of the production application.
- C is not correct because it is the option with the most effort and is prone to errors.
+ D is correct. This is the recommended approach.
```

- https://cloud.google.com/debugger/docs/using/snapshots
- https://cloud.google.com/debugger/docs/using/logpoints


## 10
You work with a video rendering application that publishes small tasks as messages to a Cloud Pub/Sub topic. You need to deploy the application that will execute these tasks on multiple virtual machines (VMs). Each task takes less than 1 hour to complete. The rendering is expected to be completed within a month. You need to minimize rendering costs. What should you do?
- [ ] A. Deploy the application as a managed instance group.
- [ ] B. Deploy the application as a managed instance group. Configure a Committed Use Discount for the amount of CPU and memory required.
- [x] C. Deploy the application as a managed instance group with Preemptible VMs. 
- [ ] D. Deploy the application as a managed instance group with Preemptible VMs. Configure a Committed Use Discount for the amount of CPU and memory required.

**Feedback**
```diff
- A is incorrect. This is not the cheapest method.
- B is incorrect because CUDs are for a 1-year minimum, so you would be overbilled for 11 months.
+ C is correct because Preemptible VMs are the cheapest way of running a VM. Running them in a MIG will start new instances when some are terminated.
- D is incorrect because CUDs are for a 1-year minimum, so you would be overbilled for 11 months.
```

- https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#creating_groups_of_preemptible_instances
- https://cloud.google.com/compute/sole-tenant-gpu-pricing#nodes

## 11

You support a website with a global audience. The website has a frontend web service and a backend database service that runs on different clusters. All clusters are scaled to handle at least ⅓ of the total user traffic. You use 4 different regions in Google Cloud and Cloud Load Balancing to direct traffic to a region closer to the user. You are applying a critical security patch to the backend database. You successfully patch the database in the first 2 regions, but you make a configuration error while patching Region 3. The unsuccessful patching causes 50% of user requests to Region 3 to time out. You want to mitigate the impact of unsuccessful patching on users. What should you do?  
- [ ] A. Add more capacity to the frontend of Region 3.
- [ ] B. Revert the Region 3 backend database and run it without the patch.
- [x] C. Drain the requests to Region 3 and redirect new requests to other regions.
- [ ] D. Back up the database in the backend of Region 3 and restart the database.

**Feedback**
```diff
- A is incorrect because adding more Frontend servers will not fix the backend configuration problem.
- B is incorrect because running a backend without the critical security patch is a big risk.
+ C is correct because the remaining 3 regions can handle the total traffic load, which gives you time to fix the configuration error in Region 3 and then apply the patch.
- D is incorrect because backing up the database will not help at this point, and the additional load on the server could make the problem worse.
```

- https://cloud.google.com/load-balancing/docs/enabling-connection-draining
- https://cloud.google.com/compute/docs/tutorials/robustsystems#distribute
- https://landing.google.com/sre/sre-book/chapters/addressing-cascading-failures/

## 12

You have a service running on Compute Engine virtual machine instances behind a global load balancer. You need to ensure that when an instance fails, it is recovered. What should you do?
- [ ] A. Set up health checks in the load balancer configuration.
- [ ] B. Deploy a service to the instances to notify you when they fail.
- [ ] C. Use Cloud Logging alerts to trigger a workflow to reboot the instance.
- [x] D. Set up health checks in the managed instance group configuration.

**Feedback**
```diff
- A is not correct because the load balancer health check will not recover the instance. The load balancer health check will exclude the instance from receiving traffic.
- B is not correct because a service on the instance may not work when the instance fails.
- C is not correct because this is not the platform-idiomatic way of recovering failed instances.
+ D is correct because the managed instance group health check will recreate the instance when it fails, and this is the platform-native way to satisfy this use case.
```

- https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups)


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

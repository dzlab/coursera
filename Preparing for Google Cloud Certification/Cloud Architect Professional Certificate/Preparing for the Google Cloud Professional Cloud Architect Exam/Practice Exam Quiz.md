# Practice Exam Quiz

**1. Question 1**

Which service should be used in the icon with the question mark in the diagram to keep VM file data in sync across regions?

![image](https://user-images.githubusercontent.com/1645304/140662330-eca3c8f1-70fd-417a-b0c1-5a19b1b346e6.png)


- [ ] Cloud SQL
- [ ] Cloud Bigtable
- [x] Transfer Appliance
- [ ] Cloud Storage


**2. Question 2**

An existing application uses websockets. To help migrate the application to cloud you should:

- [ ] Redesign the application to use HTTP streaming.
- [ ] Redesign the application to use distributed sessions instead of websockets.
- [ ] Do nothing to the application. HTTP(S) load balancing natively supports websocket proxying.
- [x] Review websocket encryption requirements with the security team.


**3. Question 3**

A company is building an image tagging pipeline. Which service should be used in the icon with the question mark in the diagram?

![image](https://user-images.githubusercontent.com/1645304/140662406-0f4f9cfa-4357-4e94-9205-aaf0e0b38dd9.png)

- [ ] Datastore
- [ ] Dataflow
- [x] Pub/Sub
- [ ] Cloud Bigtable


**4. Question 4**

How to store data to be accessed once a month and not needed after five years. 

- [ ] Standard Storage class, lifecycle policy to delete after 5 years.
- [ ] Standard Storage class, lifecycle policy change to Coldline after 5 years.
- [ ] Nearline class, lifecycle policy change to Coldline after 5 years.
- [x] Nearline class, lifecycle policy to delete after 5 years.


**5. Question 5**

A company has a new IoT pipeline. Which services will make this design work?

Select the services that should be used to replace the icons with the number "1" and number "2" in the diagram.

![image](https://user-images.githubusercontent.com/1645304/140662548-60e56777-b75e-46cd-b7af-cdfd5a1ced04.png)


- [ ] Cloud IoT Core, Datastore
- [ ] Pub/Sub, Cloud Storage
- [x] Cloud IoT Core,Pub/Sub
- [ ] App Engine, Cloud IoT Core


**6. Question 6**

Multi-petabyte database for analysts that only know SQL and must be available 24 x 7.

- [ ] Cloud Storage
- [ ] Cloud SQL
- [x] BigQuery
- [ ] Datastore


**7. Question 7**

Which service completes the CI/CD pipeline?

Which service should be used in the icon with the question mark in the diagram?

![image](https://user-images.githubusercontent.com/1645304/140662592-68a01554-6b86-4f30-8339-f2029bcd7c1d.png)

- [ ] Pub/Sub
- [x] Cloud Build
- [ ] Cloud Storage
- [ ] Dataproc


**8. Question 8**

Simply and reliably clone a Linux VM to another project in another region.

- [ ] Use Linux dd and netcat to stream the root disk to the new VM.
- [x] Snapshot the root disk and select it for the new VM.
- [ ] Create an image from the root disk with Linux dd, create a disk from the image, and use it in the new VM.
- [ ] Snapshot the root disk, create an image, and use the image for the new VM root disk.


**9. Question 9**

A company has this business requirement: "Improve security by defining and adhering to a set of security and Identity and Access Management (IAM) best practices for cloud."

Company security has locked out SSH access to production VMs. How can operations manage the VMs?

- [x] Configure a VPN to allow SSH access to VMs.
- [ ] Develop a Cloud API application for all operations actions.
- [ ] Grant operations team access to use Cloud Shell.
- [ ] Develop an application that grants temporary SSH access.


**10. Question 10**

What security strategy would you recommend for PII (Personally Identifiable Information) data on Cloud Storage?

- [ ] Signed URL with expiration.
- [ ] Read-only access to users, and default ACL on bucket.
- [x] No Cloud IAM roles to users, and granular ACLs on bucket.
- [ ] Public access, random names, and share URLs in confidence.


**11. Question 11**

A company has decided to use Cloud SDK tools to deploy to App Engine flexible environment. Which one of the following requirements does this meet?

- [ ] Requirement 1: Support failover of the production environment to the cloud during an emergency.
- [ ] Requirement 2: Encrypt data on the wire and at rest.
- [x] Requirement 3: Use managed services whenever possible.
- [ ] Requirement 4: Identify production services that can migrate to the cloud to save capacity.


**12. Question 12**

Which of the following business requirements can Cloud DNS help satisfy?


- [ ] Support multiple VPN connections between the production data center and cloud environment.
- [ ] Analyze and optimize architecture for performance in the cloud.
- [ ] Build a reliable and reproducible environment with scaled parity of production.
- [x] Support failover of the production environment to cloud during an emergency.


**13. Question 13**

A company has business requirements to keep up with industry transformation and growth by adopting leading technology and to use "incremental innovation" based on business insights. Which one of the following Google Cloud features will support this requirement?


- [ ] Google has many years of experience with containers.
- [ ] Compute Engine provides automatic discounts with increased usage.
- [x] Cloud Machine Learning and BigQuery are designed for petabyte scale.
- [ ] Compute Engine bills per minute, saving costs compared to hourly billing.


**14. Question 14**

A game company wants to meet its scaling requirements and also provide insights to investors. Which solution will best meet these needs?


- [ ] Import delayed MySQL game statistics to BigQuery for provisioning analysis and indicator reporting.
- [ ] Use Cloud Monitoring custom metrics for autoscaling and reporting.
- [x] Autoscale based on CPU load and use Data Studio to share metrics.
- [ ] Autoscale based on network latency as a measure of user experience.


**15. Question 15**

A company wants to test a risky update to an App Engine application requiring live traffic. Which of the following options is the best approach?

- [ ] Deploy as default temporarily, then roll it back.
- [ ] Create a separate isolated test project and onboard users.
- [ ] Create a second App Engine project, then redirect a subset of users.
- [x] Deploy a new version, use traffic splitting to test a percentage.


**16. Question 16**

How to automatically and simultaneously deploy new code to each cluster?

![image](https://user-images.githubusercontent.com/1645304/140663073-bce26f06-60a1-4ba7-9642-abaca714ec78.png)


- [ ] Use an automation tool, such as Jenkins.
- [x] Change the clusters to activate federated mode.
- [ ] Use Parallel SSH with Google Cloud Shell and kubectl.
- [ ] Use Container Builder to publish the new images.


**17. Question 17**

A microservice has intermittent problems that bursts logs. How can you trap it for live debugging?

- [ ] Log into the machine with the microservice and wait for the log messages.
- [ ] Look for error in Error Reporting dashboard.
- [ ] Configure microservice to send traces to Cloud Trace.
- [x] Set a log metric in Cloud Logging, alert on it past a threshold.


**18. Question 18**

A company wants penetration security testing that primarily matches an end user perspective.


- [ ] Notify Google you are going to run a penetration test.
- [ ] Deploy scanners in the cloud and test from there.
- [ ] Use on prem scanners over VPN.
- [x] Use on prem scanners over public Internet.


**19. Question 19**

A sales company runs weekly resiliency tests of the current build in a separate environment by replaying the last holiday sales load. What can improve resiliency?

- [ ] Apply twice the load to the test.
- [x] Run the resiliency tests daily instead of weekly.
- [ ] Use preemptible instances.
- [ ] Develop a script that mimics a zone outage and add it to the test.


**20. Question 20**

Release failures keep causing rollbacks in a web application. Fixes to QA process reduced rollbacks by 80%. What additional steps can you take?

- [ ] Replace the platform’s relational database systems with a NoSQL database.
- [x] Fragment the monolithic platform into microservices.
- [ ] Remove the QA environment. Start executing canary releases.
- [ ] Remove the platform’s dependency on relational database systems.


**21. Question 21**

A car reservation system has long-running transactions. Which one of the following deployment methods should be avoided?

- [ ] Execute canary releases.
- [ ] Perform A/B testing prior to release.
- [x] Introduce a blue-green deployment model.
- [ ] Introduce a pipeline deployment model.


**22. Question 22**

Last week a region had a 1% failure rate in web tier VMs? How should you respond?

- [ ] Monitor the application for a 5% failure rate.
- [ ] Duplicate the application on prem to compensate for failures in the cloud.
- [x] Perform a root cause analysis, reviewing cloud provider and deployment details to prevent similar future failures.
- [ ] Halt all development until the application issue can be found and fixed.


**23. Question 23**

Why is it a recommended best practice not to assign blame to an individual or an organization?


- [ ] It might humiliate them. It would be wrong.
- [x] Because you might be wrong and you might assign blame to the wrong party.
- [ ] Because it prematurely ends analysis, you don't discover the root cause in the technology or procedures.
- [ ] Because it can be really hard to find out who is at fault.


**24. Question 24**

A healthcare company wants to compliantly use Cloud Storage to store customer medical (HIPAA) data.


- [x] Cloud Storage is already HIPAA compliant by default.
- [ ] HIPAA compliance is not currently supported for Cloud Storage.
- [ ] Execute a Business Associate Agreement (BAA), but you must still use the service in a HIPAA compliant way.
- [ ] Execute a Business Associate Agreement (BAA).


**25. Question 25**

Which network feature could help a company meet its global service expansion goals by reducing latency?


- [ ] HTTP/TCP load balancing
- [ ] Network TCP/UDP
- [ ] Cloud Router
- [x] Cloud CDN



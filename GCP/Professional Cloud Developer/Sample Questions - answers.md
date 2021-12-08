# Answers

### 1
You are using Google Cloud Storage to store files for a two-year project. You plan to stream in files on an ongoing basis and access these files once a month for analysis. Which type of storage is most appropriate for your needs?

- [x] Nearline

**Explanation**

Nearline and Coldline offer ultra low-cost, highly-durable, highly available archival storage. Coldline is ideal for cold storage , or data that your business expects to touch less than once a year. For warmer storage, choose Nearline, or data you expect to access once a month or less, but possibly multiple times throughout the year.

https://cloud.google.com/storage/docs/storage-classes

### 2
You are managing a project using Google Container Registry, and have written a script to mark all current objects (including the image you just pushed) in your registry public. Which command should you use, assuming that your project ID is "your-project-id"?

- [x] gsutil acl ch -u AllUsers:R gs://artifacts.your-project-id.appspot.com

**Explanation**

You can control who has access to the images in your Container Registry by using access control commands on the Google Cloud Storage bucket that contains your project's container images.

Mark all current objects (including the image you just pushed) in your registry public by running the following command in your shell or terminal window:
```
gsutil acl ch -r -u AllUsers:R gs://artifacts.your-project-id.appspot.com
```
 

https://cloud.google.com/container-registry/docs/access-control

### 3
You are managing customer success for a mid-size online retailer, and need to quickly implement a solution to analyze large amounts of customer feedback, and reliably identify and separate negative and positive reviews. Which Google Machine Learning service can you implement within your solution?

- [x] AutoML Natural Language Sentiment Analysis

**Explanation**

AutoML Natural Language Sentiment Analysis allows you to analyze text and identify the attitude conveyed in the message, whether positive or negative, for example.

https://cloud.google.com/natural-language/automl/sentiment/docs/

### 4
You realize the reason you are unable to login via SSH to your newly configured GCE virtual machine is the default-allow-ssh firewall rule has been mysteriously deleted. You decide to add the rule back to your firewall. What settings should you select?

- [x] Allow ingress connections on TCP port 22 from any source to any instance in the network with a rule priority of 65534.

**Explanation**

A default network is pre-populated with firewall rules that allow incoming traffic to instances. These rules can be deleted or modified as necessary. The default-allow-ssh rule is one of the four rules. The others are:

- default-allow-internal, which permits incoming connections to VM instances from others in the same network.
- default-allow-rdp, which enables connections to instances running the Microsoft Remote Desktop Protocol (RDP).
- deault-allow-icmp, enables tools like ping.

https://cloud.google.com/vpc/docs/firewalls#default_firewall_rules

### 5
If you have configured Stackdriver Logging to export logs to BigQuery, but logs entries are not getting exported to BigQuery, what is the most likely cause?

- [x] Stackdriver Logging does not have permission to write to the BigQuery dataset.

**Explanation**

When you create a sink, Stackdriver Logging creates a new service account for the sink, called a unique writer identity.

In order to write logs to a BigQuery dataset, you must grant the sink's writer identity either Can edit permission or the Writer role.

It is not necessary to create a firewall rule to allow traffic between Stackdriver and BigQuery.

The Cloud Data Transfer Service is for importing data to Google Cloud Platform from an external source.

BigQuery can easily handle any volume of Stackdriver logs.

https://cloud.google.com/logging/docs/export/configure_export_v2#errors_exporting_to_bigquery

### 6
You are planning to use Google's Dataflow SDK to analyze customer data such as displayed below. Your project requirement is to extract only the customer name from the data source and then write to an output PCollection.Tom,555 X streetTim,553 Y streetSam, 111 Z streetWhich operation is best suited for the above data processing requirement?
- [x] ParDo

**Explanation**

In Google Cloud dataflow SDK, you can use the ParDo to extract only a customer name of each element in your PCollection.

https://cloud.google.com/dataflow/model/par-do

### 7

Suppose you have a table that includes a nested column called "city" inside a column called "person", but when you try to submit the following query in BigQuery, it gives you an error.SELECT person FROM `project1.example.table1` WHERE city = "London"How would you correct the error?

- [x] Add ", UNNEST(person)" before the WHERE clause.

**Explanation**

To access the person.city column, you need to "UNNEST(person)" and JOIN it to table1 using a comma.

https://cloud.google.com/bigquery/docs/reference/standard-sql/migrating-from-legacy-sql#nested_repeated_results

### 8

Your company would like to establish a direct, private connection between your on-premise network with Google networks, to connect with GCP resources without transmitting over the public internet. However, your on-premise network is too far from a Google colocation facility to establish a physical connection. You also expect your network topology to change in the next 18 months, so you will need to update all on-premise destination IP addresses. You would like this update to be entirely managed by your company's employees, even though you will need to connect through a service provider. Which GCP Hybrid Connectivity option will allow you to establish your desired network connection, and independently manage your upcoming network updates?

- [x] Partner Interconnect

**Explanation**

A Partner Interconnect connection is the best choice in this case. A Dedicated Interconnect connection will not be possible due to the distance between your on-premise office and the nearest Google colocation facility. Using either Direct Peering or Carrier Peering requires contacting Google in order to update the IP address ranges for your network, so these two options will not suffice. This leaves Partner Interconnect as the only remaining option.

https://cloud.google.com/interconnect/docs/concepts/partner-overview

### 9
To prevent Denial of Service (DoS) attacks in your PHP App Engine application, what type of file do you need to create to store blacklisted IP addresses?
- [x] dos.yaml

**Explanation**

Create a dos.yaml file in the root directory of your application. You will specify your blacklisted IP addresses and networks in this file. The dos.yaml is limited to 100 entries, so blocking entire subnets might be necessary if you are facing a DDoS attack. 

https://cloud.google.com/appengine/docs/php/config/dos

### 10
You can review Stackdriver logs via the Logging page in the Stackdriver monitoring console, or by setting up a BigQuery dataset containing Stackdriver logs. What are two advantages of creating the BigQuery dataset containing stackdriver logs? (Choose 2 answers)
- [x] The logs for the complex system often qualify as big data.
- [x] BigQuery is faster and capable of more complex queries .

**Explanation**

Creating BigQuery datasets can be advantageous because sometimes you may need to search through a huge number of log entries and need to do complicated queries. BigQuery is lightning fast when searching through big data, and if you build a complex infrastructure in Google Cloud Platform, then the volume of log data it will generate will easily qualify as big data.

[/course/managing-your-google-cloud-infrastructure/logging/](https://cloudacademy.com/course/managing-your-google-cloud-infrastructure/logging/)

### 11
You are an architect helping an enterprise customer deploy their application on Google Compute Engine. The customer's IT team already created two projects, for marketing and sales departments, within the US-Central1 region. The network topology, firewall rules, and routes are identical for the marketing and sales projects. The IT manager wants your help in designing a single network that will be shared by applications running within the sales and marketing projects. Which statement regarding your VPC network(s) that will contain the marketing and sales resources is correct, and can help your IT manager design the best solution?

- [x] Although VPCs are global resources, sales and marketing need to use a shared VPC to access the same resources in specific subnets.

**Explanation**

Shared VPC allows an organization to connect resources from multiple projects to a common Virtual Private Cloud (VPC) network, so that they can communicate with each other securely and efficiently using internal IPs from that network. When you use Shared VPC, you designate a project as a host project and attach one or more other service projects to it. The VPC networks in the host project are called Shared VPC networks. Eligible resources from service projects can use subnets in the Shared VPC network.

Shared VPC lets organization administrators delegate administrative responsibilities, such as creating and managing instances, to Service Project Admins while maintaining centralized control over network resources like subnets, routes, and firewalls. This model allows organizations to do the following:

https://developers.google.com/compute/docs/overview

### 12
You are planning to build ticket reservation software using Google Cloud's Dataflow SDK. Your project requirement is to extract the data and then perform parallel processing operations. Which tool supports the core parallel processing operation in the Dataflow SDK?
- [x] ParDo

**Explanation**

The ParDo is the core parallel operation in the dataflow SDKs. It takes the element from the PCollection and perform parallel processing and then generates the multiple elements to an output PCollection.

https://cloud.google.com/dataflow/model/par-do

### 13
Which of the following is not a disadvantage of using salting to avoid hotspotting in Cloud Bigtable?
- [x] The hashing function can be difficult to implement.

**Explanation**

If using salting to avoid hotspotting, then you will take a hash of the timestamp and divide it by 3; take the remainder of this calculation and add the remainder to the row key. Dividing by 3 is done because this is an estimate of the number of nodes in the cluster and would provide a good division of activity across those nodes.

A disadvantage of salting in that it is difficult to choose a salt value that both distributes activity across nodes and operates well as you scale your system up or down.
The advantage of salting is its simplicity—it's essentially a simple hashing function. The disadvantage is that when you query for time ranges, you'll have to do multiple scans—one scan per salt value—and combine the results in your own code.

https://cloud.google.com/bigtable/docs/schema-design-time-series

### 14
You are leading a team including yourself, 3 app developers, and 2 data managers who will have access to a project utilizing Google BigQuery, App Engine, and Cloud Dataflow.  The app developers will work primarily in App Engine designing a data analysis delivery and analysis application but will need access to data sets for testing. The database manager will act as the lead in Big Query and Dataflow but will review the application code in App Engine to make sure the data is properly formatted. When considering the best approach to access method for access control, in this case predefined roles are ideal because your project requires ____________________________, and ______________________________. (Choose 2 answers)
- [x] varying levels of access across depending on the GCP service
- [x] team members with access to multiple services

**Explanation**

This is a clear case where fine-grained access is ideal depending on a person's role within the project. Developers will have dataEdtor or perhaps owner predefined roles in App Engine, but likely data viewer permissions within BigQuery and Dataflow. The reverse is likely for the data management team.

[/course/optimizing-google-bigquery/access-control/](https://cloudacademy.com/course/optimizing-google-bigquery/access-control/)



### 15
An arts institute library is undergoing an initiative to archive its over 10,000 existing images. As a digital archivist and beginning Python programmer at the institute, you are using the Google Cloud Vision tool to classify the images. Now you'd like to further subdivide the categories and see if the images within a category, such as leaves, can be tagged with a name after being "trained". Which tool will be most useful for this task?
- [x] Google Cloud Machine Learning

**Explanation**

Google Cloud Vision API allows users to classify images according to pre-built, pre-trained machine-learning model reflected in the API. However, if you have more specialized requirements — for example, to identify specific leaves, it can be more efficient to train and serve a new image model using Google Cloud Machine Learning (Cloud ML).

https://cloud.google.com/blog/big-data/2016/12/how-to-train-and-classify-images-using-google-cloud-machine-learning-and-cloud-dataflow

### 16
Laurie, the cloud admin at Blue Widget Corp, has been asked to build a VPC network in GCP. This VPC network will be connected to the on-prem network via the Cloud VPN service. The address space for the on-prem network spans the CIDR block of 10.128.0.0/9. After deploying the VPC network, Laurie finds that there are issues with the VPN connectivity. What could be causing the VPN connectivity issues?  
- [x] Laurie deployed an Auto Mode VPC Network

**Explanation**

When configuring your network, please be advised of the following note from GPC documentation:

If your VPC network is connected to an on-premises network by using Cloud VPN or Cloud Interconnect, check that subnet ranges do not conflict with on-premises IP addresses. Subnet routes are prioritized first so traffic to the destination range remains in your VPC network, even though it might have been intended for the on-premises network.

https://cloud.google.com/vpc/docs/vpc

### 17
To configure Stackdriver to monitor a web server and notify you if it goes down, what steps do you need to take? (Choose 2 answers)

- [x] Create an uptime check
- [x] Create an alerting policy

**Explanation**

**Uptime checks** verify that your web server is always accessible. The **alerting policy** controls who is notified if the uptime checks should fail.

You don't need to install the Stackdriver Monitoring Agent to get downtime alerts. The agent provides additional information, but it's not required. The Stackdriver Logging Agent is for additional logging, not for alerts.

Using the Monitoring agent is optional. Stackdriver Monitoring can access some metrics without the Monitoring agent, including CPU utilization, some disk traffic metrics, network traffic, and uptime information. [https://cloud.google.com/monitoring/agent/#purpose]

https://cloud.google.com/monitoring/quickstart-lamp#gs-checks


### 18
Which of the following statements about traffic splitting in App Engine is correct?
- [x] Cookie-based traffic splitting is more precise than IP-based though it requires more setup because your services will expect a specific header in the HTTP request.

**Explanation**

We have to tell App Engine whether to split traffic using IP address splitting or Cookies. IP address splitting is easier to do. It will just make App Engine hash the request’s IP address from 0-999 and then route based on whatever random value it gets. This isn’t as precise as Cookie routing though because of how IP addresses tend to be somewhat ephemeral, particularly from cell phone traffic from the public internet. IP address splitting is also bad for traffic coming from internal GCP services because those services tend to utilize a small set of internal IP addresses that will get stuck to the same version of your app. 

For better precision you should use Cookie-based splitting, though this will take a bit more setup because the application will look for a specific HTTP request header. You may need to make a code change in your app to deal with this but it will help ensure you get a precise split for traffic.
 

https://cloud.google.com/appengine/docs/standard/python/splitting-traffic#splitting_traffic_across_multiple_versions


### 19
Jennifer is the cloud admin for the Blue Widget Corp. She has been asked to deploy a Kubernetes cluster so that the organizaton can perform some testing of a containerized app that will be completed within 3 weeks. Which option below is the best solution to ensure that the team can finish its testing without worrying if the cluster will be left behind and continue racking up charges once the team is finished with it?

- [x] Jennifer should deploy an alpha cluster

**Explanation**

An alpha cluster will automatically be deleted after 30 days, ensuring it does not remain and continue to rack up charges.

https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters

### 20
Suppose you have a web server that is working properly, but you can't connect to its instance VM over SSH. Which of these troubleshooting methods can you use without disrupting production traffic? (Select 3 answers.)
- [x] Access the serial console output
- [x] Use netcat to try to connect to port 22
- [x] Create a snapshot of the disk and use it to create a new disk; then attach the new disk to a new instance

**Explanation**

If you modify your firewall rules, it could prevent traffic from flowing to your VM.

You can't attach the VM instance's disk to a new instance without detaching it from the existing instance first, which would require shutting down the instance.

If you create a startup script to collect information, you will have to restart your VM instance to run the script.

You can view the serial console output without disrupting traffic. Running commands in the interactive serial console, on the other hand, could disrupt operations.

Connecting to port 22 using netcat will only affect the SSH server on the VM, since that is the only service that listens on port 22.

You can create a snapshot of a VM instance's disk without disrupting the VM's operation.



https://cloud.google.com/compute/docs/troubleshooting#ssherrors

# Questions

### 1
You are using Google Cloud Storage to store files for a two-year project. You plan to stream in files on an ongoing basis and access these files once a month for analysis. Which type of storage is most appropriate for your needs?
- [ ] Standard
- [ ] Coldline
- [ ] Nearline
- [ ] Archive

### 2
You are managing a project using Google Container Registry, and have written a script to mark all current objects (including the image you just pushed) in your registry public. Which command should you use, assuming that your project ID is "your-project-id"?
- [ ] gsutil acl ch -u AllUsers:R gs://artifacts.your-project-id.appspot.com
- [ ] gsutil defacl ch -u AllUsers:R gs://artifacts.your-project-id.appspot.com
- [ ] gcloud docker -- publish gcr.io/your-project-id/example-image
- [ ] gcloud docker -- push gcr.io/your-project-id/example-image

### 3
You are managing customer success for a mid-size online retailer, and need to quickly implement a solution to analyze large amounts of customer feedback, and reliably identify and separate negative and positive reviews. Which Google Machine Learning service can you implement within your solution?
- [ ] AutoML Natural Language Classification
- [ ] AutoML Natural Language Entity Extraction
- [ ] AutoML Natural Language Sentiment Analysis
- [ ] AutoML Translation

### 4
You realize the reason you are unable to login via SSH to your newly configured GCE virtual machine is the default-allow-ssh firewall rule has been mysteriously deleted. You decide to add the rule back to your firewall. What settings should you select?
- [ ] Allow ingress connections on TCP port 22 from any source to any instance in the network with a rule priority of 65534.
- [ ] Allow ingress connections on TCP port 3389 from any source to any instance in the network with a rule priority of 65534.
- [ ] Allow ingress ICMP traffic from any source to any instance in the network with a rule priority of 65534.
- [ ] Allow ingress connections for all protocols and ports among instances in the network with a rule priority of 65534.

### 5
If you have configured Stackdriver Logging to export logs to BigQuery, but logs entries are not getting exported to BigQuery, what is the most likely cause?
- [ ] Stackdriver Logging does not have permission to write to the BigQuery dataset.
- [ ] There isn't a firewall rule allowing traffic between Stackdriver and BigQuery.
- [ ] The size of the Stackdriver log entries being exported exceeds the maximum capacity of the BigQuery dataset.
- [ ] The Cloud Data Transfer Service has not been enabled.

### 6
You are planning to use Google's Dataflow SDK to analyze customer data such as displayed below. Your project requirement is to extract only the customer name from the data source and then write to an output PCollection.Tom,555 X streetTim,553 Y streetSam, 111 Z streetWhich operation is best suited for the above data processing requirement?
- [ ] ParDo
- [ ] Source API
- [ ] Sink API
- [ ] Data extraction

### 7
Suppose you have a table that includes a nested column called "city" inside a column called "person", but when you try to submit the following query in BigQuery, it gives you an error.SELECT person FROM `project1.example.table1` WHERE city = "London"How would you correct the error?
- [ ] Change "person" to "person.city".
- [ ] Change "person" to "city.person".
- [ ] Add ", UNNEST(city)" before the WHERE clause.
- [ ] Add ", UNNEST(person)" before the WHERE clause.


### 8
Your company would like to establish a direct, private connection between your on-premise network with Google networks, to connect with GCP resources without transmitting over the public internet. However, your on-premise network is too far from a Google colocation facility to establish a physical connection. You also expect your network topology to change in the next 18 months, so you will need to update all on-premise destination IP addresses. You would like this update to be entirely managed by your company's employees, even though you will need to connect through a service provider. Which GCP Hybrid Connectivity option will allow you to establish your desired network connection, and independently manage your upcoming network updates?
- [ ] Dedicated Interconnect
- [ ] Partner Interconnect
- [ ] Direct Peering
- [ ] Carrier Peering

### 9
To prevent Denial of Service (DoS) attacks in your PHP App Engine application, what type of file do you need to create to store blacklisted IP addresses?
- [ ] dos.yaml
- [ ] dos.ini
- [ ] blacklist.text
- [ ] disable.php

### 10
You can review Stackdriver logs via the Logging page in the Stackdriver monitoring console, or by setting up a BigQuery dataset containing Stackdriver logs. What are two advantages of creating the BigQuery dataset containing stackdriver logs? (Choose 2 answers)
- [ ] The logs for the complex system often qualify as big data.
- [ ] BigQuery is faster and capable of more complex queries .
- [ ] The datasets reveal more parameters in the BigQuery datasets than in the console.
- [ ] Creating BigQuery data sets enables stronger data security features

### 11
You are an architect helping an enterprise customer deploy their application on Google Compute Engine. The customer's IT team already created two projects, for marketing and sales departments, within the US-Central1 region. The network topology, firewall rules, and routes are identical for the marketing and sales projects. The IT manager wants your help in designing a single network that will be shared by applications running within the sales and marketing projects. Which statement regarding your VPC network(s) that will contain the marketing and sales resources is correct, and can help your IT manager design the best solution?
- [ ] All VPC networks are global resources, so every VPC and its subnets can be shared between the marketing and sales projects running in the same region.
- [ ] Although VPCs are global resources, sales and marketing need to use a shared VPC to access the same resources in specific subnets.
- [ ] VPCs cannot be used by different projects, so sales and marketing must design separate networks within separate VPCs.
- [ ] While VPCs are global, subnets are regional, so VPCs can be used by different projects but subnets must be used by a single project to maintain proper security.

### 12
You are planning to build ticket reservation software using Google Cloud's Dataflow SDK. Your project requirement is to extract the data and then perform parallel processing operations. Which tool supports the core parallel processing operation in the Dataflow SDK?
- [ ] Distributed
- [ ] Parallel
- [ ] ParDo
- [ ] Logical

### 13
Which of the following is not a disadvantage of using salting to avoid hotspotting in Cloud Bigtable?
- [ ] The hashing function can be difficult to implement.
- [ ] You will need to combine the results of your salt value into your own code.
- [ ] It is difficult to choose a salt value that spreads activity across nodes and operates well with scaling your system up and down
- [ ] You may have to do multiple scans when querying for time ranges

### 14
You are leading a team including yourself, 3 app developers, and 2 data managers who will have access to a project utilizing Google BigQuery, App Engine, and Cloud Dataflow.  The app developers will work primarily in App Engine designing a data analysis delivery and analysis application but will need access to data sets for testing. The database manager will act as the lead in Big Query and Dataflow but will review the application code in App Engine to make sure the data is properly formatted. When considering the best approach to access method for access control, in this case predefined roles are ideal because your project requires ____________________________, and ______________________________. (Choose 2 answers)
- [ ] varying levels of access across depending on the GCP service
- [ ] team members with access to multiple services
- [ ] no need for fine-grained access
- [ ] members need create/delete permissions within each service

### 15
An arts institute library is undergoing an initiative to archive its over 10,000 existing images. As a digital archivist and beginning Python programmer at the institute, you are using the Google Cloud Vision tool to classify the images. Now you'd like to further subdivide the categories and see if the images within a category, such as leaves, can be tagged with a name after being "trained". Which tool will be most useful for this task?
- [ ] Google Cloud Analytics
- [ ] Google Cloud Big Query
- [ ] Google Cloud Dataproc
- [ ] Google Cloud Machine Learning

### 16
Laurie, the cloud admin at Blue Widget Corp, has been asked to build a VPC network in GCP. This VPC network will be connected to the on-prem network via the Cloud VPN service. The address space for the on-prem network spans the CIDR block of 10.128.0.0/9. After deploying the VPC network, Laurie finds that there are issues with the VPN connectivity. What could be causing the VPN connectivity issues?  
- [ ] Laurie deployed an Auto Mode VPC Network
- [ ] Laurie deployed a Custom Mode VPC Network
- [ ] The Cloud VPN service doesn't allow you to connect a VPC to an on-prem network
- [ ] None of the Above

### 17
To configure Stackdriver to monitor a web server and notify you if it goes down, what steps do you need to take? (Choose 2 answers)
- [ ] Install the Stackdriver Monitoring Agent on the web server
- [ ] Create an uptime check
- [ ] Create an alerting policy
- [ ] Install the Stackdriver Logging Agent on the web server


### 18
Which of the following statements about traffic splitting in App Engine is correct?
- [ ] The basic purpose of traffic splitting is to create multiple load balancers with different DNS names to allow applications to receive traffic from many different sources.
- [ ] Traffic splitting allows you to move a portion of traffic from one service in one App Engine app to a service in a separate App Engine app in another geographic region.
- [ ] Cookie-based traffic splitting is more precise than IP-based though it requires more setup because your services will expect a specific header in the HTTP request.
- [ ] The App Engine flexible environment has a ‘warmup’ mode to allow you to split traffic gradually to help reduce latency spikes and dropped requests.

### 19
Jennifer is the cloud admin for the Blue Widget Corp. She has been asked to deploy a Kubernetes cluster so that the organizaton can perform some testing of a containerized app that will be completed within 3 weeks. Which option below is the best solution to ensure that the team can finish its testing without worrying if the cluster will be left behind and continue racking up charges once the team is finished with it?
- [ ] Jennifer should deploy a private cluster with a 30-day window
- [ ] Jennifer should deploy a zonal cluster
- [ ] Jennifer should deploy a dev cluster
- [ ] Jennifer should deploy an alpha cluster

### 20
Suppose you have a web server that is working properly, but you can't connect to its instance VM over SSH. Which of these troubleshooting methods can you use without disrupting production traffic? (Select 3 answers.)
- [ ] Modify your firewall rules
- [ ] Access the serial console output
- [ ] Use netcat to try to connect to port 22
- [ ] Create a snapshot of the disk and use it to create a new disk; then attach the new disk to a new instance


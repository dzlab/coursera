# Questions

### 1
Your company is planning to migrate to Google Cloud Platform, but before migration begins all employees are learning important security best practices related to data encryption. You have read that data is encrypted using envelope encryption. Which statement correctly describes the envelope encryption process in Google Cloud Platform's Cloud Key Management Service (KMS)? 
- [ ] Create a data encryption key (DEK) locally to encrypt data chunks then encrypt the DEK using a key encryption key (KEK) and then store the KEK in Cloud KMS.
- [ ] Create a key encryption key (KEK) locally to encrypt data chunks then encrypt the KEK using the data encryption key (DEK) and then store the DEK in Cloud KMS.
- [ ] Create a single data encryption key (DEK) locally to encrypt all data, then encrypt the DEK using key encryption key (KEK) store the KEK in Cloud KMS.
- [ ] Create a data encryption key locally to encrypt data chunks then encrypt DEK using a key encryption key and then store the KEK in any third-party key storage service.

### 2
You are working as a cloud trainer for an online education business that has deployed its service on Content Engine instances. Students are accessing the website from all over the world over multiple protocols on layers 4 and 7 to access the website. Management has asked you to select a load balancer that can provide a secure connection via TLS over layers 4 and 7, is capable of distributing traffic to multiple regions, and that can terminate requests at the load balancer before they reach the virtual instances. Which of the following Load Balancer types would you choose?
- [ ] Network Load Balancing
- [ ] SSL Proxy Load Balancing
- [ ] TCP Proxy Load Balancing
- [ ] HTTP(S) Load Balancing

### 3
Your company is using different VM Instances, one for the web server and one for a database server. You want to connect to the web server to the public internet and the web server should be able to fetch data from the database server, but the database server should not be accessible from the public internet. How can you design the Firewall Rules in order to fulfill the requirement? 
- [ ] Create a firewall rule to allow ingress traffic from the application to the database by filtering using firewall tags.
- [ ] Create a firewall rule to allow ingress traffic from the application to the database by filtering using network tags.
- [ ] Create a firewall rule to allow ingress traffic from the application to the database by filtering using a service account.
- [ ] Create a firewall rule to allow ingress traffic for all instances in the network.

### 4
A Startup company is struggling to manage its employee data, so it has hired a third-party data management firm to manage documents and text files related to its personnel. This data includes sensitive personal information, such as employee salary and performance feedback, so the company wants to make sure it is not exposed to the third-party firm. Which of the following Google Cloud Data Loss Prevention (DLP) API techniques should the company use to achieve this? (Choose 2 answers)
- [ ] Image Inspection and Redaction API
- [ ] Text Classification and Redaction API
- [ ] Pseudonymization
- [ ] Date Shifting

### 5
As the security lead, you use Cloud KMS to generate the encryption keys and want the key to automatically rotate after 90 days. Which type of keys you should use for the given requirement?
- [ ] Symmetric keys
- [ ] Asymmetric keys
- [ ] Customer-supplied encryption keys
- [ ] Customer-managed encryption keys (CMEK)

### 6
Your company is planning to store pictures in Cloud Storage buckets. Your manager has asked you to use a key that is created and managed on-premises in the encryption process of the objects. What type of key service would you use?
- [ ] Use Cloud KMS default encryption
- [ ] Use HashiCorp Vault
- [ ] Use Cloud Storage customer-supplied encryption keys
- [ ] Use KMS customer-managed encryption keys

### 7
Your client has a LAMP application hosted on Compute Engine that should only receive HTTPS traffic. You have created an egress firewall rule to allow all traffic (0.0.0.0/0) with protocol HTTPS(443) with priority 65535, but the team is still not able to access the application.How can you resolve this issue?
- [ ] Decrease the priority number of the egress firewall to a number lower than 65535.
- [ ] Increase the priority number of the egress firewall rule to a number higher than 65535.
- [ ] Create an ingress firewall rule to allow traffic from all source IPs and assign the rule a priority number lower than 65535.
- [ ] Create an ingress firewall rule to allow traffic from all source IPs and assign the rule a priority number higher than 65535.

### 8
You have a team of 30 people including the client team. You are provided with a Cloud Storage bucket to upload or read the technical document uploaded by other members. You should be able to make any changes to documents uploaded by other members. What type of access control would you choose? (Choose 2 answers)
- [ ] Fine-grained access using ACLs
- [ ] IAM Roles with conditions
- [ ] Pre-signed URLs
- [ ] IAM Roles without conditions

### 9
You are working on a microservices application with many configuration files in each service that include database passwords and API keys. These details are in plain text and stored along with source code. Management is worried about this private information being stolen and exposed by malicious users. The information needs to be protected but still accessible and highly available to separate applications and GCP users managing the application. Which of the following GCP services you can use to efficiently store these details safely with minimal administration?
- [ ] Cloud KMS
- [ ] Secrets Manager
- [ ] Cloud HSM
- [ ] Titan Security Keys

### 10
Your Company has application workloads running on-premise which recently crashed due to a DDoS attack. You have suggested that they should move to Google Cloud where they can use certain services to mitigate these types of attacks in the future. Which of the following GCP services would you suggest to protect them against DDoS attacks? (Choose 2 answers)
- [ ] DNS Security Extensions (DNSSEC)
- [ ] Cloud Armor
- [ ] HTTP(S) Load Balancer
- [ ] Cloud Security Scanner

### 11
As a Cloud Security Consultant, a company has asked you to store the logs of all the incoming network traffic in real-time so that later these logs can be used for multiple internal audits. Which of the following services you should choose to get details of all incoming traffic?
- [ ] Cloud Audit Logs
- [ ] Cloud Monitoring
- [ ] VPC Flow Logs
- [ ] Security Command Center

### 12
Your organization is using Cloud Identity as its identity provider. Due to recent phishing attacks, you have been asked to implement the most secure multi-factor authentication (MFA) solution provided by Cloud Identity. Which MFA method provided by Cloud Identity would you implement?
- [ ] Google Prompt
- [ ] Google Authenticator App
- [ ] Security Keys
- [ ] Backup codes

### 13
You have built a three-tier application hosting critical workloads which you are planning to host on the Google Cloud Platform. Due to the low budget, the database is designed as a part of the server only. Your manager has asked you to design the infrastructure in a way that follows the Hot Disaster Recovery Pattern.   How would you design the architecture?
- [ ] Deploy one compute engine in one zone, failover to on-premise server.
- [ ] Deploy two compute engines in two zones each located in different regions.
- [ ] Deploy two compute engines in two zones each located in the same region.
- [ ] Deploy two compute engines in two zones each located in the same region but in different projects.

### 14
Your manager has asked you to store all Cloud Logging data access logs in Google Cloud. The Analytics team will review these logs for quality improvement and plans to retain them for up to 20 years because they will be used for historical data analysis.  Which of the following options should the Analytics team choose to store the logs, keeping cost optimization in mind?
- [ ] BigQuery
- [ ] Cloud Storage
- [ ] Cloud Logging
- [ ] Cloud Pub/Sub

### 15
Your organization is developing a suite of applications on GCP including online transaction systems along with other applications and data. What is the best method to isolate the payment processing system to achieve a more secure environment?
- [ ] There is no need for isolation. Use an identity-aware proxy for an extra layer of authentication.
- [ ] Isolate the payment processing environment by using a different service account.
- [ ] Isolate the payment processing environment into a separate GCP project.
- [ ] Isolate the payment processing environment into a separate VPC.

### 16
Your manager has asked you to grant one contingent worker to review all the Cloud Storage buckets for two hours in order to create a similar bucket configuration for his team. What is the most secure and efficient method to grant the contingent worker access to Cloud Storage for only two hours?
- [ ] Create a pre-signed URL granting two hours of access.
- [ ] Configure an access control list (ACL) to allow access from the contingent works IP address and then modify it two hours later.
- [ ] Assign an IAM role to an IAM user for the contingent worker with an expiration time of two hours.
- [ ] Create an IAM user for the contingent worker and then manually remove the IAM user after two hours.

### 17
You have hired a freelance audit reviewer to access all GCP resources within a specific account. The company is using Cloud Identity as their Identity Provider. How would you allow the audit reviewer to review all the resources in the project?
- [ ] Ask for his personal Google account and assign this account with the Project Viewer role in IAM.
- [ ] Borrow an account from a co-worker for a day who has Project Viewer access.
- [ ] Create an account in Cloud Identity and assign this account with the Project Viewer role in IAM.
- [ ] Create an account in Cloud Identity and assign this account with the Project Browser role in IAM.


### 18
Your company is hosting its e-commerce application on Google Cloud. They have more than one million customers, and they are worried about DNS spoofing or poisoning attacks. If something goes wrong with the website even for a minute, it can cause a huge financial loss. Which of the services would you use to get rid of such attacks?
- [ ] Use HTTP(s) Load Balancer
- [ ] Use DNS Security Extensions (DNSSEC)
- [ ] Use Cloud Security Scanner
- [ ] Use Cloud Armor

### 19
A firm hired you as a contractual GCP consultant two months ago and you deployed the firm's microservice application on containers hosted on Compute Engine virtual machines. The microservice application is designed is fairly complex. For the past few days, customers have been complaining about latency issues of multiple types when using the app, but you have not been able to diagnose the problem's cause, in which service it is located, and how it may affect other app services. Which of the following is the most reliable tool you can use to quickly understand the cause of performance issues?
- [ ] Cloud Monitoring
- [ ] Cloud Trace
- [ ] Cloud Logging
- [ ] VPC Flow Logs

### 20
Your employer stores important customer data locally, but plans to migrate to Google Cloud Platform. They are planning to store the data in a Cloud Storage bucket, but before uploading the data, they want to redact the customer’s unique id which consists of 25 alphanumeric characters arranged in five hyphenated groups. Here is an example: 3xr4e-11plp-i9vdf-ax990-512k2 Which of the following infoType detectors you should use to detect the customer’s unique id?
- [ ] Built-In InfoType Detector
- [ ] Regular Custom InfoType Detector
- [ ] Stored Custom InfoType Detector
- [ ] Regular Expression InfoType Detector

### 21
Your organization is planning to migrate to Google Cloud Platform for all their IT operations. They are currently using  Active Directory to authenticate all employees within the entire company and have more than 50,000 users. They are concerned about migrating the identities from Active Directory to a system within GCP as it can be a time-consuming process, and they are not sure how to migrate additional employees who join the company during the migration to Google Cloud.  Which of the following is the most convenient way to migrate Active Directory identities to Google Cloud and maintain an up-to-date directory as new employees are hired? 
- [ ] Use Google Cloud Directory Sync (GCDS) 
- [ ] Develop a custom script to import identities at regular intervals
- [ ] Use Security Assertion Markup Language (SAML) to import identities.
- [ ] Use Cloud IAM to migrate identities from Active Directory to Google Cloud.

### 22
Your client has four teams of engineers in their engineering department. Each team of engineers requires different assigned permissions to GCP services, and each team is working on applications with separate development and production environments. What is the best way to configure the team's folder and project structure to provide the appropriate level of isolation and enforce the principle of least privilege along with other GCP security practices? (Choose 2 answers)
- [ ] Create a folder for the engineering department that contains each engineering team's separate projects for its development and production environments.
- [ ] Create a folder for the engineering department with subfolders for each engineering team containing each team's projects for its development and production environments.
- [ ] Create an IAM Group for each engineering team and assign permissions at the project level.
- [ ] Create an IAM Group for each team, and assign permissions at the folder level.

### 23
A technical support team reports that when customers submit tickets through the company's online customer support site, some customers attach documents or pictures containing their personal information. All attachments to customer support tickets are stored in a customer support database for regular audits and reviews, and storing this personal information may lead to security risks. Which solution would a security engineer implement in order to mitigate this security risk, even if customers continue to attach sensitive data?
- [ ] Use Cloud Key Management Service (KMS) for encryption of PII data before moving to the database.
- [ ] Use Cloud Storage Object Lifecycle Management to delete all the attachments after resolving the issue.
- [ ] Use the Cloud Data Loss Prevention (DLP) Image Inspection and Redaction API to redact personal information before storing the ticket in the database.
- [ ] Use the Cloud Data Loss Prevention (DLP) Text Classification and Redaction API to redact personal information before storing the ticket in the database.

### 24
You have uploaded 500 GB of important project files to a Cloud Storage bucket and added a retention policy of two years to the bucket without a retention policy lock. After one month, you realize you uploaded the same folder twice, which includes approximately 100 GB of data. You need to delete that redundant folder to avoid any unnecessary storage costs, but when you attempt to delete it you receive error messages that you have not reached the required retention period. In this case, what can you do in order to delete the folder and preserve the security of data stored in this bucket?
- [ ] Disable the policy and delete the folder, and then re-enable the same policy for the bucket.
- [ ] First, unlock the policy lock and then delete the folder. Reapply the policy lock once the file is deleted.
- [ ] First, delete the retention policy and then delete the folder. Next, lock the bucket by adding a new retention policy.
- [ ] You cannot delete the folder using the console. You can use the `gsutil rm gs://your-bucket/folder-to-delete/**` command to delete the folder.

### 25
While many developers have permissions granting different levels of write access to resources within your dev/test environment, it is important to preserve specific resource configurations in this environment. Management insists the configuration of these resources should not be changed. Which of the following tools you can use in order to enforce these configurations?
- [ ] Cloud Security Scanner
- [ ] Security Command Center
- [ ] Forseti
- [ ] Cloud Logging

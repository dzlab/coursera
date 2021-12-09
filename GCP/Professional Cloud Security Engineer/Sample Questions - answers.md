# Answers

### 1
Your company is planning to migrate to Google Cloud Platform, but before migration begins all employees are learning important security best practices related to data encryption. You have read that data is encrypted using envelope encryption. Which statement correctly describes the envelope encryption process in Google Cloud Platform's Cloud Key Management Service (KMS)? 
- [x] Create a data encryption key (DEK) locally to encrypt data chunks then encrypt the DEK using a key encryption key (KEK) and then store the KEK in Cloud KMS.

**Explanation**

The correct choice is to create a data encryption key (DEK) locally to encrypt data chunks then encrypt the DEK using a key encryption key (KEK) and then store the KEK in Cloud KMS.  To encrypt the data you have to create a data encryption key locally to encrypt the data chunks where each chunk is encrypted with different DEK and then each DEK is then wrapped with a key-encryption key and stored in Cloud KMS.


The other choices are incorrect because:

- DEK is used to encrypt the data then KEK to encrypt DEK.
- in GCP, data is encrypted in chunks using different keys for each chunk of data.
- it is not recommended to use any third-party tool to store any keys unless there is no option of storing them in GCP.

https://cloud.google.com/kms/docs/envelope-encryption

### 2
You are working as a cloud trainer for an online education business that has deployed its service on Content Engine instances. Students are accessing the website from all over the world over multiple protocols on layers 4 and 7 to access the website. Management has asked you to select a load balancer that can provide a secure connection via TLS over layers 4 and 7, is capable of distributing traffic to multiple regions, and that can terminate requests at the load balancer before they reach the virtual instances. Which of the following Load Balancer types would you choose?

- [x] SSL Proxy Load Balancing

**Explanation**

SSL Proxy Load Balancing is the correct answer because SSL proxy LB works above Layer 4, it can be global, and it is a proxy-based load balancer which means the request is terminated at Load Balancer.

The other options are incorrect because:

- Network LB works at Layer 4 of the OSI Model whereas TLS works above layer 4. TLS is a later and more secure version of SSL, and the request is not terminated at Load Balancer in Network LB. 
- TCP Proxy LB doesn’t support TLS connection.
- HTTP(S) LB only supports Port 80, 8080, and 443.

https://cloud.google.com/load-balancing/docs/ssl

### 3
Your company is using different VM Instances, one for the web server and one for a database server. You want to connect to the web server to the public internet and the web server should be able to fetch data from the database server, but the database server should not be accessible from the public internet. How can you design the Firewall Rules in order to fulfill the requirement? 

- [x] Create a firewall rule to allow ingress traffic from the application to the database by filtering using a service account.

**Explanation**

The correct choice is to 'Create a firewall rule to allow ingress traffic from the application to the database by filtering using a service account.' because you can filter the traffic to a particular VM Instance that is using a specific service account. It is more secure than using Network tags. 

The other choices are incorrect because:

- To 'create a firewall rule to allow ingress traffic from the application to the database by filtering using network tags because there is no filter like firewall tags' because there is no filter like firewall tags. Either there are all instances in the network, network tags, or service accounts.
- To 'create a firewall rule to allow ingress traffic from the application to the database by filtering using network tags' is wrong because network tags are an arbitrary attribute, as there can be multiple tags associated with the VM Instance. However, it can be used to create more strict rules. You should prefer using a service account.
- To 'create a firewall rule to allow ingress traffic for all instances in the network' is wrong because it is the least secure option to use when you have other options to use.

https://cloud.google.com/vpc/docs/firewalls#service-accounts-vs-tags

### 4
A Startup company is struggling to manage its employee data, so it has hired a third-party data management firm to manage documents and text files related to its personnel. This data includes sensitive personal information, such as employee salary and performance feedback, so the company wants to make sure it is not exposed to the third-party firm. Which of the following Google Cloud Data Loss Prevention (DLP) API techniques should the company use to achieve this? (Choose 2 answers)

- [x] Text Classification and Redaction API
- [x] Pseudonymization

**Explanation**

The Text Classification and Redaction API and Pseudonumization are correct because the Text Redaction technique will hide the sensitive data using asterisk or hash whereas the Pseudonymization technique will replace the sensitive data with a token.

The Generalization and Bucketing technique is wrong because this technique will help you to generalize the data and then bucket it. It won't hide any sensitive data. For example in your company, you might have data of an assistant manager, manager, a senior manager along with their salaries. This technique will generalize them into a Manager and sum of their salaries. 

The Image Inspection and Redaction API could have been correct if the company stored image data, but this is text. It is not mentioned in the question.
 

https://cloud.google.com/dlp/docs/classification-redaction

### 5
As the security lead, you use Cloud KMS to generate the encryption keys and want the key to automatically rotate after 90 days. Which type of keys you should use for the given requirement?
- [x] Symmetric keys

**Explanation**

Symmetric keys are the right choice because the question is asking for rotation of keys automatically which is possible for symmetric keys but not asymmetric keys. Cloud KMS doesn’t support the automatic rotation of asymmetric keys.

With customer-supplied encryption keys (CSEK), the user creates and manages the encryptions keys on-premise and managed by Cloud Storage, not Cloud KMS.

With Customer-Managed Encryption Keys (CMEKs) you manage the encryption keys created for you by Cloud KMS, and rotation is done manually.

https://cloud.google.com/kms/docs/rotating-keys#automatic

### 6
Your company is planning to store pictures in Cloud Storage buckets. Your manager has asked you to use a key that is created and managed on-premises in the encryption process of the objects. What type of key service would you use?

- [x] Use Cloud Storage customer-supplied encryption keys

**Explanation**

Customer Supplied Encryption Keys, you create and manage the encryptions keys on-premise. KMS  customer-managed encryption keys (CMEK), you manage the encryption keys created for you by Cloud KMS, also you manage these keys in Cloud KMS only. KMS default encryption keys are generated and managed by Google.
 

https://cloud.google.com/storage/docs/gsutil/addlhelp/UsingEncryptionKeys#:

### 7
Your client has a LAMP application hosted on Compute Engine that should only receive HTTPS traffic. You have created an egress firewall rule to allow all traffic (0.0.0.0/0) with protocol HTTPS(443) with priority 65535, but the team is still not able to access the application.How can you resolve this issue?

- [x] Create an ingress firewall rule to allow traffic from all source IPs and assign the rule a priority number lower than 65535.

**Explanation**

All ingress traffic is denied in implied firewall rules, so to complement that rule you have to create a firewall rule to allow all HTTPS traffic with priority number less than 65535. A lower priority number implies a higher priority rule. 

The other answers are incorrect because:

- There are two implied rules already, to allow all egress traffic and to deny all ingress traffic with the lowest priority, i.e. 65535.
- Egress traffic is already managed in the implied firewall rule. Here we need the ingress firewall rule, and the lowest priority is 65535.
- You cannot create a priority number higher than 65535. It is the highest priority number you can assign.

https://cloud.google.com/vpc/docs/firewalls#priority

### 8
You have a team of 30 people including the client team. You are provided with a Cloud Storage bucket to upload or read the technical document uploaded by other members. You should be able to make any changes to documents uploaded by other members. What type of access control would you choose? (Choose 2 answers)
- [x] Fine-grained access using ACLs
- [x] IAM Roles with conditions

**Explanation**

ACLs are correct because using ACLs, you can assign permissions for each individual object. These are fine-grained permissions.

With IAM Roles with conditions, you can choose to allow users with read-write access to their individual object by providing the object name and read access to all objects which are uploaded by other members using Bucket resource type which is storage.googleapis.com/Bucket and Resource name is your bucket name. 

https://cloud.google.com/iam/docs/conditions-overview

### 9
You are working on a microservices application with many configuration files in each service that include database passwords and API keys. These details are in plain text and stored along with source code. Management is worried about this private information being stolen and exposed by malicious users. The information needs to be protected but still accessible and highly available to separate applications and GCP users managing the application. Which of the following GCP services you can use to efficiently store these details safely with minimal administration?
- [x] Secrets Manager

**Explanation**

Secrets Manager is right because passwords and API keys or any other secrets can be stored in Secret manager and while retrieving you can use secret manager dependency. The Secrets manager always encrypts your secrets before writing to the disk.

The other choices are incorrect because:

- Cloud KMS is used to store encryption keys but passwords, API keys are secrets that can be stored in Cloud KMS but it is more complex and less efficient.
- Cloud HSM is also used to store encryption keys primarily, but has an additional challenges with maintaining accessibility and high availability because they are stored on separate HSM devices, not in the cloud.
- Titan Security Keys are not used to store information - they are separate USB devices that cloud customers use to complete multi-factor authentication.

https://cloud.google.com/secret-manager/docs/overview


### 10
Your Company has application workloads running on-premise which recently crashed due to a DDoS attack. You have suggested that they should move to Google Cloud where they can use certain services to mitigate these types of attacks in the future. Which of the following GCP services would you suggest to protect them against DDoS attacks? (Choose 2 answers)

- [x] Cloud Armor
- [x] HTTP(S) Load Balancer

**Explanation**

Cloud Armor and HTTP(S) load balancers work together to protect against DDoS attacks.

The other choices are incorrect because:

- DNSSEC is used for security from spoofing which means redirecting the main website to the fake one. Also called DNS Poisoning. It is dangerous as it spreads from one DNS to another.
- Cloud Security Scanner is a web security scanner for common vulnerabilities in your applications. It doesn’t look for DDoS Attacks. It crawls user web applications to check vulnerabilities like Cross-Site scripting, insecure JavaScript files, or Flash Injections.

https://cloud.google.com/files/GCPDDoSprotection-04122016.pdf

### 11
As a Cloud Security Consultant, a company has asked you to store the logs of all the incoming network traffic in real-time so that later these logs can be used for multiple internal audits. Which of the following services you should choose to get details of all incoming traffic?

- [x] VPC Flow Logs

**Explanation**

VPC Flow Logs are the correct choice because they are enabled while creating each subnet and once you enable it, any traffic to and from your VM Instance is logged and sent to Cloud Logging.

The other choices are incorrect for the following reasons:

- Cloud Audit Logs record the actions that members in your Google Cloud organization have taken in your Google Cloud resources, whereas in this case, you need information related to incoming external requests as well, which include customers using any customer-facing applications.
- Cloud Monitoring is just for monitoring the resources, it has nothing to do with logs, It will monitor the traffic but won’t log it.
- Security Command Center is an analytics system for surfacing and remediating GCP Security across the organization. It allows you to gather data, identify threats and act on them.

https://cloud.google.com/vpc/docs/flow-logs

### 12

Your organization is using Cloud Identity as its identity provider. Due to recent phishing attacks, you have been asked to implement the most secure multi-factor authentication (MFA) solution provided by Cloud Identity. Which MFA method provided by Cloud Identity would you implement?
- [x] Security Keys

**Explanation**

All the above options can be used for MFA but as the question asked for the Strongest one, security keys offer the strongest security. It uses encryptions of keys that are less prone to phishing attacks.

https://cloud.google.com/identity/solutions/enforce-mfa

### 13
You have built a three-tier application hosting critical workloads which you are planning to host on the Google Cloud Platform. Due to the low budget, the database is designed as a part of the server only. Your manager has asked you to design the infrastructure in a way that follows the Hot Disaster Recovery Pattern.   How would you design the architecture?
- [x] Deploy two compute engines in two zones each located in different regions.

**Explanation**

The correct choice here is to deploy two compute engines in two zones each located in different regions. This is correct because Hot DR Pattern has low RTO/RPO which means Fastest recovery. If you create a compute engine in 2 zones, if the Compute Engine goes down in 1 zone or 1 region, the other zone or region is still there. It is the most expensive approach.

The other choices are incorrect because:

- Deploying one compute engine in one zone and then failing over to on-premise server is incorrect because only one Instance is there and failover to on-premise doesn’t make any sense, You will have to manage on-premise additionally.
- The two remaining choices are wrong because if the entire region goes down, there is no backup option available. Choosing different projects won’t make any difference here.

https://cloud.google.com/solutions/dr-scenarios-planning-guide#dr_patterns

### 14
Your manager has asked you to store all Cloud Logging data access logs in Google Cloud. The Analytics team will review these logs for quality improvement and plans to retain them for up to 20 years because they will be used for historical data analysis.  Which of the following options should the Analytics team choose to store the logs, keeping cost optimization in mind?
- [x] Cloud Storage

**Explanation**

Cloud Storage Bucket is a recommended inexpensive, and long-term storage option. 

Cloud Logging is wrong because Cloud Logging data access logs can be retained for time periods between 30 days and ten years, if enabled. Data access logs are disabled by default. However, the Analytics team needs to store these for up to 20 years, so this is not sufficient.
BigQuery and Cloud Pub/Sub are wrong because BigQuery is not a recommended storage option. It is mainly used for the analysis of data. Cloud Pub/Sub can help you stream the log entries to external tools like Splunk.

https://cloud.google.com/logging/docs/audit#data-access

### 15
Your organization is developing a suite of applications on GCP including online transaction systems along with other applications and data. What is the best method to isolate the payment processing system to achieve a more secure environment?

- [x] Isolate the payment processing environment into a separate GCP project.

**Explanation**

Isolating the payment processing environment in a separate GCP project is the best choice because you should keep the scope of the cardholder’s data environment as small as possible. Using a different project for the cardholder’s data environment is recommended.

The other choices are incorrect for the following reasons:

- IAP is for external user’s authentication but here we are working on internal infrastructure.
- Using a separate service account or VPC is incorrect because the scope should be as small as possible. Though you can choose this, it is recommended to choose a separate project for each environment.

https://cloud.google.com/solutions/pci-dss-and-gke-guide#segment_your_cardholder_data_environment

### 16
Your manager has asked you to grant one contingent worker to review all the Cloud Storage buckets for two hours in order to create a similar bucket configuration for his team. What is the most secure and efficient method to grant the contingent worker access to Cloud Storage for only two hours?

- [x] Assign an IAM role to an IAM user for the contingent worker with an expiration time of two hours.

**Explanation**

IAM Conditions can be added while assigning IAM Role to the users with the condition of expiring time after 2hours. After 2 hours, access will be revoked immediately.

Pre-signed URLs are mainly used for the users who need access to Cloud Storage for reading and write access. It is not recommended as anyone with the URL can access the bucket. There is no authentication followed while using Pre-signed URLs.

An ACL is used to provide more fine-grained access to each individual object. Here the requirement is for all the buckets. 

Manually doing this can be overhead if the number of users is more in the future.

https://cloud.google.com/iam/docs/managing-conditional-role-bindings#iam-conditions-add-binding-console

### 17
You have hired a freelance audit reviewer to access all GCP resources within a specific account. The company is using Cloud Identity as their Identity Provider. How would you allow the audit reviewer to review all the resources in the project?
- [x] Create an account in Cloud Identity and assign this account with the Project Viewer role in IAM.

**Explanation**

Creating a Cloud Identity account and assigning the account with the Project Viewer role in IAM is correct because you can create a temporary account in Cloud Identity and later remove it after one day. You should choose the Project Viewer role which will allow the user to review all the resources in the project.

Other choices are incorrect because:

- You should never use a personal account, you should always use an organizational account. Using a personal account might lead to a security leak or information breach which is not possible to track in the case of a personal account. 
- Identity always belongs to each individual, you should never share your accounts at any cost. You can create a temporary account in Cloud Identity and later remove it after one day. You should choose the Project Viewer role which will allow the user to review all the resources in the project.
- The Project Browser role will allow the user to go through the project but the user won’t be able to review any of the resources. It only has access to read the hierarchy for a project.

https://cloud.google.com/identity/docs/overview



### 18
Your company is hosting its e-commerce application on Google Cloud. They have more than one million customers, and they are worried about DNS spoofing or poisoning attacks. If something goes wrong with the website even for a minute, it can cause a huge financial loss. Which of the services would you use to get rid of such attacks?
- [x] Use DNS Security Extensions (DNSSEC)

**Explanation**

DNSSEC is correct because enabling DNSSEC in Cloud DNS. DNSSEC uses a system of a public key and digital signatures to verify the data.

The other choices are incorrect because:

- With HTTP(S) Load Balancers, proxy-based load balancing helps you mitigate DDoS Attacks, DNS Poisoning is all about redirecting the main website to some fake website having the same UI.
- Cloud Security Scanner is a web security scanner for common vulnerabilities in your applications. It doesn’t look for DNS Poisoning. It crawls user web applications to check vulnerabilities like Cross-Site scripting, insecure JavaScript files, or Flash Injections.
- Cloud Armor works with Global HTTP(s) Load Balancers to provide built-in defense against DDoS Attacks.

https://cloud.google.com/dns/docs/dnssec

### 19
A firm hired you as a contractual GCP consultant two months ago and you deployed the firm's microservice application on containers hosted on Compute Engine virtual machines. The microservice application is designed is fairly complex. For the past few days, customers have been complaining about latency issues of multiple types when using the app, but you have not been able to diagnose the problem's cause, in which service it is located, and how it may affect other app services. Which of the following is the most reliable tool you can use to quickly understand the cause of performance issues?
- [x] Cloud Trace

**Explanation**

Cloud Trace is the best solution in this case because it checks for latency issues from users and applications. Nowadays, Trace, debugger, profilers are rolled into one service called Stackdriver APM (Application performance management). Although Monitoring and Logging can also be used, the most reliable way to quickly diagnose the issue is to use Cloud Trace.

https://cloud.google.com/trace

### 20
Your employer stores important customer data locally, but plans to migrate to Google Cloud Platform. They are planning to store the data in a Cloud Storage bucket, but before uploading the data, they want to redact the customer’s unique id which consists of 25 alphanumeric characters arranged in five hyphenated groups. Here is an example: 3xr4e-11plp-i9vdf-ax990-512k2 Which of the following infoType detectors you should use to detect the customer’s unique id?

- [x] Regular Expression InfoType Detector

**Explanation**

Regular Expression InfoType Detector is correct because it is a user-defined infoType detector where it looks for the custom patterns. In this case, you have a custom pattern that has 25 characters separated by a hyphen after every 5 characters.

The other choices are incorrect because:

- Built-In InfoType Detector is wrong because it can be country-specific InfoTypes or Globally accepted InfoTypes like credit card details.
- Regular Custom InfoType Detector is wrong because it is a user-defined InfoType detector where it looks for a simple word list only.
- Stored Custom InfoType Detector is wrong because it is a user-defined InfoType detector where it looks for a list of words stored in BigQuery, it is a huge list.

https://cloud.google.com/dlp/docs/concepts-infotypes

### 21
Your organization is planning to migrate to Google Cloud Platform for all their IT operations. They are currently using  Active Directory to authenticate all employees within the entire company and have more than 50,000 users. They are concerned about migrating the identities from Active Directory to a system within GCP as it can be a time-consuming process, and they are not sure how to migrate additional employees who join the company during the migration to Google Cloud.  Which of the following is the most convenient way to migrate Active Directory identities to Google Cloud and maintain an up-to-date directory as new employees are hired? 

- [x] Use Google Cloud Directory Sync (GCDS) 

**Explanation**

Using GCDS, you can federate with an on-prem active directory. Google will map the same users from Active Directory to GCP using GCDS. Data is exported from the list of AD, then Google generates a list of users from Google Domain (Cloud Identity). After that comparison is made and updated to match the users. Any change in AD-like creating users or password change is done in one-way sync to Cloud Identity. AD is never updated.

Using the script you can migrate the users for one time but it won't be in sync, managing the syncing process manually would be an overhead.

SAML is used for exchanging identity data between two parties after authentication, it has nothing to do with the migration of identities. It is a way of authentication.

Cloud IAM manages the identity and authorization but it doesn’t involve migration from AD to Cloud Identity. Cloud Identity has a feature of GCDS that synchronizes the users.

https://cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction

### 22
Your client has four teams of engineers in their engineering department. Each team of engineers requires different assigned permissions to GCP services, and each team is working on applications with separate development and production environments. What is the best way to configure the team's folder and project structure to provide the appropriate level of isolation and enforce the principle of least privilege along with other GCP security practices? (Choose 2 answers)
- [x] Create a folder for the engineering department with subfolders for each engineering team containing each team's projects for its development and production environments.
- [x] Create an IAM Group for each engineering team and assign permissions at the project level.

**Explanation**

The two correct choices are 1) Create a folder for the engineering department with subfolders for each engineering team containing each team's projects for its development and production environments and 2) create an IAM Group for each engineering team and assign permissions at the project level.

The other choices are incorrect because:

- it is always recommended to create a separate project for each environment.
- assigning permissions at the folder level will give the same level of access for the users in the Development and Production environment. It is not recommended to give the same set of users access to the Production environment.
- you should always assign permissions to IAM Groups instead of individual users. However, this is not mandatory, it is only the best practice to perform.

https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations#define-hierarchy

### 23
A technical support team reports that when customers submit tickets through the company's online customer support site, some customers attach documents or pictures containing their personal information. All attachments to customer support tickets are stored in a customer support database for regular audits and reviews, and storing this personal information may lead to security risks. Which solution would a security engineer implement in order to mitigate this security risk, even if customers continue to attach sensitive data?

- [x] Use the Cloud Data Loss Prevention (DLP) Image Inspection and Redaction API to redact personal information before storing the ticket in the database.

**Explanation**

The Cloud Data Loss Prevention (DLP) Image Inspection and Redaction API is correct because we can use this technique and it will paste black or any colored slip on the PII Data and then it can be moved to the database.

Cloud Key Management Service (KMS) is incorrect because we cannot encrypt specific data from images. Either we can encrypt the whole image.

Cloud Storage Object Lifecycle Management is incorrect because this data is required for later audits so there is no scope deletion.

The Cloud Data Loss Prevention (DLP) Text Classification and Redaction API incorrect because here we are talking about image data, if we need to redact the textual data then we can use this technique.

https://cloud.google.com/dlp/docs/classification-redaction

### 24
You have uploaded 500 GB of important project files to a Cloud Storage bucket and added a retention policy of two years to the bucket without a retention policy lock. After one month, you realize you uploaded the same folder twice, which includes approximately 100 GB of data. You need to delete that redundant folder to avoid any unnecessary storage costs, but when you attempt to delete it you receive error messages that you have not reached the required retention period. In this case, what can you do in order to delete the folder and preserve the security of data stored in this bucket?

- [x] First, delete the retention policy and then delete the folder. Next, lock the bucket by adding a new retention policy.

**Explanation**

You have two separate factors to consider here, first locking the bucket using the retention policy - in this case deleting the retention policy will unlock the bucket. In another case, locking the bucket with the retention policy then locking the retention policy. In this case it won’t be possible to delete the retention policy, and hence you cannot delete the bucket until the retention policy is over.

The correct choice is right because you can delete the retention policy.

Disabling the policy is not an option, it must be deleted. Unlocking the bucket is not possible. You cannot unlock the bucket until the lock period is over.

The choice of using gsutil is wrong because you cannot do it using either console or gsutil command until you delete the retention policy.

https://cloud.google.com/storage/docs/bucket-lock

### 25
While many developers have permissions granting different levels of write access to resources within your dev/test environment, it is important to preserve specific resource configurations in this environment. Management insists the configuration of these resources should not be changed. Which of the following tools you can use in order to enforce these configurations?
- [x] Forseti

**Explanation**

Forseti is correct because it is a community-driven open-source security tool that allows the creation of rule-based policies. It consists of many modules, one of them is inventory which saves the snapshots of current GCP resources to Cloud SQL, another one is a scanner which regularly compares with policies defined to detect if any changes are made, another one is enforcer which compares the current state and desired state, if it doesn’t match, it will revert to the desired state.

The other choices are incorrect because:

Cloud Security Scanner is a web security scanner for common vulnerabilities for your apps running in CE, GAE, GKE. It doesn’t look into the configuration changes.

Security Command Center is wrong because it is a dashboard and analytics system for surfacing, understanding, and remediating security and data risks across organization. Again it doesn’t look into configuration changes. 

Cloud Logging can log any changes made but it won’t revert back the changes.

https://cloud.google.com/blog/products/identity-security/protecting-your-gcp-infrastructure-at-scale-with-forseti-config-validator

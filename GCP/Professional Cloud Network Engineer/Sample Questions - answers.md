# Answers

### 1
You are provisioning a brand new Partner Interconnect connection with your service provider. You establish connectivity with the service provider, then, in the GCP Project, you create VLAN attachments for a Partner Interconnect. Google and your service provider automatically set the correct BGP configurations for each VLAN attachment. Does this describe Layer 2 or Layer 3 connectivity, and why?
- [x] This is Layer 3 Connectivity because you do not need to configure BGP on your on-site routers.

**Explanation**

The correct answer is Layer 3 Connectivity because you do not need to configure BGP on your on-site routers. For layer 3 connections, the service provider establishes the BGP sessions. Google and the service provider automatically set configurations for the BGP sessions.
https://cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview

### 2
Which GCP Hybrid Connectivity service can connect your GCP and on-premise networks with the highest level of availability, the lowest level of latency, and the least potential points of network failure?
- [x] Dedicated Interconnect

**Explanation**

Cloud VPN can connect your on-premise and GCP networks, but does not offer the highest level of availability or least amount of latency. Partner Interconnect can also connect your on-premise and GCP networks, but has a higher number of potential points of failure than Dedicated Interconnect because the connection is made through a third-party service provider's co-location facility.

Carrier Peering is not intended as a hybrid connection between your on-premises network and GCP, but instead is an ideal connection between your on-premises network and G Suite applications through a connection point that only partially exposes your on-premises network.

https://cloud.google.com/interconnect/docs/concepts/dedicated-overview

### 3
Your organization's development team has requested access to Bigtable and BigQuery for a project hosted in Google Cloud VM instances. These services do not require the VMs to have external IP addresses and they will not need one. As the VPC network admin, what would be the best solution for configuring private API access for the services?
- [x] Enable Private Google Access for subnet containing the Cloud VMs.

**Explanation**
The correct solution for configuring private API access on the desired cloud VMs is to enable Private Google Access for subnet containing the Cloud VMs. The other configurations do not support the desired google services. The answer regarding API keys is irrelevant to this question.

https://cloud.google.com/vpc/docs/configure-private-google-access

### 4
While creating an ingress deny rule for a specific IP Address, you ran into a problem when you got to the source field. Cloud Console would not let you create the rule. Here is the IP address you were trying to enter as the source: 2001:db8:a0b:12f0::1. What went wrong?
- [x] Firewall rules only support IPv4 connections. You can only enter an IPv4 IP Address or an IPv4 block in CIDR notation.

**Explanation**

Firewall rules only support IPv4 connections. You can only enter an IPv4 IP Address or an IPv4 block in CIDR notation. The given IP Address is an IPv6 address.

https://cloud.google.com/vpc/docs/firewalls

### 5
You are the ‘owner’ of a GCP, and you decide to create a custom IAM role that gives all the permissions of a Role Admin minus the permission to delete roles. You would like for them to be able to create custom IAM roles. First, you will run a command to pull the metadata of the Role Admin role to get an accurate list of permissions. Then you will run a second command to create the new custom position. Which of the following sets of commands do you run in the gcloud console?
- [x]
  To get the permissions information, first run:
  ```
  gcloud iam roles describe roles/iam.roleAdmin
  ```
  Then run:
  ```
  gcloud iam roles create roleAdmin_custom --description= “have access to create custom roles” --permissions=iam.roles.create, iam.roles.get, iam.roles.list, iam.roles.update, resourcemanager.projects.get, resourcemanager.projects.getIamPolicy
  ```

**Explanation**

The correct commands are as follows:

To get the permissions information, first run:
```
gcloud iam roles describe roles/iam.roleAdmin
```
Then run:
```
gcloud iam roles create roleAdmin_custom --description= “have access to create custom roles” --permissions=iam.roles.create, iam.roles.get, iam.roles.list, iam.roles.update, resourcemanager.projects.get, resourcemanager.projects.getIamPolicy
```
The other answers, either invert the order of the commands, look up metadata for the wrong role, or included the delete permission the question indicates we did not want for this role.

https://cloud.google.com/iam/docs/creating-custom-roles

### 6
After a complaint of delays and slowness by some of your end-users. You pinged a few IPs in the affected region and discovered that there is some latency. Which two of the following strategies might optimize your load balancers and reduce the latency? (Choose 2 answers)

- [x] You could integrate with Cloud CDN to help with any cacheable content and to take advantage of TCP tuning.
- [x] Deploy web servers in multiple regions close to your users because HTTP(S) load balancing automatically directs users to the nearest region.

**Explanation**

Integrating with Cloud CDN to help with any cacheable content and to take advantage of TCP tuning is a plausible strategy for mitigating latency. Deploying web servers in multiple regions close to your users because HTTP(S) load balancing automatically directs users to the nearest region would also work. TCP Proxy or SSL Proxy load balancing typically increases latency compared to HTTP(S) load balancing. Having users move closer to their local routers does nothing to help the latency between the application servers and a regional IP.

https://cloud.google.com/load-balancing/docs/negs

### 7

You are using Cloud Interconnect to connect an on-premises network with a specific set of your company’s VPC networks. The organizational policy you have defined establishes that only these VPC networks can be used when creating a VLAN attachment using Dedicated Interconnect. Which constraint is best for this network requirement?
- [x] constraints/compute.restrictDedicatedInterconnectUsage

**Explanation**

The correct constrain to define the set of VPCs allowed to create an attachment using Dedicated Interconnect is: constraints/compute.restrictDedicatedInterconnectUsage The other options are real organizational policy constraints, but they do not fit the scenario.

https://cloud.google.com/resource-manager/docs/organization-policy/overview

### 8
There is one application that has been utilizing a lot of bandwidth - sending out large packets. This particular app attempts to control the TCP window size so that it can maximize its own performance, to the detriment of other services running on the same WM. Which Linux tunable below would you adjust to set the maximum OS send buffer size for all connections?
- [x] Net.core.wmem_max

**Explanation**

`Net.core.wmem_max` allows an admin with root access to set the send buffer size for all types of connections.

https://cloud.google.com/solutions/tcp-optimization-for-network-performance-in-gcp-and-hybrid


### 9
An engineer alerts you that a production application on a web server VM seems to be receiving updates from a development VM. The firewall log confirms that the production VM is receiving packets from the IP address of the development VM. You confirm that there is an ingress firewall rule that denies traffic with a target of the production VM, a source of the development VM, and a priority of 1000. Which of the following explanations would explain the problem?
- [x] There is another ingress firewall rule that allows traffic with a target of the production VM, a source of the development VM, a priority of 1.

**Explanation**

There is another ingress firewall rule that allows traffic with a target of the development VM, a source of the production VM, a priority of 1000. For an “allow” rule to override a “deny” rule, it must have a lower integer value for priority, indicating a higher priority rule, and the target and source machines for the ingress traffic must be identified properly, matching the situation in the question, “[a target of the production VM, a source of the development VM]”.
https://cloud.google.com/vpc/docs/using-firewalls

### 11
An app dev team has reached out to their IT department because they need access to VMs in us-west1 region and us-central1 region. They currently have an established VPN tunnel to us-west1, and they would like to gain additional access to the VMs in us-central1. They want a robust and reliable solution that can maintain their application’s availability in the event of a regional failure. The IT department offers to set up a second static connection to us-central1. However, the app dev team is concerned about maintaining multiple static routes that might be error-prone and disruptive to their workflow. Which Cloud Router routing configuration best resolves the request from the development team?

- [x] Global Dynamic Routing

**Explanation**

Global Dynamic Routing is the correct answer - with this configuration, Cloud Router has visibility in all connected regions and dynamically find new routes if a there is a connection problem in one region, traffic fails over to an alternate route in another region. Regional dynamic routing requires that each region connect back to the on-premise network directly. Static routing is better for smaller-scale, stable networks.

https://cloud.google.com/network-connectivity/docs/router/concepts/overview#redundant-tunnels

### 14
During your Cloud Router configuration, you receive the following error message while attempting to establish a BGP session: ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource: - Invalid value for field resource.bgp.asn: xxxxx. Local ASN conflicts with peer ASN specified by a router in the same region and network. What could this error message mean?
- [x] There might be an on-premise device that has the same ASN as the Cloud Router. Cloud Router will not be able to establish a BGP session until you change the ASN on one of the devices.

**Explanation**

The correct answer is “There might be an on-premise device that has the same ASN as the Cloud Router. Cloud Router will not be able to establish a BGP session until you change the ASN on one of the devices.” All of the other answers can cause routing issues, but they will not trigger this specific error message.
https://cloud.google.com/network-connectivity/docs/router/support/troubleshooting

### 24
Most of the users in your organization are working remotely. It is vital that their VPN connections to the on-site network resources are very reliable. Which of the following Cloud VPN strategies give the highest reliability?
- [x] Redundant routers and BGP sessions combined with on-premises devices that support grace restart.

**Explanation**

The best combination for VPN reliability is redundant routers and BGP sessions combined with on-premises devices that support grace restart. The other answers are either irrelevant to the VPN question or mutually incompatible configurations (e.g., BGP and static routing)
https://cloud.google.com/network-connectivity/docs/router/concepts/overview#redundant-tunnels

### 27
Remote engineers working on a vital project need a service-level availability well above 99% for their VPN Connection. Which of the two following statements are correct regarding a Cloud VPN configuration that provides this level of high availability? (Choose 2 answers)
- [x] If both sides of the VPN are properly configured Google Cloud gateways, high availability is guaranteed.
- [x] BGP routing must be supported on any VPN Gateway Devices.

**Explanation**

These two answers were wrong:

- If two peer devices are used, they must both be connected to the same HA VPN gateway
- The VPN gateway device will not meet the HA Requirements unless it supports static routing.

They should be:
- If two peer devices are used, each should be connected to a different VPN gateway interface.
- The VPN gateway device will not meet the HA Requirements unless it supports dynamic (BGP) routing.


https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview

### 34
You have recently migrated data to the Google Cloud Platform, and you are ready to connect your on-premise networks to Google Cloud. Review the requirements below and choose the best connection option. Guaranteed Network Availability and High Bandwidth: low Private Network connection: Not required Custom Routing: Not required Google Workspace Access: Required Budget to establish connection: None Which option fits the requirements best?
- [x] Direct Peering

**Explanation**

Direct Peering is the best choice. It is essentially free. Custom routing is not an option, and the connection is supported over the public internet rather than a private connection. Google Workspace applications are available to users.

https://cloud.google.com/network-connectivity/docs/direct-peering

### 35
You have a VLAN attachment on an active project. While building out a new project, you decide to set up a dedicated interconnect connection between the VLAN attachment and the new project. Look at the VLAN creation commands below. Which set of parameters below are required for a properly configured VLAN attachment for a successful connection to the new project VPC?
- [x]
  ```
  gcloud compute interconnects attachments dedicated create [VLAN_ATTACHMENT_NAME] \
    --region=[REGION] \
    --router=[ROUTER_NAME] \
    --project=[PROJECT_ID] \
    --interconnect=[INTERCONNECT_SELF_LINK] \
    --candidate-subnets=[CANDIDATE_SUBNETS] \
    --vlan=[VLAN_ID]
  ```

**Explanation**

The correct command includes all of the correct parameters for setting up a VLAN attachment. Other choices include incorrect values, such as  [ZONE] and [VPC] or missing vital parameters like VLAN and INTERCONNECT.

Additional link: https://cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/using-interconnects-other-projects

https://cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments

### 38
You've recently configured a new developer’s role in Cloud IAM. They've come back to you because they cannot access a resource they need to begin work. What three pieces of information do you need from the developer to troubleshoot their issue?
- [x] The Member (User’s Email), the Resource (The Full name of the Resource), and the Permission Needed

**Explanation**

Member, Resource, and Permission are the three pieces of data needed for troubleshooting access issues for users or service accounts. All of the incorrect options are various combinations of parameters used when granting roles in IAM.

Additional link: https://cloud.google.com/iam/docs/viewing-grantable-roles

https://cloud.google.com/iam/docs/troubleshooting-access

### 39
After receiving multiple user reports of “freezing” or “spinning” while trying to connect to a specific service through their browser, you were able to confirm that the VM the service was running on had gone down. However, you thought it was strange that no-one reports any error messages - they should have gotten a 502 Bad Gateway error. You suspect that a command used to create the service's backend configured health check's timeout so that customers would not receive an error message below. Which command could create this issue within the backend service?

- [x] `gcloud compute backend-services create backend-service-port3 \ --protocol http \ --port-name port3 \ --health-checks test-tcp-9000 \ --timeout = 600s --global`

**Explanation**

The create command that would have caused the issue described was this one:
```
gcloud compute backend-services create backend-service-prod1 \ --protocol http \ --port-name port003 \ --health-checks test-tcp-9000 \ --timeout = 600s --global
```
The timeout value has been set to 10 minutes, so many users would never see the error message. The other three options are all perfectly valid create commands.

https://cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-firewall-rules

### 40
You are creating a regional MIG with VMs in 3 zones. You would like to specify which zone the VMs will be created in. Which gcloud command would give you the desired MIG setup?
- [x] `gcloud compute instance-groups managed create example-rmig \ --template example-template \ --size 30 \ --zones us-east1-a,us-east1-b,us-east1-c`

**Explanation**

This configuration Is the only one that correctly creates a MIG with 3 named zones using the “--zones” flag.

gcloud compute instance-groups managed create example-rmig \ --template example-template \ --size 30 \ --zones us-east1-a,us-east1-b,us-east1-c 
https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups

### 43
Within your organization, there is a Business Manager position that exists in every department. Everyone with this job is supposed to have access to a specific set of software tools that nobody else needs. They are distributed, on different projects in different regions. What is the most efficient, accurate, and easily reversible way to go about giving all of those people access to those resources without giving them to those that do not need them?

- [x] Put the users into a “Business Manager” Google Group. Then give the permissions to the desired tools to the group.

**Explanation**

The Business Manager Solution is the most efficient, accurate, and reversible. Updating each account individually is the worst solution, and assigning service accounts is only slightly better. If you use the CSV import method, it is too easy to make mistakes that would affect many users, and tedious to reverse.

https://cloud.google.com/iam/docs/overview

### 46
You receive a request from an engineer to update his IAM role. He will be working within Cloud SQL, and he needs to be able to run queries and manipulate the data within the existing instance. Considering the policy of Least Privilege, which IAM role would be best suited for this Engineer?
- [x] Cloud SQL Editor

**Explanation**

The correct roll is Cloud SQL Editor. Editor and Cloud SQL Admin both allow too much privilege. Cloud SQL Client and Cloud SQL Viewer would not be enough privilege to complete the work.

https://cloud.google.com/iam/docs/permissions-reference





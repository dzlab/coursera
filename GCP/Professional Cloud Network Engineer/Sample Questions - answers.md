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

### 10
An executive is giving demonstrations of an application on-site at a conference. He has informed you that he will be using his laptop as he moves from meeting to meeting between rooms with different networks. He wants to know if he will need to begin a new session at every location since the IP addresses will change. You assure him that the current external load balancers provide session affinity that will mitigate any disruption. Which session affinity would make sure the executive remains within his active session as he moves between networks?

- [x] Generated cookie affinity

**Explanation**

Generated cookie affinity lets the load balancer recognize subsequent connections from that client instead of treating the connection as new. The load balancer generates a cookie upon the first request, and each request after with the same cookie is directed to the same backend VM.

https://cloud.google.com/load-balancing/docs/backend-service

### 11
An app dev team has reached out to their IT department because they need access to VMs in us-west1 region and us-central1 region. They currently have an established VPN tunnel to us-west1, and they would like to gain additional access to the VMs in us-central1. They want a robust and reliable solution that can maintain their application’s availability in the event of a regional failure. The IT department offers to set up a second static connection to us-central1. However, the app dev team is concerned about maintaining multiple static routes that might be error-prone and disruptive to their workflow. Which Cloud Router routing configuration best resolves the request from the development team?

- [x] Global Dynamic Routing

**Explanation**

Global Dynamic Routing is the correct answer - with this configuration, Cloud Router has visibility in all connected regions and dynamically find new routes if a there is a connection problem in one region, traffic fails over to an alternate route in another region. Regional dynamic routing requires that each region connect back to the on-premise network directly. Static routing is better for smaller-scale, stable networks.

https://cloud.google.com/network-connectivity/docs/router/concepts/overview#redundant-tunnels

### 12
You are troubleshooting SSH access for a user who is attempting to access a Linux instance. The user cannot connect to the instance using their project-wide public SSH keys. They are in the correct project, and they are only having trouble with this one instance. Which two of the following solutions might solve this user’s problem?
- [x] The user’s public SSH key must be added to the instance metadata.
- [x] Select the instance in the Cloud Console, and Under SSH Keys, clear “Block Project-wide SSH keys”

**Explanation**

5th answer: Make sure the user is a compute instance admin who has access to edit public SSH key metadata. This scenario points to an instance that is blocking project-wide public ssh keys. This issue can be resolved by either changing the setting for the instance in the Cloud Console or adding the user’s project-wide public SSH key to the metadata of the specified instance.

https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys#block-project-keys

### 13
You have established multiple static routes for the 192.168.168.0/24 destination. The current highest priority route has gone down. Which choice from the list below will Cloud Router select as the most likely next hop?

- [x] Priority is 750, and the next hop Cloud VPN tunnel is up.

**Explanation**

For Cloud Router to even consider a route, the next hop must be up. Once that is established, the next hop is chose based on priority. The lower the priority value, the higher the priority.

https://cloud.google.com/network-connectivity/docs/vpn/concepts/order-of-routes

### 14
During your Cloud Router configuration, you receive the following error message while attempting to establish a BGP session: ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource: - Invalid value for field resource.bgp.asn: xxxxx. Local ASN conflicts with peer ASN specified by a router in the same region and network. What could this error message mean?
- [x] There might be an on-premise device that has the same ASN as the Cloud Router. Cloud Router will not be able to establish a BGP session until you change the ASN on one of the devices.

**Explanation**

The correct answer is “There might be an on-premise device that has the same ASN as the Cloud Router. Cloud Router will not be able to establish a BGP session until you change the ASN on one of the devices.” All of the other answers can cause routing issues, but they will not trigger this specific error message.
https://cloud.google.com/network-connectivity/docs/router/support/troubleshooting

### 15
You have configured a network endpoint group specifically as a backend service for deploying containers on VMs. This also gives you granularity in distributing traffic to applications on the VM. This NEG works perfectly as a backend to an external HTTP(S) load balancer. Which type of network endpoint group have you configured?

- [x] Zonal Neg

**Explanation**

5th choice: TCP Proxy The Zonal NEG’s primary use case is deploying containers to VMs to run services in, and it allows granularity in traffic distribution to apps on the VM.It also works well as a backend to an External HTTP(S) load balancer.
https://cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts

### 16
You have configured your Cloud Routers for high availability. The Cloud Routers in us-central1 are advertising subnets in two different regions us-central1 and us-west1. VMs in each of the VPC Network regions learn about on-premises hosts automatically. How would you describe this Cloud Routing mode and configuration?
- [x] This represents Cloud Router Global Dynamic Routing

**Explanation**

Because the VMs in both regions can learn about the on-premises hosts automatically, this is dynamic routing. Because the Cloud Router has visibility in all regions is this Global Routing. This represents Cloud Router Global Dynamic Routing
https://cloud.google.com/network-connectivity/docs/router/concepts/overview

### 17
You have Endpoint-Independent Mapping enable on Cloud NAT, and you have deployed a TURN server for NAT traversal. How would you explain how a TURN server permits communication between two VMs behind NAT?

- [x] The VMs behind the NAT connect to the external IP address of a third server, and that server relays communication between the two VMs.

**Explanation**

TURN NAT traversal makes use of the external IP address of a third server to communicate behind NAT. STUN, not TURN, Traversal requires an open communication channel between the VMs. Permitting connections between existing VMs requires one to drain external IP addresses associated with NAT is true, but irrelevant to the topic of NAT traversal.

https://cloud.google.com/nat/docs/using-nat

### 18

During routine maintenance you are attempting to calculate network throughput on a single VM with iPerf3. The iPerf3 server and the cm are not able to connect to perform the test. Which of the following problems may be preventing the successful test?

- [x] The firewall rules must allow ingress and egress traffic to and from the VM.

**Explanation**

For iPerf3 to perform a throughput test on a VM, the firewalls on the VM need to be set to allow all ingress and egress traffic.

https://cloud.google.com/community/tutorials/network-throughput

### 19
You run the following command to customize the cache keys: gcloud compute backend-services update backend_service_dev1 \ --no-cache-key-include-protocol --cache-key-include-host \ --no-cache-key-include-query-string You follow up by viewing the logs to ensure that Cloud CDN is serving responses from the cache. Based on the change made to the cache keys by the command above, which of the following objects does not resolve to this cache key: “example.com/images/robot.jpg”?

- [x] https://example2.com/images/cat.jpg

**Explanation**

The URI https://example2.com/images/cat.jpg is the only choice that does not resolve to the specified cache key because the host was changed. In the others, only the protocol and the query string were adjusted.

https://cloud.google.com/cdn/docs/caching

### 20
You have created a Cloud Armor allowlisting rule intended to only allow IPs from a specified CIDR range access to external HTTP(S) Load balancers. You have not created a denylisting rule. Which of the following statements about your Cloud Armor rule are false?

- [x] Allowlisting rules automatically block any source IP address or CIDR range not defined in the rule.

**Explanation**

It is not true that allowlisting rules automatically block any source IP address or CIDR range not defined in the rule. There must be an accompanying Denylisting rule for any traffic to be blocked based on IP address or CIDR range.

https://cloud.google.com/armor/docs/security-policy-overview

### 21

A development team has launched a vital application on a regional managed instance group that must have nearly zero downtime. To ensure high availability, you now have to configure a global load balancer to direct HTTP traffic across multiple zones. After configuring the backend then the frontend of the load balancer, you click Review and Finalize. Assuming you have configured the load balancer correctly, what backend settings do you see upon review?

- [x] The Backend service is web-app-backend. The Endpoint protocol is HTTP. The Health check is web-app-load-balancer-check. The Instance group is load-balancing-web-app-group.

**Explanation**

Upon review, the backend setting for a high availability global load balancer to direct HTTP traffic across multiple zones will be as follows: The Backend service is web-app-backend. The Endpoint protocol is HTTP. The Health check is web-app-load-balancer-check. The Instance group is load-balancing-web-app-group. In the other answers, either the protocol is incorrect [TCP] or the Health Check and Instance Groups settings have been switched.

https://cloud.google.com/compute/docs/tutorials/high-availability-load-balancing#simulating_a_zonal_outage

### 22
You have set up VPC Flow Logs specifically for forensic analysis on a sensitive project. Based on current SLAs, your client requires that your team be able to produce the logs for up to two years after the timestamp of any action on this subnet. What steps should you take to ensure that the VPC flow logs are kept for at least 2 years?

- [x] The VPC Flow logs are only kept in Logging for 30 days. To keep them for any longer than that, they must be exported and stored elsewhere.

**Explanation**

The VPC Flow logs are only kept in Logging for 30 days. To keep them for any longer than that, they must be exported and stored elsewhere. This is not a configurable setting. The logs will be lost if not removed after 30 days. This has nothing to do with the sample rate.

https://cloud.google.com/vpc/docs/using-flow-logs

### 23
Your organization has deployed resources in a shared VPC. Now you need to peer it with another shared VPC that is used by a distributed team. The additional shared VPC will contain pooled resources for a large project. However, you quickly discover that peering between the shared VPCs as they are is impossible. What could have happened during the setup of these shared VPCs that would keep you from connecting them now?

- [x] The analyst who built the shared VPCs may have set them up as Auto Mode Shared VPCs. 

**Explanation**

Auto mode shared VPC subnets share the same set of default IP Address ranges, and network with overlapping IP address ranges cannot be connected through VPN or peering. To peer between shared VPCs, they must have been created in Custom Mode during setup with distinct IP Address ranges for subnets.

It is true that options to import and export custom routes when peering must be configured before any route exchanges will take place, but this is unrelated to the requirements for peering between VPCs.

https://cloud.google.com/vpc/docs/vpc#subnet-ranges

### 24
Most of the users in your organization are working remotely. It is vital that their VPN connections to the on-site network resources are very reliable. Which of the following Cloud VPN strategies give the highest reliability?
- [x] Redundant routers and BGP sessions combined with on-premises devices that support grace restart.

**Explanation**

The best combination for VPN reliability is redundant routers and BGP sessions combined with on-premises devices that support grace restart. The other answers are either irrelevant to the VPN question or mutually incompatible configurations (e.g., BGP and static routing)
https://cloud.google.com/network-connectivity/docs/router/concepts/overview#redundant-tunnels

### 25
You’ve just created a new Google Cloud Project and you have enabled the Cloud DNS API. For this VPC network, you have been asked to ensure that inbound DNS forwarding is permitted, and that outbound DNS forwarding is implemented on the same network. How would you go about handling this request?

- [x] Since the VPC Network cannot reference more than one DNS server policy, both the inbound DNS forwarding and the outbound DNS forwarding must be defined within one policy.

**Explanation**

The correct answer is: Since the VPC Network cannot reference more than one DNS server policy, both the inbound DNS forwarding and the outbound DNS forwarding must be defined within one policy. It is possible for a policy to be both an inbound and outbound policy if it implements both. An outbound DNS policy is just one method of implementing outbound DNS forwarding, but no other valid options were given in the answer choices.

https://cloud.google.com/dns/docs/overview#dns-server-policy

### 26
A customer-facing team would like to try out a new 3rd party tool. You need to configure a VPC firewall to allow VMs in that particular network to receive packets from a specific range of IPs. This firewall policy must only apply to this team and no one else at the organization. Which firewall configuration settings most closely align with the request?
- [x]
  Priority: 100
  Logs: On
  Direction of traffic: Ingress
  Action on match: Allow
  Source IP: [Specific range of IPs]

**Explanation**

The request specifies that this will be incoming traffic (Ingress), allow the traffic if it matches, and specify a source IP rather than a target IP.

https://cloud.google.com/vpc/docs/using-firewall-policies

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

### 28
You have been tasked with designing an aggressive disaster recovery plan for business-critical applications. You are specifically looking for something that will give you an RTO in minutes and an RPO that is nearly zero. Which disaster recovery plan below meets those requirements?

- [x]
  Database: Synchronous replication
  File Shares: Synchronous replication
  App Servers: Restore from a persistent disk snapshot

**Explanation**

The correct disaster recovery plan is:

Database: Synchronous replication

File Shares: Synchronous replication

App Servers: Restore from a persistent disk snapshot

This is the only plan that ensures the target systems and the source systems are both active and configured to the same size. This allows for almost immediate automatic failover to the recovery systems.

https://cloud.google.com/solutions/dr-scenarios-planning-guide

### 29
A security admin is configuring an ingress rule on the firewall for all VM instances on the network.  The new ingress rule should ensure that traffic from a specific project cannot access a designated VPC network. There are multiple ways to specify the source of traffic for an ingress rule. What two possible option can the security admin select to define the traffic’s source? (Choose 2 answers)

- [x] Source IP Ranges
- [x] Source Service Accounts

**Explanation**

IP Ranges and Service Accounts are two ways in which the source for an ingress rule can be defined. A third possible source is Source Tags, but this was not an option to select in this question.

Additional link: https://cloud.google.com/vpc/docs/using-firewalls

https://cloud.google.com/vpc/docs/firewalls#sources_or_destinations_for_the_rule

### 30
You run the command in the gcloud command-line tool to create a new VPC-native Kubernetes Cluster. It returns a Managed Instance Group error, and you suspect that there is not enough free space in the Pod IP Address range for the requested nodes. How would you fix this problem so the cluster can be created successfully?

- [x] You will need to replace the cluster. Go back over your planning, appropriately resizing the primary and secondary IP ranges. Then run the create command again.

**Explanation**

The only correct answer is “You will need to replace the cluster. Go back over your planning, appropriately resizing the primary and secondary IP ranges. Then run the create command again.” The other three answers describe solutions for other situations.

https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc

### 31
You are an administrator working on a project on a shared VPC network. The project (Project_1234) consists of three production instances (Prod_001, Prod_002, and Prod_003) and one development instance (DEV_001). You have an alert set in Cloud Monitoring that is supposed to email an alert to all network administrators when any of the three production environment VMs stay above 95% CPU usage for more than 5 minutes. Even though your logs confirm that this condition has been met on multiple occasions, no alerts have been issued from Cloud Monitoring. You need to adjust the configuration of the alert. Which configuration below will give you the desired result?

- [x]
  Resource type: VM Instance
  Metric: CPU Utilization project_id=”Project_1234” instance_name!=”DEV_0001”
  Period: 1 Minute
  Condition: is above
  Threshold: .95
  For: 5 Minutes

**Explanation**

The correct configuration is:

- Resource type: VM Instance
- Metric: CPU Utilization project_id=”Project_1234” instance_name!=”DEV_0001”
- Period: 1 Minute Condition: is above
- Threshold: .95
- For: 5 Minutes

The incorrect answers either had an incorrect value for the “instance_name” filter or configured the time for the condition threshold incorrectly. The “Period” field could be confusing because it designates the amount of time that data is collected for each data point, not the time threshold configuration for the condition.

https://cloud.google.com/logging

### 32
A network administrator for a particular VPC has noted that a service is pushing up against the CIDR block range for a given service. To resolve this issue, she will expand the CIDR range for this service. She runs the following command within the gcloud command-line tool: $ gcloud compute networks subnets expand-ip-range acmeco-hr-comp-eu-we1-dev --prefix-length=16 What is the outcome?
- [x] The IP range of the subnet acmeco-hr-comp-eu-we1-dev is expanded to /16.

**Explanation**

The IP range of the subnet acmeco-hr-comp-eu-we1-dev is expanded to /16 is the correct outcome. The subnet is acmeco-hr-comp-eu-we1-dev, and the --prefix-length= flag defines the new CIDR range.

https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/expand-ip-range

### 33
Your company is running a client-facing web application on Cloud Run, and you are tasked with enabling Cloud CDN for the service to optimize caching. What would be the best way to enable Cloud CDN for this application?
- [x] Run the gcloud compute backend-services update command for the service with the --enable-cdn flag.

**Explanation**

Running the gcloud compute backend-services update command for the service with the --enable-cdn flag is the correct way to enable Cloud CDN. One would not run the gcloud compute backend-services create command for an existing service.

https://cloud.google.com/cdn/docs/setting-up-cdn-with-bucket

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

### 36
An admin used gcloud to manually create all SSH keys for the team members on a specific project. During testing and configuration, you realize that all of the public SSH keys have been wiped out. Which action could have caused this?
- [x] A team member made an improperly specified API call.

**Explanation**

An improperly specified API call can wipe out the manually created SSH keys on a VM. This is why it is recommended to generate the keys with the Compute Engine tools if not up to the task of managing the keys. None of the other actions list would have deleted the SSH keys.

https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys#risks

### 37
The executives in your organization come to you as the network administrator because they believe that Google Cloud Premium Tier is not necessary for the company’s purposes. They are trying to make a final decision, and they want you to explain the difference between the load balancing options at the Premium Tier and what you would get at the Standard Tier. How would you best explain it?
- [x] The Standard Tier offers regional load balancing, while the Global tier offers the ability to deploy Global Load Balancing of any single anycast IPv4 or IPv6 IP.

**Explanation**

The Standard Tier offers regional load balancing, while the Global tier offers the ability to deploy Global Load Balancing of any single anycast IPv4 or IPv6 IP. Network load balancing requires a regional external IP at both tiers.
https://cloud.google.com/network-tiers#tab2

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

### 41

Due to a recent expansion in business, an application that had been running on a fixed number of instances with predictably efficient performance has started causing problems as tasks are being queued and users are reporting timeout errors. To solve this problem, you have configured the app engine with automatic scaling. Which of the following scenarios accurately describes how the automatically scaled instances are created and shut down as requests are received?
- [x] Instances are automatically created and turned down as needed to handle requests.

**Explanation**

When automatic scaling is on, Instances are automatically created and turned down as needed to handle requests. All of the other answers relate to either Manual or Basic scaling, not automatic scaling.

https://cloud.google.com/compute/docs/load-balancing-and-autoscaling

### 42
Your employer has decided to switch from your current DNS provider to Cloud DNS, and you have been tasked with migrating the existing domain to Cloud DNS. You have already created a managed zone to contain your DNS records. You also have the exported DNS configuration file in YAML records format from the current provider. What is the next step in the migration process?

- [x] The next step is to import the DNS configuration record sets into your managed zone. In the gcloud command-line tool, you will use the dns record-sets import command without the --zone-file-format flag.

**Explanation**

5th: The next step is to update your registrar’s name server records. You will do this by logging into your registrar provider and changing the authoritative name servers to point to the new ones. The next step after exporting the DNS configuration records from the current DNS provider is to import the DNS configuration record sets into your managed zone.

In the gcloud command-line tool, one will use the DNS record-sets import command without the --zone-file-format flag. The --zone-file-format flag is only necessary for BIND zone formatted record sets, otherwise YAML is the expected record-set format. The other answers are later steps in the migration process that cannot be completed until the configuration records have been imported into the correct managed zone.

https://cloud.google.com/dns/docs/migrating


### 43
Within your organization, there is a Business Manager position that exists in every department. Everyone with this job is supposed to have access to a specific set of software tools that nobody else needs. They are distributed, on different projects in different regions. What is the most efficient, accurate, and easily reversible way to go about giving all of those people access to those resources without giving them to those that do not need them?

- [x] Put the users into a “Business Manager” Google Group. Then give the permissions to the desired tools to the group.

**Explanation**

The Business Manager Solution is the most efficient, accurate, and reversible. Updating each account individually is the worst solution, and assigning service accounts is only slightly better. If you use the CSV import method, it is too easy to make mistakes that would affect many users, and tedious to reverse.

https://cloud.google.com/iam/docs/overview

### 44
Your company wants to set up a Partner Interconnect connection but has concerns about the availability and reliability of the service provider's network. What option will reduce your dependence on the service provider's network?
- [x] Establish your connection on Layer 2.

**Explanation**

For layer 2 connections, traffic passes through the service provider's network to reach the VPC or on-premises network. BGP is configured between the on-premises router and a Cloud Router in the VPC network, as shown in the following diagram:

For layer 3 connections, traffic is passed to the service provider's network, and then their network routes the traffic to the correct destination, either to the on-premises network or to the VPC network. Connectivity between the on-premises and service provider networks depends on the service provider. For example, they might request that you establish a BGP session with them or configure a static default route to their network.

https://cloud.google.com/interconnect/docs/concepts/partner-overview

### 45

You are configuring Cloud Router for a multi-NIC VM, and you note that every NIC gets a different route. Each Network Connectivity is creating custom dynamic routes in the VPC network. What has happened? What should you do?
- [x] This is working as it should. You do not need to fix anything.

**Explanation**

This is working as it should. You do not need to fix anything. Each NIC is configured in a unique VPC. The routes learned by one Cloud router are only for one NIC.

https://cloud.google.com/network-connectivity/docs/router/support/troubleshooting


### 46
You receive a request from an engineer to update his IAM role. He will be working within Cloud SQL, and he needs to be able to run queries and manipulate the data within the existing instance. Considering the policy of Least Privilege, which IAM role would be best suited for this Engineer?
- [x] Cloud SQL Editor

**Explanation**

The correct roll is Cloud SQL Editor. Editor and Cloud SQL Admin both allow too much privilege. Cloud SQL Client and Cloud SQL Viewer would not be enough privilege to complete the work.

https://cloud.google.com/iam/docs/permissions-reference

### 47
A project admin has reached out to you for help resolving a problem with the user accounts on a project. All of the users seem to have admin permissions on every service within the project, even things they are not working on. Users have been creating new instances and accessing folders that should be behind firewalls. Nothing about their permissions has changed since the beginning of the project, but they seem to automatically have access to even brand new projects that they could not have been given IAM roles for. Which of the following scenarios could cause what the project admin is experiencing?
- [x] The users have all been granted the Service Account User role at the project level.

**Explanation**

Users who have been granted the Service Account User role can indirectly access anything to which the service account has access. Users with the Service Account User role at the project level have access to all service accounts in the project and everything to which those service accounts have access.

https://cloud.google.com/solutions/best-practices-vpc-design

### 48
The network administrator has asked you to migrate a DNSSEC-signed zone to Cloud DNS. You realize before you get too far into the process that Cloud DNS does not support the same KSK algorithm that is currently in use. How will you safely, and properly migrate the zone to Cloud DNS?

- [x] Deactivate the DNSSEC at the domain registrar before you migrate the zone and update the name server records to us Cloud DNS.

**Explanation**

The only correct answer is “Deactivate the DNSSEC at the domain registrar before you migrate the zone and update the name server records to us Cloud DNS.” The other answers are just parts of later steps in the process. The only way to properly migrate the signed zone is to deactivate DNSSEC first.

https://cloud.google.com/dns/docs/dnssec-config#migrating

### 49
The network admin runs the following command in the gcloud command-line tool to create a new VPC network: gcloud compute networks create sampleco-prod-1 \ --subnet-mode=auto \ --bgp-routing-mode=global \ --mtu=1460 Which two of the following IP addresses would be available within VPC subnets automatically created by this command? (Choose 2 answers)

- [x] 10.255.4.68
- [x] 10.172.4.82

**Explanation**

The correct responses were: 10.255.4.68 and 10.172.4.82

When a VPC network is created in auto mode, IP ranges for the automatically created subnets fit within the 10.128.0.0/9 CIDR block.

https://cloud.google.com/vpc/docs/vpc

### 50
Your organization has partially migrated to the cloud, and many of your servers are maintained in an on-premises data center. You have noticed increased throughput latency when application components on the cloud and the corporate data center communicate. You have confirmed that load balancers are in place and configured correctly. How might you adjust the configuration of this hybrid environment to minimize latency and improve application performance?

- [x] Enable window-size scaling from the command line to increase bandwidth.

**Explanation**

Due to legacy uses of TCP, TCP window size - the amount of data that can be sent at once might be configured too conservatively. Increasing this window size can dramatically improve bandwidth. Enabling Round-Trip Time optimization is incorrect because RTT is a fixed value in this scenario. Doing nothing hints at the legacy application of TCP but is incorrect when using modern hardware.

https://cloud.google.com/solutions/tcp-optimization-for-network-performance-in-gcp-and-hybrid

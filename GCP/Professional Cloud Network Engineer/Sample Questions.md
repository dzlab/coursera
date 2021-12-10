# Questions

### 1
You are provisioning a brand new Partner Interconnect connection with your service provider. You establish connectivity with the service provider, then, in the GCP Project, you create VLAN attachments for a Partner Interconnect. Google and your service provider automatically set the correct BGP configurations for each VLAN attachment. Does this describe Layer 2 or Layer 3 connectivity, and why?
- [ ] This is Layer 3 Connectivity because you do not need to configure BGP on your on-site routers.
- [ ] This is Layer 2 Connectivity because you do not need to configure BGP on your on-site routers.
- [ ] This is Layer 3 Connectivity because you must configure and establish BGP sessions between your on-site routers and the Cloud Routers.
- [ ] This is Layer 2 Connectivity because you must configure and establish BGP sessions between your on-site routers and the Cloud Routers.


### 2
Which GCP Hybrid Connectivity service can connect your GCP and on-premise networks with the highest level of availability, the lowest level of latency, and the least potential points of network failure?
- [ ] Dedicated Interconnect
- [ ] Cloud VPN
- [ ] Partner Interconnect
- [ ] Carrier Peering

### 3
Your organization's development team has requested access to Bigtable and BigQuery for a project hosted in Google Cloud VM instances. These services do not require the VMs to have external IP addresses and they will not need one. As the VPC network admin, what would be the best solution for configuring private API access for the services?
- [ ] Enable Private Google Access for subnet containing the Cloud VMs.
- [ ] Enable Private Services Access for subnet containing the Cloud VMs.
- [ ] Enable Serverless VPC Access for the subnet containing the Cloud VMs.
- [ ] Enable the API for the desired services in the Cloud VM, and ensure that each user has access to enable the API. Then create an API key.

### 4
While creating an ingress deny rule for a specific IP Address, you ran into a problem when you got to the source field. Cloud Console would not let you create the rule. Here is the IP address you were trying to enter as the source: 2001:db8:a0b:12f0::1. What went wrong?
- [ ] Each firewall rule applies to either ingress or egress connection. You cannot have both in the same rule.
- [ ] Firewall rules only support IPv4 connections. You can only enter an IPv4 IP Address or an IPv4 block in CIDR notation.
- [ ] Each firewall rule is either an allow or deny action. You cannot have both in the same rule.
- [ ] Denying associated response traffic in a firewall rule is not permitted.

### 5
You are the ‘owner’ of a GCP, and you decide to create a custom IAM role that gives all the permissions of a Role Admin minus the permission to delete roles. You would like for them to be able to create custom IAM roles. First, you will run a command to pull the metadata of the Role Admin role to get an accurate list of permissions. Then you will run a second command to create the new custom position. Which of the following sets of commands do you run in the gcloud console?
- [ ] 
    To get the permissions information, first run:
    ```
    gcloud iam roles describe roles/iam.roleAdmin
    ```
    Then run:
    ```
    gcloud iam roles create roleAdmin_custom --description= “have access to create custom roles” --permissions=iam.roles.create, iam.roles.get, iam.roles.list, iam.roles.update, resourcemanager.projects.get, resourcemanager.projects.getIamPolicy
    ```
- [ ]
    To get the permissions information, first run:
    ```
    gcloud iam roles describe roles/owner
    ```
    Then run:
    ```
    gcloud iam roles create roleAdmin_custom --description= “have access to create custom roles” --permissions=iam.roles.create, iam.roles.delete, iam.roles.get, iam.roles.list, iam.roles.update, resourcemanager.projects.get, resourcemanager.projects.getIamPolicy
    ```
- [ ]
    To get the permissions information, first run:
    ```
    gcloud iam roles create roleAdmin_custom --description= “have access to create custom roles” --permissions=iam.roles.create, iam.roles.get, iam.roles.list, iam.roles.update, resourcemanager.projects.get, resourcemanager.projects.getIamPolicy
    ```
    Then run:
    ```
    gcloud iam roles describe roles/iam.roleAdmin
    ```
- [ ]
    To get the permissions information, first run:
    ```
    gcloud iam roles describe roles/iam.roleViewer
    ```
    Then run:
    ```
    gcloud iam roles create roleAdmin_custom --description= “have access to create custom roles” --permissions=iam.roles.create, iam.roles.get, iam.roles.list, iam.roles.update, resourcemanager.projects.get, resourcemanager.projects.getIamPolicy
    ```

### 6
After a complaint of delays and slowness by some of your end-users. You pinged a few IPs in the affected region and discovered that there is some latency. Which two of the following strategies might optimize your load balancers and reduce the latency? (Choose 2 answers)
- [ ] You could integrate with Cloud CDN to help with any cacheable content and to take advantage of TCP tuning.
- [ ] Deploy web servers in multiple regions close to your users because HTTP(S) load balancing automatically directs users to the nearest region.
- [ ] Use TCP Proxy or SSL Proxy load balancing if possible.
- [ ] Have your users close unnecessary tabs and move closer to their routers.

### 7
You are using Cloud Interconnect to connect an on-premises network with a specific set of your company’s VPC networks. The organizational policy you have defined establishes that only these VPC networks can be used when creating a VLAN attachment using Dedicated Interconnect. Which constraint is best for this network requirement?
- [ ] constraints/compute.restrictDedicatedInterconnectUsage
- [ ] constraints/compute.restrictPartnerInterconnectUsage
- [ ] constraints/compute.restrictVpnPeerIPs
- [ ] constraints/compute.vmExternalIpAccess

### 8
There is one application that has been utilizing a lot of bandwidth - sending out large packets. This particular app attempts to control the TCP window size so that it can maximize its own performance, to the detriment of other services running on the same WM. Which Linux tunable below would you adjust to set the maximum OS send buffer size for all connections?
- [ ] Net.core.rmem_max
- [ ] Net.core.wmem_max
- [ ] net.ipv4.tcp_rmem
- [ ] net.ipv4.tcp_wmem

### 9
An engineer alerts you that a production application on a web server VM seems to be receiving updates from a development VM. The firewall log confirms that the production VM is receiving packets from the IP address of the development VM. You confirm that there is an ingress firewall rule that denies traffic with a target of the production VM, a source of the development VM, and a priority of 1000. Which of the following explanations would explain the problem?
- [ ] There is another ingress firewall rule that allows traffic with a target of the production VM, a source of the development VM, and a priority of 1000.
- [ ] There is another ingress firewall rule that allows traffic with a target of the production VM, a source of the development VM, and a priority of 1001.
- [ ] There is another ingress firewall rule that denies traffic with a target of the production VM, a source of the development VM, and a priority of 1.
- [ ] There is another ingress firewall rule that allows traffic with a target of the production VM, a source of the development VM, a priority of 1.

### 10
An executive is giving demonstrations of an application on-site at a conference. He has informed you that he will be using his laptop as he moves from meeting to meeting between rooms with different networks. He wants to know if he will need to begin a new session at every location since the IP addresses will change. You assure him that the current external load balancers provide session affinity that will mitigate any disruption. Which session affinity would make sure the executive remains within his active session as he moves between networks?
- [ ] Client IP Affinity
- [ ] Generated cookie affinity
- [ ] Header field affinity
- [ ] Port and protocol affinity

### 11
An app dev team has reached out to their IT department because they need access to VMs in us-west1 region and us-central1 region. They currently have an established VPN tunnel to us-west1, and they would like to gain additional access to the VMs in us-central1. They want a robust and reliable solution that can maintain their application’s availability in the event of a regional failure. The IT department offers to set up a second static connection to us-central1. However, the app dev team is concerned about maintaining multiple static routes that might be error-prone and disruptive to their workflow. Which Cloud Router routing configuration best resolves the request from the development team?
- [ ] Global Static Routing
- [ ] Regional Dynamic Routing
- [ ] Global Dynamic Routing
- [ ] Regional Static Routing

### 12
You are troubleshooting SSH access for a user who is attempting to access a Linux instance. The user cannot connect to the instance using their project-wide public SSH keys. They are in the correct project, and they are only having trouble with this one instance. Which two of the following solutions might solve this user’s problem?
- [ ] The user’s public SSH key must be added to the instance metadata.
- [ ] Select the instance in the Cloud Console, and Under SSH Keys, clear “Block Project-wide SSH keys”
- [ ] Select the instance in the Cloud Console, and Under SSH Keys, select “Block Project-wide SSH keys”
- [ ] The user’s project-wide public SSH key must be removed from the instance metadata.

### 13
You have established multiple static routes for the 192.168.168.0/24 destination. The current highest priority route has gone down. Which choice from the list below will Cloud Router select as the most likely next hop?
- [ ] Priority is 1000, and the next hop Cloud VPN tunnel is up.
- [ ] Priority is 750, and the next hop Cloud VPN tunnel is up.
- [ ] Priority is 300, and the next hop Cloud VPN tunnel is down.
- [ ] Priority is 1000, and the next hop Cloud VPN tunnel is down.

### 14
During your Cloud Router configuration, you receive the following error message while attempting to establish a BGP session: ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource: - Invalid value for field resource.bgp.asn: xxxxx. Local ASN conflicts with peer ASN specified by a router in the same region and network. What could this error message mean?
- [ ] There might be an on-premise device that has the same ASN as the Cloud Router. Cloud Router will not be able to establish a BGP session until you change the ASN on one of the devices.
- [ ] You have likely attempted to use an external IP address for the BGP Session. You can only use link-local IP addresses for BGP sessions.
- [ ] You might have two Cloud Routers with the same ASN. iBGP between two Cloud Routers with the same ASN is not supported.
- [ ] You likely have IP ranges for a VPC subnet that are overlapping with route advertisements from your on-premise network. Routes can be dropped if you have overlapping IP ranges.

### 15
You have configured a network endpoint group specifically as a backend service for deploying containers on VMs. This also gives you granularity in distributing traffic to applications on the VM. This NEG works perfectly as a backend to an external HTTP(S) load balancer. Which type of network endpoint group have you configured?
- [ ] Internet NEG
- [ ] Serverless NEG
- [ ] Zonal Neg
- [ ] SSL Proxy

### 16
You have configured your Cloud Routers for high availability. The Cloud Routers in us-central1 are advertising subnets in two different regions us-central1 and us-west1. VMs in each of the VPC Network regions learn about on-premises hosts automatically. How would you describe this Cloud Routing mode and configuration?
- [ ] This represents Cloud Router Global Dynamic Routing
- [ ] This represents Cloud Router Regional Dynamic Routing
- [ ] This represents Cloud Router Global Static Routing
- [ ] This represents Cloud Router Regional Static Routing

### 17
You have Endpoint-Independent Mapping enable on Cloud NAT, and you have deployed a TURN server for NAT traversal. How would you explain how a TURN server permits communication between two VMs behind NAT?
- [ ] The VMs behind the NAT connect to the external IP address of a third server, and that server relays communication between the two VMs.
- [ ] Once a communication channel is established, TURN allows direct communication between the VMs behind NAT.
- [ ] The VMs behind the NAT connect to the internal IP address of a third server, and that server relays communication to external clients.
- [ ] Permitting connections between existing VMs requires one to drain external IP addresses associated with NAT.

### 18
During routine maintenance you are attempting to calculate network throughput on a single VM with iPerf3. The iPerf3 server and the cm are not able to connect to perform the test. Which of the following problems may be preventing the successful test?
- [ ] Likely, the snapshot length is too high. Capture headers with a lower snapshot length value, like -s 100.
- [ ] The firewall rules must allow ingress and egress traffic to and from the VM.
- [ ] On the Linux VM Increase net.core.rmem_default and net.core.rmem_max to increase the size of the TCP window.
- [ ] CPU throttling can limit the test. Use the -P flag to launch multiple client streams.

### 19
You run the following command to customize the cache keys: gcloud compute backend-services update backend_service_dev1 \ --no-cache-key-include-protocol --cache-key-include-host \ --no-cache-key-include-query-string You follow up by viewing the logs to ensure that Cloud CDN is serving responses from the cache. Based on the change made to the cache keys by the command above, which of the following objects does not resolve to this cache key: “example.com/images/robot.jpg”?
- [ ] https://example2.com/images/cat.jpg
- [ ] https.example.com/images/cat.jpg?user=user001
- [ ] http://example.com/images/cat.jpg
- [ ] example.com/images/cat.jpg?user=user001

### 20
You have created a Cloud Armor allowlisting rule intended to only allow IPs from a specified CIDR range access to external HTTP(S) Load balancers. You have not created a denylisting rule. Which of the following statements about your Cloud Armor rule are false?
- [ ] Allowlisting rules enable you to allow specific source IP addresses or CIDR ranges to access external HTTP(S) load balancers.
- [ ] IPv4 and IPv6 addresses are supported in allowlist rules
- [ ] Deny rules can return HTTP 403, 404, or 502 responses.
- [ ] Allowlisting rules automatically block any source IP address or CIDR range not defined in the rule.

### 21
A development team has launched a vital application on a regional managed instance group that must have nearly zero downtime. To ensure high availability, you now have to configure a global load balancer to direct HTTP traffic across multiple zones. After configuring the backend then the frontend of the load balancer, you click Review and Finalize. Assuming you have configured the load balancer correctly, what backend settings do you see upon review?
- [ ] The Backend service is web-app-backend. The Endpoint protocol is HTTP. The Health check is web-app-load-balancer-check. The Instance group is load-balancing-web-app-group.
- [ ] The Backend service is web-app-backend. The Endpoint protocol is TCP. The Health check is load-balancing-web-app-group. The Instance group is web-app-load-balancer-check.
- [ ] The Backend service is web-app-backend. The Endpoint protocol is HTTP. The Health check is load-balancing-web-app-group. The Instance group is web-app-load-balancer-check.
- [ ] The Backend service is web-app-backend. The Endpoint protocol is TCP. The Health check is web-app-load-balancer-check. The Instance group is load-balancing-web-app-group.

### 22
You have set up VPC Flow Logs specifically for forensic analysis on a sensitive project. Based on current SLAs, your client requires that your team be able to produce the logs for up to two years after the timestamp of any action on this subnet. What steps should you take to ensure that the VPC flow logs are kept for at least 2 years?
- [ ] The VPC Flow logs are only kept in Logging for 30 days. To keep them for any longer than that, they must be exported and stored elsewhere.
- [ ] The VPC Flow logs storing and collection are a configurable setting. In the Google Cloud Console, you would change the “Log Expire after” setting to 24 months.
- [ ] VPC Flow logs are stored until they are manually deleted.
- [ ] VPC Flow logs are sampled. By changing the sample rate to 1.0, 100% of the logs are kept.

### 23
Your organization has deployed resources in a shared VPC. Now you need to peer it with another shared VPC that is used by a distributed team. The additional shared VPC will contain pooled resources for a large project. However, you quickly discover that peering between the shared VPCs as they are is impossible. What could have happened during the setup of these shared VPCs that would keep you from connecting them now?
- [ ] The analyst who built the shared VPCs may have set them up as Custom Mode Shared VPCs. 
- [ ] The options to import and export custom routes when peering must be configured before any route exchanges will take place between shared networks.
- [ ] One or both of the shared VPCs has not met the minimum number of service projects required for peering.
- [ ] The analyst who built the shared VPCs may have set them up as Auto Mode Shared VPCs. 

### 24
Most of the users in your organization are working remotely. It is vital that their VPN connections to the on-site network resources are very reliable. Which of the following Cloud VPN strategies give the highest reliability?
- [ ] Redundant routers and BGP sessions combined with on-premises devices that support grace restart.
- [ ] Static routing for Cloud VPN Tunnels combined with Cloud Interconnect.
- [ ] Each device is connected to its own VPN gateway interface.
- [ ] Static routing combined with BGP sessions.

### 25
You’ve just created a new Google Cloud Project and you have enabled the Cloud DNS API. For this VPC network, you have been asked to ensure that inbound DNS forwarding is permitted, and that outbound DNS forwarding is implemented on the same network. How would you go about handling this request?
- [ ] Since the VPC Network cannot reference more than one DNS server policy, both the inbound DNS forwarding and the outbound DNS forwarding must be defined within one policy.
- [ ] Since no more than one definition can be included in a single DNS server policy, the inbound DNS forwarding and the outbound DNS forwarding must be defined in separate policies.
- [ ] Since the VPC Network cannot reference more than one DNS server policy, you would only define the outbound DNS forwarding policy. The inbound DNS forwarding would then need to be configured separately.
- [ ] Since no more than one definition can be included in a single DNS server policy, Cloud DNS uses an internal IP from the primary IP address range of a subnet in your VPC network. These are used as entry points for inbound requests.

### 26
A customer-facing team would like to try out a new 3rd party tool. You need to configure a VPC firewall to allow VMs in that particular network to receive packets from a specific range of IPs. This firewall policy must only apply to this team and no one else at the organization. Which firewall configuration settings most closely align with the request?
- [ ]
  - Priority: 100
  - Logs: On
  - Direction of traffic: Ingress
  - Action on match: Allow
  - Target IP: [Specific range of IPs]
- [ ]
  - Priority: 100
  - Logs: On
  - Direction of traffic: Ingress
  - Action on match: Allow
  - Source IP: [Specific range of IPs]
- [ ]
  - Priority: 100
  - Logs: On
  - Direction of traffic: Egress
  - Action on match: Deny
  - Target IP: [Specific range of IPs]
- [ ]
  - Priority: 100
  - Logs: Off
  - Direction of traffic: Egress
  - Action on match: Allow
  - Source IP: [Specific range of IPs]

### 27
Remote engineers working on a vital project need a service-level availability well above 99% for their VPN Connection. Which of the two following statements are correct regarding a Cloud VPN configuration that provides this level of high availability? (Choose 2 answers)
- [ ] If both sides of the VPN are properly configured Google Cloud gateways, high availability is guaranteed.
- [ ] If two peer devices are used, they must both be connected to the same high availability VPN gateway.
- [ ] The VPN gateway device will not meet the HA Requirements unless it supports static routing.
- [ ] BGP routing must be supported on any VPN Gateway Devices.

### 28
You have been tasked with designing an aggressive disaster recovery plan for business-critical applications. You are specifically looking for something that will give you an RTO in minutes and an RPO that is nearly zero. Which disaster recovery plan below meets those requirements?
- [ ]
  - Database: Backup/restore
  - File Shares: Backup/restore
  - App Servers: Restore from a persistent disk snapshot
- [ ]
  - Database: Synchronous replication 
  - File Shares: Backup/restore
  - App Servers: Restore from a persistent disk snapshot
- [ ]
  - Database: Backup/restore
  - File Shares: Asynchronous replication
  - App Servers: Restore from a persistent disk snapshot
- [ ]
  - Database: Synchronous replication
  - File Shares: Synchronous replication
  - App Servers: Restore from a persistent disk snapshot

### 29
A security admin is configuring an ingress rule on the firewall for all VM instances on the network.  The new ingress rule should ensure that traffic from a specific project cannot access a designated VPC network. There are multiple ways to specify the source of traffic for an ingress rule. What two possible option can the security admin select to define the traffic’s source? (Choose 2 answers)
- [ ] Source IP Ranges
- [ ] Source VM Names
- [ ] Source SSL Certificate
- [ ] Source Service Accounts

### 30
You run the command in the gcloud command-line tool to create a new VPC-native Kubernetes Cluster. It returns a Managed Instance Group error, and you suspect that there is not enough free space in the Pod IP Address range for the requested nodes. How would you fix this problem so the cluster can be created successfully?
- [ ] You will need to replace the cluster. Go back over your planning, appropriately resizing the primary and secondary IP ranges. Then run the create command again.
- [ ] Another VPC-native cluster is being created at the same time. Retry the creation command.
- [ ] If the Pod range is not included in your Cloud NAT configuration, you will need to update the Cloud NAT configuration and retry to the creation command.
- [ ] If the Kubernetes Engine API is enabled, and you still get this error, that probably means that the host projects service account has been deleted. You will have to disable and re-enable the API to correct the issue.

### 31
You are an administrator working on a project on a shared VPC network. The project (Project_1234) consists of three production instances (Prod_001, Prod_002, and Prod_003) and one development instance (DEV_001). You have an alert set in Cloud Monitoring that is supposed to email an alert to all network administrators when any of the three production environment VMs stay above 95% CPU usage for more than 5 minutes. Even though your logs confirm that this condition has been met on multiple occasions, no alerts have been issued from Cloud Monitoring. You need to adjust the configuration of the alert. Which configuration below will give you the desired result?
- [ ]
  - Resource type: VM Instance
  - Metric: CPU Utilization project_id=”Project_1234” instance_name!=”DEV_0001”
  - Period: 1 Minute
  - Condition: is above
  - Threshold: .95
  - For: 5 Minutes
- [ ]
  - Resource type: VM Instance
  - Metric: CPU Utilization project_id=”Project_1234” instance_name=”DEV_0001”
  - Period: 5 Minute
  - Condition: is above
  - Threshold: .95
  - For: most recent value
- [ ]
  - Resource type: VM Instance
  - Metric: CPU Utilization project_id=”Project_1234” instance_name!=”DEV_0001”
  - Period: 1 Minute
  - Condition: is below
  - Threshold: .05
  - For: most recent value
- [ ]
  - Resource type: VM Instance
  - Metric: CPU Utilization project_id=”Project_1234” instance_name=[Prod_001, Prod_002, and Prod_003]
  - Period: 1 Minute
  - Condition: is above
  - Threshold: .95
  - For: 5 Minutes

### 32
A network administrator for a particular VPC has noted that a service is pushing up against the CIDR block range for a given service. To resolve this issue, she will expand the CIDR range for this service. She runs the following command within the gcloud command-line tool: $ gcloud compute networks subnets expand-ip-range acmeco-hr-comp-eu-we1-dev --prefix-length=16 What is the outcome?
- [ ] The IP range of the subnet acmeco-hr-comp-eu-we1-dev is expanded to /16.
- [ ] The IP range of the subnet networks is expanded to /16.
- [ ] The IP range of the subnet acmeco-hr-comp-eu-we1-dev is expanded to /24.
- [ ] The IP range of the subnet acmeco is expanded to /8.

### 33
Your company is running a client-facing web application on Cloud Run, and you are tasked with enabling Cloud CDN for the service to optimize caching. What would be the best way to enable Cloud CDN for this application?
- [ ] Run the gcloud compute backend-services update command for the service with the --enable-cdn flag.
- [ ] Run the gcloud compute backend-services create command for the service with the --no-enable-cdn flag.
- [ ] Run the gcloud compute backend-services update command for the service with the --no-enable-cdn flag.
- [ ] Run the gcloud compute backend-services create command for the service with the --enable-cdn flag.

### 34
You have recently migrated data to the Google Cloud Platform, and you are ready to connect your on-premise networks to Google Cloud. Review the requirements below and choose the best connection option. Guaranteed Network Availability and High Bandwidth: low Private Network connection: Not required Custom Routing: Not required Google Workspace Access: Required Budget to establish connection: None Which option fits the requirements best?
- [ ] Direct Peering
- [ ] Carrier Peering
- [ ] Dedicated Interconnect
- [ ] Partner Interconnect

### 35
You have a VLAN attachment on an active project. While building out a new project, you decide to set up a dedicated interconnect connection between the VLAN attachment and the new project. Look at the VLAN creation commands below. Which set of parameters below are required for a properly configured VLAN attachment for a successful connection to the new project VPC?
- [ ] 
```
gcloud compute interconnects attachments dedicated create [VLAN_ATTACHMENT_NAME] \
    --region=[REGION] \
    --router=[ROUTER_NAME] \
    --VPC=[VPC_ID] \
    --interconnect=[INTERCONNECT_SELF_LINK] \
    --candidate-subnets=[CANDIDATE_SUBNETS] \
    --vlan=[VLAN_ID]
```

- [ ] 
```
gcloud compute interconnects attachments dedicated create [VLAN_ATTACHMENT_NAME] \
    --region=[REGION] \
    --router=[ROUTER_NAME] \
    --project=[PROJECT_ID] \
    --interconnect=[INTERCONNECT_SELF_LINK] \
    --candidate-subnets=[CANDIDATE_SUBNETS] \
    --vlan=[VLAN_ID]
```

- [ ] 
```
gcloud compute interconnects attachments dedicated create [VLAN_ATTACHMENT_NAME] \
    --zone=[ZONE] \
    --router=[ROUTER_NAME] \
    --VPC=[VPC_ID] \
    --interconnect=[INTERCONNECT_SELF_LINK] \
    --candidate-subnets=[CANDIDATE_SUBNETS] \
    --vlan=[VLAN_ID]
```

- [ ] 
```
gcloud compute interconnects attachments dedicated create [VLAN_ATTACHMENT_NAME] \
    --region=[REGION] \
    --router=[ROUTER_NAME] \
    --project=[PROJECT_ID] \
    --candidate-subnets=[CANDIDATE_SUBNETS] \
```


### 36
An admin used gcloud to manually create all SSH keys for the team members on a specific project. During testing and configuration, you realize that all of the public SSH keys have been wiped out. Which action could have caused this?
- [ ] A team member made an improperly specified API call.
- [ ] The SSH key directory has been moved.
- [ ] The admin who made the SSH keys did not have the correct permissions to create the SSH keys.
- [ ] The team did not use the keys before they expired.

### 37
The executives in your organization come to you as the network administrator because they believe that Google Cloud Premium Tier is not necessary for the company’s purposes. They are trying to make a final decision, and they want you to explain the difference between the load balancing options at the Premium Tier and what you would get at the Standard Tier. How would you best explain it?
- [ ] The Standard Tier offers regional load balancing, while the Global tier offers the ability to deploy Global Load Balancing of any single anycast IPv4 or IPv6 IP.
- [ ] The Premium Tier offers regional load balancing, while the Standard tier offers the ability to deploy Global Load Balancing of any single anycast IPv4 or IPv6 IP.
- [ ] Network load balancing at the Premium Tier requires a regional external IP address, while network load balancing at the Standard Tier does not.
- [ ] Network load balancing at the Standard Tier requires a regional external IP address, while network load balancing at the Premium Tier does not.

### 38
You've recently configured a new developer’s role in Cloud IAM. They've come back to you because they cannot access a resource they need to begin work. What three pieces of information do you need from the developer to troubleshoot their issue?
- [ ] The Project-id, IAM Policy, and Role-id
- [ ] The Role-id, Resource (Full Name of the Resource), and Group
- [ ] The Member (User’s Email), the Resource (The Full name of the Resource), and the Permission Needed
- [ ] The IAM Policy, the Permission Needed, and the Resource (The Full name of the Resource)

### 39
After receiving multiple user reports of “freezing” or “spinning” while trying to connect to a specific service through their browser, you were able to confirm that the VM the service was running on had gone down. However, you thought it was strange that no-one reports any error messages - they should have gotten a 502 Bad Gateway error. You suspect that a command used to create the service's backend configured health check's timeout so that customers would not receive an error message below. Which command could create this issue within the backend service?
- [ ] `gcloud compute backend-services create backend-service-port3 \ --protocol http \ --port-name port3 \ --health-checks test-tcp-9000 \ --timeout = 600s --global`
- [ ] `gcloud compute backend-services create backend-service-prod1 \ --protocol http \ --port-name port003 \ --enable-cdn --health-checks test-tcp-9000 \ --timeout = 10s --global`
- [ ] `gcloud compute backend-services create backend-service-prod1 \ --protocol http \ --port-name port003 \ --health-checks test-tcp-9000 \ --timeout = 30s --global`
- [ ] `gcloud compute backend-services create backend-service-prod1 \ --protocol http \ --port-name port003 \ --enable-logging --health-checks test-tcp-9000 \ --timeout = 10s --global`

### 40
You are creating a regional MIG with VMs in 3 zones. You would like to specify which zone the VMs will be created in. Which gcloud command would give you the desired MIG setup?
- [ ] `gcloud compute instance-groups managed create example-rmig \ --template example-template \ --size 30 \ --zones us-east1-a,us-east1-b,us-east1-c`
- [ ] `gcloud compute instance-groups managed create example-rmig \ --template example-template \ --size 30 \ --region us-east1,us-west1,us-west2`
- [ ] `gcloud compute instance-groups managed create example-rmig \ --template example-template \ --size 30 \ --zones us-east1-b,us-east1-c`
- [ ] `gcloud compute instance-groups managed create example-rmig \ --template example-template \ --size 30 \ --instance-redistribution-type NONE \ --zones us-east1-b,us-east1-c`

### 41
Due to a recent expansion in business, an application that had been running on a fixed number of instances with predictably efficient performance has started causing problems as tasks are being queued and users are reporting timeout errors. To solve this problem, you have configured the app engine with automatic scaling. Which of the following scenarios accurately describes how the automatically scaled instances are created and shut down as requests are received?
- [ ] Instances are automatically created and turned down as needed to handle requests.
- [ ] Instances are created as needed, and they are shut down when idle based on the idle_timeout configuration parameter
- [ ] Instances receive a start request from the App Engine as an empty GET request to `/_ah/start`.
- [ ] The instances are always up and the state is preserved from one request to the next.

### 42
Your employer has decided to switch from your current DNS provider to Cloud DNS, and you have been tasked with migrating the existing domain to Cloud DNS. You have already created a managed zone to contain your DNS records. You also have the exported DNS configuration file in YAML records format from the current provider. What is the next step in the migration process?
- [ ] The next step is to import the DNS configuration record sets into your managed zone. In the gcloud command-line tool, you will use the dns record-sets import command without the --zone-file-format flag.
- [ ] The next step is to import the DNS configuration record sets into your managed zone. In the gcloud command-line tool, you will use the dns record-sets import command with the --zone-file-format flag.
- [ ] The next step is to verify DNS propagation to the name servers. You will do this using the Linux command watch.
- [ ] The next step is to verify DNS propagation to the name servers. You will do this using the Linux command dig.

### 43
Within your organization, there is a Business Manager position that exists in every department. Everyone with this job is supposed to have access to a specific set of software tools that nobody else needs. They are distributed, on different projects in different regions. What is the most efficient, accurate, and easily reversible way to go about giving all of those people access to those resources without giving them to those that do not need them?
- [ ] Add the permissions to each user individually in the Google Cloud console.
- [ ] Put the users into a “Business Manager” Google Group. Then give the permissions to the desired tools to the group.
- [ ] Create a service account that has all the necessary permissions. Then assign that to each user in the console.
- [ ] Update the user account using a CSV import.

### 44
Your company wants to set up a Partner Interconnect connection but has concerns about the availability and reliability of the service provider's network. What option will reduce your dependence on the service provider's network?
- [ ] Establish your connection on Layer 2.
- [ ] Establish your connection on Layer 3.
- [ ] Use static routing instead of the standard Border Gateway Protocol.
- [ ] Use a 100 Gbps VLAN connection instead of a 10 Gbps VLAN connection.

### 45
You are configuring Cloud Router for a multi-NIC VM, and you note that every NIC gets a different route. Each Network Connectivity is creating custom dynamic routes in the VPC network. What has happened? What should you do?
- [ ] This is working as it should. You do not need to fix anything.
- [ ] A cloud router can’t re-advertise routes learned from one BGP to another. You need to connect each network to your on-premises network using Cloud Interconnect.
- [ ] You have exceeded the limits for learned routes. Check your quotas and limits.
- [ ] Cloud Router is trying to establish a BGP session with a device that has the same ASN as the Cloud Router. Change the ASN of the router.

### 46
You receive a request from an engineer to update his IAM role. He will be working within Cloud SQL, and he needs to be able to run queries and manipulate the data within the existing instance. Considering the policy of Least Privilege, which IAM role would be best suited for this Engineer?
- [ ] Cloud SQL Editor
- [ ] Cloud SQL Viewer
- [ ] Cloud SQL Client
- [ ] Cloud SQL Admin

### 47
A project admin has reached out to you for help resolving a problem with the user accounts on a project. All of the users seem to have admin permissions on every service within the project, even things they are not working on. Users have been creating new instances and accessing folders that should be behind firewalls. Nothing about their permissions has changed since the beginning of the project, but they seem to automatically have access to even brand new projects that they could not have been given IAM roles for. Which of the following scenarios could cause what the project admin is experiencing?
- [ ] The users have all been granted the Service Account User role at the project level.
- [ ] The admin has deleted service accounts that are in use by an active instance, and parts of the application have failed.
- [ ] The admin used Custom IAM roles when setting up the users instead of using Predefined IAM roles.
- [ ] The users were all granted the Basic role, Viewer, which pre-dates the introduction of IAM

### 48
The network administrator has asked you to migrate a DNSSEC-signed zone to Cloud DNS. You realize before you get too far into the process that Cloud DNS does not support the same KSK algorithm that is currently in use. How will you safely, and properly migrate the zone to Cloud DNS?
- [ ] Deactivate the DNSSEC at the domain registrar before you migrate the zone and update the name server records to us Cloud DNS.
- [ ] Leave the DNSSEC enabled. Manually copy the DNSKEYs.
- [ ] Change the DNSSEC state from ‘ON’ to ‘Transfer’ to stop the ZSK before the migration.
- [ ] Remove the DS records and wait for them to expire from the cache before migrating.

### 49
The network admin runs the following command in the gcloud command-line tool to create a new VPC network: gcloud compute networks create sampleco-prod-1 \ --subnet-mode=auto \ --bgp-routing-mode=global \ --mtu=1460 Which two of the following IP addresses would be available within VPC subnets automatically created by this command? (Choose 2 answers)
- [ ] 10.255.4.68
- [ ] 10.172.4.82
- [ ] 192.168.10.100
- [ ] 10.88.20.64

### 50
Your organization has partially migrated to the cloud, and many of your servers are maintained in an on-premises data center. You have noticed increased throughput latency when application components on the cloud and the corporate data center communicate. You have confirmed that load balancers are in place and configured correctly. How might you adjust the configuration of this hybrid environment to minimize latency and improve application performance?
- [ ] Enable window-size scaling from the command line to increase bandwidth.
- [ ] Enable Round-Trip Time optimization from the command line to increase bandwidth.
- [ ] Do nothing. This latency is necessary and acceptable because it prevents a backlog of packets consuming the resources of the receiving server.
- [ ] After calling the [RTT.insert] method, check the RTT status by calling [RTT.get] with the job ID and location, and check the [status.state] value to learn the job status.

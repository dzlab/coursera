# Answers

### 1
- [x] Project number

**Explanation**

Projects have three different types of identifiers. They have the project name, the project number, and the project ID.

The user always creates the project name. It's basically a user-friendly identifier for your project, and it should allow you to recognize at a glance what that project is. 

The project ID can be assigned by the user or randomly assigned by GCP, and it cannot be modified once assigned.

The project number is something automatically generated for you by Google, and it can't be changed.

https://cloud.google.com/docs/overview/#projects

### 2
You are connecting via bastion host to an instance that has no external IP address. What statement regarding the use of bastion hosts is correct?

- [x] Keep the bastion host hardened from the outside to keep the connection secure.

**Explanation**

When connecting via bastion host to an instance that has no external IP address, keep that bastion host hardened from the outside so that it's secure, though it is a good solution when we have a cloud-native infrastructure.

https://cloud.google.com/solutions/connecting-securely#bastion

### 3
- [x] 1 Cloud VPN Gateway, 1 Peer Gateway, and 1 Cloud Router

**Explanation**

VPC networks allow you to regionally segment the network IP space into prefixes (subnets) and control which prefix a VM instance's internal IP address is allocated from. If you want to avoid statically managing these subnets, including the burden of adding and removing related static routes for your VPN, you can do so by enabling dynamic routing for your VPNs using Cloud Router.

The diagram at https://cloud.google.com/compute/images/cloudrouter/cr-w-subnets.svg shows a VPN Gateway, a Peer Gateway, and a Cloud Router.

https://cloud.google.com/compute/docs/cloudrouter#cloud_router_for_vpns_with_vpc_networks

### 4
Which is the fastest instance storage option that will still be available when an instance is stopped?
- [x] SSD Persistent Disk

**Explanation**

Local SSDs and RAM disks disappear when you stop an instance. Standard Persistent Disks and SSD Persistent Disks both survive when you stop an instance, but SSD Persistent Disks have up to 4 times the throughput and up to 40 times the I/O operations per second of a Standard Persistent Disk.

https://cloud.google.com/compute/docs/disks/

### 5
Of the options given, which is designed to allow you to create and host APIs on App Engine?
- [x] Cloud Endpoints

**Explanation**

Google Cloud Endpoints is a feature that enables developers to easily develop and host APIs on App Engine with OAuth 2.0 support. From this single API source, Endpoints also lets developers generate strongly-typed client libraries for Java (Android) and Objective-C (iOS), along with dynamically-typed libraries for JavaScript.

https://cloud.google.com/appengine/docs/python/endpoints/getstarted/

### 6
To minimize the risk of someone changing your log files to hide their activities, which of the following principles would help? (Select 3 answers.)
- [x] Restrict usage of the owner role for projects and log buckets.
- [x] Implement object versioning on the log-buckets.
- [x] Require two people to inspect the logs.

**Explanation**

Logs are stored to Cloud Storage in the originating project. By default, project owners and editors have ownership permissions for all Cloud Storage buckets in the project and objects under the bucket's hierarchical permissions model.
To minimize the risk of inadvertent or malicious changes to your logs, apply the following principles.

Least privilege

Grant the least-broad permissions that are required to do the job. Restrict the usage of owner role for projects and log-buckets.

Non-repudiation

Cloud Storage automatically encrypts all data before it is written to disk. [Since the logs are automatically encrypted, it's not necessary to use Cloud KMS to encrypt them.] You can provide some additional assurance of non-repudiation by implementing object versioning on the log-buckets. When an object is overwritten or deleted in a bucket, a copy of the object is automatically saved with generation properties that identify it. Unfortunately, this feature can't protect against a project owner deleting the archived object or disabling the versioning.

Separation of duties

You can provide some additional assurance of separation of duties. For example, you might require two people to inspect and sign off on the logs. You can copy the log-buckets to a project that has a different owner by using gsutil cp as part of a frequent cron job, or if the amount of data copied will be greater than 10TB of log data at a time, by using the Cloud Storage Transfer Service. This approach can't protect against a project owner who deletes the original bucket before the copy occurs or who disables the original logging.

https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations#prevent_unwanted_changes_to_logs


### 7
`__________________` storage is attached to the same server hardware that hosts your GCE virtual machines. In addition, when an instance using this storage type stops or is deleted, the data is lost.
- [x] Local SSD

**Explanation**

Local SSDs are physically attached to the server that hosts your virtual machine instance. Local SSDs have higher throughput and lower latency than standard persistent disks and SSDs. Though the data that you store on local SSDs persist only until you stop or delete the instance. 

https://cloud.google.com/compute/docs/disks/

### 8
Which of the following GCE instance state descriptions are incorrect? (Choose 2 answers)
- [x] Running - the instance is prepared and has fully booted
- [x] Terminated - the instance has been stopped and deleted

**Explanation**

The descriptions of Provisioning, Staging, and Stopping are correct, but the descriptions of Running and Terminated are incorrect. A GCE instance is running when the instance has been fully prepared but has not necessarily been fully booted. Terminated instances are completely stopped, but they are not deleted or lost. They can be restarted.

https://cloud.google.com/compute/docs/instances/checking-instance-status

### 9
- [x] Service account

**Explanation**

A service account is an account that belongs to your application instead of to an individual end user. When you run code that is hosted on Cloud Platform, you specify the account that the code should run as. You can create as many service accounts as needed to represent the different logical components of your application.

https://cloud.google.com/iam/docs/overview

### 10
Regarding Cloud IAM, what type of role(s) are available?
- [x] primitive, predefined and custom roles

**Explanation**

Prior to Cloud IAM, you could only grant Owner, Editor, or Viewer roles to users. A wide range of services and resources now surface additional IAM roles out of the box. For example, the Cloud Pub/Sub service exposes Publisher and Subscriber roles in addition to the Owner, Editor, and Viewer roles.

There are two kinds of roles in Cloud IAM:

- Primitive roles: The roles historically available in the Google Cloud Platform Console will continue to work. These are the Owner, Editor, and Viewer roles.
- Predefined roles: Predefined roles are the new IAM roles that give finer-grained access control than the primitive roles. For example, the curated role Publisher provides access to only publish messages to a Pub/Sub topic.

https://cloud.google.com/iam/docs/overview

### 11
Which of the following GCP resources are multi-regional? (Choose 2 answers)
- [x] Cloud Storage data
- [x] GCP Virtual Private Cloud networks

**Explanation**

Data stored in Cloud Storage is a multi-regional resource because it is not tied to a specific region and can be moved between regions, and regions can be added and removed from a region group. For example, buckets in the European Union location for Google Cloud Storage keep data-at-rest inside the European Union, but at-rest data can be stored in or moved to any Cloud Storage region within the European Union.

Virtual Private Cloud networks can span multiple regions.

https://cloud.google.com/docs/geography-and-regions#multi-regional_resources

### 12
You want to connect to single GCE instances that do not have external IP addresses, to do some troubleshooting, and do not have an existing cloud network. Which connection method is ideal in this case?
- [x] Connection via serial console

**Explanation**

One option mentioned in the GCP Systems Operations course is connecting to an instance via the serial console. This option allows us to use the web console, the G Cloud command line, or the SSH client to connect to an instance via its serial port.

Using this does require that we enable the feature with a metadata key value setting. However, should you need to connect to a single instance for troubleshooting those one-off issues, this could be useful. 

https://cloud.google.com/vpc/docs/special-configurations#externalhttpconnection

### 13

Your company would like to establish a direct, private connection between your on-premise network with Google networks, to connect with GCP resources without transmitting over the public internet. However, your on-premise network is too far from a Google colocation facility to establish a physical connection. You also expect your network topology to change in the next 18 months, so you will need to update all on-premise destination IP addresses. You would like this update to be entirely managed by your company's employees, even though you will need to connect through a service provider. Which GCP Hybrid Connectivity option will allow you to establish your desired network connection, and independently manage your upcoming network updates?
- [x] Partner Interconnect

**Explanation**

A Partner Interconnect connection is the best choice in this case. A Dedicated Interconnect connection will not be possible due to the distance between your on-premise office and the nearest Google colocation facility. Using either Direct Peering or Carrier Peering requires contacting Google in order to update the IP address ranges for your network, so these two options will not suffice. This leaves Partner Interconnect as the only remaining option.

https://cloud.google.com/interconnect/docs/concepts/partner-overview

### 14
You are using an instance configured as a NAT Gateway to give access to GCE instances that do not have external IP addresses. What should you bear in mind? (Choose 2 answers)
- [x] The NAT Gateway is a single point of failure.
- [x] The NAT Gateway cannot manage high levels of traffic for multiple instances.

**Explanation**

When an instance does not have an external IP address assigned it cannot make direct connections to external services, including other Cloud Platform services. To allow these instances to reach services on the public Internet, you can set up and configure a NAT gateway machine, which can route traffic on behalf of any instance on the network. Be aware that a single instance should not be considered highly available, and cannot support high traffic throughput for multiple instances.

https://cloud.google.com/vpc/docs/special-configurations#natgateway

### 15
Google Compute Engine provides _____________ snapshots so that each snapshot only contains data that has changed since the previous snapshot.
- [x] Incremental

**Explanation**

Google Cloud Platform backs up different resources in different ways. This question focuses on persistent disks.

Here is GCP's description of a persistent disk: Persistent disks are durable network storage devices that your instances can access like physical disks in a desktop or a server. The data on each persistent disk is distributed across several physical disks. 

Google Compute Engine provides incremental snapshots of persistent disks by default, which allow for better performance and lower storage charges for users.

GCP has a different method for backing up virtual machines themselves. It creates a snapshot of a VM called a machine image. 

In GCP's words, a machine image is a Compute Engine resource that stores all the configuration, metadata, permissions, and data from one or more disks required to create a Virtual machine (VM) instance. You can use a machine image in many system maintenance scenarios, such as instance creation, backup and recovery, and instance cloning.

Machine image snapshots can be differential or incremental. The first snapshot is usually differential, and subsequent snapshots of the same VM are incremental.

https://cloud.google.com/compute/docs/disks/persistent-disks#snapshots

### 16
Cloud Source Repositories provide a hosted version of which version control system?
- [x] Git

**Explanation**

Google Cloud Source Repositories are fully-featured, private Git repositories hosted on Google Cloud Platform.

https://cloud.google.com/source-repositories/docs/

### 17
Which of the following is not helpful for mitigating the impact of an unexpected failure or reboot?
- [x] Configure tags and labels

**Explanation**

At some point in time, you will experience an unexpected single instance failure and reboot. Unlike unexpected single instance failures, your instance fails and is automatically rebooted by the Google Compute Engine service. To help mitigate these events, [back up your](https://cloud.google.com/compute/docs/tutorials/robustsystems#backup) data, use persistent [disks](https://cloud.google.com/compute/docs/disks/add-persistent-disk), and use startup scripts to quickly re-configure software.

https://cloud.google.com/compute/docs/tutorials/robustsystems

### 18
Which database service requires that you configure a failover replica to make it highly available?
- [x] Cloud SQL

**Explanation**

Cloud Datastore, Cloud Spanner, and BigQuery are all horizontally scalable and are automatically replicated to multiple zones. Since Cloud SQL is not horizontally scalable, you must configure a failover replica to make it highly available.

https://cloud.google.com/sql/docs/mysql/configure-ha

### 19
In Google Compute Engine, where should an image be uploaded before being added to the Compute Engine project?
- [x] You must upload your image into a Google Cloud Storage bucket.

**Explanation**

Google Compute Engine uses Google Cloud Storage to store images. Once you have built your image tarball, you must upload your image into a Google Cloud Storage bucket before you can add the image to your Compute Engine project. To add a custom image to your project from a tar file of an existing image, you must first add the image to Google Cloud Storage and import it to your Compute Engine project.

https://cloud.google.com/compute/docs/tutorials/building-images

### 20
Which of the following GCP resources is regional?
- [x] GCP App Engine applications

**Explanation**

GCP App Engine applications are regional resources because the applications are redundantly deployed across all zones in a given region, which maintains its availability in the event that a zone within a region goes down. An outage would have to affect an entire region to make App Engine applications unavailable.

https://cloud.google.com/docs/geography-and-regions#regional_resources

### 21

Google Cloud Datastore is ideal for applications that ____.
- [x] rely on highly available structured data at scale

**Explanation**

Cloud Datastore is not a relational database and it is not an effective storage solution for analytic data. Instead, use Cloud Datastore for applications that rely on highly available structured data at scale.

https://cloud.google.com/datastore/docs/concepts/overview#what_its_good_for

### 22
- [x] storage specialized

**Explanation**

Each of the machine types below is a predefined machine type in GCE except for storage specialized. If these predefined machine types are not ideal for your workloads, GCE offers custom machine types.

https://cloud.google.com/compute/docs/machine-types#predefined_machine_types

### 23
To ensure that your application will handle the load even if an entire zone fails, what should you do? (Choose the best answer.)
- [x] Overprovision your regional managed instance group by at least 50%.

**Explanation**

To account for the extreme case where one zone fails or an entire group of instances stops responding, Compute Engine strongly recommends overprovisioning your managed instance group by at least 50%. Spreading instances across three zones already helps you preserve at least 2/3 of your serving capacity and the other two zones in the region can continue to serve traffic without interruption. By overprovisioning to 150%, you can ensure that if 1/3 of the capacity is lost, 100% of traffic is supported by the remaining zones.

You need to select the "Multizone" option (or the --region flag if you're using the gcloud command) when creating a managed instance group.

It is only possible to create regional managed instance groups. You cannot create regional unmanaged instance groups.

https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#provisioning_the_correct_managed_instance_group_size

### 24
What are two different features that fully isolate groups of VM instances?
- [x] Projects and networks

**Explanation**

Google uses software-defined networking that enables you to subject every packet to security checks, thereby enabling complete isolation of Cloud Platform projects.

Networks within projects are used to isolate groups of VM instances.

Subnetworks on Compute Engine enable you to control the address space in which VM instances are created, while maintaining the ability to route between them.

Firewall rules only restrict incoming network traffic. They cannot restrict outgoing network traffic.

https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations#use_projects_to_fully_isolate_resources

### 25

What is a "topic" in Google Pub/Sub?
- [x] A named entity that represents a feed of messages

**Explanation**

Google Cloud Pub/Sub is a publish/subscribe (Pub/Sub) messaging service between senders and receivers. In the Pub/Sub flow, a topic is a named entity that represents a feed of messages. More than one "publisher" can compose messages on a single topic.

https://cloud.google.com/pubsub/architecture

### 26
Which statement regarding Cloud IAM primitive roles is incorrect?
- [x] Primitive roles can be assigned to Google accounts, service accounts, and Google App domains.

**Explanation**

Three roles existed before the introduction of Cloud IAM: Owner, Editor, and Viewer. These roles are concentric; that is, the Owner role includes the permissions in the Editor role, and the Editor role includes the permissions in the Viewer role.

Predefined roles can be assigned to Google accounts, service accounts, and Google App domains. Primitive roles are for users only.

https://cloud.google.com/iam/docs/understanding-roles#primitive_roles

### 27
Which of the following products will allow you to host a static website?
- [x] Cloud Storage

**Explanation**

Cloud Storage will allow you to host a static website. It provides the means to set an index page, and a 404 page. The site can be served up at a very fast speed, and at a low cost.

https://cloud.google.com/storage/docs/static-website

### 28
To use load balancing and protocol forwarding, you must create a forwarding rule that directs traffic to specific _____________________ that contain instances from multiple zones.
- [x] target pools

**Explanation**

In Google Compute Engine, forwarding rules work in conjunction with target pools and target instances to support load balancing and protocol forwarding features. To use load balancing and protocol forwarding, the user must create a forwarding rule that directs traffic to specific target pools (for load balancing) or target instances (for protocol forwarding). It is not possible to use either of these features without a forwarding rule.

https://cloud.google.com/compute/docs/protocol-forwarding/

### 29
You are configuring your Compute Engine instances for a highly available application on GCP. What are common ways to improve the availability of your application? (Select all that apply.)
- [x] Over-provision your instances in multiple zones in case of zone failure.
- [x] Create an autoscaling instance group for all of your instances.
- [x] Place your instance group behind a load balancer.

**Explanation**

Creating multiple instances is essential, in case one instance fails. Locating them in different instances is also recommend, to withstand a zone outage, and to manage the temporarily increased workload in the event of a zone failure, over-provisioning as needed depending on your number of instances and number of zones is also recommended.

You also want to create an autoscaling instance group, which allows you to monitor the health of your instances and replace or scale horizontally as needed. Finally, the instance group should be placed behind a load balancer, which can redirect incoming traffic across multiple zones, as well as monitor and report on the health of your instances in each zone.

[/course/designing-a-google-cloud-infrastructure/compute-1/](https://cloudacademy.com/course/designing-a-google-cloud-infrastructure/compute-1/)

### 30
What determines the maximum number of virtual CPUs you can add to a custom machine type? (Choose 2 answers)
- [x] the zone of the instance
- [x] the CPU type of the instance

**Explanation**

Zones that support the Intel Xeon (Skylake) CPU can support machine types with up to 96 vCPUs, but zones that don't support that type of CPU have a lower maximum number of vCPUs. Also, if you choose a lesser CPU platform, such as Haswell, for your custom machine type, then the maximum number of vCPUs is lower.

https://cloud.google.com/compute/docs/regions-zones/#available

### 31
- [x] App Engine

**Explanation**

App Engine is great for running web-based apps, line of business apps, and mobile backends. Compute Engine is great for when you need more control of the underlying infrastructure.

Container Engine is in between because it gives you control of the containers running on top of Compute Engine.

https://cloud.google.com/compute/docs/faq#how_do_google_app_engine_and_product_name_relate_to_each_other


### 32
Which of the following features makes applying firewall settings easier?
- [x] Tags

**Explanation**

Assign tags to help you easily apply networking or firewall settings. Tags are used by [networks and firewalls](https://cloud.google.com/compute/docs/networking) to identify which instances that certain firewall rules apply to. For example, if there are several instances that perform the same task, such as serving a large website, you can tag these instances with a shared word or term and then use that tag to give HTTP access to those instances. Tags are also reflected in the metadata server, so you can use them for applications running on your instances.

https://cloud.google.com/compute/docs/label-or-tag-resources

### 33
Which two places hold information you can use to monitor the effects of a Cloud Storage lifecycle policy on specific objects? (Select 2 answers.)
- [x] Expiration time metadata
- [x] Access logs

**Explanation**

If a Delete action is specified for a bucket with the Age condition (and no NumberOfNewerVersions condition), then some objects may be tagged with expiration time metadata. An object's expiration time indicates the time at which the object becomes (or became) eligible for deletion by Object Lifecycle Management. The expiration time may change as the bucket's lifecycle configuration changes.

To find out what lifecycle management actions have been taken, you can enable access logs for your bucket. A value of "GCS Lifecycle Management" in the “cs_user_agent” field in the log entry indicates the action was taken by Google Cloud Storage based on the lifecycle configuration.

A lifecycle config file is used to configure a lifecycle policy, but it does not contain information about how that policy has affected specific objects.

There is no service called "Cloud Storage Lifecycle Monitoring".

https://cloud.google.com/storage/docs/lifecycle#expirationtime

### 34
Google App Engine has a second hosting option, called App Engine Flexible Environment. Which of the following best describes App Engine Flexible Environment? 
- [x] The Flexible Environment supports App Engine applications on configurable Compute Engine instances.

**Explanation**

Google App Engine has a second hosting option, the flexible environment, which has the following attributes:

- The flexible environment lets you run App Engine applications on configurable Compute Engine Virtual Machines (VMs)
- This VM hosting environment offers more flexibility and provides more CPU and memory options.

https://cloud.google.com/appengine/docs/flexible/

### 35
What are two of the actions you can take to troubleshoot a virtual machine instance that won't start up at all? (Select 2 answers.)
- [x] Examine your virtual machine instance's serial port output.
- [x] Validate that your disk has a valid file system.

**Explanation**

Here are some tips to help troubleshoot your persistent boot disk if it doesn't boot.
- **Examine your virtual machine instance's serial port output.**
An instance's BIOS, bootloader, and kernel will print their debug messages into the instance's serial port output, providing valuable information about any errors or issues that the instance experienced.
- **Enable interactive access to the serial console.**
You can enable interactive access to an instance's serial console so you can log in and debug boot issues from within the instance, without requiring your instance to be fully booted.
- **Validate that your disk has a valid file system.**
If your file system is corrupted or otherwise invalid, you won't be able to launch your instance.
- **Validate that the disk has a valid master boot record (MBR).**

If your virtual machine won't boot at all, then you can't use SSH to connect to it because the SSH server on the VM won't be running.

Increasing the CPU and memory on the instance might help if the VM boots partway, but not if it can't boot at all.

https://cloud.google.com/compute/docs/troubleshooting#pdboot

### 36
Which database service(s) support standard SQL queries?
- [x] Cloud Spanner and Cloud SQL

**Explanation**

Cloud SQL is a managed service for MySQL and PostgreSQL, which both support SQL queries. Cloud Spanner supports SQL queries. Cloud Bigtable and Cloud Datastore are NoSQL databases.

https://cloud.google.com/products/storage/

### 37
A 5 TB persistent disk is attached to a standard Compute Engine instance. Currently, 2 TB of the total storage is used. The user took an initial snapshot yesterday, and 250 GB of the 2 TB now stored is new or updated data since that snapshot was taken. If the user creates a second snapshot of the instance disk now, approximately how large will the snapshot be (do not take snapshot data compression into account)?
- [x] 250 GB

**Explanation**

Persistent disk snapshots are only charged for the total size of the snapshot. For example, if only 2TB of disk space is used on a 5TB persistent disk, the snapshot size will be around 2TB, rather than the full 5TB of provisioned disk space.

Additionally, snapshots are updated incrementally. If the user took a snapshot yesterday, and only 250 GB of data is new or updated since that snapshot was taken, this means the current snapshot will be roughly 250 GB.

https://cloud.google.com/compute/docs/disks/create-snapshots#before-you-begin

### 38
Which description of a Recovery Time Objective (RTO) is correct?
- [x] It is the maximum acceptable amount of time a system can be offline.

**Explanation**

A recovery time objective (RTO) is the maximum acceptable time to restore system service after a disruption, while a recovery point objective (RPO) is the maximum acceptable amount of data loss measured in time. The two concepts are interrelated. The amount of data loss a business can tolerate usually determines the desired recovery time objective. The desired RTO then generally determines the disaster recovery method.

https://en.wikipedia.org/wiki/Recovery_point_objective

### 39
In Google Compute Engine, ______________ work in conjunction with target pools and target instances to support load balancing and protocol forwarding features.
- [x] forwarding rules

**Explanation**

In Google Compute Engine, forwarding rules work in conjunction with target pools and target instances to support load balancing and protocol forwarding features. To use load balancing and protocol forwarding, the user must create a forwarding rule that directs traffic to specific target pools (for load balancing) or target instances (for protocol forwarding). It is not possible to use either of these features without a forwarding rule.

https://cloud.google.com/compute/docs/protocol-forwarding/

### 40
What are the two consistency levels for Datastore queries?
- [x] Strongly consistent and eventually consistent

**Explanation**

The two consistency levels for Datastore queries are strongly consistent queries, which guarantee the most up-to-date (transactionally consistent) results and eventually consistent queries, which may produce stale results but generally run faster.

https://cloud.google.com/datastore/docs/concepts/structuring_for_strong_consistency

### 41
Regarding Compute Engine: What is a managed instance group?
- [x] A managed instance group uses an instance template to create identical instances

**Explanation**

A managed instance group uses an instance template to create identical instances. You control a managed instance group as a single entity. If you wanted to make changes to instances that are part of a managed instance group, you would apply the change to the whole instance group.

https://cloud.google.com/compute/docs/instance-groups/

### 42
In GCE, metadata is stored in the `_____` format.
- [x] key:value

**Explanation**

In GCE, every instance stores its metadata on a metadata server. You can query this metadata server programmatically for information about the instance, such as the instance's host name, instance ID, startup and shutdown scripts, custom metadata, and service account information. Metadata is stored in the format key:value.

https://cloud.google.com/compute/docs/metadata

### 43
You are creating a GCE custom machine with more than one vCPU. Which rules apply in this case? (Choose 3 answers)
- [x] The custom machine must include an even number of vCPUs.
- [x] The custom machine must have between 0.9 and 6.5 GBs of memory per vCPU.
- [x] The custom machine's total memory must be a multiple of 256 MB.

**Explanation**

Each choice below is a rule when creating a GCE custom machine types except there is no set limit of custom instance per zone per GCP account.

https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type

### 44
Which statements regarding GCP automatic and custom subnetworks are correct? (Choose 2 answers)
- [x] Automatic subnets create one subnet in each region.
- [x] Automatic subnets can be converted to custom subnets, but not returned back to automatic.

**Explanation**

A network spans all regions, but each subnet can only be in one region. A subnet allows you to define an IP address range and a default gateway for the instances you put in it. The IP address ranges of the different subnets must be non-public (such as 10.0.0.0) and must not overlap, but other than that, there are no restrictions on them. 

A network can have either automatic or custom subnets. With automatic, the subnets are created for you, one in each region. With custom, you create them yourself. If you discover that you need to customize a network with automatic subnets, then you can convert it to custom mode, but once you do, you cannot convert it back to automatic mode.

https://cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets

### 45
Which of the following is a zonal GCP resource?
- [x] GCP Compute Engine virtual machine instances

**Explanation**

GCP Compute Engine virtual machine instances are deployed within specific zones within GCP regions. If a zone experiences an outage or failure, instances within that zone can be lost or affected unless the GCE instances are backed up or redundantly supported by other resources.

The other choices are regional or multi-regional resources.

https://cloud.google.com/docs/geography-and-regions#regional_resources

### 46
Google Compute Engine offers ________________ to distribute incoming network traffic across multiple virtual machine instances.
- [x] Load balancing

**Explanation**

Google Compute Engine offers server-side load balancing to distribute incoming network traffic across multiple virtual machine instances. Load balancing is useful because it helps the user support heavy traffic and provides redundancy to avoid failures.

https://developers.google.com/compute/docs/load-balancing/

### 47
What alternative to Cloud Datastore is recommended by Google if your data is not highly structured or you do not require support for ACID transactions?
- [x] Google Cloud Bigtable

**Explanation**

These are recommendations as alternatives to Cloud Datastore:

- Google Cloud SQL for a relational database with full SQL support for an online transaction processing (OLTP) system
- Google Cloud Bigtable for data is not highly structured or support not needed for ACID transactions
- Google BigQuery for interactive querying in an online analytical processing (OLAP) system
- Google Cloud Storage to store large immutable blobs, such as large images or movies

https://cloud.google.com/datastore/docs/concepts/overview#comparison_with_traditional_databases

### 48
Which of the following is not an IAM best practice?
- [x] Use primitive roles by default

**Explanation**

- Treat each component of your application as a separate trust boundary. If you have multiple services that requires different permissions, [create a separate service account](https://cloud.google.com/iam/docs/managing-service-accounts) for each of the services so that they can be permissioned differently.
- Grant primitive roles in the following cases:
  - when the Cloud Platform service does not provide a predefined role. See the [predefined roles table](https://cloud.google.com/iam/docs/understanding-roles#predefined_roles) for a list of all available predefined roles.
  - when you want to grant broader permissions for a project. This often happens when you’re granting permissions in development or test environments.
  - when you need to allow a member to modify permissions for a project, you’ll want to grant them the owner role because only owners have the permission to grant access to other users for for projects.
  - when you work in a small team where the team members don’t need granular permissions.
- Remember that a policy set on a child resource cannot restrict access granted on its parent. Check the policy granted on every resource and make sure you understand the [hierarchical inheritance](https://cloud.google.com/iam/docs/resource-hierarchy-access-control).
- Grant roles at the smallest scope needed. For example, if a user only needs access to publish Pub/Sub topic, grant the [Publisher](https://cloud.google.com/pubsub/access_control#tbl_roles) role to the user for that topic.
- Restrict who [can act as service accounts](https://cloud.google.com/iam/docs/service-accounts#granting_another_user_the_ability_to_act_as_a_service_account). Users who are granted the Service Account Actor role for a service account can access all the resources for which the service account has access. Therefore be cautious when granting the Service Account Actor role to a user.
- Restrict who has access to create and manage service accounts in your project.
- Granting [owner](https://cloud.google.com/iam/docs/understanding-roles#primitive_roles) role to a member will allow them to modify the IAM policy. Therefore grant the owner role only if the member has a legitimate purpose to manage the IAM policy. This is because as your policy contains sensitive access control data and having a minimal set of users manage it will simplify any auditing that you may have to do.

https://cloud.google.com/iam/docs/using-iam-securely

### 49
If you do not grant a user named Bob permission to access a Cloud Storage bucket, but then use an ACL to grant access to an object inside that bucket to Bob, what will happen? 
- [x] Bob will be able to access the object because bucket and object ACLs are independent of each other.

**Explanation**

Bucket and object ACLs are independent of each other, which means that the ACLs on a bucket do not affect the ACLs on objects inside that bucket. It is possible for a user without permissions for a bucket to have permissions for an object inside the bucket. For example, you can create a bucket such that only GroupA is granted permission to list the objects in the bucket, but then upload an object into that bucket that allows GroupB READ access to the object. GroupB will be able to read the object, but will not be able to view the contents of the bucket or perform bucket-related tasks.
https://cloud.google.com/storage/docs/best-practices#security

### 50
Which of these is not a principle you should apply when setting roles and permissions?
- [x] Whenever possible, assign primitive roles rather than predefined roles.

**Explanation**

Predefined roles provide more granular access than primitive roles. Grant predefined roles to identities when possible, so you only give the least amount of access necessary to access your resources.

https://cloud.google.com/iam/docs/using-iam-securely

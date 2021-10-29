# Sample Questions

## Ensuring solution quality.

Case studies and Best practice questions. There will be a lot of them.

### Example 1
**Question:** You are monitoring GCP Operations (formerly Stackdriver) metrics which show that your Bigtable instance’s storage utilization is approaching 70% per node. What do you do?

**Answer**: Add additional nodes to the cluster to increase storage processing capacity. Even though Cloud Bigtable table data is stored in Google Colossus, a cluster needs to be sized appropriately so that nodes have enough resources to process the total storage in use. When instance storage utilization reaches 70% per node, additional nodes should be added.

**Read:** [Quotas & limits | Cloud Bigtable Documentation | Google Cloud](https://cloud.google.com/bigtable/quotas#storage-per-node)

### Example 2
**Question:** Your organization has just recently started using Google Cloud. Everyone in the company has access to all datasets in BigQuery, using it as they see fit without documenting their use cases. You need to implement a formal security policy, but need to first determine what everyone has been doing in BigQuery. What is your first step to do so?

**Answer:** Use Stackdriver Logging to review data access. Stackdriver Logging will record the audit logs of jobs and queries of each individual user’s actions. Query slots won’t work because they measure BigQuery performance and resource usage, but gives no visibility to individual user activity. You will not be able to view user activity via billing records. IAM policies are applied to datasets, but not individual tables inside each dataset. Furthermore, IAM policies show who has permissions to resources, but not their activity.

**Read:** [BigQuery documentation | Google Cloud](https://cloud.google.com/bigquery/docs)

### Example 3
**Question:** Your security team have decided that your Dataproc cluster must be isolated from the public internet and not have any public IP addresses. How can you achieve this?

**Answer:** Using the — no-address flag will prevent public IPs from being assigned to nodes in a Cloud Dataproc cluster. However, Private Google Access is still required for the subnet to access certain GCP APIs.

**Read:** [Dataproc Cluster Network Configuration | Dataproc Documentation](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/network#create_a_cloud_dataproc_cluster_with_internal_ip_address_only)

Explore what Google recommends as best practice

- BigQuery: https://cloud.google.com/bigquery/docs/best-practices
- Stackdriver and Logging: https://cloud.google.com/products/operations
- BigTable: https://cloud.google.com/bigtable/docs/performance
- IAM and security: https://cloud.google.com/iam/docs/concepts
- Cloud Storage: https://cloud.google.com/storage/docs/best-practices

After all I would recommend to read overviews of all database products as there will be a lot of questions about them: https://cloud.google.com/products/databases

## Designing data processing systems

### Example

**Question:** A customer has a 400GB MySQL database running in a datacentre. What would be the best approach for migrating this database to GCP?

**Answer:** Create a Cloud SQL for MySQL 2nd generation instance and migrate the data. For a MySQL database of this size, a Cloud SQL for MySQL instance would be the recommended approach. Using Compute Engine adds additional operational overhead. Postgres and Spanner would not be suitable migration hosts for a MySQL database.

**Recommended read:** [Migration from MySQL to Cloud SQL | Solutions | Google Cloud](https://cloud.google.com/solutions/migrating-mysql-to-cloudsql-concept)


## Choosing Google Database products
![image](https://user-images.githubusercontent.com/1645304/139313574-ecce8c9a-1c0e-4e46-b927-5280244610e1.png)

### Example:
Your database is 500 GB in size. The data is semi-structured and does not need full atomicity. You need to process transactions in a point-of-sale application on Google Cloud Platform? You need to account for exponential user growth, but you do not want to deal with managing your infrastructure overhead?

Use **Datastore**

### Example:
Data is more than 1 Tb and low latency required (also you probably don’t care about costs):

Use **BigTable**

### Example:
Low latency not required and/or need to run ANSI SQL analytics and do it economically? Need to easily load data from CSV and JSON for later inspection with SQL?

Use **BigQuery**. Cloud Datastore supports JSON and SQL-like queries but cannot easily ingest CSV files. Cloud SQL can read from CSV but not easily convert from JSON. Cloud Bigtable does not support SQL-like queries.

### Example:
You are designing a relational data repository on Google Cloud to grow as needed. The data will be transactionally consistent and added from any location in the world. You want to monitor and adjust node count for input traffic, which can spike unpredictably.

Use **Cloud Spanner**

### Example:
You need strongly consistent transactions? Data less than 500 Gb? The data does not need to be streaming or real-time?

Use **Cloud SQL**

### Pay attention to:
**High Availability and Performances** and things like **failover and read replicas**.

## After all there are a lot of BigTable questions.

### Pay attention to:
Development and Production instances, Disk Types (HDD vs. SSD).

### Example
**BigTable Performance Example:** Your organization will be deploying a new fleet of IoT devices, and writes to your Bigtable instance are expected to peak at 50,000 queries per second. You have optimized your row key design and need to design a cluster that can meet this demand. What do you do?

**Answer:** An optimized Bigtable instance with a well-designed row key schema can theoretically support up to 10,000 write queries per second per node, so 5 nodes are required.

**Read:** [Understanding Cloud Bigtable performance](https://cloud.google.com/bigtable/docs/performance)

### Example
**BigTable Performance Example:** You are asked to investigate a Bigtable instance that is performing poorly. Each row in the table represents a record from an IoT device and contains 128 different metrics in their own column, each metric containing a 32-bit integer. How could you modify the design to improve performance?

**Answer:** Large numbers of cells in a row can cause poor performance in Cloud Bigtable. When the data itself is so small, as in this scenario, it would be more efficient to simply retrieve all of the metrics from a single cell, and use delimiters inside the cell to separate the data. Row versioning would compound the problem by creating the most new entries along the least efficient dimension of the table, and HDD disks will always slow things down.

**Read:** [Understanding Cloud Bigtable performance](https://cloud.google.com/bigtable/docs/performance)

### Example
**BigTable Performance Example:** Your production Bigtable instance is currently using four nodes. Due to the increased size of your table, you need to add additional nodes to offer better performance. How should you accomplish this without the risk of data loss?

**Answer:** Edit instance details and increase the number of nodes. Save your changes. Data will re-distribute with no downtime.You can add/remove nodes to Bigtable with no downtime necessary.

**Read:** [Overview of Cloud Bigtable | Cloud Bigtable Documentation](https://cloud.google.com/bigtable/docs/overview)

### Example
**BigTable Performance Example:** You currently have a Bigtable instance you’ve been using for development running a development instance type, using HDDs for storage. You are ready to upgrade your development instance to a production instance for increased performance. You also want to upgrade your storage to SSDs as you need maximum performance for your instance. What should you do?

**Answer:** you cannot change the disk type on an existing Bigtable instance, you will need to export/import your Bigtable data into a new instance with the different storage type. You will need to export to Cloud Storage then back to Bigtable again.

### Example
**BigTable Performance Example:** Your customer uses a Bigtable instance that contains 2 replicating clusters for regional disaster recovery. Table transactions from the application are required to be strongly consistent. How can you guarantee that for this configuration?

**Answer:** Determine one cluster as the master, and use an application profile that specifies single-cluster routing. By default, Cloud Bigtable is eventually consistent. To guarantee strong consistency you must limit queries to a single cluster in an instance by using an application profile.

**Read:** [Overview of Replication | Cloud Bigtable Documentation | Google Cloud](https://cloud.google.com/bigtable/docs/replication-overview#consistency-model)

**Read:** [Overview of Cloud Bigtable | Cloud Bigtable Documentation](https://cloud.google.com/bigtable/docs/overview)

### Example
**BigTable Performance Example:** What will happen to your data in a Bigtable instance if a node goes down?

**Answer:** Nothing, as the storage is separated from the node compute. Rebuilding from RAID is not a valid Bigtable function. Storage and compute are separate, so a node going down may affect performance, but not data integrity; nodes only store pointers to storage as metadata.

**Read:** [Overview of Cloud Bigtable | Cloud Bigtable Documentation](https://cloud.google.com/bigtable/docs/overview)

### Example
**BigTable Performance Example:** You are monitoring GCP Operations (formerly Stackdriver) metrics which show that your Bigtable instance’s storage utilization is approaching 70% per node. What do you do?

**Answer:** Add additional nodes to the cluster to increase storage processing capacity. Even though Cloud Bigtable tablet data is stored in Google Colossus, a cluster needs to be sized appropriately so that nodes have enough resources to process the total storage in use. When instance storage utilization reaches 70% per node, additional nodes should be added.

**Read:** [Quotas & limits | Cloud Bigtable Documentation | Google Cloud](https://cloud.google.com/bigtable/quotas#storage-per-node)

### Example
**BigTable Performance Example:** Which of these is NOT a valid reason to choose an HDD storage type over SSD in a Bigtable instance?

**Answer:** Bigtable can integrate with Cloud Storage regardless of the type of disk in use by the instance. The other reasons are valid for choosing HDD as an outlying case, but in general SSD disks are preferred as HDD disks will cause a significant drop in performance.

**Read:** [Overview of Cloud Bigtable | Cloud Bigtable Documentation](https://cloud.google.com/bigtable/docs/overview)

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

# Sample Questions

**Example 1:** You are monitoring GCP Operations (formerly Stackdriver) metrics which show that your Bigtable instance’s storage utilization is approaching 70% per node. What do you do?

**Answer**: Add additional nodes to the cluster to increase storage processing capacity. Even though Cloud Bigtable table data is stored in Google Colossus, a cluster needs to be sized appropriately so that nodes have enough resources to process the total storage in use. When instance storage utilization reaches 70% per node, additional nodes should be added.

**Read:** [Quotas & limits | Cloud Bigtable Documentation | Google Cloud](https://cloud.google.com/bigtable/quotas#storage-per-node)

**Example 2:** Your organization has just recently started using Google Cloud. Everyone in the company has access to all datasets in BigQuery, using it as they see fit without documenting their use cases. You need to implement a formal security policy, but need to first determine what everyone has been doing in BigQuery. What is your first step to do so?

**Answer:** Use Stackdriver Logging to review data access. Stackdriver Logging will record the audit logs of jobs and queries of each individual user’s actions. Query slots won’t work because they measure BigQuery performance and resource usage, but gives no visibility to individual user activity. You will not be able to view user activity via billing records. IAM policies are applied to datasets, but not individual tables inside each dataset. Furthermore, IAM policies show who has permissions to resources, but not their activity.

**Read:** [BigQuery documentation | Google Cloud](https://cloud.google.com/bigquery/docs)

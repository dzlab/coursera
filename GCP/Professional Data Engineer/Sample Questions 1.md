#

**Example 1:** You are monitoring GCP Operations (formerly Stackdriver) metrics which show that your Bigtable instance’s storage utilization is approaching 70% per node. What do you do?

**Answer**: Add additional nodes to the cluster to increase storage processing capacity. Even though Cloud Bigtable table data is stored in Google Colossus, a cluster needs to be sized appropriately so that nodes have enough resources to process the total storage in use. When instance storage utilization reaches 70% per node, additional nodes should be added.

**Read:** [Quotas & limits | Cloud Bigtable Documentation | Google Cloud](https://cloud.google.com/bigtable/quotas#storage-per-node)

# Reading

## Best practices
- Best practices: Building containers https://cloud.google.com/solutions/best-practices-for-building-containers
- Best practices: Compute Engine region selection https://cloud.google.com/solutions/best-practices-compute-engine-region-selection
- Best practices: Bigtable schema design https://cloud.google.com/bigtable/docs/schema-design
- Best practices: Cloud Spanner schema design https://cloud.google.com/spanner/docs/schema-design
- Best practices: Cloud Storage https://cloud.google.com/storage/docs/best-practices
- Best Practices: Datastore https://cloud.google.com/datastore/docs/best-practices
- Best Practices: Firestore https://cloud.google.com/firestore/docs/best-practices

## Networking
- https://cloud.google.com/architecture/best-practices-vpc-design

### Cloud Interconnect
Cloud Interconnect extends your on-premises network to Google's network through a highly available, low latency connection. You can use Dedicated Interconnect to connect directly to Google or use Partner Interconnect to connect to Google through a supported service provider.

- https://cloud.google.com/network-connectivity/docs/interconnect
- https://cloud.google.com/network-connectivity/docs/how-to/choose-product
- https://cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities


|Solution|Capacity|Description|Connectivity|
|-|-|-|-|
|Dedicated Interconnect|10-Gbps or 100-Gbps circuits with flexible VLAN attachment capacities from 50 Mbps to 50 Gbps.|A direct connection to Google, must meet Google's network in colocation facility |not through the public internet.|
|Partner Interconnect|Flexible capacities from 50 Mbps to 50 Gbps.| connectivity through one of our supported service providers.|not through the public internet.|

## Services
- Overview of Google Cloud services https://cloud.google.com/docs/overview/cloud-platform-services
- https://cloud.google.com/products/
- https://cloud.google.com/products/databases

### AppEngine
- https://cloud.google.com/appengine
- https://cloud.google.com/appengine/docs/flexible/python/splitting-traffic

### Compute Engine
- Managed Instance Group https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups

### Cloud Functions
- Run your code in the cloud with no servers or containers to manage. Cloud Functions is a scalable, pay-as-you-go functions as a service (FaaS) product to help you build and connect event driven services with simple, single purpose code.
- Cloud Functions is event-driven and is not meant for long-running tasks.

https://cloud.google.com/functions

### Cloud Tasks
- Distributed task queues
- Cloud Tasks is a fully managed service that allows you to manage the execution, dispatch, and delivery of a large number of distributed tasks. Using Cloud Tasks, you can perform work asynchronously outside of a user or service-to-service request.


https://cloud.google.com/tasks

### Cloud Scheduler
Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. It allows you to schedule virtually any job, including batch, big data jobs, cloud infrastructure operations, and more. You can automate everything, including retries in case of failure to reduce manual toil and intervention. Cloud Scheduler even acts as a single pane of glass, allowing you to manage all your automation tasks from one place.

https://cloud.google.com/scheduler

### Cloud Run
Cloud Run is a managed compute platform that enables you to run containers that are invocable via requests or events. Cloud Run is serverless: it abstracts away all infrastructure management, so you can focus on what matters most ??? building great applications.

- https://cloud.google.com/run/docs/fit-for-run
- https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration

### Cloud Endpoints
Endpoints is an API management system that helps you secure, monitor, analyze, and set quotas on your APIs using the same infrastructure Google uses for its own APIs. 

Depending on where your API is hosted and the type of communications protocol your API uses:

|Option|Limitation|
|-|-|
|OpenAPI||
|gRPC|Not supported on App Engine or Cloud Functions|
|Endpoints Frameworks|Supported only on App Engine standard Python 2.7 and Java 8|


- https://cloud.google.com/endpoints/docs

### 
- https://cloud.google.com/resource-manager/docs

### GKE
- GKE - Custom and external metrics https://cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics
- Troubleshooting GKE https://cloud.google.com/kubernetes-engine/docs/troubleshooting
- Migrating a monolithic to microservices on GKE https://cloud.google.com/solutions/migrating-a-monolithic-app-to-microservices-gke

#### Auto-scaling
- https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler
- https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler
- https://cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps

### Cloud Build
With Cloud Build, continuously build, test, and deploy software across all languages and in multiple environments

- https://cloud.google.com/build/docs/configuring-builds/configure-build-step-order
- https://cloud.google.com/build/docs/configuring-builds/create-basic-configuration
- https://cloud.google.com/build/docs/build-config
- https://cloud.google.com/solutions/continuous-delivery/

#### Good to know
There is a persistent file system that is shared between steps in a Cloud Build. We change the story to be:
1. Deploy the Cloud Function.
2. Save the results of calling the Cloud Function to a file.
3. Delete the Cloud Function.
4. Test the content of the file.
Since step 2 can now never fail, step 3 is executed and step 4 defines the outcome of the build as a whole.

### Cloud Debugger
- https://cloud.google.com/source-repositories/docs/debug-overview
- https://cloud.google.com/source-repositories/docs/debug-snapshots
- https://cloud.google.com/debugger/docs/source-options#github

### Cloud Compute
- https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups

### BigQuery
BigQuery is a data warehouse. It has limited update/delete capabilities for inserted rows and hence is a bad choice for user session data, which changes as the session with the user progresses.
- https://cloud.google.com/solutions/building-scalable-web-apps-with-cloud-datastore
- https://cloud.google.com/bigquery/docs/loading-data-cloud-firestore
- https://cloud.google.com/blog/topics/developers-practitioners/how-migrate-premises-data-warehouse-bigquery-google-cloud


#### Syntax
- JOIN types https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#join_types

| Join | Description | Example |
| - | - | - |
|[INNER] JOIN | An INNER JOIN, or simply JOIN, effectively calculates the Cartesian product of the two from_items and discards all rows that do not meet the join condition.| `FROM A INNER JOIN B ON A.w = B.y` |
| CROSS JOIN | returns the Cartesian product of the two from_items. In other words, it combines each row from the first from_item with each row from the second from_item.| `FROM A CROSS JOIN B` |
| FULL [OUTER] JOIN | A FULL OUTER JOIN (or simply FULL JOIN) returns all fields for all rows in both from_items that meet the join condition.| `FROM A FULL OUTER JOIN B ON A.w = B.y`|
| LEFT [OUTER] JOIN | A LEFT OUTER JOIN (or simply LEFT JOIN) for two from_items always retains all rows of the left from_item in the JOIN operation, even if no rows in the right from_item satisfy the join predicate. | `FROM A LEFT OUTER JOIN B ON A.w = B.y` |
| RIGHT [OUTER] JOIN | A RIGHT OUTER JOIN (or simply RIGHT JOIN) is similar and symmetric to that of LEFT OUTER JOIN. | `FROM A RIGHT OUTER JOIN B ON A.w = B.y` |


### Anthos
- Introduction to Anthos https://cloud.google.com/anthos

Migration types [https://cloud.google.com/architecture/migration-to-gcp-getting-started]

- Lift and shift: you move workloads from a source environment to a target environment with minor or no modifications or refactoring.
- Improve and move: modernize the workload while migrating it.
- Remove and replace (or rip and replace): you decommission an existing app and completely redesign and rewrite it as a cloud-native app.

Migration tools
- [Kf](https://cloud.google.com/migrate/kf/docs/2.9/getting-started) offers developers the Cloud Foundry experience while empowering operators to adopt declarative Kubernetes practice. It makes migrating Cloud Foundry workloads to Kubernetes straightforward, and most importantly, avoids major changes to developer workflows. 
- https://cloud.google.com/solutions/modernize-apps-with-anthos



### Cloud Sql
- https://cloud.google.com/sql/docs/
- https://cloud.google.com/sql/docs/postgres/import-export/importing
- https://cloud.google.com/solutions/migrating-postgresql-to-gcp
- https://www.techonthenet.com/sql/union.php
- https://cloud.google.com/sql

#### Cloud SQL Proxy
- https://cloud.google.com/sql/docs/mysql/external-connection-methods

#### Migration
- https://cloud.google.com/solutions/migrating-postgresql-to-gcp
- https://cloud.google.com/sql/docs/postgres/import-export/importing

### Cloud Storage
- https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fcloud.google.com%2Fstorage%2Fdocs%2Fstorage-classes%23available_storage_classes
- https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fcloud.google.com%2Fstorage%2Fdocs%2Fstorage-classes%23standard-availability

Storage classes for any workload
Save costs without sacrificing performance by storing data across different storage classes. You can start with a class that matches your current use, then reconfigure for cost savings.

|Class | Storage Cost | Access Frequency | Description |
| - | - | - | - |
|Standard | High | Access data frequently | Hot or Frequently accessed data: websites, streaming videos, and mobile apps.|
|Nearline | Low | Access data only once a month | Data stored for at least 30 days, including data backup and long-tail multimedia content.|
|Coldline | Very low | Access data only once a year. | Data stored for at least 90 days, including disaster recovery.|
|Archive | Lowest | | Data stored for at least 365 days, including regulatory archives.|
| Multi-Regional Storage| High | Access data frequently | Equivalent to Standard Storage, except it can only be used for objects stored in multi-regions or dual-regions. |


### BigTable
Bigtable is a NoSQL DB is more performant and stores data in a unique way which can help with time-series data (such as Financial market data).
- https://cloud.google.com/bigtable/docs/overview
- https://cloud.google.com/bigtable/docs/schema-design#types_of_row_keys
- https://cloud.google.com/bigtable/docs/schema-design-time-series#ensure_that_your_row_key_avoids_hotspotting

### Firestore
Firestore is the next generation of Datastore. Easily develop rich applications using a fully managed, scalable, and serverless document database.

Firestore in Native mode is recommended for storing user-session information and is a natural choice for this test.
- https://cloud.google.com/architecture/building-scalable-web-apps-with-cloud-datastore

### Memorystore
Memorystore is an in-memory database not suitable for data analysis.

### Logging
- Setup https://cloud.google.com/logging/docs/agent/installation
- Quotas https://cloud.google.com/logging/quotas

#### Audit
| Log Type | Description | Documentation |
| - | - | - |
| Admin activity| show destroy, create, modify, etc. events for a VM instance. | [link](https://cloud.google.com/logging/docs/audit/#admin-activity) |
| Data access| Show read activities. | [link](https://cloud.google.com/logging/docs/audit/#data-access)
| Syslog | A service running in systemd that outputs to stdout will have logs in syslog and will be scraped by the logging agent. | [link](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/tree/master/configs/config.d) |
| System event| Tell you about live migration, etc. | [link](https://cloud.google.com/logging/docs/audit/#system-event)|
| VPC flow logs | uses the substrate specific logging to capture everything. | [link](https://cloud.google.com/vpc/docs/using-flow-logs) [course](https://cloudacademy.com/course/implementing-a-gcp-virtual-private-cloud-1224/vpc-flow-logs/)

#### Export
Logging retains app and audit logs for a limited period of time. You might need to retain logs for longer periods to meet compliance obligations. Alternatively, you might want to keep logs for historical analysis.

You can route logs to Cloud Storage, BigQuery, and Pub/Sub. Using filters, you can include or exclude resources from the export. For example, you can export all Compute Engine logs but exclude high-volume logs from Cloud Load Balancing.

- Configuration https://cloud.google.com/logging/docs/export/configure_export_v2
- Sinks https://cloud.google.com/logging/docs/export/using_exported_logs



### Error Reporting
- https://cloud.google.com/error-reporting/docs/troubleshooting

## Performance
- https://www.atlassian.com/software/clover
- https://jmeter.apache.org/
- https://snyk.io/blog/secure-code-review/
- https://cloud.google.com/solutions/application-deployment-and-testing-strategies#canary_test_pattern
- https://cloud.google.com/blog/products/application-development/release-with-confidence-how-testing-and-cicd-can-keep-bugs-out-of-production

## Monitoring

- Introduction to Prometheus https://cloud.google.com/stackdriver/docs/solutions/gke/prometheus
- Introduction to OpenTelemetry https://cloud.google.com/learn/what-is-opentelemetry

https://www.youtube.com/watch?v=CjGv1bDy9rI

### Cloud Trace
- Cloud Trace is a distributed tracing system that collects latency data from your applications and displays it in the Google Cloud Console. You can track how requests propagate through your application and receive detailed near real-time performance insights.
- All Cloud Run, Cloud Functions and App Engine standard applications are automatically traced and libraries are available to trace applications running elsewhere after minimal setup.

https://cloud.google.com/trace/images/quickstart-waterfall-example.png

https://cloud.google.com/trace

### Cloud Profiler
Cloud Profiler is a statistical, low-overhead profiler that continuously gathers CPU usage and memory-allocation information from your production applications. It attributes that information to the application's source code, helping you identify the parts of the application consuming the most resources, and otherwise illuminating the performance characteristics of the code.

https://cloud.google.com/profiler/docs/images/profiler-quickstart-filtered.png

https://cloud.google.com/profiler/

## DevOps
- https://spinnaker.io/



### Deployments Strategies

- Blue/green deployments: gradually transfers user traffic from a previous version (blue) of an app or microservice to a new release???both (green) of which are running in production. 
- Traffic-splitting deployments: allows you to conduct A/B testing between your versions and provides control over the pace when rolling out features. When using a traffic-splitting deployment, you can specify the percentage of production traffic and the amount of time to monitor a new application version before completing the deployment. Once the deployment starts, you can monitor the health of your new application version by tracking events/logs in real time.
- Rolling deployments: A rolling deployment is a deployment strategy that slowly replaces previous versions of an application with new versions of an application by completely replacing the infrastructure on which the application is running. For example, in a rolling deployment in Amazon ECS, containers running previous versions of the application will be replaced one-by-one with containers running new versions of the application. A rolling deployment is generally faster than a blue/green deployment; however, unlike a blue/green deployment, in a rolling deployment there is no environment isolation between the old and new application versions. This allows rolling deployments to complete more quickly, but also increases risks and complicates the process of rollback if a deployment fails.
- Canary deployments: Canary deployments are a pattern for rolling out releases to a subset of users or servers. The idea is to first deploy the change to a small subset of servers, test it, and then roll the change out to the rest of the servers. The canary deployment serves as an early warning indicator with less impact on downtime: if the canary deployment fails, the rest of the servers aren't impacted.


Managing Deployments Using Kubernetes Engine https://www.cloudskillsboost.google/focuses/639?parent=catalog

## Security
- Securing Cloud Functions https://cloud.google.com/functions/docs/securing
- Practicing the principle of least privilege https://cloud.google.com/blog/products/identity-security/dont-get-pwned-practicing-the-principle-of-least-privilege
- Key rotation in Cloud Key Management Service https://cloud.google.com/kms/docs/key-rotation
- Container analysis and vulnerability scanning https://cloud.google.com/container-registry/docs/container-analysis
- https://cloud.google.com/container-analysis/docs

### Resource Manager
Google Cloud provides container resources such as organizations and projects that allow you to group and hierarchically organize other Google Cloud resources. This hierarchical organization helps you manage common aspects of your resources, such as access control and configuration settings. The Resource Manager API enables you to programmatically manage these container resources.

https://cloud.google.com/resource-manager/docs

### Permission
See https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations

- A general recommendation is to have one project per application per environment.
- We recommend collecting users with the same responsibilities into groups and assigning IAM roles to the groups rather than to individual users. 
- We recommend that you use service accounts for server-to-server interactions.

## Other
- https://www.restapitutorial.com/httpstatuscodes.html
- Google Cloud system design considerations https://cloud.google.com/architecture/framework/design-considerations

- Case Study: HipLocal https://services.google.com/fh/files/blogs/master_case_study_hiplocal.pdf



- Patterns for scalable and resilient apps https://cloud.google.com/solutions/scalable-and-resilient-apps


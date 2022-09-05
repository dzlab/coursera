# Professional Cloud DevOps Engineer
See sections https://cloud.google.com/certification/guides/cloud-devops-engineer

Kubernetes Concepts:
- https://kubernetes.io/docs/concepts/
- https://www.mirantis.com/blog/kubernetes-cheat-sheet/
- secrets - [link](https://kubernetes.io/docs/concepts/configuration/secret/)

## Section 2. Building and implementing CI/CD pipelines for a service
- Artifact Registry
  - https://cloud.google.com/artifact-registry
  - Software supply chain security - [link](https://cloud.google.com/software-supply-chain-security/docs/overview)
  - region vs multi-region locations - [link](https://cloud.google.com/artifact-registry/docs/repositories/repo-locations)
  - Cloud Run deploy from Source - [link](https://cloud.google.com/run/docs/deploying-source-code)
  - GKE image streaming - [link](https://cloud.google.com/kubernetes-engine/docs/how-to/image-streaming)
  - Cloud build integration - [link](https://cloud.google.com/artifact-registry/docs/configure-cloud-build)
  - Container analysis and vulnerability scanning - [link](https://cloud.google.com/artifact-registry/docs/analysis)
  - VPC service controls - [link](https://cloud.google.com/vpc-service-controls/docs/overview)
  - Binary Authorization in GCP - [link](https://cloud.google.com/binary-authorization/docs/overview)
  - Binary Authorization Kritis (open source) - [link](https://github.com/grafeas/kritis/blob/master/docs/binary-authorization.md)
- Spinnaker:
  - Concepts: https://spinnaker.io/docs/concepts/
  - Kubernetes: https://spinnaker.io/docs/guides/user/kubernetes-v2/
  - Deployment Strategies: https://spinnaker.io/docs/guides/user/kubernetes-v2/rollout-strategies/ 
  - https://cloud.google.com/blog/products/gcp/guest-post-multi-cloud-continuous-delivery-using-spinnaker-at-waze
  - Route Traffic During a Deployment (Blue/Green) - [link](https://spinnaker.io/docs/guides/user/kubernetes-v2/traffic-management/#route-traffic-during-a-deployment-bluegreen)
- Anthos:
  - https://cloud.google.com/anthos
  - https://cloud.netapp.com/blog/hybrid-deployment-with-google-anthos-an-intro-gc-cvo-blg
  - Binary Autorization https://cloud.google.com/binary-authorization/docs
- Cloud Build:
  - CI and CD with Cloud Build: https://cloud.google.com/build
  - CI/CD pipeline triggers with Cloud Source Repositories, external SCM, and Pub/Sub [link](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#whats_next)
  - Managing secrets: https://cloud.google.com/build/docs/securing-builds/use-secrets
- Skafold:
  - https://cloud.google.com/skaffold
  - https://cloud.google.com/deploy/docs/using-skaffold
  - Skafold https://cloud.google.com/blog/products/application-development/kubernetes-development-simplified-skaffold-is-now-ga
- Cloud Code:
  - https://cloud.google.com/code
- Binary Autorization
  - https://cloud.google.com/binary-authorization
- IAM:
  - https://www.strongdm.com/blog/gcp-iam-roles
  - policies: https://cloud.google.com/iam/docs/policies
  - https://ermetic.com/blog/gcp/introduction-to-iam-in-google-cloud-platform-gcp/
- Cloud Deploy
  - Overview - [link](https://cloud.google.com/deploy/docs/overview)
## Section 3. Implementing service monitoring strategies
- Cloud Logging - [link](https://cloud.google.com/logging)
  - Configure the Logging agent https://cloud.google.com/logging/docs/agent/logging/configuration
  - Customizing Cloud Logging logs for Google Kubernetes Engine with Fluentd - [link](https://cloud.google.com/architecture/customizing-stackdriver-logs-fluentd)
  - Cloud Logging API https://cloud.google.com/logging/docs/apis
- Cloud Monitoring - [link](https://cloud.google.com/monitoring)
  - How to guides https://cloud.google.com/monitoring/docs/how-to
  - Kubernetes monitoring - [link](https://cloud.google.com/stackdriver/docs/solutions/gke/observing)
  - Metrics Explorer: create charts - [link](https://cloud.google.com/monitoring/charts/metrics-explorer)
  - Metrics Explorer: select metrics - [link](https://cloud.google.com/monitoring/charts/metrics-selector)
  - Alerts - [link](https://cloud.google.com/monitoring/alerts)
  - Deliver Cloud Monitoring notifications to third-party services - [link](https://cloud.google.com/community/tutorials/delivering-cloud-monitoring-notifications-to-third-party-services)
  - Cloud Monitoring integrations - [link](https://cloud.google.com/monitoring/agent/integrations)
  - Multiple projects - [link](https://cloud.google.com/monitoring/settings)
  - Metrics Scope - [link](https://cloud.google.com/monitoring/settings/manage-api)
  - Create public uptime checks - [link](https://cloud.google.com/monitoring/uptime-checks/)
  - Google Cloud metrics - [link](https://cloud.google.com/monitoring/api/metrics_gcp)
  - Legacy Monitoring and Logging agent metrics - [link](https://cloud.google.com/monitoring/api/metrics_agent)
  - Stackdriver tips and tricks: Understanding metrics and building charts - [link](https://cloud.google.com/blog/products/management-tools/stackdriver-tips-and-tricks-understanding-metrics-and-building-charts)
  - Manage custom dashboards - [link](https://cloud.google.com/monitoring/charts/dashboards)
  - Introduction to alerting - [link](https://cloud.google.com/monitoring/alerts/)
- Cloud Logging Platform
  - Cloud Audit Logs (data access logs) - [link](https://cloud.google.com/logging/docs/audit)
  - VPC flow logs - [link](https://cloud.google.com/vpc/docs/using-flow-logs)
  - logs-based metrics - [link](https://cloud.google.com/logging/docs/logs-based-metrics)
  - logging exclusion - [link](https://cloud.google.com/logging/docs/routing/overview#exclusions)
  - logging export - [link](https://cloud.google.com/logging/docs/export/configure_export_v2)
  - resource hierarchy - [link](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)
  - project-level / org-level export
  - export logs in Cloud Storage and BigQuery 
  - restrict access to audit logs - [link](https://cloud.google.com/logging/docs/audit/configure-data-access)
  - restrict export configuration - [link](https://cloud.google.com/compute/docs/images/restricting-image-access)

### Section 4. Optimizing service performance
- Identify performance issues:
  - Google Cloud’s operations suite - [link](https://cloud.google.com/blog/topics/developers-practitioners/introduction-google-clouds-operations-suite)
  - Cloud Trace - [link](https://cloud.google.com/trace)
  - Cloud Profiler - [link](https://cloud.google.com/profiler/docs)
  - Troubleshoot issues with the image/OS - [link](https://cloud.google.com/artifact-registry/docs/docker/troubleshoot)
  - Troubleshooting Virtual Machine Networking Issues on GCP - [link](https://cloudacademy.com/course/troubleshooting-virtual-machine-networking-issues-gcp-2801/ssh-errors/)
  - Troubleshoot network issues (e.g., VPC flow logs, firewall logs, latency, view network details)
  - Compute networking issues: - [link](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-networking)
- Cloud Debugger - [link](https://cloud.google.com/debugger/docs)
  - Debug Snapshots - [link](https://cloud.google.com/debugger/docs/using/snapshots)
  - Debug Logpoints - [link](https://cloud.google.com/debugger/docs/using/logpoints)
  - App Engine local development server - [link](https://cloud.google.com/appengine/docs/legacy/standard/python/tools/using-local-server)
- Optimize resource utilization
  - Identify resource utilization levels - [link](https://cloudacademy.com/course/optimizing-resource-utilization-on-gcp-1466/identifying-resource-utilization-levels/)
  - Manage preemptible VMs - [link](https://cloud.google.com/compute/docs/instances/preemptible)
  - Creating groups of preemptible instances - [link](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#creating_groups_of_preemptible_instances)


### Section 5. Managing service incidents
- Addressing Cascading Failures - [link](https://sre.google/sre-book/addressing-cascading-failures/)
- Distribute your VMs - [link](https://cloud.google.com/compute/docs/tutorials/robustsystems#distribute)
- Enabling connection draining - [link](https://cloud.google.com/load-balancing/docs/enabling-connection-draining)
- monitoring groups - [link](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups%29)

## Resources
https://ivam-luz.medium.com/how-to-pass-the-google-professional-cloud-devops-engineer-certification-ea809d69b0e5

https://cloud.google.com/certification/cloud-devops-engineer

https://github.com/sathishvj/awesome-gcp-certifications/blob/master/professional-cloud-devops-engineer.md

https://www.coursera.org/professional-certificates/sre-devops-engineer-google-cloud



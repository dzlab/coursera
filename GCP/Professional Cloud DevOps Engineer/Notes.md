## SLO, SLI, SLA
See https://sre.google/workbook/implementing-slos/

### SLI
While many numbers can function as an SLI, we generally recommend treating the SLI as the ratio of two numbers: the number of good events divided by the total number of events. For example:

- Number of successful HTTP requests / total HTTP requests (success rate)
- Number of gRPC calls that completed successfully in < 100 ms / total gRPC requests
- Number of search results that used the entire corpus / total number of search results, including those that degraded gracefully
- Number of “stock check count” requests from product searches that used stock data fresher than 10 minutes / total number of stock check requests
- Number of “good user minutes” according to some extended list of criteria for that metric / total number of user minutes

**error budget**: SLO is a target percentage and the error budget is 100% minus the SLO. For example, if you have a 99.9% success ratio SLO, then a service that receives 3 million requests over a four-week period had a budget of 3,000 (0.1%) errors over that period. If a single outage is responsible for 1,500 errors, that error costs 50% of the error budget.


Table 2-1. Potential SLIs for different types of components

|Type of service|Type of SLI|Description|
|-|-|-|
|Request-driven|Availability|The proportion of requests that resulted in a successful response.
|Request-driven|Latency|The proportion of requests that were faster than some threshold.
|Request-driven|Quality|If the service degrades gracefully when overloaded or when backends are unavailable, you need to measure the proportion of responses that were served in an undegraded state. For example, if the User Data store is unavailable, the game is still playable but uses generic imagery.
|Pipeline|Freshness|The proportion of the data that was updated more recently than some time threshold. Ideally this metric counts how many times a user accessed the data, so that it most accurately reflects the user experience.
|Pipeline|Correctness|The proportion of records coming into the pipeline that resulted in the correct value coming out.
|Pipeline|Coverage|For batch processing, the proportion of jobs that processed above some target amount of data. For streaming processing, the proportion of incoming records that were successfully processed within some time window.
|Storage|Durability|The proportion of records written that can be successfully read. Take particular care with durability SLIs: the data that the user wants may be only a small portion of the data that is stored. For example, if you have 1 billion records for the previous 10 years, but the user wants only the records from today (which are unavailable), then they will be unhappy even though almost all of their data is readable.

SLOs and SLIs for Game Service https://sre.google/workbook/slo-document/

## Cloud Build
Cloud Build service account requires the Compute Engine Instance Admin role to be able to build VM images

1. Locate the Cloud Build service account (it has the role `roles/cloudbuild.builds.builder`)
```shell
CLOUD_BUILD_ACCOUNT=$(gcloud projects get-iam-policy $PROJECT --filter="(bindings.role:roles/cloudbuild.builds.builder)"  --flatten="bindings[].members" --format="value(bindings.members[])")
```
2. Add Compute Engine Instance Admin role (i.e. `roles/compute.instanceAdmin`) to the service account:

```shell
gcloud projects add-iam-policy-binding $PROJECT \
  --member $CLOUD_BUILD_ACCOUNT \
  --role roles/compute.instanceAdmin
```
Source https://cloud.google.com/build/docs/building/build-vm-images-with-packer

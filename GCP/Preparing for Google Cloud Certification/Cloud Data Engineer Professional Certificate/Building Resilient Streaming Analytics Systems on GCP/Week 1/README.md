# Week 1

## Introduction to Processing Streaming Data

### Quiz
**1. Question 1**

Dataflow offers the following that makes it easy to create resilient streaming pipelines when working with unbounded data:

(Select all 2 correct responses)

- [x] Ability to flexibly reason about time
- [x] Controls to ensure correctness
- [ ] Global message bus to buffer messages
- [ ] SQL support to query in-process results


**2. Question 2**
Match the GCP product with its role when designing streaming systems

|Product|Role|
|-|-|
|__ 1. Pub/Sub|A. Controls to handle late-arriving and out-of-order data|
|__ 2. Dataflow|B. Global message queue|
|__ 3. BigQuery|C. Latency in the order of milliseconds when querying against overwhelming volume|
|__ 4. Bigtable|D. Query data as it arrives from streaming pipelines|


- [ ]
  - A
  - B
  - D
  - C

- [x]
  - B
  - A
  - D
  - C

- [ ] 
  - C
  - A
  - D
  - B

- [ ] 
  - D
  - A
  - B
  - C

## Cloud Pub/Sub

### Quiz: Serverless Messaging with Cloud Pub/Sub
**1. Question 1**

Which of the following about Cloud Pub/Sub is NOT true?

- [ ] Pub/Sub simplifies systems by removing the need for every component to speak to every component
- [ ] Pub/Sub connects applications and services through a messaging infrastructure
- [x] Pub/Sub stores your messages indefinitely until you request it


**2. Question 2**

True or False?

Cloud Pub/Sub guarantees that messages delivered are in the order they were received

- [ ] True
- [x] False


**3. Question 3**
Which of the following about Cloud Pub/Sub topics and subscriptions are true?

(Select all 2 correct responses)

- [x] 1 or more publisher(s) can write to the same topic
- [x] 1 or more subscriber(s) can request from the same subscription
- [ ] Each topic will deliver ALL messages for a topic for each subscriber
- [ ] Each topic MUST have at least 1 subscription


**4. Question 4**

Which of the following delivery methods is ideal for subscribers needing close to real time performance?

- [ ] Pull Delivery
- [x] Push Delivery


## Cloud Dataflow capabilities for streaming data

### Quiz: Cloud Dataflow Streaming Features
**1. Question 1**

The Dataflow models provides constructs that map to the four questions that are relevant in any out-of-order data processing pipeline:

|Questions|Constructs|
|-|-|
|__ 1. What results are calculated?|A. Answered via Event-time windowing|
|__ 2. Where in event time are results calculated?|B. Answered via transformations|
|__ 3. When in processing time are results materialized?|C. Answered via Accumulation modes|
|__ 4. How do refinements of results relate?|D. Answered via Watermarks, triggers, and allowed lateness.|

- [ ]
  - A
  - D
  - C
  - B

- [ ]
  - B
  - A
  - D
  - C

- [ ]
  - C
  - A
  - D
  - B

- [ ] x
  - D
  - B
  - A
  - C



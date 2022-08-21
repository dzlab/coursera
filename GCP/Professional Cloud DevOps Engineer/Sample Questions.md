# Sample Questions.md

## 1
You are helping with the design of an e-commerce application. The web application receives web requests and  stores sales transactions in a database. A batch job runs every hour to trigger analysis of sales numbers, available inventory, and forecasted sales numbers. You want to identify minimal Service Level Indicators (SLIs) for the application to ensure that forecasted numbers are based on the latest sales numbers. Which SLIs should you set for the application?

- [ ] A.
  - Web Application - Quality 
  - Database - Availability
  - Batch Job - Coverage
- [ ] B.
  - Web Application - Latency
  - Database - Latency
  - Batch Job - Throughput
- [x] C.
  - Web Application - Availability
  - Database - Availability
  - Batch Job - Frenshness
- [ ] D.
  - Web Application - Availability, Quality
  - Database - Durability
  - Batch Job - Coverage

**Feedback**
```diff
- A is not correct because Web Application Quality and Batch Job Coverage SLIs don’t help in meeting the objective.
- B is not correct because the latency of the web application, although important to measure, doesn’t help with meeting the objective of the latest data available in the database.
+ C is the correct answer because these are the minimal set of SLIs to measure in order to meet the objective of using the latest data in a batch job.
- D is not correct because Web Application Quality and Batch Job Coverage SLIs don’t help in meeting the objective.
```
https://landing.google.com/sre/workbook/toc/

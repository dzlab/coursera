# Week 1 Model Serving: Introduction

## Introduction to Model Serving

### Introduction to Model Serving
#### What exactly is Serving a Model?
Training a good machine learning model is only the first part. You do need to make your model available to your end-users, and you do this by either providing access to the model on your server, which we'll explore this week. Serving also includes the facility to deploy a model file to an application, and this is a scenario that's usually found with mobile ML.
![image](https://user-images.githubusercontent.com/1645304/132610545-4385c1af-8146-4fec-8e8f-7840b32616d7.png)

#### Model Serving Patterns
These components are used by an inference process which is aimed at getting the data to be ingested by a model in order to compute predictions.
![image](https://user-images.githubusercontent.com/1645304/132610725-491db96b-5847-472b-8ebd-97ae29d5795a.png)

#### ML workflows
![image](https://user-images.githubusercontent.com/1645304/132610832-11401ca2-0374-4ee9-adf0-75223dc2f89b.png)

#### Important Metrics
The important metrics to optimize online inference are: latency, throughput, and cost. 
![image](https://user-images.githubusercontent.com/1645304/132610930-9d6bf949-3eb7-421e-b67b-eb8f106e73fc.png)

#### Latency
![image](https://user-images.githubusercontent.com/1645304/132611079-4205180f-cdb4-4596-9907-2b71c212426a.png)

#### Throughput
![image](https://user-images.githubusercontent.com/1645304/132611117-cf90bda0-0776-4ce6-bd54-090d86e31ef9.png)

#### Cost
Consider the cost for things like CPUs, hardware accelerators like GPUs, and caches for storing input features for easy retrieval with minimum latency.
![image](https://user-images.githubusercontent.com/1645304/132611197-d1b6cefc-38fc-4fdd-8fec-1d4077ff0cc9.png)

#### Minimising Latency, Maximizing Throughput
We can scale the infrastructure used to meet these thresholds of response time and throughput, but this can increase the cost proportionally.
![image](https://user-images.githubusercontent.com/1645304/132611303-2bf169b2-07bf-4812-a58c-9c6921e96469.png)

#### Balance Cost, Latency and Throughput
there are tactics you can use to try to minimize any impact on your customer while you attempt to control cost. These may include reducing costs by sharing assets like GPU's, using multiple models to increase throughput, and perhaps even exploring optimizing your models.
![image](https://user-images.githubusercontent.com/1645304/132611481-1584eb6f-7d03-47ce-8bbf-b108884c8030.png)

### Quiz: Introduction to Model Serving

**Question 1**

What are the three key components we should consider when serving an ML Model in a production environment? (Select all that apply)

- [x] A model
- [x] An interpreter
- [ ] An orchestrator
- [x] Input Data

**Question 2**

What happens after a while in operation to an offline-trained model dealing with new real-live data?

- [x] The model becomes stale.
- [ ] The model abruptly forgets all previously learned information.
- [ ] The model adapts to new patterns.

**Question 3**

In applications that are not user-facing, is throughput more critical than latency for customer satisfaction?

- [ ] No, because users might complain that the app is too slow.
- [x] Yes, in this case, we are concerned with maximizing throughput with the lowest CPU usage.

**Question 4**

Nowadays, developers aim to minimize latency and maximize throughput in customer-facing applications. However, in doing so, infrastructure scales and costs increase. So, what strategies can developers implement to balance cost and customer satisfaction? (Select all that apply)

- [x] GPU sharing
- [x] Multi-model serving
- [x] Optimizing inference models
- [ ] Stress testing

### Reading: Ungraded Labs - Best Practices
As you progress through this course you will see that the majority of ungraded labs are hosted in our [public repo](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public) and are meant to be run in your local machine using a terminal. 

Some of them do not require you to have a cloned version of the repo but some do. For this reason, we encourage you to clone the repo right away. For the labs that rely on files within the repo, the best way to follow along is to read its documentation from your browser while working on the cloned version of the repo on your local machine.

To clone the repo, use the following command:
```
git clone https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public.git
```
or for cloning via SSH use:
```
git clone git@github.com:https-deeplearning-ai/machine-learning-engineering-for-production-public.git
```

If you are unsure which method to use, go for the first one.


Have fun in the ungraded labs! 

### Reading: Ungraded Lab - Introduction to Docker
During this lab you will get a high level overview of Docker and some instructions to install it on your local machine.

Follow this [link](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week1-ungraded-labs/C4_W1_Lab_1_Docker_Intro.md) to start the lab!

## Introduction to Model Serving Infrastructure

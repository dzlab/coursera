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

### Introduction to Model Serving Infrastructure
#### Optimizing Models for Serving
More complex model architectures including more and more features. And this often results in longer prediction latencies and but hopefully a boost in prediction accuracy.
![image](https://user-images.githubusercontent.com/1645304/132785673-a2b43268-240a-4688-b3ee-0d66920c8670.png)

#### As Model Complexity Increases Cost Increases
As models become more complex with more features. The resource requirements increase for every part of the training and serving infrastructure, increased resource requirements means increased costs.
And increased hardware requirements management of larger model registries and this results in a higher support and maintenance burden.
![image](https://user-images.githubusercontent.com/1645304/132785757-fba38cd2-0f6c-4f20-9a4d-a750912723ba.png)

#### Balancing Cost and Complexity
The Challenge for ML practitionners is to balance complexity and cost.

#### Optimizing and Satisficing Metrics
- model's optimizing metric reflects the model's predictive effectiveness and this includes things like accuracy, precision, recall, and so on.
- Models gating metric reflects an operational constraint that the model has to satisfy, such as prediction latency.

![image](https://user-images.githubusercontent.com/1645304/132785999-7090f30d-1f60-415e-a6d6-00ecff9b6bcf.png)

One approach is to:
1. Specify the serving infrastructure, CPU, GPU and all that. And then 
2. Start increasing your model complexity to improve your model's predictive power until you hit one or more of your gating metrics on that infrastructure.
3. Assess the results and either accept the model as it is or work to improve accuracy and or reduce complexity or make the decision to increase the specifications of the serving infrastructure.
![image](https://user-images.githubusercontent.com/1645304/132786329-8faf7696-0a09-40ce-8184-a1396aef0c6b.png)

#### Use of Accelerators in Serving Infrastructure
These decisions can have a significant effect on your projects budget. 
- GPUs tend to be optimized for parallel through pot and they are often used in training infrastructure. 
- TP use as well as being useful in training have advantages for large complex models and large batch sizes, especially during inference.

![image](https://user-images.githubusercontent.com/1645304/132786550-b21be0c6-6129-4d5f-890e-74ca56ea303d.png)

#### Maintaining Input Feature Lookup
You may need caches to retrieve data with low latency (e.g. real time prediction) as you cannot wait many seconds for retrieving data from the database. And this has cost implications.
![image](https://user-images.githubusercontent.com/1645304/132786952-caf1880a-5697-4cd5-8a45-fffdb34f443a.png)


#### NoSQL Databases: Caching and Feature Lookup
You have to carefully choose from the different available offerings based on your requirements and then balance that with your budget constraints.
![image](https://user-images.githubusercontent.com/1645304/132787007-4cb499fb-ee57-4272-bdd7-b90c0b3a41c7.png)

### Deployment Options
#### Model Deployments
- A centralized model in a data center that's access via a remote call.
- distributed instances of the model to users so they can use it locally such as a mobile or embedded system. 

#### Running in huge Data Centers
Costs and efficiency are important at any scale, companies like Google constantly look for ways to improve resource utilization and reduce costs in applications in data centers.
![image](https://user-images.githubusercontent.com/1645304/132787602-58ab5c03-465d-47a4-9498-087dd1ff726f.png)

#### Constrained Environment: Mobile Phone
- At most one GPU, which is shared by a number of applications.
- limited GPU available and using it can lead to battery draining quickly or makes the phone too hot because of complex operations in your ML model. 
- Storage limitation since users don't appreciate large apps using up storage on their phones. 

![image](https://user-images.githubusercontent.com/1645304/132787767-4c9aa93b-8f71-4cb0-a50f-a4f708a95483.png)


#### Restrictions in a Constrained Environment
You may choose to deploy a model to a server and then expose it through a REST API so that we can use it for inference in our app. This might not be feasible to deploy a model to a server in environments where prediction latency is super-important or when a network connection may not always be available (a.g. autonomuous vehicule).

![image](https://user-images.githubusercontent.com/1645304/132788175-cc6327bf-368b-4eab-894d-dfd61138155b.png)


#### Prediction Latency is Almost Always important

![image](https://user-images.githubusercontent.com/1645304/132788422-b5589af2-8458-455b-8017-707af5cb44b3.png)


#### Choose Best Model for the Task
One example is MobileNets, and these are models that are specifically designed for computer vision on mobile devices. All the work in performing trade-offs for the best mobile model had been done for you already and you can build on this.
![image](https://user-images.githubusercontent.com/1645304/132788489-aa4d674c-ca9e-4edc-bb83-56fee5347bc2.png)

### Improving Prediction Latency and Reducing Resource Costs

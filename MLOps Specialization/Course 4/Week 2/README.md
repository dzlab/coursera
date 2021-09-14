# Week 2 Model Serving Architecture

## Model Serving Architecture

### Model Serving Architecture

#### ML Infrastructure
![image](https://user-images.githubusercontent.com/1645304/133006141-a9dae8ad-abae-4be3-bd95-8b8489d64c48.png)

#### Model Serving
![image](https://user-images.githubusercontent.com/1645304/133006157-32b394d3-2c91-44e7-8a25-360111982ed6.png)

#### Model servers
![image](https://user-images.githubusercontent.com/1645304/133006172-2e4991fb-2e47-4904-b6ab-5a307a976a94.png)

![image](https://user-images.githubusercontent.com/1645304/133006184-0cfc305d-e99b-49b5-9681-2c3b1bf0fa7f.png)

### Model Servers: TensorFlow Serving

#### TensorFlow Serving
TensorFlow Serving provides
- Both batch and real time inference.
- Multi model serving allows you to have multiple models for the same task and the server chooses between them.For example, for A/B testing audience segmentation and more. 
- remote procedure calls or traditional rest endpoints on which you can call your server.
![image](https://user-images.githubusercontent.com/1645304/133006307-285e982f-b306-4f0d-8053-ed530264608c.png)

#### TensorFlow Serving Architecture

![image](https://user-images.githubusercontent.com/1645304/133006379-08e5cb99-a86d-4cc3-b311-34d1682896d8.png)

### Model Servers: Other Providers

#### NVIDIA Triton Inference Server
![image](https://user-images.githubusercontent.com/1645304/133006568-a81e0d9c-e938-4503-8bf7-1bfe8c8e5b9d.png)

![image](https://user-images.githubusercontent.com/1645304/133006583-ca9a25cb-6368-41a5-b095-0340bba4b1fe.png)

#### Designed for scalability
It Can integrate with KubeFlow pipelines for end to end AI workflow
![image](https://user-images.githubusercontent.com/1645304/133006599-df19a853-f3cc-4d4f-8374-69c1263cdf5f.png)

#### TorchServe
![image](https://user-images.githubusercontent.com/1645304/133006641-219eb884-8907-43af-9330-8e54bc5aa2df.png)

#### TorchServe Architecture
![image](https://user-images.githubusercontent.com/1645304/133006659-e9694322-2466-4287-9ba3-cfba1e7fa92e.png)

#### KFServing
![image](https://user-images.githubusercontent.com/1645304/133006683-5ecc9244-0fa5-4de7-8717-adfc8b67a593.png)

### Documentation on model servers
The video lecture covered some of the most popular model servers: TensorFlow Serving, TorchServer, KubeFlow Serving and the NVidia Triton inference server.  Here are the links to relevant documentation for each of these options:

- TensorFlow Serving https://www.tensorflow.org/tfx/serving/architecture
- TorchServe https://github.com/pytorch/serve
- KubeFlow Serving https://www.kubeflow.org/docs/components/serving/
- NVIDIA Triton https://developer.nvidia.com/nvidia-triton-inference-server

### Quiz Model serving architecture
**1. Question 1**

What is the core idea of the TensorFlow Serving Architecture?

- [x] The servable
- [ ] The loader
- [ ] The manager
- [ ] The source

**2. Question 2**

True or False: Triton Inference Server simplifies deployment since it is compatible with trained AI models from any framework.

- [x] True
- [ ] False

**3. Question 3**

In the TorchServe architecture, where does the actual inference take place?

- [x] Model Workers at the backend
- [ ] Inference endpoints at the frontend
- [ ] Model Store

### Ungraded Lab - Deploy a ML model with FastAPI and Docker
During this lab you will work with FastAPI and Docker to deploy a Dockerized version of your model while learning important concepts for container-based applications.

Follow this [link](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week2-ungraded-labs/C4_W2_Lab_1_FastAPI_Docker/README.md) to start the lab!

## Scaling Infrastructure

### Scaling Infrastructure
#### Why is Scaling Important?
- The larger and more sophisticated the network, the more parameters that need to be tuned and fine-tuned. Large networks have many millions of parameters that need to be learned.
- When you deploy your model to a server. Huge volumes of requests to the server for inference can overwhelm it. The ability to scale the runtime inference, as well as the training is vital.

#### Vertical Scaling / Scale Up
![image](https://user-images.githubusercontent.com/1645304/133012188-36139d7f-b015-4522-a5e2-42cc10c09686.png)

#### Horizontal Scaling / Scale out
![image](https://user-images.githubusercontent.com/1645304/133012246-019f840f-cf59-4917-bfbe-7cc0ef7d2462.png)

#### Why Horizontal vs Vertical Scaling
![image](https://user-images.githubusercontent.com/1645304/133012297-d532dad9-400f-4856-9e37-7b9c762d05e4.png)

There are lots of vendors offering cloud platforms that allow you to scale horizontally. Keep an eye out for three things:
Can I manually scale? What happens if I say I only want any instances of a VM, for example. Can I autoscale? What happens if I want my app to automatically spin up and down based on demand? What does latency and costs look like? Finally, how aggressive is the system at spinning up and down based on my need? Then of course, the next question arises, and that is, how can I manage my additional VMs to ensure that they have the content on them that I want? For machine learning, there might be a lot of dependencies, access to data, permissions, and many other configurable items.

|Typical System Architecture|Virtual Machine (VM) Architecture|Containers Architecture|
|-|-|-|
|![image](https://user-images.githubusercontent.com/1645304/133013939-2d0aef86-0690-40ca-a1b3-74af6b206f46.png)|![image](https://user-images.githubusercontent.com/1645304/133016233-4aef2ec3-2ab4-4777-a403-c7483cbd0fb0.png)|![image](https://user-images.githubusercontent.com/1645304/133016294-8e9d3c10-28af-479d-9831-2824109fe76e.png)|

#### Containers Advantges
![image](https://user-images.githubusercontent.com/1645304/133017474-c3ae79ae-52b8-43ba-982a-38e18f10b7de.png)

#### Docker: Container Runtime
![image](https://user-images.githubusercontent.com/1645304/133017510-410bbac8-8784-41c9-87cb-85c616219b50.png)

#### Enter Container Orchestration
![image](https://user-images.githubusercontent.com/1645304/133017565-9635b2b6-2d85-434f-a4a9-62a8cc021d7b.png)

Popular Container Orchestration Tools:
- Kubernetes
- Docker Swarm

#### ML Workflow on Kubernetes - Kubeflow
![image](https://user-images.githubusercontent.com/1645304/133018496-46f1e926-59be-41ef-8bbe-e5470e065762.png)


### Reading Learn about scaling with boy bands
In the next few minutes you’ll learn about horizontal and vertical scaling. Before going into that, here’s a fun case study on managing scale. 

In this extreme case a famous boy band called ‘One Direction’ hosted a 10-hour live stream on YouTube, where they instructed fans to go visit a web site with a quiz on it every 10 minutes. This led to a really interesting pattern in scalability where the application would have zero usage for the vast majority of the time, but then, every 10 minutes may have hundreds of thousands of people hitting it. 

It’s a complex problem to solve when it comes to scaling. It could be very expensive to operate. Using smart scaling strategies, Sony Music and Google solved this problem very inexpensively. Laurence isn’t allowed to share how much it cost for the cloud services, but, when he and several of the other engineers went out for celebration drinks after the success of the project, the bar bill was more expensive than the cloud bill. (And they didn’t drink a lot!) 

Check out the talk about how scaling worked for this system here: https://www.youtube.com/watch?v=aIxNm5Eed_8

Learn about the event and the app here: https://www.computerweekly.com/news/2240228060/Sony-Music-Google-cloud-One-Directions-1D-Day-event-platform-services

### Reading Explore Kubernetes and KubeFlow
In the videos we explored Kubernetes and KubeFlow, and before going further, I strongly recommend that you have a play with them to see how they work. 

#### Kubernetes
First is Kubernetes. The site is https://kubernetes.io/, and at the top of the page, there’s a big friendly button that says ‘Learn Kubernetes Basics’:


Click on this, and you’ll be taken to: https://kubernetes.io/docs/tutorials/kubernetes-basics/

From here you can go through a lesson to create a cluster, deploy and app, scale it, update it and more. It’s interactive, fun, and worth a couple of hours of your time to really get into how Kubernetes works.

You may also want to check this [video](https://youtu.be/H06qrNmGqyE) tutorial out. 

#### KubeFlow
For KubeFlow, visit: https://www.kubeflow.org/, and at the top of the page, there’s a Get Started button.


Click on it to go to the tutorials. It doesn’t have the nice interactive tutorials that Kubernetes has, but, if you can, try to at least install KubeFlow on one of the deployment options listed on this page – even if it’s just your development machine. If you find it tricky to follow, don't worry because you will have an ungraded lab next week that will walk you through installing Kubeflow Pipelines (one of the Kubeflow components) in Kubernetes. In the meantime, you can watch [this playlist](https://www.youtube.com/watch?v=dC659IsHNyg&list=PLIivdWyY5sqLS4lN75RPDEyBgTro_YX7x&index=3&ab_channel=GoogleCloudTech) particularly video #5 on Kubeflow Pipelines to get a short intro to this toolkit.


### Quiz: Scaling Infrastructure
**1.Question 1**

Why is managing scale paramount when serving a sophisticated model? (Select all that apply)

- [ ] The changes in the dynamic environment in which the model operates may cause the model to drift.
- [x] The high volumes of requests to the model for inference can overwhelm the server.
- [ ] The costs of training deep neural networks with billions of operations on massive datasets are high.
- [x] The number of parameters increases considerably in more extensive and more sophisticated networks.

**2. Question 2**

True or False: The elasticity of vertical scaling allows to upgrade the hardware resources without taking the app offline.

- [x] False
- [ ] True

**3. Question 3**

How do containers become lighter and more flexible than virtual machines?

- [ ] By running the apps on a bin/library within an operating system that does not run on hardware.
- [x] By using the same operating system for all partitions.
- [ ] By having a hypervisor managing multiple instances of operating systems and apps.

### Reading Ungraded Lab: Intro to Kubernetes
In this lab, you will get more hands-on practice with Kubernetes in preparation for this week's graded assignment. If you haven't already, please clone the public repo. You can do so with the following commands:
```
git clone https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public
```
After that, please navigate to `course4/week2-ungraded-labs/C4_W2_Lab_2_Intro_to_Kubernetes/` then read the root `README.md` with your favorite Markdown reader. Alternatively, you can just clone the repo then just go [here](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/tree/main/course4/week2-ungraded-labs/C4_W2_Lab_2_Intro_to_Kubernetes) to use Github's built-in Markdown viewer. Either way, that README file will contain the instructions on how to run the lab in your machine. 

In case you run into any issues, remember to post it in Discourse so mentors and course staff can assist. 

Happy learning!

## Online Inference

### Online Inference
#### Online Inference
![image](https://user-images.githubusercontent.com/1645304/133178615-311202f5-a638-42a0-b16c-0f2c83e133ab.png)

#### Optimizing ML Inference
**Latency** is how long does it take for the data to be passed to the server, for the inference to execute and then for the response to be handled. From the users perspective, it's the delay between their action and the response of the app. It's not just the inference, you could have a poorly designed app that has a fabulous model and if latency is introduced by the transport of the data or even the rendering of the results, the user will see a delay.
![image](https://user-images.githubusercontent.com/1645304/133178684-45208998-5fe6-43bc-806c-cd72d9ae2d84.png)

**Throughput** measured in requests managed per unit time is often more important for non customer facing systems like intensive data processing apps.
![image](https://user-images.githubusercontent.com/1645304/133178906-0597df61-de92-4727-ade4-6b8cd4c61ef2.png)

**Cost** Most budgets aren't unlimited, so work that you do to make latency and throughput as efficient as possible. There are multiple costs in your system:
- Hardware but also things like
- engineering and testing time and effort?
- Software licenses,
- opportunity costs for slow updates and
- lost costs for new applications.
![image](https://user-images.githubusercontent.com/1645304/133179080-e8c1b36d-57a2-4034-a60b-7b4e0685eb5b.png)

#### Inference Optimization
1. **Infrastructure**  The first is the infrastructure used to serve the models and handle the user input and output. This can be scaled with additional or more powerful hardware as well as containerized a virtualized environments like the ones we presented earlier this week.
2. **Model Architecture** The second of course, is to understand your model architecture and the metrics was trained and tested with. Often there's a trade off between inference speed and accuracy, If a 99% accurate model is 10 times slower than a 98% accurate model, is it really worth the extra cost?
3. **Model Compilation** If you know the hardware on which you're going to deploy the model You can refine your model graph and inference runtime to reduce memory consumption and latency. For example with a post training step that consists of creating a model artifact and a model execution runtime that's adapted to the underlying support hardware. 
![image](https://user-images.githubusercontent.com/1645304/133179729-29324a7a-5ec4-43bd-ba7d-bf2a0aadba39.png)

#### Additional Optimization
There is lot hitting to the database, an optimization to consider is to cashe frequent data in something faster than a typical data store. But faster the storage, the more expensive it is, so there's a trade off here and it may not be feasible for all of your data to be in such a store. If you can find that trade off for how many to put in there, you can maximize for latency while minimizing your extra costs.
![image](https://user-images.githubusercontent.com/1645304/133180103-ce5db3b0-6c11-4bdf-b70a-5c4193ee688d.png)

#### NoSQL Databases Caching and Feature Lookup
Fast data cashing is usually achieved using NoSQL databases on memory cashing. 
![image](https://user-images.githubusercontent.com/1645304/133180369-b65dfb1e-f2ce-4133-88d4-eb49e25b73f9.png)

### Quiz Online Inference
**1. Question 1**

What are the main features of prediction from online inference? (Select all that apply)

- [x] They are generated in real-time upon request.
- [x] They are based on a single data observation at runtime.
- [x] They can be made at any time of the day on demand.
- [ ] They are produced for all the data points at once.

**2. Question 2**

In which area of online inference is a model artifact and model run created to reduce memory consumption and latency?

- [ ] Infrastructure
- [ ] Model Architecture
- [x] Model Compilation

**3. Question 3**

True or False: Fast data caching using NoSQL databases is a cheap way of optimizing inference.

- [ ] True
- [x] False

### Reading Ungraded Lab - Latency testing with Docker Compose and Locust
During this lab you will work with Docker Compose and Locust to perform load testing on the servers you coded in the previous ungraded lab.

Follow this [link](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week2-ungraded-labs/C4_W2_Lab_3_Latency_Test_Compose/README.md) to start the lab!

## Data Preprocessing

### Data Preprocessing
We explored hardware and container strategies, model architectures, and things like caching in your app to make sure that data access doesn't become a bottleneck. But there are other places where you can optimize. 

#### Data Preprocessing and Inference
The observation data being passed into the system may be in one format but that's not necessarily the same format that the model was designed to take in. For example, a language model where the observation is a sentence that the user typed and is stored as a string. The model is designed to classify that text to see if it's toxic. NLP models like this are trained on input vectors where words are transformed into a high dimensional vector and sentences are sequences of these vectors.

![image](https://user-images.githubusercontent.com/1645304/133183212-c84cfe5c-97f9-4174-843b-2b22de32ec62.png)

#### Preprocessing Operations Needed Before Inference
![image](https://user-images.githubusercontent.com/1645304/133183584-372d5a66-996c-41b2-9135-fc361ecc3f69.png)

#### Processing After Obtaining Predictions
Post processing of data is everything in pre processing can apply but usually in reverse. For example, in a smart reply app, the model may give a few predictions about what the best next sentences could be and these may be a sequence of vectors representing words in a sentence, but not the sentence itself. Your app will need to convert these into a string before returning them to the user.

![image](https://user-images.githubusercontent.com/1645304/133183713-7a7143f3-60a8-40ec-94cc-d8fa3d92bbda.png)

### Reading: Data preprocessing
Apache Beam is a product that gives you a unified programming model that lets you implement batch and streaming data processing jobs on any execution engine. It’s ideally suited for data preprocessing!

Go to https://beam.apache.org/get-started/try-apache-beam/ to try Apache Beam in a Colab so you can get a handle on how the APIs work. Make sure you try it in Python as well as Java by using the tabs at the top. 

Note: You can click the `Run in Colab` button below the code snippet to launch Colab. In the Colab menu bar, click `Runtime > Change Runtime type` then select `Python 3` before running the code cells. You can get more explanations on the WordCount example [here](https://beam.apache.org/get-started/wordcount-example) and you can use the [Beam Programming Guide](https://beam.apache.org/documentation/programming-guide/) as well to look up any of the concepts.

You can learn about TensorFlow Transform here: https://www.tensorflow.org/tfx/transform/get_started . It also uses Beam style pipelines but has modules optimized for preprocessing Tensorflow datasets.

### Quiz: Data Preprocessing
**1. Question 1**

True or False: Data values that differ significantly from other observations are dealt with at the end of the preprocessing process.

- [ ] True x
- [x] False

**2. Question 2**

In which step you transform a given set of input features to generate a new set of more powerful features for prediction?

- [x] Feature Construction
- [ ] Feature Tuning
- [ ] Feature Selection

**3. Question 3**

Which of the following are classic uses of Representation Transformations? (Select all that apply)

- [x] One-hot encoding
- [x] Vectorization
- [ ] Normalization
- [x] Change data format for the model

## Batch Inference Scenarios

### Batch Inference Scenarios

#### Batch Inference
In ML model can provide predictions in batches which will be applied to a use case at sometime in the future. Prediction based on batch inference is when your ML model is used in a batch scoring job for a large number of data points where predictions are not required or not feasible to generate in real-time. I

![image](https://user-images.githubusercontent.com/1645304/133187131-ab5c9caf-28c8-4613-9d4a-b36b172c73e1.png)

#### Advantages of Batch Inference
- You can use complex machine learning models in order to improve the accuracy of your predictions since there's no constraint on inference time.
- Caching of predictions like this is usually not required.
- Batch inference can also wait for data retrieval to make predictions since the predictions are not available in real-time.
 
![image](https://user-images.githubusercontent.com/1645304/133187282-66de83e1-2bf6-4fdc-b329-130e73e341a9.png)


#### Limitations of Batch Inference
Batch influence also has a few disadvantages:
- Predictions cannot be made available for real-time purposes.
- Update latency of predictions can be hours or sometimes even days.
- Predictions are often made using old data.

This is problematic in certain scenarios. Suppose a service like a movie streaming one generates recommendations at night. If a new user signs up they may not be able to see personalized recommendations right away. To get around this, the system is designed to show recommendations from other users:
- in a similar demographic like the same age bracket or
- maybe the same geolocation as a new user.

![image](https://user-images.githubusercontent.com/1645304/133187571-1818ed49-b966-4dbe-ab66-2cee2e11a145.png)

#### Important Metrics to Optimize
You should always aim to increase the throughput in batch predictions rather than the latency. When data is available in batches the model should be able to process large volumes of data at a time. As throughput increases the latency with which each prediction is generated increases also. But this is not a big concern in batch prediction systems since predictions need not be available immediately. Predictions are usually stored for later use and hence, latency can be compromised.

![image](https://user-images.githubusercontent.com/1645304/133188002-e5d9b35d-6c13-4b73-b72a-dfb3171b3911.png)

Throughput of an ML model or Production System processing data in batches can be increased by:
- usage of hardware accelerators like GPUs, TPUs and all that.
- Also increase the number of servers or workers in which the model is deployed.
- Load several instances of the models and multiple workers to increase the throughput. 

![image](https://user-images.githubusercontent.com/1645304/133188131-8fe43818-8b00-4d7e-9273-51400e3ef6a1.png)

#### Use Case - Product Recommendation
New product recommendations on an e-commerce site can be generated on a recurring schedule then caching these predictions for easy retrieval. This can save inference costs since you don't need to guarantee the same latency as real-time inference needs to have.
You can also use more predictions to train more complex models since you don't have the constraint of prediction latency. This helps personalization to a greater degree but using delayed data that may not include new information about the user.

![image](https://user-images.githubusercontent.com/1645304/133188239-63b90b4f-54bd-485b-beb1-f949dc82c5e2.png)

#### Use Case - Sentiment Analysis
Based on the users reviews, usually in text format, you might want to predict if a review was positive, neutral or negative. Systems that analyze user sentiment for your products or services based on customer reviews can make use of a batch prediction on a recurring schedule. Some systems might generate products sentiments on a weekly basis, for example. Real-time prediction is not needed in this case since the customers and stakeholders are not waiting to complete an action in real time based on the predictions. Sentiment predictions can be used for improvements of services or products over time. As you can see, it's not really a real-time business process. 

![image](https://user-images.githubusercontent.com/1645304/133188624-4c5fa01e-6acf-4da5-9d01-292c0be314ea.png)

#### Use Case - Demand Forecasting
You can use batch predictions for models that estimate the demand for your products perhaps on a daily basis for inventory and ordering optimization. It can be modeled as a time series problem since you're predicting future demand based on historical data. Since batch predictions have minimal latency constraints, time series models like AROMA, SARIMA or an RNN can be used.

![image](https://user-images.githubusercontent.com/1645304/133189142-530cba5c-1272-403c-9cfe-800a0132e80e.png)

### Quiz: Batch inference scenarios
**1. Question 1**

Which of the following are advantages of batch inference?

- [ ] You achieve shorter latency of predictions.
- [x] You can wait for data retrieval to make predictions since they are not made available in real time.
- [x] You don’t need caching strategies so costs decrease.
- [x] You can use complex machine learning models to improve accuracy since there is no constraint on inference time.

**2. Question 2**

True or False: The most important metric to optimize while performing batch predictions is throughput.

- [ ] False
- [x] True

**3. Question 3**
How can you save inference costs when generating recommendations on e-commerce?

- [ ] Generating them every time a user logs in.
- [x] Generating them on a schedule.
- [ ] Using hardware accelerators.

## Batch Processing with ETL

### Batch Processing with ETL

#### Data Processing - Batch and Streaming
![image](https://user-images.githubusercontent.com/1645304/133190610-f1406ba5-7ec0-49ac-b0a0-1bdbad50ba09.png)

#### ETL on data
![image](https://user-images.githubusercontent.com/1645304/133190666-6299fa61-af0d-4f0b-9fed-357cb214de0a.png)

#### ETL Pipelines
![image](https://user-images.githubusercontent.com/1645304/133190737-46a27af1-7485-42b8-916e-59b887262bcd.png)

#### Distributed Processing
![image](https://user-images.githubusercontent.com/1645304/133190775-fae14455-e760-4fd4-ac04-c2d8c980fe55.png)

#### ETL Pipeline components Batch Processing
![image](https://user-images.githubusercontent.com/1645304/133190823-076c1930-a708-4a13-9cbb-88fb143edecf.png)

#### ETL Pipeline components Streaming Processing
![image](https://user-images.githubusercontent.com/1645304/133190910-a763316f-067a-463f-8857-58ab8197dff5.png)

### Reading: Machine Learning with Apache Beam and TensorFlow
This optional lab will show you how to preprocess, train, and make batch predictions on a machine learning model using Apache Beam and Tensorflow Transform. To prevent costs of using Cloud resources, you will just run the entire pipeline in Colab. We linked the original article which gives the option to run in GCP in case you want to give it a shot afterwards. 

[Click here to launch Colab!](https://colab.research.google.com/github/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week2-ungraded-labs/C4_W2_Lab_4_ETL_Beam/C4_W2_Lab_4_Apache_Beam_and_Tensorflow.ipynb)

### Quiz: Batch Processing with ETL
**1. Question 1**

What is the purpose of ETL pipelines?

- [x] To extract data from data sources, transforming, and loading it into an output destination.
- [ ] To codify and automate the workflow it takes to produce a machine learning model.
- [ ] To make batch predictions.

**2. Question 2**

True or False: In distributed processing, latency increases because data is split into chunks and parallely processed by multiple workers.

- [x] False
- [ ] True

**3. Question 3**

Which of the following engines perform ETL on data? (Select all that apply)

- [ ] Data Lake
- [x] Google Cloud DataFlow
- [x] Apache Beam
- [x] Apache spark

### Graded External Tool: Autoscaling TensorFlow model deployments with TF Serving and Kubernetes
In this assignment, you will use TensorFlow Serving and Google Cloud Kubernetes Engine (GKE) to configure a high-performance, autoscalable serving system for TensorFlow models. More concretely, you will:

1. Create a GKE cluster and deploy a model.

2. Download the model files to a storage bucket.

3. Create Kubernetes ConfigMap that points to the location of the model in the storage bucket.

4. Create Kubernetes Deployment using a standard TensorFlow Serving image from Docker Hub.

5. Create Kubernetes Service to expose the deployment through a load balancer.

6. Configure Horizontal Pod Autoscaler.

7. Test the model.

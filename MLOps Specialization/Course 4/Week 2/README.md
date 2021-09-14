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

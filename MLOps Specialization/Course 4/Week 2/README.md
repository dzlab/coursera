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

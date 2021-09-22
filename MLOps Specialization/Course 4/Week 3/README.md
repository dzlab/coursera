# Week 3: Experiment Tracking

## ML Experiments Management and Workflow Automation

### Experiment Tracking
Machine learning can be considered an experimental science since experimenting and analyzing results is at the heart of ML development. We need rigorous processes and reproducible results, which has created a need for experiment tracking.

#### Why Experiment Tracking
![image](https://user-images.githubusercontent.com/1645304/133358387-01b21760-cc69-4735-998b-bf0031f0d154.png)

#### What does it mean to track experiments?
![image](https://user-images.githubusercontent.com/1645304/133358559-cd7735ac-0646-40aa-8b81-e7cb78ac38ce.png)

#### Simple Experiments with Notebooks
![image](https://user-images.githubusercontent.com/1645304/133358732-15650d97-6e98-40a2-9d28-62b504e8b3dc.png)

#### Smoke testing for Notebooks
You can use commands like this to extract the code from your notebook and then try running it. If it fails, then there were things happening in your notebook that your code depended on.
```
$ jupyter nbconvert --to script train_model.ipynb python train_model.py
$ python train_model.py
```

#### Not Just One Big File
![image](https://user-images.githubusercontent.com/1645304/133359089-d0ca293e-90bf-4c29-9da9-70f746bc4d73.png)

#### Tracking Runtime Parameters
As you perform experiments, you're often changing runtime parameters including your model's hyperparameters. It's important to include the values of those parameters in your experiment tracking and how you set them will determine how you do that.
- A simple and robust method is to use configuration files and change those values by editing those files. The files can be versioned along with your code for tracking.
- Another option is to set your parameters on the command line. but this requires more code to save those parameters and associate them with your experiment
![image](https://user-images.githubusercontent.com/1645304/133359384-dc967dd8-56a2-4f24-98e5-6993e2117cc8.png)

#### Log Runtime Parameters
Using Neptune.ai API
![image](https://user-images.githubusercontent.com/1645304/133359443-7be3bada-3d5c-46fb-99b7-f9e7ee021d5a.png)

### Tools for Experiment Tracking

#### Data Versioning
![image](https://user-images.githubusercontent.com/1645304/133359633-d9654d14-daa6-420d-bf7a-bde6d40e7285.png)


#### Tools for Data Versioning
- **Neptune** which includes data versioning, experiment tracking and model registry.
- **Pachyderm** which lets you continuously update data in the master branch of your repo while experimenting with specific data commits in a separate branch or branches.
- **Delta Lake** which runs on top of your existing data lake and provides data versioning including rollbacks and full historical audit trails.
- **Git LFs** which is an extension to get and replaces large files such as audio samples, videos, datasets and graphics with text pointers inside Git.
- **DoIt** which is a SQL database that you can fork, clone, branch, merge, push and pull just like a Git repository.
- **LakeFS**, which is an open source platform that provides a Git like branching and committing model the scales to petabytes of data.
- **DVC**, which is an open source version control system for machine learning projects and runs on top of Git. 
- **ML-Metadata**, which is a library for recording and retrieving metadata associated with ML developer and data scientist workflows including datasets. ML MD or ML-Metadata is an integral part of TFX but it's designed so that it can also be used independently.

#### Experiment tracking to compare results
![image](https://user-images.githubusercontent.com/1645304/133360033-ce1f17dd-04a4-48bf-b88d-67015d269795.png)

#### Example: Logging metrics using TensorBoard
TensorBoard is an amazing tool for analyzing your training, which makes it very useful for understanding your experiments. For example, you can use a TensorBoard callback to log metrics and logs the confusion matrix at the end of every epoch. When you display the results, you get a clear view of how your model is doing in this case by examining a confusion matrix.
![image](https://user-images.githubusercontent.com/1645304/133360233-886a8417-bdfa-41e5-8ed6-f12fda4f1c67.png)

![image](https://user-images.githubusercontent.com/1645304/133360376-df7dd16c-fe02-4f78-b334-aa6c83c7aed9.png)

#### Organizing model development
![image](https://user-images.githubusercontent.com/1645304/133360552-f23dc202-1064-4a9f-a104-8a43cc563cf4.png)

#### Tooling for teams
Tooling, which enables sharing can really help. For example, if you can use the experiment management tool provided by Neptune AI to send a link that shares a comparison of the experiments. It makes it easy for you and your team to track and review progress, discuss problems and inspire new ideas. 
![image](https://user-images.githubusercontent.com/1645304/133360700-527b3a19-b2ac-4ba9-a075-541361dd4077.png)
Vertex TensorBoard and similar cloud based tools can also offer significant advantages. 
![image](https://user-images.githubusercontent.com/1645304/133360817-ad62e4b9-74bc-466d-b318-302a9a975570.png)

#### Experiments are iterative in nature

![image](https://user-images.githubusercontent.com/1645304/133364243-74817a64-4582-4533-bda9-45fc509d9bd9.png)

### Reading: Experiment Tracking
Learn more about experiment tracking by checking this two resources out:

1. Machine Learning Experiment Tracking - [link](https://towardsdatascience.com/machine-learning-experiment-tracking-93b796e501b0)
2. Machine Learning Experiment Management: How to Organize Your Model Development Process - [link](https://neptune.ai/blog/experiment-management)

### Introduction to MLOps

#### Data Scientists vs. Software Engineers

|Data Scientists|Software Engineers|
|-|-|
|![image](https://user-images.githubusercontent.com/1645304/133364578-f205f1c6-9851-47f5-9616-e08ca32f31a1.png)|![image](https://user-images.githubusercontent.com/1645304/133364703-cd6e915e-0007-438b-838a-1a80fcd9920e.png)|

#### Growing Need for ML in Products and Services
![image](https://user-images.githubusercontent.com/1645304/133364971-3acd6a75-cfbf-490f-a8f6-c4fb129a29dd.png)
All of this drives an evolution of product focused engineering practices for ML, which is the basis for the development of MLOps.

#### Key problems affecting ML efforts today
![image](https://user-images.githubusercontent.com/1645304/133365170-b35fa897-ca08-4a80-83f2-2210bb51e198.png)

#### Bridging ML and IT with MLOps
![image](https://user-images.githubusercontent.com/1645304/133365417-5a6ee8ac-3b19-4019-a061-8b99937a9399.png)

#### ML Solution Lifecycle
![image](https://user-images.githubusercontent.com/1645304/133365589-d41d10fd-0b79-4788-bb71-88312eac6ab3.png)

#### Standardizing ML processes with MLOps
new practice for collaboration and communication between data scientists and operation professionals which is known as MLOps.

![image](https://user-images.githubusercontent.com/1645304/133365820-5abbc6bb-1e77-45bb-8ec3-e7d8ae194abf.png)

MLOps provides capabilities that will help you:
- build, deploy and manage machine learning models that are critical for ensuring the integrity of business processes. It also provides a consistent and reliable means to move models from development to production by managing the ML Lifecycle.
- Models generally need to be iterated and versioned. To deal with an emerging set of requirements, the models change based on further training or real world data that's closer to the current reality. MLOps also includes creating versions of models as needed and maintaining model version history.
- And as the real world and its data continuously change, it's critical that you manage model decay. With MLOps you can ensure that by monitoring and managing the model results continuously, you can make sure that accuracy, performance and other objectives and key requirements are acceptable.
- MLOps platforms also generally provide capabilities to audit compliance, access control, governance testing and validation and change and access logs. The logged information can include details related to access control like who is publishing models, why modifications are done and when models were deployed or used in production. You also need to secure your models from both attacks and unauthorized access.
- MLOps solutions can provide some functionality to protect models from being corrupted by infected data, being made on unavailable by denial of service contracts or being inappropriately accessed by unauthorized users.
- Once you've made sure your models are secure, trustable and good to go, it's often a good practice to establish a platform where they can be easily discovered by your team. MLOps can do that by providing model catalogs for models produced as well as a searchable model marketplace. These model discovery solutions will provide information to track the data origination, significance, model architecture and history and other metadata for a particular model.

### Quiz: ML Experiments Management and Workflow Automation
**1. Question 1**

Is debugging in ML different from debugging in software engineering?

- [x] Yes, debugging in ML is fundamentally different from debugging in software engineering.
- [ ] No, debugging in ML and software engineering aim for the same goals.

**2. Question 2**

Which of the following tools allow you to track experiments with notebooks? (Select all that apply)

- [x] Nbdime
- [x] Jupytext
- [ ] nbQA
- [x] Nbconvert

**3. Question 3**

Which of the following are some good tools for Data Versioning?

- [x] Neptune
- [ ] OpenRefine
- [x] Pachyderm
- [x] Delta Lake

**4. Question 4**

What are the main objectives of DevOps? (Select all that apply)

- [x] Increasing deployment velocity.
- [ ] Delivering software functionalities through automated deployments.
- [x] Ensuring dependable releases of high-quality software.
- [x] Shortening the systems development life cycle.

## MLOps Methodology

### MLOps Level 0
#### What defines an MLOps process' maturity?
![image](https://user-images.githubusercontent.com/1645304/133537215-979b4456-2370-4364-ad97-b89b3cfcd7ab.png)

Triggers for automated model training and deployment can be calendar events, messaging or monitoring events, as well as changes in data, model training code and application code or detected model decay.

#### MLOps level 0: Manual process
- Manual, script-driven, interactive (jupyter) steps
- Disconnection between ML and operations
- Less frequent releases, so no CI/CD

How do you scale?
- Deployment and lack of active performance monitoring

![image](https://user-images.githubusercontent.com/1645304/133537587-235c2785-04b5-44d3-979b-c9a5771fbe8c.png)

#### Challenges for MLOps level 0

![image](https://user-images.githubusercontent.com/1645304/133537833-457df1ea-2243-4fe3-b05b-5359fb889834.png)

### MLOps Levels 1&2
#### MLOps Levels 1: ML pipeline automation

![image](https://user-images.githubusercontent.com/1645304/133540304-d3c52d88-31c3-4d23-b98e-674bcfe634e3.png)

Notice here that since the steps of the experimentation are orchestrated, the transition between steps is automated. That enables you to rapidly iterate on your experiments, and makes it easier to move the whole pipeline to production.

![image](https://user-images.githubusercontent.com/1645304/133540429-fb60ff77-6820-460a-b955-6a2771bbd6a5.png)

![image](https://user-images.githubusercontent.com/1645304/133540504-037ee19f-afac-4d33-b01c-24ebbfcd35cb.png)


An optional additional component for level one MLOps is a feature store. A feature store is a centralized repository where you standardize the definition, storage, and access of features for training and serving. Ideally, a feature store will provide an API for both high throughput batch serving and low latency, real time serving for the feature values, and support both training and serving workloads. A feature store helps you in many ways. First of all, it lets you discover and reuse available feature sets instead of recreating the same or similar feature sets, avoiding having similar features that have different definitions by maintaining features and their related metadata. Moreover, you can potentially serve up to date feature values from the feature store, and avoid training serving skew by using the feature store as a data source for experimentation, continuous training, and online serving. This approach makes sure that the features used for training are the same ones used during serving. For example, when it comes to experimentation, data scientists can get an offline extract from the feature store to run their experiments. For continuous training, the automated training pipeline can fetch a batch of the up to date feature values of the data set. For online prediction, the prediction service can fetch feature values such as customer demographic features, product features, and current session aggregation features.

#### MLOps level 2 CI/CD pipeline automation
This diagram presents one of the current architectures, which is focused on enabling rapid and reliable update of the pipelines in production. This requires robust automated CICD to enable your data scientists and ML engineers to rapidly explore new ideas around feature engineering, model architecture, and hyperparameters.

These MLOps setup includes components like source code control, test and build services, deployment services, a model registry, a feature store, a metadata store, and a pipeline orchestrator.

![image](https://user-images.githubusercontent.com/1645304/133541453-701febd8-ede4-4b51-a37c-f8e34a73ca3b.png)

![image](https://user-images.githubusercontent.com/1645304/133541680-be332f4d-6e41-41a3-ac18-4af611e16364.png)

### Reading: MLOps Resources
If you want to learn more about MLOps check this [blog](https://neptune.ai/blog/mlops-what-it-is-why-it-matters-and-how-to-implement-it-from-a-data-scientist-perspective) out, and visit this curated [list](https://github.com/visenger/awesome-mlops) of references  for more information, ideas, and tools.

### Reading: Ungraded Lab: Intro to Kubeflow Pipelines
In this lab, you will familiarize yourself with Kubeflow Pipelines, a platform for building and organizing machine learning workflows. You will be using this as well in the Qwiklabs this week so it's good to practice using it. Please click on the link below to start the lab.

[Launch Colab!](https://colab.research.google.com/github/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week3-ungraded-labs/C4_W3_Lab_1_Intro_to_KFP/C4_W3_Lab_1_Kubeflow_Pipelines.ipynb)

### Developing Components for an Orchestrated Workflow

#### Orchestrate your ML workflows with TFX
![image](https://user-images.githubusercontent.com/1645304/133542336-78e1ab7e-6e36-4cd4-aea1-1a7be905f8a5.png)


#### Hello TFX
The components in orange are a training pipeline and the ones in green are an inference pipeline for doing batch inference
![image](https://user-images.githubusercontent.com/1645304/133542430-7f41d924-318d-4d7d-8866-0bf5f516f720.png)

#### Anatomy of a TFX Component

![image](https://user-images.githubusercontent.com/1645304/133542613-6bc0e571-50b7-4574-b066-690cf9af3fcd.png)

#### TFX components at runtime
![image](https://user-images.githubusercontent.com/1645304/133542840-d504a3d4-2338-46f4-bb28-b0dfc1a1d747.png)

#### Python function-based components
In this style you write a function that is decorated and annotated with type hints. The type hints describe the InputArtifacts, OutputArtifacts and parameters of your component.
![image](https://user-images.githubusercontent.com/1645304/133543001-9d0a66ad-e3b5-405d-bd5d-be4781529ae8.png)

#### Container-based components
Container-based components are backed by containerized command line arguments or programs rather. And in some ways are similar to creating a Docker file. To create one, you need to specify a Docker container image that includes your components dependencies. Then you call the create container component function and pass the component definition, including the components, inputs, outputs and parameters.

![image](https://user-images.githubusercontent.com/1645304/133543030-a8c64f06-bad9-4002-8edf-fdf027e425ee.png)


There are other parts of the configuration, like the container image name and optionally the image tag. Finally, for the body of the component, you have the command parameter which defines the container entry point command line. As with docker files this isn't executed within a shell unless you specify that in your command line.

![image](https://user-images.githubusercontent.com/1645304/133543139-c32142ee-92c3-48c5-8f39-d30cbcf31f7d.png)

This approach is the most suitable for including non-python code in your pipeline or for building Python components with complex runtime environments or dependencies.

#### Fully custom components
![image](https://user-images.githubusercontent.com/1645304/133543391-9f4de4ea-1ba2-40e3-bbbd-a8b6d5e6187f.png)


#### Defining input and output specifications
![image](https://user-images.githubusercontent.com/1645304/133543454-92844261-fbcc-4480-beef-c7dd797772d9.png)

#### Implement the executor
![image](https://user-images.githubusercontent.com/1645304/133543531-7f5d978f-559c-490b-9b39-cdd15e898f2b.png)

![image](https://user-images.githubusercontent.com/1645304/133543574-fcd8b2d3-d5f9-4285-b56f-d74a97da2afe.png)


#### Make the component pipeline-compatible
First you need to make the component class a subclass of base_component.BaseComponent or a different component if you're extending an existing component. And next you assign class variables, SPEC_CLASS and executor spec with a component spec and executor classes respectively, that you just defined. The final step to completing the custom component is to finish implementing the init, which will initialize the component. Here you define the constructor function by using the arguments to the function to construct an instance of the component spec class and invoke the super function with that value along with an optional name.

![image](https://user-images.githubusercontent.com/1645304/133543638-37bc6663-1538-4883-962c-e8f48e7df41e.png)

#### Completing the component class
![image](https://user-images.githubusercontent.com/1645304/133543746-933e06cf-13d6-4610-86c0-234a2084e40f.png)

#### Assemble into a TFX pipeline
The last step is to plug the new custom component into a TFX pipeline.
![image](https://user-images.githubusercontent.com/1645304/133543779-0960e372-4787-43f2-a618-7282e03fb3db.png)

![image](https://user-images.githubusercontent.com/1645304/133543881-5ee56a5c-2b66-4ff9-88f5-e631004e84c9.png)

### Reading: Architecture for MLOps using TFX, Kubeflow Pipelines, and Cloud Build
To learn more about MLOps using TFX please check this [document](https://cloud.google.com/architecture/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build) out.

### Quiz: MLOps Methodology

**1. Question 1**

What determines the maturity of the MLOps process?

- [ ] The standard pattern for MLOps building.
- [ ] The accuracy of the deployed model.
- [ ] The technical scenario for MLOps implementation.
- [x] The level of automation of ML pipelines.

**2. Question 2**

True Or False: At the basic level of maturity, or level 0, tracking or logging are required to detect model performance degradation and other model behavioral drifts.

- [x] False
- [ ] True

**3. Question 3**

What steps do you need to introduce into the ML pipeline to move towards MLOps maturity level one? (Select all that apply)

- [x] Automated Data Validation
- [ ] Automated Theorem Proving
- [x] Automated Model Validation
- [ ] Dependently Typed Programming

**4. Question 4**

In case of an interruption, what key component of the pipeline allows you to resume execution seamlessly?

- [x] Metadata Store
- [ ] Models Registry
- [ ] Trigger
- [ ] Feature Store

Not Trigger. In MLOps, it's common to retrain your model when new data is available. Once programmatically scheduled, the trigger runs the pipeline when more data is added, but it won't resume execution if the process is interrupted.
Not Feature Store. A feature store lets you discover and reuse available feature sets. You can also serve up-to-date feature values from the feature store and avoid training-serving skew. However, it's not designed for contingencies.
Incorrect
Not Model Registry. The Model Registry component is a centralized model store, set of APIs, and UI, to collaboratively manage the MLOps lifecycle. It provides model lineage, model versioning, stage transitions, and annotations, but it won't resume execution if interrupted.

### Reading: Ungraded Lab: Developing TFX Custom Components
In this lab, you will practice some of the methods discussed in building TFX components. Namely, you will develop a custom component to filter a dataset, then reuse the standard CsvExampleGen to make another custom component. Please click on the link below to start the lab.

[Launch Colab!](https://colab.research.google.com/github/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week3-ungraded-labs/C4_W3_Lab_2_TFX_Custom_Components.ipynb)

### Graded External Tool: TFX on Google Cloud AI Platform Pipelines
Tensorflow Extended (TFX) is Google's end-to-end platform for training and deploying TensorFlow models into production. TFX pipelines orchestrate ordered runs of a sequence of components for scalable, high-performance machine learning tasks in a directed graph.

In this assignment, you will use the following tools and services to deploy and run a TFX pipeline on Google Cloud that automates the development and deployment of a TensorFlow 2.3 Classifer to predict forest cover from cartographic data:

1. The TFX CLI utility to build and deploy a TFX pipeline.

2. A hosted AI Platform Pipeline instance (Kubeflow Pipelines) for TFX pipeline orchestration.

3. Dataflow jobs for scalable, distributed data processing for TFX components.

4. An AI Platform Training job for model training and flock management for parallel tuning trials.

5. AI Platform Prediction as a model server destination for blessed pipeline model versions.

6. CloudTuner and AI Platform Vizier for advanced model hyperparameter tuning using the Vizier algorithm.

7. You will then create and monitor pipeline runs using the TFX CLI as well as the KFP UI.

## Model Management and Deployment Infrastructure

### Managing Model Versions
#### Why versioning ML models?
In normal software development, especially with teams, organizations rely on version control software to help teams manage and control changes to their code. But imagine if you didn't have that.
- How would you enable multiple developers to stay in sync?
- How do you roll back when there are problems?
- How would you do continuous integration?
 
Well, just like with software development, when you're developing models, you have all of these needs and more.

![image](https://user-images.githubusercontent.com/1645304/134100481-2efeb795-ca19-440f-9825-a43d68ebacc3.png)

#### How ML Models are versioned?
![image](https://user-images.githubusercontent.com/1645304/134100572-11b7ce39-e7fb-45f7-b562-9fb44518da2d.png)

#### A Model Versioning Proposal

I'd like to focus on how to retrieve older models, leverage model lineage, and use model registries to simplify production workflow. 
![image](https://user-images.githubusercontent.com/1645304/134100701-22df271d-b2a3-427f-8012-50c472c551fb.png)


#### Retrieving older models
You may have an intuition that for an ML framework to retrieve older models, the framework has to be internally versioning the models through some versioning technique.
![image](https://user-images.githubusercontent.com/1645304/134100736-26a9537e-31b1-4f9f-9a68-a75309164863.png)


#### What is model lineage?
One technique is by making use of model lineage. Model lineage is a set of relationships among the artifacts that resulted in the trained model. To build model artifacts, you have to be able to track the code that builds them and the data, including pre-processing operations that the model was trained and tested with. ML orchestration frameworks like TFX will store this model lineage for many reasons including recreating different versions of the model when necessary. Note that model lineage usually only includes those artifacts and operations that were part of model training. Post-training artifacts and operations are usually not part of the lineage.
![image](https://user-images.githubusercontent.com/1645304/134100844-8da34ecc-c046-4c1a-9cdf-4fba41d39b74.png)


#### What is model registry?
![image](https://user-images.githubusercontent.com/1645304/134101009-5bf5375b-d454-401e-968c-85efac3f5ebf.png)

#### Metadata stored by model registry
![image](https://user-images.githubusercontent.com/1645304/134101080-d8b49aab-4c29-416a-bb70-93db68d06624.png)

#### Capabilities Enabled by Model Registries
![image](https://user-images.githubusercontent.com/1645304/134101371-63b2222a-848d-4e7d-8e5c-b617f825f13c.png)

#### Examples of Model Registries
![image](https://user-images.githubusercontent.com/1645304/134101428-eab66d9f-ac12-48ad-882f-1a9f60dd7319.png)


### Reading: Ungraded Lab - Model Versioning with TF Serving
During this lab you will see how you can use Tensorflow Serving to host different versions of your models either by numerical versioning or by using labels.

Follow this [link](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week3-ungraded-labs/C4_W3_Lab_3_TFS_Model_Versioning/README.md) to start the lab!

### Reading: ML Model Management
Take a deeper dive into managing ML model versions by checking this [blog](https://neptune.ai/blog/machine-learning-model-management) out.

### Continuous Delivery

#### What is Continuous Integration (CI)
![image](https://user-images.githubusercontent.com/1645304/134101620-22150b2b-70ac-4c0c-8cfc-2e3d6c06dfa9.png)


#### What is Continous Delivery (CD)
![image](https://user-images.githubusercontent.com/1645304/134101667-914346e2-bb1b-41b7-9b15-331457c514fa.png)


#### CI/CD Infrastructure
![image](https://user-images.githubusercontent.com/1645304/134101790-acffd76f-061b-4585-b657-3e4cdd4ae397.png)


#### Unit Testing in CI
![image](https://user-images.githubusercontent.com/1645304/134103423-0741bf0d-e29a-4314-8d9b-cf17a6c339cd.png)


#### Unit Testing Input Data
Unit testing for data is not the same as performing data validation on your raw features. It's primarily concerned with the results of your feature engineering. You can write unit tests to check if engineered features are calculated correctly. It includes tests to check whether they are scaled or normalized correctly. One hot vector values are correct and embedding are generated and used correctly, etc. And you will also do tests to confirm if columns and data are the correct types in the right range, not empty and so forth.

![image](https://user-images.githubusercontent.com/1645304/134103510-f21d0d62-93a3-4de6-a125-b61e922c6aaa.png)


#### Unit Testing Model Performance
![image](https://user-images.githubusercontent.com/1645304/134103649-52b26b41-c2d8-4556-b6db-91e82e6c68a5.png)


#### ML Unit Testing Considerations
![image](https://user-images.githubusercontent.com/1645304/134103762-b2e604d2-6e18-4383-b5f4-179afebec65b.png)


#### Infrastructure validation
![image](https://user-images.githubusercontent.com/1645304/134103869-167d24ca-aa92-454f-8d23-5201ada1cf02.png)


### Reading: Ungraded Lab - CI/CD pipelines with GitHub Actions
During this lab you will work with GitHub Actions to configure and run your own CI/CD pipelines to unit test the webserver you coded in a previous ungraded lab.

Follow this [link](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week3-ungraded-labs/C4_W3_Lab_4_Github_Actions/README.md) to start the lab!

### Reading: Continuous Delivery
Explore this [website](https://continuousdelivery.com/) to learn more about continuous delivery.


### Progressive Delivery

#### Progressive Delivery
an improvement over CI/CD. It includes many modern software and development processes including canary deployments, A/B testing, bandits, and observability. It focuses on gradually rolling out new features in order to limit potential negative impact and gauge user response to new product features.
![image](https://user-images.githubusercontent.com/1645304/134271113-f4ba44b4-f57b-476e-b989-afa34c5a326a.png)

#### Complex Model Deployment Scenarios
![image](https://user-images.githubusercontent.com/1645304/134271174-6d79c731-630d-4e9e-a05f-4db070e3265a.png)

#### Blue/Green deployment
A simple form of progressive delivery is blue/green deployment where there are two production serving environments. Requests flow through a load balancer which directs traffic to the currently live environment which is called blue. Meanwhile, a new version is deployed to the green environment which acts as a staging setup where a series of tests are conducted to ensure performance and functionality. After passing the tests, traffic is directed to the green deployment. If there are any problems, traffic can be moved back to blue. This means that there's no downtime during deployment, rollback is easy, and there is a high degree of reliability, and it includes smoke testing before going live. 

![image](https://user-images.githubusercontent.com/1645304/134271273-e5cf2837-129d-46d7-86c5-6db61dc6cbd4.png)


#### Canary deployment
similar to a blue/green deployment, but instead of switching the entire incoming traffic from blue to green all at once, traffic is switched gradually. As traffic begins to use the new version, the performance of the new version is monitored. If necessary, the deployment can be stopped and reversed with no downtime and minimal exposure of users to the new version. Eventually, all the traffic is being served using the new version.

![image](https://user-images.githubusercontent.com/1645304/134271437-55292e93-79e2-4421-a906-18bf997f3652.png)

#### Live Experimentation
Progressive deployment is closely related to live experimentation. Live experimentation is used to test models to measure the actual business results delivered or data as closely associated with business results as you can actually measure.

![image](https://user-images.githubusercontent.com/1645304/134271545-2ffaa469-7384-43b8-8726-1c3f44c7786d.png)

#### Live Experimentation: A/B Testing
One simple form of live experimentation is A/B testing. In A/B testing, you have at least two different models or perhaps n different models and you compare the business results between them to select the model that gives the best business performance.

![image](https://user-images.githubusercontent.com/1645304/134271678-5e4e9eb0-498d-4e30-913b-336546ebe54a.png)

![image](https://user-images.githubusercontent.com/1645304/134271759-d87da599-1714-4104-aa3e-215cdc7fd1ca.png)


#### Live Experimentation: Multi-Armed Bandit (MAB)
An even more advanced approach is multi-armed bandits. The multi-armed bandit approach is similar to A/B testing but uses ML to test or to learn rather from test results which are gathered during the test. As it learns which models are performing better, it dynamically routes more and more requests to the winning models. What this means is that eventually, all of the requests will be routed to a single model or smaller group of similarly performing models. One of the major benefits of that is that it minimizes the use of low-performing models by not waiting for the end of the test to select the winner. The multi-arm bandit approach is a reinforcement learning architecture which balances exploration and exploitation.

![image](https://user-images.githubusercontent.com/1645304/134271910-79487762-9d1d-42b6-955b-6f18466e23a1.png)

#### Live Experimentation: Contextual Bandit
An even more advanced approach is contextual bandit. The contextual bandit algorithm is an extension of the multi-arm bandit approach where you also factor in the customer's environment or other context of the request when choosing a bandit. The context affects how reward is associated with each bandit, so as contexts change, the model should learn to adapt its bandit choice. For example, consider recommending clothing choices to people in different climates. A customer in a hot climate will have a very different context than a customer in a cold climate. Not only do you want to find the maximum reward, you also want to reduce the reward loss when you're exploring different bandits. When judging the performance of a model, the metric that measures the reward loss is called regret which is the difference between the cumulative reward from the optimal policy and the model's cumulative sum of rewards over time. The lower the regret, the better the model. Contextual bandits helps with minimizing regret.

![image](https://user-images.githubusercontent.com/1645304/134272133-8da5401f-2bf2-4cc1-96e8-28aedfc6a353.png)

### Reading: Progressive Delivery
Explore more about progressive delivery with Kubernetes operators allowing for minimum downtime and easy rollbacks in this [documentation](https://codefresh.io/docs/docs/ci-cd-guides/progressive-delivery/).

### Quiz: Model Management and Deployment Infrastructure

**1- Question 1**

When does the minor version number increase in the MAJOR.MINOR.PIPELINE approach of model versioning?

- [ ] When you make incompatible API changes.
- [x] When we’ve improved the model's output.
- [ ] When you make backward-compatible bug fixes. x
- [ ] When we have an incompatible data change.

**2- Question 2**

Which well known product uses pipeline execution versioning?


- [ ] Google Cloud AI Prediction
- [ ] Microsoft Azure AI
- [x] TensorFlow Extended

**3- Question 3**

What are some non-standard ML Unit Testing Considerations? (Select all that apply)


- [ ] Code Coverage
- [x] Mocking
- [ ] Uniqueness
- [x] Data Coverage

 
**4- Question 4**

Which of the following is true about the comparison between canary and blue-green deployment?


- [x] Canary is cheaper than a blue-green deployment because it does not require two production environments.
- [ ] Blue-green deployment is more complex, slower, and harder to implement than canary deployment.
- [ ] Canary deployment is riskier than blue-green deployment because it shifts all user traffic at once.

### Graded External Tool: Implementing Canary Releases of TensorFlow model deployments with Kubernetes and Istio
In this assignment, you will use Istio on Google Kubernetes Engine (GKE) and TensorFlow Serving to create canary deployments of TensorFlow machine learning models. More concretely, you will:

1. Prepare a GKE cluster with the Istio add-on for TensorFlow Serving.

2. Create a canary release of a TensorFlow model deployment.

3. Configure various traffic splitting strategies.


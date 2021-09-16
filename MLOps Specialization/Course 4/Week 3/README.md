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


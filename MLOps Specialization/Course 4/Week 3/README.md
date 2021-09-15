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


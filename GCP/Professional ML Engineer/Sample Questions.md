# Sample questions

**1.** You are in the process of developing a new binary classification machine learning model using a deep neural network and need a baseline to easily test the model's quality.  Since this is a new model, there is not an existing model to compare to the new model.  

Which of the following should you choose to use as a baseline to access your models quality?

- [ ] A. Compare your model output against a model that always predicts the most common label.
- [ ] B. Compare your model output against a model generated with just one epoch.
- [ ] C. Compare your model output against a model trained with no regularization.
- [ ] D. Compare your model with one that predicts each label 50% of the time.

**2.** You are working on a machine learning model that uses PyTorch and are migrating the project from on-premise to the Google Cloud AI Platform.  Your team is also using a few dependencies that are not related to machine learning.  Your job is to recommend what steps the team needs to take to run this work on Cloud AI Platform Training.

Which of the following solutions should you recommend for this machine learning project to run on Cloud AI Platform Training?

- [ ] A. Use an existing pre-built PyTorch container.
- [ ] B. Migrate your project to TensorFlow and use the standard runtime container.
- [ ] C. Use the standard runtime container and list required dependencies in a YAML file.
- [ ] D. Create a custom container with the required dependencies.

**3.** Your team is building an image classification model to detect motor vehicles in images using Google AI Platform training.  You are using TensorFlow to build the model, and for training, you use the BASIC_TPU scale tier, which includes a standard master virtual machine and a worker Cloud TPU (Tensor Processing Units) with eight TPU v2 cores. 

For the first training run, you set the batch size to 10 and the number of iterations per loop to 500.  The training time is much slower than you expected, and the output from the training run does not provide any obvious clues.

Which of the following is most likely causing training to run slower than anticipated?

- [ ] A.The batch size is too large.
- [ ] B. The number of iterations per loop is too big.
- [ ] C. The batch size is too small.
- [ ] D. The number of iterations per loop is too small.

**4.** A credit card company is working on a machine learning model to predict whether a transaction is fraudulent or not.  The prediction model runs on Google AI Platform Prediction.  The team working on the project wants to continually evaluate how the model is performing over time.   Each day a sample of model predictions is saved for this evaluation.  

What steps should this team take to use these samples in a continuous evaluation process for this fraud detection model?

- [ ] A
  - Use Google AI Platform and set up a continuous evaluation job. 
  - Choose to use the Google-managed data labeling service for the ground truth labeling method.  
  - Evaluate model performance using binary cross-entropy loss.

- [ ] B
  - Use Google AI Platform and set up a continuous evaluation job. 
  - Choose to provide your own labels for the ground truth labeling method. 
  - Evaluate model performance using precision-recall curves and a confusion matrix.

- [ ] C
  - Use Google AI Platform and set up a continuous evaluation job. 
  - Choose to provide your own labels for the ground truth labeling method. 
  - Evaluate model performance using binary cross-entropy loss.

- [ ] D
  - Use Google AI Platform and set up a continuous evaluation job. 
  - Choose to use the Google-managed data labeling service for the ground truth labeling method.  
  - Evaluate model performance using precision-recall curves and a confusion matrix.

**5.** You are developing a machine learning model for a food-focused social networking platform to categorize recipes uploaded to the site as either an entree, appetizer, or dessert.  The training data is labeled using one-hot encoding, and you plan to use TensorFlow on the Google Cloud AI platform to train your model.

Which of these loss functions should you choose to train this model?

- [ ] A Categorical cross-entropy
- [ ] B Sparse cross-entropy
- [ ] C Binary cross-entropy
- [ ] D Mean squared error

**6.** You are working on a linear regression machine learning model to predict the price of a used car.  The following information is provided for each automobile in the training dataset:

`| price | mileage | # of owners | color | manufacturer | model | model year |`

The color of the automobile is saved in the dataset as non-numeric data with possible values like 'red,' 'grey,' 'black,' and 'white.'  As you prepare the dataset before training, you need to decide how best to handle this non-numeric feature.

Which of the following approaches should you choose to prepare a non-numeric feature like 'color' in this example?.'

- [ ] A Use the hashcode (an integer) of the feature value (red, grey, black, white)
- [ ] B Use an ordinal encoder like this: red = 1, grey = 2, black = 3, white = 4
- [ ] C Use one-hot encoding to transform the data
- [ ] D Use an embedding layer

**7.** A lending company for small business owners is developing a machine learning algorithm to predict whether a borrower will repay a loan based on financial information from a customer. 

Which type of supervised learning problem does this scenario represent?

- [ ] A multi-class classification
- [ ] B binary classification
- [ ] C clustering
- [ ] D linear regression

**8.** You are working on a project to build a continuous integration/continuous delivery (CI/CD) process using Kubeflow to automatically deploy a newly trained machine learning model to Google AI Platform Prediction.  Two primary triggers in the process can result in the pipeline delivering a new model to production: (1) a developer updates model or pipeline code (2) new training data is available.   You are responsible for testing the scenario when new training data triggers the process.

Which of the following actions should you expect to occur when new training data is available?

- [ ] A The new training data triggers the training pipeline to run and train a new model with the updated training data.  If the model evaluation passes, the system deploys a new model.
- [ ] B The new training data triggers the system to deploy a new training pipeline.  The system runs the training pipeline to train a new model with the updated training data.  If the model evaluation passes, the system deploys a new model.
- [ ] C The new training data triggers the training pipeline to run and train a new model with the updated training data.  The system runs automated tests on the training pipeline components and if tests pass, the system deploys a new model.
- [ ] D The new training data triggers the system to build the training pipeline.  The system runs the training pipeline to train a new model with the updated training data.  If the model evaluation passes, the system deploys a new model.

**9.** A team of machine learning engineers is working on a project to build a CI/CD automation pipeline for a model that serves online predictions to a mobile application.  New training data is available in a Cloud Storage bucket anywhere from every 14 to 28 days.  The team is using Kubeflow to implement the training pipeline and needs to decide how often they should trigger a new training job.

Which of the following strategies should the team use to trigger the training pipeline?

- [ ] A Use Pub/Sub and Cloud Functions to trigger the pipeline and retrain the model when a new training data file is added to Cloud Storage.
- [ ] B Use Cloud Monitoring to track the cumulative count of predictions (prediction_count).  Retrain the model when the number of predictions goes above some maximum level.
- [ ] C Use Cloud Monitoring to trigger the pipeline and retrain the model when a new training data file is added to Cloud Storage.
- [ ] D Use Cloud Scheduler to set up a cron job to retrain the model every 14 days.

**10.** A company that provides an online platform for employers to post open positions is building a machine learning model to predict the expected salary for a particular job posting.  The team working on the model is in the exploratory phase and plans to implement a deep neural network (DNN) using TensorFlow for their machine learning algorithm.  The training data set includes about 100,000 examples.  The team needs to choose the appropriate hardware and platform for training the model while balancing performance and cost.  

Which of the following Google AI services and configurations should the team choose for this project?

- [ ] A Use AutoML Tables with a standard machine type and a 6-hour training budget.
- [ ] B Use Google AI Platform with scale tier = CUSTOM (a single worker instance with a high CPU machine type)
- [ ] C Use Google AI Platform Training with scale tier =  BASIC (a single worker instance with a standard machine type)
- [ ] D Use Google AI Platform Training with scale tier =  BASIC_GPU (a single worker instance with a standard machine type + 1 GPU)

**11.** Your team is working on deploying a machine learning model to make online predictions into production.  Before this happens, your team needs to implement a continuous training pipeline that will be part of a larger continuous integration/continuous delivery (CI/CD) pipeline.  The data to train the model is in BigQuery, and you are using Google AI Platform for training and prediction.  The basic components for the  training pipeline are:

  1. Data Storage (Big Query)
  2. Data Extract and Validation
  3. Data Transformation
  4. Model Training (Google AI Platform Training)
  5. Model Evaluation / Validation
  6. Model Serving (Google AI Platform Prediction)

You need to decide on the right Google service to implement steps 2 & 3, and a solution to orchestrate the pipeline. 

Which of the following solutions is the correct choice?

- [ ] A Use Dataprep for steps 2 - 3 and use Kubeflow to orchestrate the training pipeline.
- [ ] B Use Cloud Data Fusion for steps 2 - 3 and use Cloud Composer to orchestrate the training pipeline.
- [ ] C Use Dataproc for steps 2 - 3 and use Cloud Composer to orchestrate the training pipeline.
- [ ] D Use Dataflow for steps 2 - 3 and use Kubeflow to orchestrate the training pipeline.

**12.** You are training a classification model to detect fraudulent credit card behavior.  Your training data set includes 10,000 examples;  100 are labeled as 'fraud', and 9900 are marked 'not fraud'.  After training the model, the accuracy is about 97%.  Also, the generalization curve shows the loss for the training and validation data gradually decreasing and leveling off with the number of iterations.  However, you find in production that the model is not identifying any fraudulent activity.

What is likely causing this problem in production, and what can you do to address this issue?

- [ ] A
  - Problem: Class Imbalance
  - Solution: Retrain the model with a smaller set of the examples labeled with 'not fraud' (downsampling), and add a weight to these examples (upweighting).
- [ ] B
  - Problem: Overfitting
  - Solution: Retrain the model and implement early stopping (reduce the number of iterations) to avoid overfitting.
- [ ] C
  - Problem: Class Imbalance
  - Solution: Retrain the model with a smaller subset of the examples labeled with 'not fraud' (downsampling), and add a weight to the examples marked with 'fraud' (upweighting).
- [ ] D
  - Problem: Overfitting
  - Solution: Retrain the model and use a smaller number of features to reduce the complexity of the model.

**13.** A team of data analysts at a company that manufactures agricultural equipment is working on a project to build a machine learning model to predict the likelihood of a component failure based on the past maintenance history for a given product.  The team is familiar with SQL but does not have extensive experience with programming languages like Python or Java.  The team is looking for the appropriate Google Cloud services to help prepare the training data and train the machine learning model.

Which set of Google Cloud services should the team choose for this project? 

- [ ] A Use BigQuery for data preparation and BigQuery ML to create the model.
- [ ] B Use BigQuery for data preparation and AI Platform Training to create the model.
- [ ] C Use Dataflow for data preparation and BigQuery ML to create the model.
- [ ] D Use Dataflow for data preparation and AI Platform Training to create the model.

**14.** You are training a machine learning model to predict the starting salary for recent graduates from various degree programs throughout the country using a deep neural network (DNN).  After doing some initial data analysis on the training data set, you notice that one numeric feature is distributed relatively uniformly but contains a few extreme outliers.  You are concerned that this feature could affect your model's performance and stability and want to take steps to avoid this.

What can you do to ensure this feature does not negatively impact the training stability and model performance?

- [ ] A During data preparation, normalize the feature using clipping.
- [ ] B During model training, use L2 regularization
- [ ] C During data preparation, normalize the feature using linear scaling.
- [ ] D During model training, use a reLU activation function on all layers.

**15.** You are using a Google AI Platform Notebook to develop a new machine learning model.  Your dataset is in BigQuery, and you plan to write some preprocessing code to prepare the data using Python before running your training experiments.  You need to decide the best way to load the data.

Which of the following approaches should you use to load your data from BigQuery into your notebook?

- [ ] A Use the BigQuery Storage API to load the data directly into a Pandas DataFrame.
- [ ] B Export data to DataFlow and read in the data from DataFlow
- [ ] C Use BigQuery connector to provide read access from within the AI Platform Notebook.
- [ ] D Export the data from BigQuery to Cloud Storage, and read in the data from Cloud Storage.

**16.** A company that provides computer vision and robotics to agricultural machinery is working on a new product that identifies and precisely treats plant species in the field.  You are working on training a machine learning model for this project with roughly 100,000 labeled images of plants.  You are using Google AI platform and are taking advantage of TPU accelerators to improve training times.  You want to make sure reading in the large volume of images does not create a bottleneck during training.

Which of the following solutions can help reduce bottleneck issues with data ingestion?

- [ ] A Store each image file on Google Cloud Storage and read the images into a tf.data.Dataset for training.
- [ ] B Package the images in several TFRecord files and store them on Google Cloud Storage.  Read the images into a `tf.data.TFRecordDataset` for training.
- [ ] C Package the images in several compressed files and store them on Cloud Storage.  Read the images into a `tf.data.Dataset` for training.
- [ ] D Store each image file on Google Cloud Storage and read in the images during training using Dataflow.

**17.** You are working with a team of data scientists in charge of deploying a machine learning (ML) model to production.  The model requires ongoing updates to adapt to changes in the machine learning model and training pipeline.  The team needs to respond quickly to these changes without manual steps, so they want to implement an ML continuous integration (CI) process.

Which series of steps describes a high-level overview of a basic ML continuous integration process?

- [ ] A
	1. Developer commits model/pipeline code
	2. Run the training pipeline and train a new model
	3. Trigger a build on Cloud Build to evaluate the new model

- [ ] B
	1. New training data is available
	2. Run the training pipeline and train a new model
	3. Evaluate the new model and create a new model version

- [ ] C
	1. New training data is available
	2. Trigger a build on Cloud Build to build the pipeline
	3. Deploy and run the training pipeline to train a new model

- [ ] D
  1. Developer commits model/pipeline code
  2. Trigger a build on Cloud Build to build the pipeline
  3. Deploy and run the training pipeline to train a new model version

**18.** Your team is preparing a data set to train a new machine learning model.  A junior data analyst is responsible for cleaning up and analyzing the dataset before moving into BigQuery and does not have much coding experience.  You are looking for a service that would allow the analyst to visually inspect the data, identify problems, and quickly transform the data without writing code.  You would also like the output of this process to be something that is easily repeatable.

Which of these Google Cloud services should you choose for this data preparation step?

- [ ] A Dataflow
- [ ] B Cloud Composer
- [ ] C Cloud Data Fusion
- [ ] D Dataprep by Trifacta

**19.**  A team of data analysts at a human resources consulting firm is building a machine learning model to predict the number of days it will take to fill a job opening the company manages for its customers.  The team has structured data for its training data set, but does not have a lot of experience choosing machine learning algorithms.

Which of the following Google services should the team use to build this machine learning model?

- [ ] A BigQuery ML
- [ ] B AI Platform Notebooks
- [ ] C AutoML Tables
- [ ] D AI Platform Training

**20.** A team of machine learning engineers uses Google Cloud AI Platform and Tensorflow to implement a new model to predict products that a user might like based on the user's profile data and ordering history.  The team needs to decide how best to implement the process to prepare the input data for both training and online prediction.  The team expects the preprocessing step to involve the following operations:

  - **Cleansing data**: Correct data that is invalid or missing.
  - **Feature tuning**: Normalizing numeric data and clipping outliers in numeric data.

The data processing steps used to train the model must be the same steps for preparing data to make predictions.  Therefore, the statistics generated during training to normalize data (for example) need to be available when data preparation happens on some input data for prediction.

Which of these solutions can the team choose to ensure that the computed statistics needed for data preparation are available with the exported model used for serving predictions?

- [ ] A Transform data using Dataflow and the TensorFlow Data Validation library.
- [ ] B Transform data using Dataflow and store the statistics needed to prepare data at prediction time in Cloud SQL.
- [ ] C Transform data using Dataflow and the TensorFlow Transform library.
- [ ] D Transform data using BigQuery and store the statistics needed to prepare data at prediction time.

**21.** A global media company provides news stories to its customers in various languages spoken throughout the world.  The company has started an initiative to reduce the resources needed to translate the stories into multiple languages and has asked a team of machine learning engineers to help with this problem.  Before starting the project, the machine learning engineers want to begin with a clear statement about what the machine learning model will predict and define how they plan to measure success.

Which set of statements would be an appropriate description of the ideal outcome of the project and how the team will measure success?

- [ ] A
  - Ideal outcome: The team uses fewer resources by only translating popular news stories.
  - Success metric: Success means that the area under the curve (AUC) evaluation metric is greater than some specified value for the model.

- [ ] B
  - Ideal outcome: The model is able to identify news stories that users will find interesting.
  - Success metric: Success means the team sees a specified reduction in the CPU resources needed to translate stories.

- [ ] C
  - Ideal outcome: Identify news stories that users will find interesting.
  - Success metric: Success means that the area under the curve (AUC) evaluation metric is greater than some specified value for the model.

- [ ] D
  - Ideal outcome: The team uses fewer resources by only translating popular news stories.
  - Success metric: Success means the team sees a specified reduction in the CPU resources needed to translate stories.

**22.** A company that manufactures automobiles is developing a machine learning model to forecast the number of parts they need to order from suppliers to support future warranty claims.  The data scientists working on the project have historical data that includes the number of parts consumed per month for the past ten years.

Which of the following machine learning algorithms would you use to examine this time series data and make a prediction about part inventory requirements in the coming months?

- [ ] A Convolutional Neural Network
- [ ] B Generalized linear model
- [ ] C Feed-Forward Neural Network
- [ ] D Long short-term memory (LSTM) 

**23.** You work for a company that provides an online auction platform to buy and sell consumer-to-consumer goods. You recently deployed a machine learning model to the Google Cloud AI Platform to predict a reasonable starting price for any item listed on the website. You trained the model using TensorFlow. Recently, after calling the REST endpoint for the prediction service in production, you receive an out-of-memory status code (HTTP 429).

What steps can you take to address this issue without increasing the memory allocated for the prediction node?  (Choose 2 answers)

- [ ] A Reduce the model's size by quantizing continuous data.
- [ ] B Retry the request with a smaller number of instances in the request body.
- [ ] C Increase the precision of model weights.
- [ ] D Retrain the model and use one-hot encoding for all categorical features.

**24.** An organization that connects donors to grant proposals for public school projects is building a machine learning model using Google Cloud AI Platform to predict the likelihood that a project becomes fully funded.  Part of the grant process involves educators completing an application that includes some questions that allow free responses.  This unstructured text data will serve as input to train the model;  however, it can potentially include personally identifiable information.  

What Google Service should the team choose to help ensure that personal user information is protected during model training?

- [ ] A Dataproc
- [ ] B Identity and Access Management (IAM)
- [ ] C Secret Manager
- [ ] D Cloud Data Loss Prevention

**25.** You are training a machine learning model using a Dense Neural Network (DNN) to predict the starting salary of recent college graduates.  After the most recent training run, you notice that the generalization curve shows the loss for the training data continues to decrease gradually with the number of iterations. In contrast, the loss for the validation data set initially decreases but begins to increase with more iterations.

What is likely causing this behavior, and what can you do to address this issue?

- [ ] A
  - Problem: Overfitting
  - Proposed Solution: Retrain the model using L2 regularization to minimize the overfitting problem.
- [ ] B
  - Problem: Underfitting
  - Proposed Solution: Retrain the model with an additional hidden layer to the DNN
- [ ] C
  - Problem: Overfitting
  - Proposed Solution: Retrain the model using a larger training data set and a larger number of iterations.
- [ ] D
  - Problem: Underfitting
  - Proposed Solution: Retrain the model with additional features included in the training algorithm.

**26.** You are using Google AI platform notebooks to experiment with a new binary classification model to predict if a bank should give a customer a business loan.  During the model development process, you would like to use an interactive visual tool to compare two models.  Also, of particular importance, the tool that you choose must be capable of evaluating different fairness policies.

Which of the following Google AI tools would be most appropriate for your investigation?

- [ ] A Use IPython Magics for BigQuery within your notebook.
- [ ] B Use the What-If Tool (WIT) within your notebook.
- [ ] C Use Google AI Platform Explanations within your notebook.
- [ ] D Use TensorBoard Profiling tool within your notebook.

**27.** You are working on a classification model to predict if an image is a picture of a sedan, a truck, or a sport utility vehicle (SUV).  You are planning to use TensorFlow and build your model using a deep neural network (DNN).  The output of the model should be the probability that the image is either a sedan, a truck, or an SUV.

How many output nodes should your model include, and which activation function should you choose for the output layer?

- [ ] A Choose an output layer with 3 output nodes with a softmax activation function.
- [ ] B Choose an output layer with 1 output node with a softmax activation function.
- [ ] C Choose an output layer with 3 output nodes with a reLU activation function.
- [ ] D Choose an output layer with 1 output node with a reLU activation function.

**28.** You are working on a binary classification model to predict whether a patient will return for care within seven days of being released from the hospital.  After training the model, you find that the precision is lower than anticipated, so you decide to increase the classification threshold.  

What effect would you expect to see after increasing the classification threshold?

- [ ] A
  - Precision will always increase 
  - Recall will probably increase
- [ ] B
  - Precision will probably increase
  - Recall will stay the same
- [ ] C
  - Precision will always increase
  - Recall will always decrease or stay the same
- [ ] D
  - Precision will probably increase
  - Recall will always decrease or stay the same

**29.** A company that provides an online real estate marketplace uses a TensorFlow machine learning model deployed to Google AI Platform prediction to predict housing prices based on a large set of features. One of the features the model uses is the 'building type,' and it expects the values 'house,' 'duplex,' and 'apartment';  however, at prediction time, an instance is submitted with a building type = 'mobile home.'   

The team is implementing a CI/CD automation pipeline to manage model updates and monitor model performance.  

What steps should the team take to identify and handle instances of schema skew that may impact model performance?

- [ ] A
  - Use TensorFlow Data Validation (TFDV) to detect anomalies in the predefined schema. 
  - Update the schema and data pipeline, then retrain the model.
- [ ] B
  - Use Dataprep to detect anomalies in the predefined schema. 
  - Update the schema and data pipeline, then retrain the model.
- [ ] C
  - Use Dataprep to detect anomalies in the predefined schema. 
  - Trigger the training pipeline when new training data is available.
- [ ] D
  - Use TensorFlow Data Validation (TFDV) to detect anomalies and update the schema. 
  - Use Cloud Scheduler to trigger the training pipeline on a recurring schedule.

**30.** You are using Google AI Platform notebooks to experiment with a new machine learning model.  It is important to reduce costs as much as possible for this project.   The raw data is stored in BigQuery, and your team has a git repository for projects.

What steps should you take to ensure you not charged for Google AI Platform notebook when you are not actively working on the project?  (Choose 2 answers)

- [ ] A Save the notebook to Cloud Storage
- [ ] B Delete the notebook instance
- [ ] C Save the training data to Cloud Storage
- [ ] D Push your code to a git repository

## Answers
### 1.
- [x] Use Pub/Sub and Cloud Functions to trigger the pipeline and retrain the model when a new training data file is added to Cloud Storage.

**Explanation**
- The choice to use Pub/Sub and Cloud Functions to trigger the pipeline and retrain the model when a new training data file is added to Cloud Storage is correct because this is the only answer that will trigger the build as soon as new data is available.
- The choice to use Cloud Scheduler to set up a cron job to retrain the model every 14 days (or on some recurring schedule) could also work, but it is not as optimal a choice because when the job runs new data may or may not be ready.
- The choice to use Cloud Monitoring to track the cumulative count of predictions (prediction_count) and retrain the model when the number of predictions goes above some maximum level is incorrect because it has nothing to do with new training data.
- The choice to use Cloud Monitoring to trigger the pipeline and retrain the model when a new training data file is added to Cloud Storage is incorrect because Cloud Monitoring can not be used in this way.
 

https://cloud.google.com/architecture/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build

### 2.
- [x] Use the BigQuery Storage API to load the data directly into a Pandas DataFrame.

**Explanation**
The BigQuery Storage Read API allows you to access your data in BigQuery using one of several popular programming languages (Go, Java, Python).  

The following list explains why the remaining choices are incorrect:

- The option that suggests exporting the data from BigQuery to Cloud Storage and then reading in the data from Cloud Storage is not the best approach.  While it is possible to implement it this way, it is more work and cost than is necessary.
- The option that says to use BigQuery connector to provide read access from within the AI Platform Notebook is incorrect because BigQuery connector offers read/write access to BigQuery from Cloud Dataproc.  You do not use a BigQuery connector from an AI Platform notebook.
- The option that suggests using Dataflow is incorrect because this is a straightforward machine learning experiment and does not need infrastructure code to manage data preparation.

**Additional Resources:**
- IPython magics for BigQuery https://cloud.google.com/bigquery/docs/bigquery-storage-python-pandas#download_query_results_using_the_ipython_magics_for
- Download table data using the BigQuery client library https://cloud.google.com/bigquery/docs/bigquery-storage-python-pandas#download_table_data_using_the_client_library

https://cloud.google.com/bigquery/docs/reference/storage

### 3.
- [x] Long short-term memory (LSTM) 

**Explanation**

[Long short-term memory (LSTM)](https://en.wikipedia.org/wiki/Long_short-term_memory)  is a special type of recurrent neural network (RNN) designed to handle time-series data.  Using LSTM works better than vanilla RNN because it does not suffer from the problem of vanishing gradients.

The other options do not work well for modeling temporal sequences.  Here is a description of the other options:

- [Convolutional Neural Network](https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks) (CNN) - Machine learning engineers use CNN when building an image classification model.
- [Feed-Forward Neural Network](https://developers.google.com/machine-learning/glossary#feedforward-neural-network-ffn) (FNN) - Traditional neural networks use feed-forward.  In a feed-forward algorithm, there are no cycles or recursion like with a recurrent neural network.
- [Generalized linear model](https://developers.google.com/machine-learning/glossary#generalized-linear-model)
 

[/course/recurrent-neural-networks/lstm-and-gru/](https://cloudacademy.com/course/recurrent-neural-networks/lstm-and-gru/)

### 4.
- [x] Transform data using Dataflow and the TensorFlow Transform library.

**Explanation**

Data preparation for machine learning is an important consideration, particularly when training a model to support an application in production.  While deciding on the right implementation to prepare data for ML, you need to think about finding a solution that will minimize the chances of running into problems with a [training-serving skew](https://developers.google.com/machine-learning/guides/rules-of-ml/#training-serving_skew) or handling transformation that involve a complete pass of the data.  

There are a variety of tools you could choose to help you preprocess your data for ML: BigQuery, Dataflow, etc.  Ideally, you want to store the statistical information used at training time to normalize data directly with the model to transform the data in the same way automatically.  The only solution that provides this ability is to use Dataflow with the TensorFlow Transform library.  

The following options could certainly be a way to implement data preparation;  however, these are not ideal choices because the data is not stored with the machine learning model and could be more challenging to maintain.

- Transform data using BigQuery and store the statistics needed to prepare data at prediction time.
- Transform data using Dataflow and store the statistics needed to prepare data at prediction time in Cloud SQL.

The option of using Dataflow and the TensorFlow Data Validation library is incorrect because you would not use the TensorFlow Data Validation library to transform data.  You could, however,  use it to validate the data and check for schema skew.

https://cloud.google.com/architecture/data-preprocessing-for-ml-with-tf-transform-pt1#preprocessing_options_summary

**5.** AutoML Tables

**Explanation**

AutoML Tables is a good choice for teams that have structured training data but may not have the time or expertise to determine the right machine learning algorithm for their problem.  Another benefit of using AutoML Tables is it takes care of all the work to tune and optimize the model.

The other choices require some specific knowledge of machine learning algorithms and programming languages.

https://cloud.google.com/automl-tables

### 6.
- [x] Use Google AI Platform Training with scale tier =  BASIC_GPU (a single worker instance with a standard machine type + 1 GPU)

**Explanation**
Using AutoML Tables with a standard machine type and a 6-hour training budget is incorrect because the problem statement says that the team is using Tensorflow to build the model.  AutoML Tables would not support this type of use case.  Also, with AutoML, you would not select a machine type since the service takes care of this for you.

The correct AI service to choose in this case is Google AI Platform Training.  The next choice is to decide the appropriate scale tier to use.  Because the team uses a DNN with TensorFlow, a configuration that includes a GPU accelerator would be the best choice for performance.  The team should start with a BASIC_GPU configuration to minimize costs, and if performance is not where it needs to be, they can move up to another scale tier to meet their needs.

**Additional Resources**

- [Using GPUs for Training Models](https://cloud.google.com/ai-platform/training/docs/using-gpus)
- [AutoML Tables  > Training Models](https://cloud.google.com/automl-tables/docs/train)

https://cloud.google.com/ai-platform/training/docs/machine-types#scale_tiers

### 7.
- [x]
  - Use TensorFlow Data Validation (TFDV) to detect anomalies in the predefined schema. 
  - Update the schema and data pipeline, then retrain the model.

**Explanation**

The choices that say to use Dataprep to detect anomalies in a predefined schema are incorrect because you can not use Dataprep in an automated CI/CD pipeline to detect schema anomalies.  However, you can use TensorFlow Data Validation (TFDV) to detect anomalies in the predefined schema.  Also, the library is specifically designed to support MLOps pipelines.

In the production phase, if you are using TensorFlow Data Validation (TFDV) to detect schema skew, the next step is to update the schema, data pipeline and retrain the model.

**Additional Resources**

- [TensorFlow Data Validation](https://www.tensorflow.org/tfx/data_validation/get_started)
- [TensorFlow Data Validation in Production](https://cloud.google.com/architecture/analyzing-and-validating-data-at-scale-for-ml-using-tfx#tfdv_in_the_production_phase)

https://cloud.google.com/architecture/analyzing-and-validating-data-at-scale-for-ml-using-tfx


### 8.
- [x] Compare your model output against a model that always predicts the most common label.

**Explanation**

If you are building a machine learning model for the first time, it is good to establish a simple heuristic that you can use as a quick test to evaluate the model.  If your model, which is by definition more complex than a simple heuristic, performs worse than the heuristic, then you need to refine the model.  Of the choices, there are two that suggest comparing the model against a conventional heuristic:

- Compare your model output against a model that always predicts the most common label.
- Compare your model with one that predicts each label 50% of the time.

The second choice (above) would not be a good heuristic because there is no reason to suppose that the proportion of each label is 50%.  The best heuristic to use is the first choice (above).

Other choices:

- The choice that suggests setting the baseline to a model trained with no regularization is not correct because that would mean that the model has more complexity than your model.
- The choice that suggests setting the baseline to a model trained with just one epoch is not correct because that model would be meaningless.

https://developers.google.com/machine-learning/testing-debugging/common/model-errors#establish-a-baseline

### 9.
- [x] Cloud Data Loss Prevention

**Explanation**

Cloud Data Loss prevention is a managed service customers can use to identify and redact personally identifiable information in data to comply with a company's privacy policy.  In machine learning, this can be particularly useful to redact sensitive information that the system might otherwise expose in a set of training data.  

**Additional Resources**

- [Cloud Data Loss Prevention: How-to guides](https://cloud.google.com/dlp/docs/how-to)

https://cloud.google.com/architecture/sensitive-data-and-ml-datasets

### 10.
- [x] The batch size is too small.

**Explanation**

When using TPU hardware, as in this case, you should use a batch size of at least 8 per TPU core.  So, in this case, that would be a batch size of 64.  Ideally, a larger batch size would be better, and the recommended size is 128 per TPU core, which is a batch size of 1024 in this case.  The correct answer to this question is that the batch size is too small.

Though, in this case, the problem was with the batch size, it is also important that you set the number of iterations per loop (iterations_per_loop in the TPUConfig) appropriately when submitting your training job.  Setting the iterations_per_loop too small can cause performance issues because of the communication overhead associated with sending data to the TPU server.  You will know if you set the iterations_per_loop too low if you see the `"Enqueue next (X) batch(es) of data to infeed "` message printed frequently in your logs. 

https://cloud.google.com/tpu/docs/troubleshooting#batch-too-small

### 11.
- [x] During data preparation, normalize the feature using clipping.

**Explanation**

The appropriate step in this problem is to normalize the data for this feature.  Which normalization method is the best choice?  Since the data includes some outliers, you should choose a clipping strategy when normalizing the data.  With this approach, you set a fixed value for all examples above or below a certain threshold.  The clipping operation can take place before or after you normalize the data.

You could use linear scaling before or after you perform clipping, but when you have outliers as described in this problem, normalization using linear scaling may still cause instability.


https://developers.google.com/machine-learning/data-prep/transform/normalization

### 12.
- [x]
  - Problem: Class Imbalance
  - Solution: Retrain the model with a smaller set of the examples labeled with 'not fraud' (downsampling), and add a weight to these examples (upweighting).

**Explanation**

Let's start by identifying the problem described in this scenario.  Is this an example of overfitting or class imbalance? 

- **Overfitting:** This scenario is not an example of overfitting because the problem says that the loss curve shows a gradual decrease for both the training data and validation data.  If this were a problem with overfitting, we would expect to see the loss for the validation set begin to increase.
- **Class Imbalance:**  This scenario is an example of class imbalance.  The items in the training dataset representing fraudulent data make up only 1% of the total samples.  In a classification problem such as this one, if the proportion of the minority class is significant, then you may need to take steps to address the imbalance.

What steps do machine learning engineers take to address class imbalance?  Ideally, it would be great if you could come up with more examples representing fraudulent behavior.  However, for some problems, the minority class does not happen in real life very often, so these examples might be hard to find.  An alternative is to use a data preparation approach called downsampling and upweighting.  You would apply this technique to the majority class; in this case, the examples that are not labeled as fraudulent.   Here is a description of the process:

- **Downsampling:**  Use a smaller set of the examples labeled with 'not fraud' (majority class) so that there is less of an imbalance between the two classes.
- **Upweighting:** After downsampling, you need to add weight to the data that makes up the downsampling set.  This weight should be proportional to the factor by which you downsampled the majority class.
 

https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/imbalanced-data

### 13.
- [x] The new training data triggers the training pipeline to run and train a new model with the updated training data.  If the model evaluation passes, the system deploys a new model.

**Explanation**

This question scenario is an example of continuous training (CT) in an MLOps pipeline.  Continuous training is a practice whereby the training pipeline is automatically triggered when new training data is available.  When new training data is available, the system kicks off the training pipeline, and if the model passes the evaluation metrics, it is deployed into production.  When training data is available, a new pipeline is not deployed.  Deploying a new pipeline only happens when developers update the code that defines the pipeline or the training code.

https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning

### 14.
- [x]
  - Developer commits model/pipeline code
  - Trigger a build on Cloud Build to build the pipeline
  - Deploy and run the training pipeline to train a new model version

**Explanation**

Continuous integration is a development practice whereby developers frequently commit code to a source repository, and then the code is built, tested, and then deployed to a test environment.  When implementing a continuous integration process for ML projects, the code stored in a source repository would include artifacts like training code, training pipeline code, or data preparation code.  When a developer commits code to a particular source repository, this will trigger a build system to initiate a build.  The build process builds and packages the training pipeline and runs automated tests to verify the quality of the new code.  If all tests pass, the build will output a new training pipeline.  The last step in the process is to deploy and run the new training pipeline. 

The correct option that describes the series of steps for a basic ML continuous integration process is:

1. Developer commits model/pipeline code.
2. Trigger a build on Cloud Build to build the pipeline.
3. Deploy and run the training pipeline to train a new model version.

Another option is worth pointing out also.  The option that says:

1. New training data is available
2. Run the training pipeline and train a new model
3. Evaluate the new model and create a new model version

is a description of a process called continuous training (CT).  Continuous training is triggered when new training data is available.  The process kicks off a new training run (through the training pipeline) and can result in a new model version.  However, continuous training does not involve deploying a new training pipeline.

Teams often will implement both continuous training and continuous integration at the same time.

**Additional Resources**

- [Cloud Build](https://cloud.google.com/build/docs/concepts)

https://cloud.google.com/architecture/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build#cicd_pipeline_compared_to_ct_pipeline

### 15.
- [x] Package the images in several TFRecord files and store them on Google Cloud Storage.  Read the images into a `tf.data.TFRecordDataset` for training.

**Explanation**

The option that suggests storing each image file on Google Cloud Storage and then reading the images into a tf.data.Dataset for training would work.  However, this would most certainly cause a performance issue.  Instead, you should process the data prior to training and package the images into TFRecord format.  Then, during training, read the data into a TFRecordDataset.

**Additional Resources**
- [Input processing bottleneck](https://cloud.google.com/tpu/docs/troubleshooting#processing-bottleneck)

https://codelabs.developers.google.com/codelabs/keras-flowers-data/#4

### 16.
- [x] Categorical cross-entropy

**Explanation**

When working with a multi-class classification problem, and the values are labeled using one-hot encoding, you should use **categorical cross-entropy** as your loss function.

Here is a brief explanation of the remaining choices:

- [Binary cross-entropy](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryCrossentropy) - Use as the loss function in a binary classification problem.
- [Sparse cross-entropy](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalCrossentropy) -  is similar to categorical cross-entropy, but the difference is how you represent the labeled value.  With sparse cross-entropy, you indicate the labeled values with an integer rather than one-hot encoding.
- Mean squared error - is not used as a loss function for classification problems.  Instead, you would use mean squared error for regression algorithms.

https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy


### 17.
- [x]
  - Use Google AI Platform and set up a continuous evaluation job. 
  - Choose to provide your own labels for the ground truth labeling method. 
  - Evaluate model performance using precision-recall curves and a confusion matrix.

**Explanation**

The continuous evaluation service allows you to evaluate how well your model performs on real-world data over time.  For the service to assess model performance, the system must first sample some data submitted to the prediction service.  Next, before the system can judge how the model predicts the correct outcome, each sample instance must be assigned a ground-truth label.  A ground-truth label is a label that a human assigns to an instance after reviewing the information.  There are two options for assigning ground-truth labels:

- Use Google's Data Labeling Service, and human reviewers review your data
- You provide ground truth labels yourself for the data

The choice you make for how to assign ground truth labels depends in part on the type of model you are evaluating and the type of expertise that is needed to determine the ground truth label.  Our scenario is a general classification model, and the data labeling service is not available for this type of model.  Instead, we must choose to label the sample instances ourselves on an ongoing basis based.

Finally, we should use precision-recall curves or a confusion matrix to evaluate the model's ongoing performance.  Binary cross-entropy loss is a metric used during model training and would not be appropriate at this stage.

**Additional Resources**
- [Model Types supported by Continuous Evaluation](https://cloud.google.com/ai-platform/prediction/docs/continuous-evaluation/before-you-begin#model-requirements)

https://cloud.google.com/ai-platform/prediction/docs/continuous-evaluation

### 18.
- [x] Reduce the model's size by quantizing continuous data.
- [x] Retry the request with a smaller number of instances in the request body.

**Explanation**

If you need to address an out-of-memory condition without increasing the memory allocated for the prediction node, you will need to reduce the model size.  To reduce your model size, this might mean that you need to retrain the model;  however, you can also do some model optimization with post-training quantization.  

In the choice list, there are only two options that will allow you to reduce the memory usage at prediction time.    These choices are:  (1) Reduce the size of the model by quantizing continuous data (2) Retry the request with a smaller number of instances in the request body.  With option #2, you can try another request without updating the model on the prediction node;  however, with option 1 you would need to retrain or preform post-training optimiztion.

**Additional Information**
- [Model Optimization: Post-training quantization](https://www.tensorflow.org/model_optimization/guide/quantization/post_training)

https://cloud.google.com/ai-platform/training/docs/troubleshooting#http_status_codes

### 19.
- [x] Dataprep by Trifacta

**Explanation**

Dataprep by Trifecta allows data analysts the ability to explore and transform data from various data sources.  The output from Dataprep is called a recipe.  A recipe is a set of transformations applied to data from one or more sources and saved in another destination.  The underlying data in the source system is not modified.  You can run a recipe multiple times.

https://docs.trifacta.com/display/DP/Product+Overview

### 20.
- [x] Use Dataflow for steps 2 - 3 and use Kubeflow to orchestrate the training pipeline.

**Explanation**

Let's first start by looking at the appropriate workflow orchestration framework for a machine learning project.  Both Cloud Composer and Kubeflow are workflow orchestration services;  however, [Kubeflow](https://www.kubeflow.org/) is specifically dedicated to making machine learning deployments simple.  For the orchestration framework, we are looking for an answer that includes Kubeflow.

Next, we need to decide the appropriate service for steps 2 and 3 in our process: (2) Data Extract and Validation and (3) Data Transformation.  The correct answer is to use Dataflow.  Dataflow is a serverless streaming/batch data processing service that machine learning engineers use to preprocess and prepare training data for machine learning pipelines.  While you can use Dataprep to create data preparation 'recipes', this tool is a visual tool that is not well suited for an automated pipeline.

https://cloud.google.com/architecture/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build

### 21.
- [x] Use BigQuery for data preparation and BigQuery ML to create the model.

**Explanation**

BigQuery ML is a good machine learning platform to select if you are comfortable with SQL syntax but do not have a strong background in programming in languages like Python or Java.  BigQuery ML provides an SQL-like syntax to train models and supports the most common ML algorithms.  BigQuery ML also supports building a time series model such as the one described in this question.  The other option in this problem describes using AI Platform Training.  This would not be an ideal choice since it would require programming in a language like Python to build the model.

For data preparation, Dataflow would require non-SQL programming skills.  Only BigQuery would work in this case for data preparation.

https://cloud.google.com/bigquery-ml/docs/introduction

### 22.
- [x] Use one-hot encoding to transform the data

**Explanation**

There are several ways to encode categorical data.  One of the most common approaches is to use one-hot encoding.  To see how this works, consider the following car data:
```
+-----------------+----------+-----------+
|           car_id|       ...|      color|
+-----------------+----------+-----------+
|            12345|          |        red|
|            12345|          |      white|
|            56789|          |       grey|
|            10777|          |      black|
+-----------------+----------+-----------+
```
After one hot encoding, the data looks like this:
```
+-----------------+----------+-------------+-------------+-------------+-------------+
|           car_id|       ...|      color_r|      color_w|      color_g|      color_b|
+-----------------+----------+-------------+-------------+-------------+-------------+
|            12345|          |            1|            0|            0|            0|
|            12345|          |            0|            1|            0|            0|
|            56789|          |            0|            0|            1|            0|
|            10777|          |            0|            0|            1|            0|
+-----------------+----------+-------------+-------------+-------------+-------------+
```
One of the drawbacks of using one-hot encoding is that it increases the amount of space needed to store a dataset in memory, which can be particularly problematic if there are many categories to encode.  There are other ways to handle these situations, but it is beyond the scope of this question.

The option that says to use ordinal encoding could work, but it is not an ideal choice because it assigns a numeric weight to the car's color when there should not be one.  An ordinal encoding might be the right choice for a category like size (small, medium, and large).  Assigning a higher ordinal to larger has some meaning within the model.

You could use an [embedding layer](https://developers.google.com/machine-learning/glossary#embeddings) if you were using a neural network algorithm, but it is not an ideal choice in this scenario.

https://developers.google.com/machine-learning/data-prep/transform/transform-categorical

### 23.
- [x] Create a custom container with the required dependencies.

**Explanation**

The correct choice is to create a custom container with the required dependencies and use this container for training.  The AI Platform Training library support does not include PyTorch;  instead, you need to use a custom container.  There is a pre-built PyTorch container that you could use, but in this case, the team is using other library dependencies that will require them to create their own custom container.

Use the `--master-image-uri` flag to specify the custom container to use if you are using the gcloud ai-platform CLI.

**Additional Resources**

- [gcloud ai-platform CLI Documentation](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--master-image-uri)
 
https://cloud.google.com/ai-platform/training/docs/containers-overview


### 24.
- [x] Choose an output layer with 3 output nodes with a softmax activation function.

**Explanation**

This question describes a multi-class classification problem, and the algorithm is a multi-class neural network.  There are three classes of vehicles in the training dataset, so the number of output nodes should be three, one for each type of vehicle.  The activation function best suited for this type of problem is the softmax activation function.  The softmax takes values in each of the three output nodes and normalizes them into a probability distribution.  After applying the softmax function, the sum of the values in the output nodes should add up to 1.  The node with the maximum probability corresponds to the predicted label for an example.

**Additional Resources**

- [ReLU activation function](https://developers.google.com/machine-learning/crash-course/introduction-to-neural-networks/anatomy#common-activation-functions)

https://developers.google.com/machine-learning/crash-course/multi-class-neural-networks/softmax

### 25.
- [x]
  - Precision will probably increase
  - Recall will always decrease or stay the same

**Explanation**

Let's first start by defining how to calculate precision and recall:
```
precision = TP / (TP + FP) 
recall    = TP / (TP + FN)
```

where TP = true positive, FP = false positive, FN = false negative, and TN = true negative.

Now, imagine increasing the classification threshold on this set of data: 
```
0 ------------------------------------------------------- 1.0
                                      |
  o  o  o  o  o  o  o  o  o  x  o  x  | x  o  x  o  o  o 
  TN TN TN TN TN TN TN TN TN FN TN FN | FP TP FP TP TP TP
                                      |
                                 Threshold (0.8)
```
- **Precision:**  Generally, when you increase the threshold, the number of false positives will decrease.  When the number of false positives goes down, you will see an increase in precision.  However, it is still possible that the precision could also decrease or stay the same.  The correct answer for how precision responds to increasing the threshold is that it will probably increase.
- **Recall:**  When you increase the threshold, the number of false negatives will either increase or stay the same.  At the same time, the number of true positives will either decrease or remain the same.  In either scenario, this will cause the recall to always decrease or stay the same.
 

https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall


### 26.
- [x]
  - Problem: Overfitting
  - Proposed Solution: Retrain the model using L2 regularization to minimize the overfitting problem.

**Explanation**

The generalization curve described in the question statement is an example of overfitting.  Overfitting occurs when a model matches training data so closely that it doesn’t generalize well to other data.  Machine learning engineers often use a technique called regularization to address overfitting problems.  Here are some examples of regularization:

- [Early stopping](https://developers.google.com/machine-learning/glossary#early-stopping) - A simple technique that stops training before the model becomes too complex and overfitting occurs.
- [Dropout](https://developers.google.com/machine-learning/crash-course/training-neural-networks/best-practices#dropout-regularization) - A technique used with DNN that randomly removes nodes in the neural network to prevent overfitting.
- [L1/L2](https://developers.google.com/machine-learning/crash-course/training-neural-networks/best-practices#dropout-regularization) regularization - With L1/L2 regularization, we add a complexity term to the overall loss function we are trying to minimize while training.  This complexity term differs depending on whether you are using L1 or L2 regularization.  This complexity term is there to penalize models that are too complex.

Underfitting can also occur when our model is not complex enough and cannot learn well from the features we are using to train the model.

https://developers.google.com/machine-learning/crash-course/regularization-for-simplicity/l2-regularization

### 27.
- [x]
  - Ideal outcome: The team uses fewer resources by only translating popular news stories.
  - Success metric: Success means the team sees a specified reduction in the CPU resources needed to translate stories.

**Explanation**

Before starting a machine learning project, it is important to begin by thinking about the ideal outcome you want and how you will measure if you have reached this goal.  

In this case, the question statement already states the ideal outcome pretty plainly in the question statement; the ideal outcome is that the team uses fewer resources by only translating popular news stories.  The next part is choosing the right metric to measure success.  The success metric you choose should not include statements about metrics you would use to evaluate the model.  For example, you would not specify a target AUC value to indicate success.  Instead, you will need to specify success criteria that are measurable and connected to the ideal output.  In this case, a quantifiable reduction in CPU utilization (and cost).

https://developers.google.com/machine-learning/problem-framing/framing


### 28.
- [x]
  - Push your code to a git repository
  - Delete the notebook instance

**Explanation**

If you want to reduce costs, you can either shut down or delete your AI Platform notebook instance when it is not in use.  If you shut down the instance, you will still pay for storage but not the compute resources.  By deleting the instance, you eliminate compute and storage costs.  If you choose to delete the instance, you will need to save your work to another location.  Since this team is already using git as a source repository, pushing the code to the git repository is the best option.

https://cloud.google.com/architecture/best-practices-for-ml-performance-cost#treat_your_ai_platform_notebooks_as_ephemeral_instances

### 29.
- [x] binary classification

**Explanation**

In the scenario presented for this question, the model needs to predict an outcome that is a choice between two discrete values;  this is considered a binary classification problem.  If the prediction were a choice between multiple discrete values, the problem would be a multi-class classification problem. 

Another class of machine learning problems is when you need to predict a continuous value; in this situation, linear regression would be the appropriate choice to consider.

[/course/intro-machine-learning/supervised-learning/](https://cloudacademy.com/course/intro-machine-learning/supervised-learning/)

### 30.
- [x] Use the What-If Tool (WIT) within your notebook.

**Explanation**

You can use the What-If Tool (WIT) to inspect your AI Platform models right within your notebook environment.  WIT includes a dashboard that can help you visually compare models and better understand the behavior of your model.  

To learn more about the alternative choices, you can take a look at these resources:

- [IPython Magics for BigQuery](https://googleapis.dev/python/bigquery/latest/magics.html) - You can use BigQuery magics to easily access data stored in BigQuery from within your AI Platform notebooks.  You do not use these tools to evaluate models.
- [TensorBoard Profiling Tool](https://www.tensorflow.org/tensorboard/tensorboard_profiling_keras) - You can use TensorBoard within your notebook to visually explore information about your model.  However, the profiling tool is not the right choice for comparing two models or evaluating fairness.  Instead, you use the profiling tool to debug performance bottlenecks based on CPU and GPU events.
- [AI Platform Explanations](https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/overview) - You can use AI Platform Explanations to explore your machine learning models and individual data points within your dataset.  However, it is not interactive and does not help you evaluate model fairness policies.

**Additional Resources:**

- [What-If Tool Documentation](https://pair-code.github.io/what-if-tool/)
- [Blog: Playing with AI Fairness](https://pair-code.github.io/what-if-tool/ai-fairness.html)

https://cloud.google.com/ai-platform/prediction/docs/using-what-if-tool

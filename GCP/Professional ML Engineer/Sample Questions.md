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

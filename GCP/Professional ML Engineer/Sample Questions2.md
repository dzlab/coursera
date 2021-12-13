# Sample Questions

You work for a textile manufacturer and have been asked to build a model to detect and classify fabric defects. You trained a machine learning model with high recall based on high resolution images taken at the end of the production line. You want quality control inspectors to gain trust in your model. Which technique should you use to understand the rationale of your classifier?

- [ ] A. Use K-fold cross validation to understand how the model performs on different test datasets.
- [x] B. Use the Integrated Gradients method to efficiently compute feature attributions for each predicted image.
- [ ] C. Use PCA (Principal Component Analysis) to reduce the original feature set to a smaller set of easily understood features.
- [ ] D. Use k-means clustering to group similar images together, and calculate the Davies-Bouldin index to evaluate the separation between clusters.

**Feedback**
```diff
- A is not correct because K-fold cross validation offers no explanation on the predictions made by the model.
+ B is correct because it identifies the pixel of the input image that leads to the classification of the image itself.
- C is not correct because PCA simplifies higher dimensional datasets but offers no added benefit to the scenario.
- D is not correct because clustering images does not provide any insight into why the classification model made the predictions that it did.
```
- https://storage.googleapis.com/cloud-ai-whitepapers/AI%20Explainability%20Whitepaper.pdf
- https://cloud.google.com/ml-engine/docs/ai-explanations/overview


You need to write a generic test to verify whether Dense Neural Network (DNN) models automatically released by your team have a sufficient number of parameters to learn the task for which they were built. What should you do?
- [ ] A. Train the model for a few iterations, and check for NaN values.
- [ ] B. Train the model for a few iterations, and verify that the loss is constant.
- [ ] C. Train a simple linear model, and determine if the DNN model outperforms it.
- [x] D. Train the model with no regularization, and verify that the loss function is close to zero.
 
**Feedback**
```diff
- A is not correct because the test does not check that the model has enough parameters to learn the task.
- B is not correct because the loss should decrease if you have enough parameters to learn the task.
- C is not correct because outperforming the linear model does not guarantee that the model has enough parameters to learn tasks with non-linear data representations. The option also doesn’t quantify a metric to give an indication of how well the model performed.
+ D is correct because the test can check that the model has enough parameters to memorize the task.
```
- https://developers.google.com/machine-learning/testing-debugging/pipeline/deploying#testing-for-algorithmic-correctness

 
Your team is using a TensorFlow Inception-v3 CNN model pretrained on ImageNet for an image classification prediction challenge on 10,000 images. You will use AI Platform to perform the model training. What TensorFlow distribution strategy and AI Platform training job configuration should you use to train the model and optimize for wall-clock time?

- [ ] A. Default Strategy; Custom tier with a single master node and four v100 GPUs.
- [ ] B. One Device Strategy; Custom tier with a single master node and four v100 GPUs.
- [ ] C. One Device Strategy; Custom tier with a single master node and eight v100 GPUs.
- [x] D. MirroredStrategy; Custom tier with a single master node and four v100 GPUs.
 
**Feedback**
```diff
- A is not correct because Default Strategy does not distribute training across multiple devices.
- B is not correct because One Device Strategy does not distribute training across multiple devices.
- C is not correct because One Device Strategy does not distribute training across multiple devices.
+ D is correct because this is the only strategy that can perform distributed training; albeit there is only a single copy of the variables on the CPU host.
```
- https://www.tensorflow.org/guide/distributed_training


You work on a team where the process for deploying a model into production starts with data scientists training different versions of models in a Kubeflow pipeline. The workflow then stores the new model artifact into the corresponding Cloud Storage bucket. You need to build the next steps of the pipeline after the submitted model is ready to be tested and deployed in production on AI Platform. How should you configure the architecture before deploying the model to production?
- [x] A. Deploy model in test environment -> Evaluate and test model -> Create a new AI Platform model version
- [ ] B. Validate model -> Deploy model in test environment -> Create a new AI Platform model version
- [ ] C. Create a new AI Platform model version -> Evaluate and test model -> Deploy model in test environment
- [ ] D. Create a new AI Platform model version - > Deploy model in test environment -> Validate model
 
**Feedback**
```diff
+ A is correct because the model can be validated after it is deployed to the test environment, and the release version is established before the model is deployed in production.
- B is not correct because the model cannot be validated before being deployed to the test environment.
- C is not correct because the model version is being set up for the release candidate before the model is validated. Moreover, the model cannot be validated before being deployed to the test environment.
- D is not correct because the model version is being set up for the release candidate before the model is validated.
```
- https://cloud.google.com/solutions/machine-learning/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build


You work for a maintenance company and have built and trained a deep learning model that identifies defects based on thermal images of underground electric cables. Your dataset contains 10,000 images, 100 of which contain visible defects. How should you evaluate the performance of the model on a test dataset?
- [x] A. Calculate the Area Under the Curve (AUC) value.
- [ ] B. Calculate the number of true positive results predicted by the model.
- [ ] C. Calculate the fraction of images predicted by the model to have a visible defect.
- [ ] D. Calculate the Cosine Similarity to compare the model’s performance on the test dataset to the model’s performance on the training dataset.

**Feedback**
```diff
+ A is correct because it is scale-invariant. AUC measures how well predictions are ranked, rather than their absolute values. AUC is also classification-threshold invariant. It measures the quality of the model's predictions irrespective of what classification threshold is chosen.
- B is incorrect because calculating the number of true positives without considering false positives can lead to misleading results. For instance, the model could classify nearly every image as a defect. This would result in many true positives, but the model would in fact be a very poor discriminator.
- C is incorrect because merely calculating the fraction of images that contain defects doesn’t indicate whether your model is accurate or not.
- D is incorrect because this metric is more commonly used in distance-based models (e.g., K Nearest Neighbors). This isn’t an appropriate metric for checking the performance of an image classification model.
```
- https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
- https://developers.google.com/machine-learning/clustering/algorithm/advantages-disadvantages

 
You work for a manufacturing company that owns a high-value machine which has several machine settings and multiple sensors. A history of the machine’s hourly sensor readings and known failure event data are stored in BigQuery. You need to predict if the machine will fail within the next 3 days in order to schedule maintenance before the machine fails. Which data preparation and model training steps should you take?

- [ ] A. Data preparation: Daily max value feature engineering; Model training: AutoML classification with BQML
- [ ] B. Data preparation: Daily min value feature engineering; Model training: Logistic regression with BQML and AUTO_CLASS_WEIGHTS set to True
- [ ] C. Data preparation: Rolling average feature engineering; Model training: Logistic regression with BQML and AUTO_CLASS_WEIGHTS set to False
- [ ] D. Data preparation: Rolling average feature engineering; Model training: Logistic regression with BQML and AUTO_CLASS_WEIGHTS set to True
 
**Feedback**
```diff
- A is not correct because a rolling average is a better feature engineering technique, as it will smooth out the noise and fluctuation in the data to demonstrate whether there is a trend. Using the max value could be an artifact of some noise and may not capture the trend accurately.
- B is not correct because a rolling average is a better feature engineering technique, as it will smooth out the noise and fluctuation in the data to demonstrate whether there is a trend. Using the min value could be an artifact of some noise and may not capture the trend accurately.
- C is not correct because the model training does not balance class labels for an imbalanced dataset.
+ D is correct because it uses the rolling average of the sensor data and balances the weights using the BQML auto class weight balance parameter.
```

- https://cloud.google.com/dataprep/docs/html/ROLLINGAVERAGE-Function_57344753
- https://cloud.google.com/dataprep/docs/html/AVERAGE-Function_57344661
- https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create
- https://en.wikipedia.org/wiki/Precision_and_recall
- https://en.wikipedia.org/wiki/Sensitivity_and_specificity
- https://en.wikipedia.org/wiki/Moving_average


You are an ML engineer at a media company. You want to use machine learning to analyze video content, identify objects, and alert users if there is inappropriate content. Which Google Cloud products should you use to build this project?
- [ ] A. Pub/Sub, Cloud Function, Cloud Vision API
- [ ] B. Pub/Sub, Cloud IoT, Dataflow, Cloud Vision API, Cloud Logging
- [x] C. Pub/Sub, Cloud Function, Video Intelligence API, Cloud Logging
- [ ] D. Pub/Sub, Cloud Function, AutoML Video Intelligence, Cloud Logging

**Feedback**
```diff
- A is not correct as there is no tool for alerting and notifying.
- B is not correct as it uses Cloud Vision API for processing videos.
+ C is correct as Video Intelligence API can find inappropriate components and other components satisfy the requirements of real-time processing and notification. (https://cloud.google.com/video-intelligence)
- D is not correct as AutoML Video intelligence should be only used in case of customization.
```
- https://cloud.google.com/solutions/processing-user-generated-content-using-video-intelligence

 
You work for a large retailer. You want to use ML to forecast future sales leveraging 10 years of historical sales data. The historical data is stored in Cloud Storage in Avro format. You want to rapidly experiment with all the available data. How should you build and train your model for the sales forecast?
- [x] A. Load data into BigQuery and use the ARIMA model type on BigQuery ML.
- [ ] B. Convert the data into CSV format and create a regression model on AutoML Tables.
- [ ] C. Convert the data into TFRecords and create an RNN model on TensorFlow on AI Platform Notebooks.
- [ ] D. Convert and refactor the data into CSV format and use the built-in XGBoost algorithm on AI Platform Training.

**Correct answer**
A. Load data into BigQuery and use the ARIMA model type on BigQuery ML.

**Feedback**
```diff
+ A is correct because BigQuery ML is designed for fast and rapid experimentation and it is possible to use federated queries to read data directly from Cloud Storage. Moreover, ARIMA is considered one of the best in class for time series forecasting.
- B is not correct because AutoML Tables is not ideal for fast iteration and rapid experimentation. Even if it does not require data cleanup and hyperparameter tuning, it takes at least one hour to create a model.
- C is not correct because in order to build a custom TensorFlow model, you would still need to do data cleanup and hyperparameter tuning.
- D is not correct because using AI Platform Training requires preprocessing your data in a particular CSV structure and it is not ideal for fast iteration, as training times can take a long time because it cannot be distributed on multiple machines.
```
- https://cloud.google.com/automl-tables/
- https://cloud.google.com/automl-tables/docs/features?hl=en#bqml
- https://towardsdatascience.com/how-to-do-time-series-forecasting-in-bigquery-af9eb6be8159
- https://cloud.google.com/bigquery/external-data-sources

 
You need to build an object detection model for a small startup company to identify if and where the company’s logo appears in an image. You were given a large repository of images, some with logos and some without. These images are not yet labelled. You need to label these pictures, and then train and deploy the model. What should you do?
- [x] A. Use Google Cloud’s Data Labelling Service to label your data. Use AutoML Object Detection to train and deploy the model.
- [x] B. Use Vision API to detect and identify logos in pictures and use it as a label. Use AI Platform to build and train a convolutional neural network.
- [x] C. Create two folders: one where the logo appears and one where it doesn’t. Manually place images in each folder. Use AI Platform to build and train a convolutional neural network.
- [x] D. Create two folders: one where the logo appears and one where it doesn’t. Manually place images in each folder. Use AI Platform to build and train a real time object detection model.

**Feedback**
```diff
+ A is correct as this will allow you to easily create a request for a labelling task and deploy a high-performance model.
- B is not correct because Vision API is not guaranteed to work with any company logos, and in the statement it explicitly mentions a small startup, which will further decrease the chance of success.
- C is not correct because the task of manually labelling the data is time consuming and should be avoided if possible.
- D is not correct because the task of labelling object detection data is very tedious, and real time object detection is designed detecting objects in videos rather than in images.
```
- https://cloud.google.com/ai-platform/data-labeling/docs

 
You work for a large financial institution that is planning to use Dialogflow to create a chatbot for the company’s mobile app. You have reviewed old chat logs and tagged each conversation for intent based on each customer’s stated intention for contacting customer service. About 70% of customer inquiries are simple requests that are solved within 10 intents. The remaining 30% of inquiries require much longer and more complicated requests. Which intents should you automate first?
- [ ] A. Automate a blend of the shortest and longest intents to be representative of all intents.
- [ ] B. Automate the more complicated requests first because those require more of the agents’ time.
- [x] C. Automate the 10 intents that cover 70% of the requests so that live agents can handle the more complicated requests.
- [ ] D. Automate intents in places where common words such as “payment” only appear once to avoid confusing the software.

**Feedback**
```diff
- A is incorrect because you should not automate the higher value requests.
- B is incorrect because live agents are better suited to handle these complicated requests.
+ C is correct because it enables a machine to handle the most simple requests and gives the live agents more opportunity to handle higher value requests.
- D is incorrect because Dialogflow can handle the same word in multiple intents.
```

- https://cloud.google.com/blog/products/ai-machine-learning/discover-card-how-we-designed-an-experiment-to-evaluate-conversational-experience-platforms

 
You work for a gaming company that develops and manages a popular massively multiplayer online (MMO) game. The game’s environment is open-ended, and a large number of positions and moves can be taken by a player. Your team has developed an ML model with TensorFlow that predicts the next move of each player. Edge deployment is not possible, but low-latency serving is required. How should you configure the deployment?
- [ ] A. Use a Cloud TPU to optimize model training speed.
- [x] B. Use AI Platform Prediction with a NVIDIA GPU to make real-time predictions.
- [ ] C. Use AI Platform Prediction with a high-CPU machine type to get a batch prediction for the players.
- [ ] D. Use AI Platform Prediction with a high-memory machine type to get a batch prediction for the players.

**Correct answer**
- [x] B. Use AI Platform Prediction with a NVIDIA GPU to make real-time predictions.

**Feedback**
```diff
A is not correct because changing the training will not improve the prediction latency.
B is correct because using a VM with a GPU and NVIDIA drivers enables you to use TensorRT. NVIDIA has developed TensorRT (an inference optimization library) for high-performance inference on GPUs. Google Cloud’s Deep Learning VMs are ideal for this case because they have everything you need pre-installed.
B is not correct because batch jobs do not satisfy the low-latency requirements for an online multiplayer game.
D is not correct because batch jobs do not satisfy the low-latency requirements for an online multiplayer game.
```

- https://cloud.google.com/blog/products/ai-machine-learning/train-fast-on-tpu-serve-flexibly-on-gpu-switch-your-ml-infrastructure-to-suit-your-needs
- https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-prediction
- https://cloud.google.com/compute/docs/gpus
- https://cloud.google.com/solutions/machine-learning/minimizing-predictive-serving-latency-in-machine-learning#precomputing_and_caching_predictions


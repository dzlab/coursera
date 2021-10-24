# Chapter 9 Deploying Machine Learning Pipelines

## Review Questions


1. You have been tasked with helping to establish ML pipelines for your department. The models will be trained using data from several sources, including several enterprise transaction processing systems and third-party data provider datasets. Data will arrive in batches. Although you know the structure of the data now, you expect that it will change, and you will not know about the changes until the data arrives. You want to ensure that your ingestion process can store the data in whatever structure it arrives in. After the data is ingested, you will transform it as needed. What storage system would you use for batch ingestion?
- [x] A. Cloud Storage
- [ ] B. Cloud Spanner
- [ ] C. Cloud Dataprep
- [ ] D. Cloud Pub/Sub

2. A startup company is building an anomaly detection service for manufacturing equipment. IoT sensors on manufacturing equipment transmit data on machine performance every
30 seconds. The service will initially support up to 5,000 sensors, but it will eventually grow to millions of sensors. The data will be stored in Cloud Bigtable after it is preprocessed and transformed by a Cloud Dataflow workflow. What service should be used to ingest the IoT data?
- [ ] A. Cloud Storage
- [ ] B. Cloud Bigtable
- [ ] C. BigQuery Streaming Insert
- [x] D. Cloud Pub/Sub

3. A machine learning engineer has just started a new project. The engineer will be building a recommendation engine for an e-commerce site. Data from several services will be used, including data about products, customers, and inventory. The data is currently available in a data lake and stored in its raw, unprocessed form. What is the first thing you would recommend the machine learning engineer do to start work on the project?
- [ ] A. Ingest the data into Cloud Storage
- [x] B. Explore the data with Cloud Dataprep
- [ ] C. Transform the data with Cloud Dataflow
- [ ] D. Transform the data with BigQuery

4. A machine learning engineer is in the process of building a model for classifying fraudulent transactions. They are using a neural network and need to decide how many nodes and layers to use in the model. They are experimenting with several different combinations of number of nodes and number of layers. What data should they use to evaluate the quality of models being developed with each combination of settings?
- [ ] A. Training data
- [x] B. Validation data
- [ ] C. Test data
- [ ] D. Hyperparameter data

5. A developer with limited knowledge of machine learning is attempting to build a machine learning model. The developer is using data collected from a data lake with minimal data preparation. After models are built, they are evaluated. Model performance is poor. The developer has asked for your help to reduce the time needed to train the model and increase the quality of model predictions. What would you do first with the developer?
- [x] A. Explore the data with the goal of feature engineering
- [ ] B. Create visualizations of accuracy, precision, recall, and F measures
- [ ] C. Use tenfold cross-validation
- [ ] D. Tune hyperparameters

6. A developer has built a machine learning model to predict the category of new stories.
The possible values are politics, economics, business, health, science, and local news. The developer has tried several algorithms, but the model accuracy is poor even when evaluating the model on using the training data. This is an example of what kind of potential problem with a machine learning model?
- [ ] A. Overfitting
- [x] B. Underfitting
- [ ] C. Too much training data
- [ ] D. Using tenfold cross-validation for evaluation

7. A developer has built a machine learning model to predict the category of new stories.
The possible values are politics, economics, business, health, science, and local news.
The developer has tried several algorithms, but the model accuracy is quite high when evaluating the model using the training data but quite low when evaluating using test data. What would you recommend to correct this problem?
- [ ] A. Use confusion matrices for evaluation
- [ ] B. Use L1 or L2 regularization when evaluating
- [x] C. Use L1 or L2 regularization when training
- [ ] D. Tune the hyperparameters more

8. Your e-commerce company deployed a product recommendation system six months ago. The system uses a machine learning model trained using historical sales data from the previous year. The model performed well initially. When customers were shown product recommendations, the average sale value increased by 14 percent. In the past month, the model has generated an average increase of only 2 percent. The model has not changed since it was deployed six months ago. What could be the cause of the decrease in effectiveness, and what would you recommend to correct it?
- [ ] A. The model is overfitting—use regularization.
- [x] B. The data used to train the model is no longer representative of current sales data, and the model should be retrained with more recent data.
- [ ] C. The model should be monitored to collect performance metrics to identity the root cause of the decreasing effectiveness of the model.
- [ ] D. The model is underfitting—train with more data.

9. A startup company is developing software to analyze images of traffic in order to understand congestion patterns better and how to avoid them. The software will analyze images that are taken every minute from hundreds of locations in a city. The software
will need to identify cars, trucks, cyclists, pedestrians, and buildings. The data on object identities will be used by analysis algorithms to detect daily patterns, which will then be used by traffic engineers to devise new traffic flow patterns. What GCP service would you use for this?
- [x] A. AutoML Vision Object Detection
- [ ] B. AutoML Vision Edge - Object Detection
- [ ] C. AutoML Video Intelligence Classification
- [ ] D. Auto ML Video Intelligence Object Tracking

10. An analyst would like to build a machine learning model to classify rows of data in a dataset. There are two categories into which the rows can be grouped: Type A and Type B. The dataset has over 1 million rows, and each row has 32 attributes or features. The analyst does not know which features are important. A labeled training set is available with a sufficient number of rows to train a model. The analyst would like the most accurate model possible with the least amount of effort on the analyst’s part. What would you recommend?
- [ ] A. Kubeflow
- [ ] B. Spark MLib
- [x] C. AutoML Tables
- [ ] D. AutoML Natural Language

11. The chief financial officer of your company would like to build a program to predict
which customers will likely be late paying their bills. The company has an enterprise data warehouse in BigQuery containing all the data related to customers, billing, and payments. The company does not have anyone with machine learning experience, but it does have analysts and data scientists experienced in SQL, Python, and Java. The analysts and
data scientists will generate and test a large number of models, so they prefer fast model building. What service would you recommend using to build the model?
- [ ] A. Kubeflow
- [ ] B. Spark MLib
- [x] C. BigQuery ML
- [ ] D. AutoML Tables

12. A team of researchers is analyzing buying patterns of customers of a national grocery store chain. They are especially interested in sets of products that customers frequently by together. The researchers plan to use association rules for this frequent pattern mining. What machine learning option in GCP would you recommend?
- [ ] A. Cloud Dataflow
- [x] B. Spark MLib
- [ ] C. BigQuery ML
- [ ] D. AutoML Tables

## Week 2 - Introduction to Preprocessing

### Feature Engineering
#### PRACTICE QUIZ - Feature Engineering and Preprocessing

Question 1
In the mapping of categorical values, can models directly multiply strings by the learned weights?

- Yes
- No x

Question 2
Feature engineering can be applied before modeling or be part of the model on the input stage. Regarding Feature Engineering, we can say that: (Only one correct answer).

- Feature Engineering within the model is limited to batch computations. x
- Feature Engineering within the model reduces inference time.
- Feature Engineering within the model slows down iterations.
- TF Transform applies feature engineering separately from the model.

Question 3
Which of the following is not considered a feature engineering inconsistency:

- Training & serving code paths are different
- Diverse deployments scenarios
- Training-serving skews
- All transformations are the same in any scenario x

### Feature Transformation at Scale
#### PRACTICE QUIZ - Feature Transformation

Question 1
Transformation operations can happen at the instance level or be applied to the entire dataset. Which one is an instance-level transformation?

- Standard Scaling
- Feature Cross x
- Minmax
- Bucketizing

Question 2
In a pre-processing training dataset, all transformations that are carried out must be done in the serving set:

- False
- True x

Question 3
What statement is true about TensorFlow Transform?

- In a TFX pipeline, this component is usually placed after TF trainer
- TF Transform eliminates the training serving skew x
- TF Transform requires specifying preprocessing steps at serving time
- TF Transform Analyzers are run during training and serving time

### Reading Week 2: Feature Engineering, Transformation and Selection
If you wish to dive more deeply into the topics covered this week, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Mapping raw data into feature https://developers.google.com/machine-learning/crash-course/representation/feature-engineering
- Feature engineering techniques https://www.commonlounge.com/discussion/3ce75d036e924c70ab7e47f534ec40fc/history
- Scaling https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv
- Facets https://pair-code.github.io/facets/
- Embedding projector http://projector.tensorflow.org/
- Encoding features https://developers.google.com/machine-learning/crash-course/feature-crosses/encoding-nonlinearity

- TFX:
  1. https://www.tensorflow.org/tfx/guide#tfx_pipelines
  2. https://ai.googleblog.com/2017/02/preprocessing-for-machine-learning-with.html

- Breast Cancer Dataset http://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+%28diagnostic%29

### Feature Selection
#### PRACTICE QUIZ - Feature Selection

Question 1
Consider a binary classification problem in a 2D  feature space. What is the shape of the boundary separating the 2 classes in an ideal setting?

- Linear x
- Parabola
- Sigmoid
- Perceptron

Question 2
Feature selection is characterized by: (check all that apply).

- Ensuring that the serving dataset is representative of future inference requests.
- Ensuring numerical features follow the same numerical range
- Accounting for data changes over time (drift, seasonality, etc).
- Remove features that don’t influence the outcome. x
- Identify features that best represent the relationship. x

Question 3
What is the definition of backward elimination?

- We first start with no features. In each iteration we keep adding features which will increase the model performance until no performance improvement is observed. 
- In this method we start by selecting all the features. We then remove the least significant feature based on model performance. We repeat this step until no improvement is observed in model performance. x
- We start by selecting all features in the feature set and calculating their feature importances. We then prune features from the current feature set to select a subset of the features based on the feature importances, We recursively prune features on the new subset until no model performance improvement is observed.

Question 4
Embedded methods combine the best of both worlds, filter and wrapper methods. Embedded methods are: (Check all that apply)

- Faster than wrapper methods x
- More efficient than filter methods x
- More efficient than wrapper methods
- Faster than filter methods

### Data Journey and Data Storage

#### PRACTICE QUIZ - Data Journey

Question 1
Machine learning pipelines for production have become prominent in several industries. They introduce complexity to the ML lifecycle due to the large amount of data, tools, and workflows involved. If data and models are not tracked properly during the life cycle, it becomes infeasible to recreate an ML model from scratch or to explain to stakeholders how it was created. What can be done to prevent these shortcomings?

- Establish data and model provenance tracking mechanisms. x
- Debug the model so it becomes reliable.
- Use a TFX publisher.
- Use a relational database.

Question 2
ML Metadata (MLMD) is a library for recording and retrieving metadata associated with ML production pipelines among other applications. What is the definition of attribution in this library? 

- Is a record of the relationship between artifacts and contexts. x
- Is a record of the relationship between executions and contexts.
- Is a record of a component run or a step in an ML workflow and the runtime parameters
- Is a record of the relationship between artifacts and executions.


Question 3
Every run of a production ML pipeline generates metadata about its components, their executions (e.g. training runs), and the resulting artifacts (e.g. trained models). ML metadata (MLMD) registers this information in a database called the Metadata Store. The MetaDataStore object receives a connection configuration that corresponds to the storage backend used. Which of the following configurations will you use for fast experimentation and local runs?

- MongoDB
- SQL
- Fake Database x
- MySQL

### Evolving Data
#### Schema development
Inspect  anomalies in serving dataset
```python
stats_options = tfdv.StatsOptions(schema=schema, infer_type_from_schema=True)

eval_stats = tfdv.generate_statistics_from_csv(data_location=SERVING_DATASET, stats_options=stats_options)

serving_anomalies = tfdv.validate_statistics(eval_stats, schema)
tfdv.display_anomalies(serving_anomalies)
```
Schema environments:
- Customize the schema for each environment (training vs serving)
- Ex: Add or remove label in schema based on type of dataset

Create environments for each schema
```python
schema.default_environment.append('TRAINING')
schema.default_environment.append('SERVING')

tfdv.get_feature(schema, 'Cover_type').not_in_environment.append('SERVING')
```

Inspect anomalies in serving dataset
```python
serving_anomalies = tfdv.validate_statistics(eval_stats, schema, environemnt='SERVING')
tfdv.display_anomalies(serving_anomalies)
```
#### PRACTICE QUIZ  - Schema Environments

Question 1
Schemas are relational objects summarizing the features in a dataset including: (Check all that apply).

- Feature valency
- Feature type x
- Feature misconfigurations
- Feature name x

Question 2
As data keeps evolving, the ML platform of your choice should be resilient to: (Check all that apply)

- High data volume
- Misconfigurations x
- Disruptions from software x
- Inconsistent Data x

Question 3
Your system and your development process must treat data errors as first-class citizens, just like code bugs.

- False
- True x

### Enterprise Data Storage

#### Reading Week 3: Data Journey and Data Storage 
If you wish to dive more deeply into the topics covered this week, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

Data Versioning:

1. https://dvc.org/
2. https://git-lfs.github.com/

ML Metadata:

1. https://www.tensorflow.org/tfx/guide/mlmd#data_model
2. https://www.tensorflow.org/tfx/guide/understanding_custom_components

Chicago taxi trips data set: 

1. https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew/data
2. https://archive.ics.uci.edu/ml/datasets/covertype

Feast:

1. https://cloud.google.com/blog/products/ai-machine-learning/introducing-feast-an-open-source-feature-store-for-machine-learning
2. https://github.com/feast-dev/feast
3. https://blog.gojekengineering.com/feast-bridging-ml-models-and-data-efd06b7d1644

#### PRACTICE QUIZ - Enterprise Data Storage
Question 1
As data evolves during its life cycle, which of the following factors should ML pipelines address to operate properly?(check all that apply).

- Monitor model and data provenance. x
- Account for anomaly detection. x
- Use feature engineering. x
- Account for scalable solutions.
- Provide resilient mechanisms for disruptions.

Question 2
Many modeling problems use identical or similar features, and there is substantial value in enabling teams to share features between their own projects and for teams in different organizations to share features with each other. Which of the following storage solutions is deliberately designed to address these user cases?

- Data lake
- Data warehouse
- Relational database
- Feature Store x

Question 3
Which are the main advantages of using a cloud-based data warehouse ?(check all that apply)

- User owns and controls data governance.
- They are cost efficient x
- Provides easy on-demand scalable solution x
- User needs to handle all maintenance

Question 4
About data lakes it’s only true that:

- Handles only processed data
- Handles only structured data.
- Aggregates data from a single source only.
- Can handle both structured and unstructured data. x

## Week 1

### PRACTICE QUIZ - Intro to MLEP

Question 1
Static datasets are used for production ML modeling.
- [x] False
- [ ] True

Question 2
In production ML, the design priority is fast training.
- [ ] Yes 
- [x] No

Question 3
Developers adhere to modern software development to produce low-maintenance software, and to address project evolution. Select all the key aspects of modern software development (Check all that apply):

- [x] Testability
- [x] Best practices
- [x] Monitoring
- [ ] Fast Training

Question 4
Model-performance needs to be continuously monitored, and new data, ingested and re-trained.
- [x] Yes
- [ ] No

Question 5
ML pipeline workflows are almost always DAGs.

- [x] True
- [ ] False

Question 6
TensorFlow Extended (TFX) is an end-to-end platform for deploying production ML pipelines.

- [ ] No
- [x] Yes

Question 7
Production machine learning combines which key disciplines?

- [x] Modern software development
- [x] Machine learning development
- [ ] Software testing
- [ ] Feature selection and engineering

Question 8
What are the typical challenges of a production grade ML system? (Check all that apply)

- [x] Handling continuously changing data.
- [x] Optimizing computational resources and costs.
- [ ] Deploying the model to serve requests.
- [ ] Assessing model performance.
- [x] Continually operating while in production.
- [ ] Training the model on real world data.
- [ ] Building integrated ML systems.

Question 9
Production grade machine learning challenges are addressed by implementing an important concept:

- [x] Machine learning pipelines
- [ ] Directed Acyclic Graphs (DAGs)
- [ ] Orchestrators
- [ ] Tensorflow Extended (TFX) 

Question 10
TensorFlow Lite is a deep learning framework to deploy TFX pipelines into:

- [x] Mobile devices
- [ ] Web browser
- [ ] Servers

### PRACTICE QUIZ - Data Collection

Question 1
In ML, data are first-class citizens?
- [x] Yes
- [ ] No

Question 2
A data pipeline is a series of data processing steps such as:

- [x] Data collection
- [ ] Data ingestion
- [ ] Data Analysis
- [x] Data Preparation

Question 3
Is the Data pipeline vital for the success of the production ML system?

- [x] Yes
- [ ] No

Question 4
What do you apply to maximize predictive signals in your data?

- [ ] Data formatting
- [ ] Data coverage
- [x] Feature engineering
- [ ] Feature selection


Question 5
Your training data should reflect the diversity and cultural context of the people who will use it. What can be done to mitigate inherent biases in a given data set?

- [x] Collect data from equal proportions from different user groups.
- [ ] Commit to fairness.
- [ ] Adapt to continuously changing data
- [ ] Engineer better features


Question 6
More often than not,  ML systems can fail the users it serves. In this context, what is representational harm?

- [x] The amplification or negative reflection of certain groups stereotypes.
- [ ] Making predictions and decisions that preclude certain groups from accessing resources or opportunities.
- [ ] Giving skewed outputs more frequently for certain groups of users
- [ ] Inferring prejudicial links between certain demographic traits and user behaviors.


Question 7
Accurate labels are necessary to properly train supervised models. Many times, human subjects known as raters perform this labeling effort. What are the main categories of human raters? (check all that apply). 

- [x] Generalists
- [x] Subject matter experts
- [x] Your users
- [ ] Loggers
- [ ] Aggregators
- [ ] Classifiers

### PRACTICE QUIZ - Data Labeling

Which factors substantially complicate production machine learning? (Check all that apply)

- [ ] Model Retraining driven by model improvements
- [ ] Ground truth that changes slowly 
- [x] Labeling through Weak Supervision
- [x] Model Retraining driven by declining model performance.

Direct Labeling is one of the methods used in production ML to label data. About it we can say that: 

- [x] It captures strong label signals
- [ ] It can be applied very often in many scenarios
- [x] It needs to match prediction results with their corresponding original inference request.
- [ ] With it, obtained labels don’t adapt quickly to world changes

A cardiologist labeling MRI images is a typical example of Direct Labeling.
- [ ] True
- [x] False

### PRACTICE QUIZ - Issues in Training Data

Question 1
What formula represents a dataset shift?

- [ ] $Ptrain(y|x)≠Pserve(y|x)$ and $Ptrain(x)=Pserve(x)$
- [ ] $Ptrain(y|x)=Pserve(y|x)$ and $Ptrain(x)≠Pserve(x)$
- [x] $P_{train}(y,x) \neq P_{serve}(y,x)P$


What measure is typically used to determine the degree of data drift?

- [x] Chebyshev distance (L-infinity)
- [ ] Euclidean distance (L2)
- [ ] Manhattan distance (L1)
- [ ] Hamming distance

Distribution skew occurs when the distribution of the training dataset is significantly different from the distribution of the serving dataset, and is typically caused by: (check all that apply). 

- [ ] A data source that provides some feature values is modified between training and serving time.
- [ ] Occurs when serving and training data don’t conform to the same schema. For example, int32 != float.
- [x] Trend, seasonality, changes in data over time.
- [ ] Faulty sampling method that selects a sample for training which is not representative of serving data distribution.
- [ ] There is different logic for generating features between training and serving. For example, if you apply some transformation only in one of the two code paths.
- [x] Different data sources for training and serving data.


TensorFlow Data Validation (TFDV) helps TFX users maintain the health of their ML pipelines. TFDV can analyze training and serves data to:

- [x] Compute descriptive statistics.
- [x] Detect data anomalies.
- [ ] Perform feature selection.
- [ ] Deploy pipeline to a mobile application.
- [ ] Perform feature engineering.
- [x] Infer a schema.

### Week 1 Optional References
Week 1: Collecting, Labeling and Validating Data 

This is a compilation of optional resources including URLs and papers appearing in lecture videos. If you wish to dive more deeply into the topics covered this week, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- MLops https://cd.foundation/blog/2020/02/11/announcing-the-cd-foundation-mlops-sig/
- Data 1st class citizen https://medium.com/@karpathy/software-2-0-a64152b37c35
- Runners app https://pair.withgoogle.com/chapter/data-collection/
- Rules of ML https://developers.google.com/machine-learning/guides/rules-of-ml
- Bias in datasets https://ai.googleblog.com/2018/09/introducing-inclusive-images-competition.html
- Logstash https://www.elastic.co/logstash
- Fluentd https://www.fluentd.org/
- Google Cloud Logging https://cloud.google.com/logging/
- AWS ElasticSearch https://aws.amazon.com/elasticsearch-service/
- Azure Monitor https://azure.microsoft.com/en-us/services/monitor/
- TFDV https://blog.tensorflow.org/2018/09/introducing-tensorflow-data-validation.html
- Chebyshev distance https://en.wikipedia.org/wiki/Chebyshev_distance

Papers

Konstantinos, Katsiapis, Karmarkar, A., Altay, A., Zaks, A., Polyzotis, N., … Li, Z. (2020). Towards ML Engineering: A brief history of TensorFlow Extended (TFX). http://arxiv.org/abs/2010.02013 

Paleyes, A., Urma, R.-G., & Lawrence, N. D. (2020). Challenges in deploying machine learning: A survey of case studies. http://arxiv.org/abs/2011.09926

ML code fraction:

Sculley, D., Holt, G., Golovin, D., Davydov, E., & Phillips, T. (n.d.). Hidden technical debt in machine learning systems. Retrieved April 28, 2021, from Nips.cc https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf

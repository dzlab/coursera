## Week 4: Model Analysis
### Model Analysis Overview
#### Model Performance Analysis
What is next after model training/deployment?
- Is model performing well?
- Is there scope for improvement?
- Can the data change in future?
- Has the data changed since you created your training dataset?

Black-box evaluation vs model introspection
- Models can be tested for metrics like accuracy and losses like test error without knowing internal details
- For finer evaluation, models can be inspected part by part

Performance metrics:
- Will vary based on the task like regression, classification, etc.
- Within a type of task, based on the end-goal, your performance metrics may be different
- Performance is measured after a round of optimization

Optimization objectives:
- Machine Learning formulates the problem statement into an objective function
- Learning algorithms find optimum values for each variable to converge into local/global minima

#### TensorBoard
If you wish to dive more deeply into TensorBoard usage for model analysis feel free to check out this optional reference. You won’t have to read these to complete this week’s practice quizzes.

TensorBoard https://blog.tensorflow.org/2019/12/introducing-tensorboarddev-new-way-to.html

#### PRACTICE QUIZ - Model Analysis
1; In many instances it is necessary to understand how the model is working internally. This is very useful when you are experimenting with new architectures to understand how data is flowing internally within each layer of the model. This can help you adjust and iterate on your model architecture to improve performance and efficiency. Which of the following is a correct approach to understand the inner workings of a given model?

- [ ] Black box evaluation
- [x] Model introspection
- [ ] Performance metrics
- [ ] Optimization objective

2: TensorBoard is an example of a tool for black-box evaluation.

- [ ] False
- [x] True

3: Performance metrics are independent of the kind of task done.

- [x] False
- [ ] True

### Advanced Model Analysis and Debugging
#### Introduction to TensorFlow Model Analysis
TFMA Architecture

![image](https://user-images.githubusercontent.com/1645304/125171145-82f66900-e167-11eb-8bba-69203170b282.png)


#### TFMA in practice
- Analyze impact of different slices of data over various metrics
- How to track metrics over time?

##### Step 1: Export EvalSavedModel for TFMA
```python
import tensorflow as tf
import tensorflow_transform as tft
import tensorflow_model_analysis as tfma

def get_serve_tf_examples_fn(model, tf_transform_output):
  # return a function that parses a serialized tf.Example and applies TFT
  tf_transform_output = tft.TFTransformOutput(transform_output_dir)
  
signatures = {
  'serving_default': get_serve_tf_examples_fn(model, tf_transform_output).get_concrete_function(tf.TensorSpec(...)),
}
model.save(serving_model_dir_path, save_format='tf', signatures=signatures)
```
##### Step 2: Create EvalConfig
```python
# Specify slicing spec
slice_spec = [slicer.SingleSliceSpec(columns=['column_name']), ...]
# Define metrics
metrics = [tf.keras.metrics.Accuracy(name='accuracy'), tfma.metrics.MeanPrediction(name='mean_prediction'), ...]
metrics_spec = tfma.metrics.specs_from_metrics(metrics)

eval_config = tfma.EvalConfig(model_specs=[tfma.ModelSpec(label_key=features.LABEL_KEY)], slicing_specs=slice_spec, metrics_specs=metrics_specs, ...)
```
##### Step 3: Analyze model
```python
# Specify the path to the eval graph and to where the result should be written
eval_model_dir = ...
result_path = ...

eval_shared_model = tfma.default_eval_shared_model(eval_saved_model_path=eval_model_dir, eval_config=eval_config)

# Run TensorFlow Model Analysis
eval_result = tfma.run_model_analysis(eval_shared_model=eval_shared_model, output_path=result_path, ...)
```
##### Step 4: Visualizing metrics
```python
# render results
tfma.viewer.render_slicing_metrics(result)
```

#### TensorFlow Model Analysis
If you wish to dive more deeply into TensorFlow Model Analysis (TFMA) capabilities, feel free to check out these resources. You won’t have to read these to complete this week’s practice quizzes.

- TFMA https://blog.tensorflow.org/2018/03/introducing-tensorflow-model-analysis.html
- TFMA architecture https://www.tensorflow.org/tfx/model_analysis/architecture

#### Model Debugging Overview
Model robustness
- Robustness is much more than generalization
- Is the model accurate even for slightly corrupted input data

Robustness metrics
- Robustness measurement shouldn't take place during training
- Split data in to train/val/dev sets
- Specific metrics for regression and classification metrics

Model debugging
- Deals with detecting and dealing with problems in ML systems
- Applies mainstream software engineering practices to ML models

Model debugging objectives
- Opaqueness
- Social discrimination
- Security vulnerabilities
- Privacy harms
- Model decay

Model debugging techniques
- Benchmark models
- Sensitivity analysis
- Residual analysis

#### Benchmark Models
- Simple, trusted and interpretable models solving the same problem (i.g. baseline model like linear regression)
- Compare your model against these models on all dataset or slices
- Benchamark model is the starting point of ML development

#### Sensitivity Analysis and Adversarial Attacks
Sensitivity Analysis
- Simulate data of your choice and see what your model predicts
- See how model reacts to data which has never been used before

What-if Tool for sensitivity analysis

Random Attacks
- Expose models to high volumes of random input data
- Exploits the unexpected software and math bugs
- Great way to start debugging

Partial dependence plots
- Visualize the effects of changing one or more variables in your model
- PDPbox and PyCEbox open source packages

How vulnerable to attacks is your model? Sensitivity can mean vulnerability
- Attacks are aimed at fooling your model
- Successful attacks could be catastrophic
- Test adversial examples
- Harden your model

Example:
- A self-driving car craches becuase black and white stickers applied to a stop sign cause a classifier to interpret as a Speed Limit 45 sign.
- A spam detector fails to classify an email as spam. The spam mail has been designed to look like a normal email, but is actually phishing.
- A machine learning powered scanner scans suitcases for weapons at an airport. A knife was developed to avoid detection by making the system think it is an umbrella.

Informational and Behavioral Harms
- Information Harm: Leakage of information
  - Membership inference: was this person's data used for training?
  - Model Inversion: recreate the training data
  - Model Extarction: recreate the model
- Behavioral Harm: Manipulating the behavior of the model
  -  Poisoning: insert malicious data into training data
  - Evasion: input data that causes the model to intentionaly misclassify that data

Measuring your vulnerability to attack
- Cleverhans: an open-source Python library to benchmark machine learning system's vulnerability to adversial examples
- Foolbox: an open-source Python library that lets you easily run adversial attacks against machine learning models

Adversial example searches: Attempted defences against adversial examples
- Defensive distillation

#### Sensitivity Analysis and Adversarial Attacks
If you wish to dive more deeply into adversarial attacks, feel free to check out this paper:

- Explaining and Harnessing Adversarial Examples https://arxiv.org/abs/1412.6572

To access the Partial Dependence Plots libraries please check these resources:

- PDPbox https://github.com/SauceCat/PDPbox
- PyCEbox https://github.com/AustinRochford/PyCEbox
The demo shown in the previous video is based on this Google Colab notebook. https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/generative/adversarial_fgsm.ipynb

#### Residual Analysis
Residual Analysis
- Measures the difference between model's predictions and ground truth
- Randomly distributed error are good
- Correlated or systematic errors show that a model can be improved

Residual Analysis
- Residual should not be correlated with another feature
- Adjacent residuals should not be correlated with each other (auto-correlation)

if the presented autocorrelation or pattern that means they can be predicted by a feature.

#### Model Remediation
Remediation techniques
- Data augmentation:
  - Adding synthetic data into training set
  - Helps correct for unbalanced training data
- Interpretble and explainable ML
  - Overcome myth of neural networks as black box
  - Understand how data is getting transformed
- Model editing:
  - Applies to decition trees
  - Manual tweaks to adapt your use case
- Model assertions:
  - Implement business rules that override model predictions
- Discrimination remediation:
  - Include people with varied backgrounds for collecting training data
  - Conduct feature selection on training data
  - Use fairness metrics to select hyperparameters and decision cut-off thresholds
- Model monitoring
  - Conduct model debugging at regular intervals
  - Inspect accuracy, faireness, security problems, etc.
- Anomaly detection
  - Anomalies can be warning of an attack
  - Enforce data integrity constraints on incoming data

#### Fairness
Fairness indicators
- Open source library to compute fairness metrics
- Easily scales across dataset of any size
- Built in top of TFMA

What does fairness indicators do?
- Compute commonly-identified fairness metrics for classification models
- Compare model performance across subgroups to other models
- No remediation tools provided

Evaluate at individual slices
- Overall metrics can hide poor performance for certain parts of data
- Some metrics may fare well over others

Aspects to consider
- Establish context and different user types
- Seek domain experts help
- Use data slicing widely and wisely

General guidelines
- Compute performance metrics at all slices of data
- Evaluate your metrics across multiple thresholds
- if decision margin is small, report in more detail

#### Measuring Fairness
Positive rate / Negative rate
- Percentage data points classified as positive / negative
- Independent of ground truth
- Use case: having equal final percentages of groups is important

True positive rate (TPR) / False negative rate (FNR)
- TPR: percentage of positive data points that are correctly labeled positive
- FNR: percentage of positive data points that are incorrectly labeled negative
- Measures equality of opportunity, when the positive class should be equal across subgroups
- Use case: where it is important that same percent of qualified candidates are rated positive in each group

Accuracy and Area under the curve (AUC)
- Accuracy: the percentage of data points that are correctly labeled
- AUC: the percentage of data points that are correctly labeled when each class is given equal weight independent of number of samples
- Metrics related to predictive parity
- Use case: when precision is critical

Tips
- Unfair skews if there is a gap in a metric between two groups
- Good fairness indicators doesn't always mean the model is fair
- Continuous evaluation throught development and deployment
- Conduct adversial testing for rare, malicious examples

##### Lab:
About the CelebA dataset
- 200k celibrity images
- Each image has 40 attribute annotations
- Each image has 5 landmark locations
- Assumption on smiling attributes

Fairness indicators in practice
- Build a classifier to detect smiling
- Evaluate fairness and performance across age groups
- Generate visualizations to gain model performance insight

#### Model Remediation and Fairness
If you wish to dive more deeply into model remediation and fairness, feel free to check out these optional resources and tools. You won’t have to read these to complete this week’s practice quizzes.

- Fairness https://www.tensorflow.org/responsible_ai/fairness_indicators/guide
- Learning fair representations https://arxiv.org/pdf/1904.13341.pdf
- Fairness-aware Machine Learning library https://github.com/cosmicBboy/themis-ml
- AI 360 open source model fairness library http://aif360.mybluemix.net/
- Model remediation https://www.tensorflow.org/responsible_ai/model_remediation
- Model cards https://modelcards.withgoogle.com/about

#### PRACTICE QUIZ - Model Analysis and Debugging
Question 1: When evaluating an ML model during training the goal is to improve top-level metrics such as overall accuracy. This information is used to decide whether the model is doing well or not, but it doesn't show how well it does on individual parts of the data. Which technique is extremely helpful to address this shortcoming?

- [ ] Streaming metrics
- [ ] TensorFlow Metric Analysis (TFMA)
- [ ] Apache Beam
- [x] Data Slicing

Question 2: Streaming metrics are approximations to full-pass performance metrics computed on __________. 

- [ ] the full validation data set.
- [ ] the full data set
- [ ] slices of data
- [x] mini-batches of data

Question 3: A recent credit card loyalty program offered by a big technology company has been labeled as “sexist”, a clear example of algorithm based social discrimination. Let’s examine a user complaint on Twitter: “My wife and I filed joint tax returns, live in a community-property state, and have been married for a long time. Yet the black box algorithm thinks I deserve 20x the credit limit she does. No appeals work.” These and other similar claims have triggered a full-blown investigation by the New York State Department of Financial Services. Which of the reviewed techniques in lecture could have been implemented to prevent this embarrassing problem?

- [ ] Data slicing
- [x] Model debugging
- [ ] Residual analysis
- [ ] Model robustness

Question 4: State of the art convolutional neural networks can be fooled to misclassify craftily noise corrupted images with changes that are completely imperceptible to the human eye, as illustrated by the following picture:

What type of analysis can help us detect and prevent these types of scenarios?

- [ ] Adversarial attack
- [x] Sensitivity analysis
- [ ] Residual Analysis
- [ ] Dimensionality reduction

Question 5: A performance-metric gap between two or more groups could be a sign that an ML model may have unfair skews. Therefore, is achieving performance equality (on fairness indicators) across groups a definite sign that a model is fair?

- [x] No
- [ ] Yes

Question 6: After a model has been deployed, is it usually feasible to perform residual analysis?

- [x] No
- [ ] Yes


### Continuous Evaluation and Monitoring
Why do models need to be monitored?
- Training data is a snapshot of the world at a point in time
- Many types of data change over time, some quickly
- ML models do not get better with age
- As model performance degrades, you want an early warning

Data drift and shift
- COncept drift: loss of prediction quality
- Concept Emergence: new type of data distribution
- Types of dataset shift:
  - coveriate shift
  - prior probability shift

Statistical process control
- Method used in drift detection method
- Models number of error as binomial random variable
- Alert rule

Sequential analysis
- Method used in linear four rates
- If data is stationary, contingency table should remain constant

Error distribution monitoring
- Method used in Adaptive Windowing (ADWIN)
- Calculate mean error rate at every window of data
- Size of window adapts, becoming shorter when data is not stationary

Clustering / novelty detection
- Assing data to known cluster or detect emerging concept
- Multiple algorightms available: OLINDDA, MINAS, ECSMiner, and GC3
- Susceptible to curse of dimensionality
- Does not detect population level changes

Feature distribution monitoring
- Monitors individual feature separately at every window of data
- Algorithms to compare:
  - Pearson correlation in CHange of Concept
  - Helinger Distance in HDDDM
- Use PCA to reduce number of features

Model-dependent monitoring
- Concentrate efforts near decision margin in latent space
- One algorithm is Margin Density Drift Detection (MD3)
- Area in latent space where classifiers have low confidence matter more
- Reduces false alarm rate effectively

Google Cloud AI COntinuous Evaluation
- Leverages AI platform prediction and data labeling services
- Deploy your model to AI platform prediction with model version
- Create evaluation job
- Input and output are saved in BigQuery table
- Run evaluation job on few of these samples
- View the evaluation metrics on Google Cloud console

How often should you retrain?
- Dependes on the rate of change
- if possible, automate the management of detecting model drift and trigfering model retraining

#### Continuous Evaluation and Monitoring
If you wish to dive more deeply into continuous evaluation and model monitoring, feel free to check out these optional resources and tools. You won’t have to read these to complete this week’s practice quizzes.

- Instrumentation, Observability & Monitoring of Machine Learning Models https://www.infoq.com/presentations/instrumentation-observability-monitoring-ml/
- Monitoring Machine Learning Models in Production - A Comprehensive Guide https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/
- Concept Drift detection for Unsupervised Learning https://arxiv.org/pdf/1704.00023.pdf
- Google Cloud https://cloud.google.com/ai-platform/prediction/docs/continuous-evaluation
- Amazon SageMaker https://aws.amazon.com/sagemaker/model-monitor/
- Microsoft Azure https://docs.microsoft.com/en-us/azure/machine-learning/how-to-monitor-datasets?tabs=python

#### PRACTICE QUIZ - Continuous Evaluation and Monitoring
Question 1: Many ML models suffer from declining predicting capabilities over time. A common solution used to overcome this deterioration is to keep retraining your model with new data. As part of this process you may encounter a phenomenon called concept emergence. Which of the following statements accurately describes this emergent phenomenon?

- The lack of covariate shift.
- The persistent appearance of stationary data that remains immutable over time.
- [x] The appearance of new patterns in data distribution that were not previously present in your dataset.
- The loss of prediction quality over time. 

Question 2: Statistical process control is a technique that detects concept drift assuming that the errors follow a binomial distribution. Would the system trigger an alarm if $p_{t}=\sigma_{t}=0.3p$ and $p_{min}=\sigma_{min}=0.12p $

- [ ] No
- [x] Yes

Question 3: In sequential analysis you detect concept drift by calculating the negative predictive value, precision, recall, and specificity of the system based on a standard contingency table. If the data is stationary these quantities should not change over time. This analysis is tedious as it requires recomputing all these metrics each time we get a new sample. Which of the following approaches is usually implemented to overcome this problem? 

- [x] Incremental update rule
- [ ] Monte Carlo sampling
- [ ] Recursive computation and caching
- [ ] Adaptive windowing


Question 4: Drift detection techniques in unsupervised settings typically suffer from the curse of dimensionality. Which of the following techniques is an appropriate solution to mitigate the effects of this curse? (Check all that apply)

- [x] PCA (Principal components analysis)
- [ ] SVD (Singular Value Decomposition)
- [x] NMF (Non Negative Matrix Factorization)
- [ ] K-means 

Question 5: In unsupervised settings, clustering is a very useful method to detect novelty in your data. In this method, you cluster the incoming batches of data to one of the known classes. If you observe that the features of the new data are lying far away from the classes of known features, you can term it as an emerging concept. The downside of this method is that it detects only __________ drift and not ___________ changes.

- [x] cluster-based, population-based.
- [ ] cluster-based, feature
- [ ] feature, cluster-based
- [ ] population-based, cluster-based


Question 6: It is a sad truth that most of the machine learning models are trained with a fixed set of stationary data. It is very likely that in this process you may have slightly biased your model in favor of your limited data at training. Consequently, as time progresses, your ML model's performance will deteriorate with time. Monitoring helps prevent this performance decay in which ways? (Check all that apply)

- [ ] By retraining your model constantly
- [ ] Reduces false alarm rates
- [ ] By performing dimensionality reduction
- [x] Allows you to identify distribution changes close to the classification boundaries
- [ ] Allows you to establish ground truth labels
- [ ] Identify regions in latent space where the model performs poorly

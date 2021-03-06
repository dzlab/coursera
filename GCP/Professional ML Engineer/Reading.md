# Reading

Exam focuses on the following areas:
- Knowledge of ML concepts and related tools — Tensorflow, Keras, XGB
- Knowledge of GCP ML services — AI Platform, ML APIs, BQML
- Knowledge of MLOps and related tools — TFX, Kubeflow, Best practices

How to engineer an ML solution:
- Start with GCP ML APIs to check any existing API that can be leveraged
- Else AutoML Training
- Else AI Platform Inbuilt algo
- Else AI Platform Custom Training on TF
- Else AI Platform Custom Training on Containers (e.g. for pytorch or XGBoost models)

## Resources
- Considerations for Sensitive Data within Machine Learning Datasets - [link](https://cloud.google.com/solutions/sensitive-data-and-ml-datasets)
- Prototyping models in AI Platform Notebooks - [link](https://codelabs.developers.google.com/codelabs/prototyping-caip-notebooks/#0)
- Cloud Dataprep Quickstart - [link](https://cloud.google.com/dataprep/docs/quickstarts/quickstart-dataprep)



- Data Split Example - [link](https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/example)
- Introduction to Transforming Data - [link](https://developers.google.com/machine-learning/data-prep/transform/introduction)
- Imbalanced Data - [link](https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/imbalanced-data)
- What is transfer learning? - [link](https://www.tensorflow.org/js/tutorials/transfer/what_is_transfer_learning)

- Access control - [link](https://cloud.google.com/ai-platform/training/docs/access-control)
- Training Neural Networks: Best Practices - [link](https://developers.google.com/machine-learning/crash-course/training-neural-networks/best-practices)
- Classification: Prediction Bias - [link](https://developers.google.com/machine-learning/crash-course/classification/prediction-bias)
- Making and serving predictions - [link](https://cloud.google.com/solutions/machine-learning/minimizing-predictive-serving-latency-in-machine-learning#making_and_serving_predictions)
- Optimizing models for serving - [link](https://cloud.google.com/solutions/machine-learning/minimizing-predictive-serving-latency-in-machine-learning#optimizing_models_for_serving)
- Optimize the frequency of retraining the model - [link](https://cloud.google.com/solutions/machine-learning/best-practices-for-ml-performance-cost#optimize_the_frequency_of_retraining_the_model)

- machine learning guides - [link](https://developers.google.com/machine-learning/guides)
- Machine Learning Glossary - [link](https://developers.google.com/machine-learning/glossary)
- Google Cloud samples demonstrating the usage of Google Cloud products - [link](https://cloud.google.com/docs/samples)

### Google Cloud Solutions
- Cloud Architecture Center - Machine learning and artificial intelligence (ML/AI) - [link](https://cloud.google.com/architecture?category=aiandmachinelearning)
- Architecture for MLOps using TFX, Kubeflow Pipelines, and Cloud Build - [link](https://cloud.google.com/solutions/machine-learning/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build)
- Best practices for performance and cost optimization for machine learning - [link](https://cloud.google.com/solutions/machine-learning/best-practices-for-ml-performance-cost)
- Building production-ready data pipelines using Dataflow: Overview - [link](https://cloud.google.com/solutions/building-production-ready-data-pipelines-using-dataflow-overview)
- Minimizing real-time prediction serving latency in machine learning - [link](https://cloud.google.com/solutions/machine-learning/minimizing-predictive-serving-latency-in-machine-learning)
- Considerations for Sensitive Data within Machine Learning Datasets - [link](https://cloud.google.com/architecture/sensitive-data-and-ml-datasets)
- Data preprocessing for machine learning: options and recommendations - [link](https://cloud.google.com/architecture/data-preprocessing-for-ml-with-tf-transform-pt1)
- Data and model validation - [link](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning#data_and_model_validation)

#### End to end application
- Machine learning with structured data: Data analysis and preparation (Part 1) - [link](https://cloud.google.com/architecture/ml-on-structured-data-analysis-prep-1)

## Machine Learning
### Crash Course
- Identifying Good Problems for ML - [link](https://developers.google.com/machine-learning/problem-framing/good)

- Using ML Output - [link](https://developers.google.com/machine-learning/problem-framing/framing?authuser=0#using-the-output)
- Identify Your Data Sources - [link](https://developers.google.com/machine-learning/problem-framing/formulate?authuser=0#identify-your-data-sources)

- Success and Failure Metrics - [link](https://developers.google.com/machine-learning/problem-framing/framing?authuser=0#success-and-failure-metrics)
- Fairness: Types of Bias - [link](https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias)


### Rules of ML
- Don’t be afraid to launch a product without machine learning - [link](https://developers.google.com/machine-learning/guides/rules-of-ml#rule_1_don%E2%80%99t_be_afraid_to_launch_a_product_without_machine_learning)
- Training-Serving Skew - [link](https://developers.google.com/machine-learning/guides/rules-of-ml#training-serving_skew)
- Turn heuristics into features, or handle them externally - [link](https://developers.google.com/machine-learning/guides/rules-of-ml#rule_7_turn_heuristics_into_features_or_handle_them_externally).
- Start with directly observed and reported features as opposed to learned features - [link](https://developers.google.com/machine-learning/guides/rules-of-ml#rule_17_start_with_directly_observed_and_reported_features_as_opposed_to_learned_features).


### Best practices for ML
- Preprocess the data once and save it as a TFRecord file - [link](https://cloud.google.com/solutions/machine-learning/best-practices-for-ml-performance-cost#preprocess_the_data_once_and_save_it_as_a_tfrecord_file)


## Model design, performance and tuning

### Regularization

Overfitting - Training Performance Excedes Test Performance:
- Can apply regularization to penalize model complexity, .i.e. generalize.
- Is the overfitting a result of class imbalance? Combating this may require some data engineering solutions.
- Develop the ability to look at a scenario and see what kind of regularization to apply.


Regularization methods:
— what is L0, L1, L2 regularization? When would you use them? 
- L1 Regularization - A type of regularization that penalizes weights in proportion to the sum of the absolute values of the weights. In models relying on sparse features, L1 regularization helps drive the weights of irrelevant or barely relevant features to exactly 0, which removes those features from the model.
- [L2 Regularization](https://developers.google.com/machine-learning/crash-course/regularization-for-simplicity/l2-regularization) - A type of regularization that penalizes weights in proportion to the sum of the squares of the weights. L2 regularization helps drive outlier weights (those with high positive or low negative values) closer to 0 but not quite to 0. L2 regularization always improves generalization in linear models.
- [Dropout Regularization](https://developers.google.com/machine-learning/crash-course/training-neural-networks/best-practices#dropout-regularization) -Randomly shut off neurons for a training step thus preventing preventing training. The more you drop out, the stronger the regularization. Helps with Overfitting, too much can lead to underfitting. 
- Other methods include: Early stopping, Max-norm regularization, Dataset Augmentation, Noise robustness, Sparse representation.

### Troubleshooting
- [Vanishing Gradients](https://developers.google.com/machine-learning/crash-course/training-neural-networks/best-practices#vanishing-gradients) - The gradients for the lower layers (closer to the input) can become very small. When the gradients vanish toward 0 for the lower layers, these layers train very slowly, or not at all. The ReLU activation function can help prevent vanishing gradients.
- [Exploding Gradients](https://developers.google.com/machine-learning/crash-course/training-neural-networks/best-practices#exploding-gradients) - If the weights in a network are very large, then the gradients for the lower layers involve products of many large terms. In this case you can have exploding gradients: gradients that get too large to converge. Batch normalization can help prevent exploding gradients, as can lowering the learning rate.
- [Dead ReLU Units](https://developers.google.com/machine-learning/crash-course/training-neural-networks/best-practices#dead-relu-units) - Once the weighted sum for a ReLU unit falls below 0, the ReLU unit can get stuck. It outputs 0 activation, contributing nothing to the network’s output, and gradients can no longer flow through it during backpropagation. With a source of gradients cut off, the input to the ReLU may not ever change enough to bring the weighted sum back above 0.. Lowering the learning rate can help keep ReLU units from dying. !!Leaky-Relu can help to address this, as can choice of optimiser eg. ADAM!!


Common pitfalls in backpropagation and their solutions:
- vanishing gradients -> use ReLu
- exploding gradients -> use batch normalization
- ReLu layers are dying -> lower learning rates

## AI Explanations
- Explainable AI — what is this? When would you use this? [link](https://cloud.google.com/explainable-ai)
with tabular data, you can use Shapely or integrated ingredients for large feature spaces; with images, you can use integrated gradients for pixel-level explanations or XRAI for region-level explanations.

- Introduction to AI Explanations for AI Platform - [link](https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/overview)
- WhatIf Tool — when do you use it? How do you use it? How do you discover different outcomes? How do you conduct experiments? [link](https://pair-code.github.io/what-if-tool/)


## MLOps
- MLOps: Continuous delivery and automation pipelines in machine learning - [link](https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- End to end hybrid and multi-cloud ML workloads - [link](https://www.kubeflow.org/docs/about/use-cases/#end-to-end-hybrid-and-multi-cloud-ml-workloads)

### TFX
- TensorFlow Extended, or TFX. You have to know the components and how to build the pipeline out of them.
- TFX on Cloud AI Platform Pipelines - [link](https://www.tensorflow.org/tfx/tutorials/tfx/cloud-ai-platform-pipelines)
- TFX pipelines and components — https://www.tensorflow.org/tfx/guide/understanding_tfx_pipelines
- Architecture for MLOps using TFX, Kubeflow Pipelines, and Cloud Build - [link](https://cloud.google.com/solutions/machine-learning/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build)

### Kubeflow
- When to use Kubeflow over TFX? When you need PyTorch, XGBoost or if you want to dockerize every step of the flow
- https://www.kubeflow.org/docs/pipelines/overview/pipelines-overview/
- How to carry out CI/CD in Machine Learning (“MLOps”) using Kubeflow ML pipelines (#3) - [link](https://medium.com/google-cloud/how-to-carry-out-ci-cd-in-machine-learning-mlops-using-kubeflow-ml-pipelines-part-3-bdaf68082112)
- Kubeflow (kfctl) GitHub Action for AI/ML CI/CD - [link](https://github.com/marketplace/actions/kubeflow-for-ci-cd)

### CI/CD
- AB and Canary testing
- Split traffic in production with small portion going to a new version of the model and verify that all metrics are as expcted, gradually increase the traffic split or rollback.

## BigQuery ML
- BigQuery ML. The default answer is that if your data is already in BigQuery and you want the output to also be there, you should use BigQuery ML for your modeling. But be aware of the limitations. 
- It supports the following types of model: linear regression, binary and multiclass logistic regression, k-means, matrix factorization, time series, boosted trees, deep neural networks, AutoML models and imported TensorFlow models
- Use it for quick and easy models, prototyping etc.
- BigQuery ML — BigQuery by itself is important. All the ML you can do with BQML is also very important. What all can you do with BQML? What are its limitations. [link](https://cloud.google.com/bigquery-ml/docs/introduction)
- BQML — Can it work with other ML libraries? Can you import models from tf, scipy, etc.?
- BQML available algorithms - [link](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create)
- BQML Syntaxes and types of Algos — https://cloud.google.com/bigquery-ml/docs/tutorials
- Example of training with BigQuery ML - [link](https://towardsdatascience.com/lessons-learned-using-google-cloud-bigquery-ml-dfd4763463c)
- How to do online prediction with BigQuery ML - [link](https://towardsdatascience.com/how-to-do-online-prediction-with-bigquery-ml-db2248c0ae5)

## Accelerators
- Choosing between CPUs, TPUs and GPUs:

> Use CPUs for quick prototypes, simple/small models or if you have many C++ custom operations; use GPU if you have some custom C++ operations and/or medium to large models; use TPUs for big matrix computations, no custom TensorFlow operations and/or very large models that train for weeks or months

- To improve performance on TPUs: if data pre-processing is a bottleneck, do it offline as a one-time cost; choose the larges batch size that fits in memory; keep the per-core batch size the same

### TPU

- Reducing memory usage - [link](https://cloud.google.com/tpu/docs/troubleshooting#memory-usage)
- Improving training speed - [link](https://cloud.google.com/tpu/docs/troubleshooting#training-speed)


## Tensorflow

For TensorFlow - `tf.estimator.train_and_evaluate(estimator, ...)` You’ll need an estimator, `RunConfig`, `TrainSpec` and `EvalSpec`.
- `RunConfig` - tells the estimator where and how often to write Checkpoints and Tensorboard logs (“summaries”) `tf.estimator.RunConfig(model_dir=output_dir, save_summary_steps=100,save_checkpoint_steps=2000)`
- `TrainSpec` - tells the estimator how to get training data `tf.estimator.TrainSpec(input_fn=train_input_fn, max_steps=50000)`
- `EvalSpec` - controls the evaluation and the checkpointing of the model since they happen at the same time `tf.estimator.EvalSpec(input_fn=eval_input_fn, steps=100, throttle_secs=600, exporters=…)`

For multiclass classification, if:
- labels and probabilities are mutually exclusive, use `softmax_cross_entropy_with_logits_v2`
- labels are mutually exclusive, but not probabilities, use `sparse_softmax_cross_entropy_with_logits`
- labels are not mutually exclusive, use `sigmoid_cross_entropy_with_logits`


### Keras API.
You have to be able to understand the sequential model architecture, what layers actually define parameters, like dense layers, what are dropout layers, what are convolutional layers.

Use the Sequential API by default. If you have multiple inputs or outputs, layer sharing or a non-linear topology, change to the Functional API, unless you have a RNN. If that is the case, Keras Subclasses instead

### Distributed training
The general answer is that GPU training is faster than CPU training, and GPU usually doesn’t require any additional setup. TPUs are faster than GPUs but have their limitations. Besides, make sure what replica roles mean: master, worker, parameter server, evaluator, and how many of each you can get.

If you need to optimize the distributed training, the default answers are:
1. use the tf.data.Dataset API for the input;
2. interleave the pipeline steps by enabling parallelism;
3. Keras API has better support for distributed training than Estimator API.

Know the differences between the different Distributed training strategies in Tensorflow [link](https://www.tensorflow.org/guide/distributed_training).

|Strategy|Synchronous / Asynchronous|Number of nodes|Number of GPUs/TPUs per node|How model parameters are stored|
|-|-|-|-|-|
|[MirroredStrategy](https://www.tensorflow.org/guide/distributed_training#mirroredstrategy)|Synchronous|one|many|On each GPU|
|TPUStrategy|Synchronous|one|many|On each TPU|
|MultiWorkerMirroredStrategy|Synchronous|many|many|On each GPU on each node|
|ParameterServerStrategy|Asynchronous|many|one|On the Parameter Server|
|CentralStorageStrategy|Synchronous|one|many|On CPU, could be placed on GPU if there is only one|
|Default Strategy|no distribution|one|one|on any GPU picked by TensorFlow|
|OneDeviceStrategy|no distribution|one|one|on the specified GPU|

### Feature column
Know how to use TF [feature column API](https://www.tensorflow.org/api_docs/python/tf/feature_column) to perform feature engineering in TensorFlow and how to produce the following features: numerical, categorical one-hot encoded/embedded/hashed, bucketized one-hot encoded/embedded/hashed, crossed.

### Other
- TF Profiler — https://www.tensorflow.org/guide/profiler

## Google Cloud Products
GCP ML APIs — Natural Language API, Vision API, Audio API
### AI Platform
- AI Platform distributed training with containers. The default answer is if you have a distributed training app, you can package each component in a separate container (master, worker, parameter server) and deploy it on the AI Platform.
- AI Platform distributed training. This is essentially the union of TensorFlow distributed training topics and AI Platform containers distributed training. However, note that distributed training is not supported for models using scikit-learn (may have guessed) or XGBoost environments.
- AI Platform Hyperparameter tuning. Might be useful to know that Bayesian optimization is used under the hood.
- AI Platform built-in algorithms. This is something in-between AutoML and custom code: you still have to do the data preprocessing, feature engineering, and hyperparameter tuning, but the model itself is already implemented. Be aware that built-in algorithms do not support distributed training.

- AI Platform Training - [link](https://cloud.google.com/ai-platform/training/docs)
  - Built-in algos - [link](https://cloud.google.com/ai-platform/training/docs/algorithms)
  - Machine types and scale tiers - [link](https://cloud.google.com/ai-platform/training/docs/machine-types)
  - Monitoring - [link](https://cloud.google.com/ai-platform/training/docs/monitor-training)
  - Training and prediction with TF Estimator - [link](https://cloud.google.com/ai-platform/docs/getting-started-keras)
  - Training with scikit-learn and XGBoost - [link](https://cloud.google.com/s/results/?q=scikit-learn&p=%2Fml-engine%2Fdocs%2F).
- AI Platform Prediction - [link](https://cloud.google.com/ai-platform/prediction/docs)
- AI Platform DL containers - [link](https://cloud.google.com/ai-platform/deep-learning-containers/docs)
- AI Platform explanation - [link](https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/overview)
- AI Platform continuous evaluation - [link](https://cloud.google.com/ai-platform/prediction/docs/continuous-evaluation)
- AI Platform pipelines - [link](https://cloud.google.com/ai-platform/pipelines/docs)
- AI Platform Vizier: black-box optimization service that helps tune hyperparameters in complex ML models - [link](https://cloud.google.com/ai-platform/optimizer/docs)


### Natural Language
- Natural Language API - [link](https://cloud.google.com/natural-language/docs/reference/rest)
- AutoML Natural Language API - [link](https://cloud.google.com/natural-language/automl/docs/tutorial)

#### AutoML API
Train your own high-quality machine learning custom models to classify, extract, and detect sentiment with minimum effort and machine learning expertise using Vertex AI for natural language, powered by AutoML. You can use the AutoML UI to upload your training data and test your custom model without a single line of code. - [link](https://cloud.google.com/natural-language/automl/docs/quickstart)
- AutoML Healthcare - [link](https://cloud.google.com/natural-language/automl/docs/automl-healthcare)
- Vertex AI - [link](https://cloud.google.com/vertex-ai/docs/tutorials/text-classification-automl)

#### Natural Language API
The powerful pre-trained models of the Natural Language API empowers developers to easily apply natural language understanding (NLU) to their applications with features including sentiment analysis, entity analysis, entity sentiment analysis, content classification, and syntax analysis. - [link](https://cloud.google.com/natural-language/docs/quickstarts)

#### Healthcare Natural Language AI
Gain real-time analysis of insights stored in unstructured medical text. Healthcare Natural Language API allows you to distill machine-readable medical insights from medical documents, while AutoML Entity Extraction for Healthcare makes it simple to build custom knowledge extraction models for healthcare and life sciences apps—no coding skills required. - [link](https://cloud.google.com/healthcare/docs/how-tos/nlp)

### Translation
Cloud Translation API helps: Translating text, Discovering supported languages, Detecting language of Text, Creating and using glossaries when translating.
- How-to Guides [link](https://cloud.google.com/translate/docs/how-to)
- AutoML Translation - [link](https://cloud.google.com/translate/automl/docs/quickstart)

### Vision AI
Create a dataset of images, train a custom AutoML for Cloud or Edge, then deploy it. If Edge is target you can then export the model in TF Lite, TF.js, CoreML, or Coral Edge TPU.

- Cloud-hosted model quickstart - [link](https://cloud.google.com/vision/automl/docs/quickstart)
- Edge device model quickstart - [link](https://cloud.google.com/vision/automl/docs/edge-quickstart)
- AutoML Vision Prediction: [individual](https://cloud.google.com/vision/automl/docs/predict) and [batch](https://cloud.google.com/vision/automl/docs/predict-batch)

### Video AI
- Video Intelligence API: Face detection, Detect people, Detect shot changes, Explicit Content Detection, Object tracking, Recognize logos(detect, track, and recognize the presence of over 100,000 brands and logos in video content), Text Detection performs Optical Character Recognition (OCR), audio track transcription - [link](https://cloud.google.com/video-intelligence/docs/quickstarts)
- AutoML Video Intelligence: train custom model for classification and object tracking - [link](https://cloud.google.com/video-intelligence/automl/docs/quickstart)

### Other
- AutoML: Natural Language, Tables, Translation, Video Intelligence, Vision - [link](https://cloud.google.com/automl/docs)
- AI Platform Data Labeling Service - [link](https://cloud.google.com/ai-platform/data-labeling/docs)
- AutoML Tables Quickstart - [link](https://cloud.google.com/automl-tables/docs/quickstart)

## Evaluation
- Classification: ROC Curve and AUC - [link](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)
- Precision - (True Positives) / (All Positive Predictions) - When model said “positive” class, was it right?
- Recall - (True Positives) / (All Actual Positives) - Out of all possible positives, how many did the model correctly identify?

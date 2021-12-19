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
- Identifying Good Problems for ML - [link](https://developers.google.com/machine-learning/problem-framing/good)
- Cloud Architecture Center - Machine learning and artificial intelligence (ML/AI) - [link](https://cloud.google.com/architecture?category=aiandmachinelearning)

- Using ML Output - [link](https://developers.google.com/machine-learning/problem-framing/framing?authuser=0#using-the-output)
- Identify Your Data Sources - [link](https://developers.google.com/machine-learning/problem-framing/formulate?authuser=0#identify-your-data-sources)

- Success and Failure Metrics - [link](https://developers.google.com/machine-learning/problem-framing/framing?authuser=0#success-and-failure-metrics)
- Fairness: Types of Bias - [link](https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias)
- AutoML Tables Quickstart - [link](https://cloud.google.com/automl-tables/docs/quickstart)
- Considerations for Sensitive Data within Machine Learning Datasets - [link](https://cloud.google.com/solutions/sensitive-data-and-ml-datasets)
- Prototyping models in AI Platform Notebooks - [link](https://codelabs.developers.google.com/codelabs/prototyping-caip-notebooks/#0)
- Cloud Dataprep Quickstart - [link](https://cloud.google.com/dataprep/docs/quickstarts/quickstart-dataprep)



- Data Split Example - [link](https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/example)
- Introduction to Transforming Data - [link](https://developers.google.com/machine-learning/data-prep/transform/introduction)
- Imbalanced Data - [link](https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/imbalanced-data)
- What is transfer learning? - [link](https://www.tensorflow.org/js/tutorials/transfer/what_is_transfer_learning)

- Continuous evaluation overview - [link](https://cloud.google.com/ai-platform/prediction/docs/continuous-evaluation)
- Access control - [link](https://cloud.google.com/ai-platform/training/docs/access-control)
- Training Neural Networks: Best Practices - [link](https://developers.google.com/machine-learning/crash-course/training-neural-networks/best-practices)
- Classification: Prediction Bias - [link](https://developers.google.com/machine-learning/crash-course/classification/prediction-bias)
- Making and serving predictions - [link](https://cloud.google.com/solutions/machine-learning/minimizing-predictive-serving-latency-in-machine-learning#making_and_serving_predictions)
- Optimizing models for serving - [link](https://cloud.google.com/solutions/machine-learning/minimizing-predictive-serving-latency-in-machine-learning#optimizing_models_for_serving)
- Optimize the frequency of retraining the model - [link](https://cloud.google.com/solutions/machine-learning/best-practices-for-ml-performance-cost#optimize_the_frequency_of_retraining_the_model)

- machine learning guides - [link](https://developers.google.com/machine-learning/guides)
- Machine Learning Glossary - [link](https://developers.google.com/machine-learning/glossary)

### Google Cloud Solutions
- Architecture for MLOps using TFX, Kubeflow Pipelines, and Cloud Build https://cloud.google.com/solutions/machine-learning/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build
- Best practices for performance and cost optimization for machine learning https://cloud.google.com/solutions/machine-learning/best-practices-for-ml-performance-cost
- Building production-ready data pipelines using Dataflow: Overview https://cloud.google.com/solutions/building-production-ready-data-pipelines-using-dataflow-overview
- Minimizing real-time prediction serving latency in machine learning https://cloud.google.com/solutions/machine-learning/minimizing-predictive-serving-latency-in-machine-learning
- Considerations for Sensitive Data within Machine Learning Datasets https://cloud.google.com/architecture/sensitive-data-and-ml-datasets
- Data preprocessing for machine learning: options and recommendations - [link](https://cloud.google.com/architecture/data-preprocessing-for-ml-with-tf-transform-pt1)
- Data and model validation - [link](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning#data_and_model_validation)

### Rules of ML
- Don’t be afraid to launch a product without machine learning - [link](https://developers.google.com/machine-learning/guides/rules-of-ml#rule_1_don%E2%80%99t_be_afraid_to_launch_a_product_without_machine_learning)
- Training-Serving Skew - [link](https://developers.google.com/machine-learning/guides/rules-of-ml#training-serving_skew)

### Best practices for ML
- Preprocess the data once and save it as a TFRecord file - [link](https://cloud.google.com/solutions/machine-learning/best-practices-for-ml-performance-cost#preprocess_the_data_once_and_save_it_as_a_tfrecord_file)


## Model design, performance and tuning

### Regularization
- Regularization methods — what is L0, L1, L2 regularization? When would you use them? (https://developers.google.com/machine-learning/crash-course/regularization-for-simplicity/l2-regularization)
- Develop the ability to look at a scenario and see what kind of regularization to apply.

## AI Explanations
- Explainable AI — what is this? When would you use this? w(https://cloud.google.com/explainable-ai)
with tabular data, you can use Shapely or integrated ingredients for large feature spaces; with images, you can use integrated gradients for pixel-level explanations or XRAI for region-level explanations.

- Introduction to AI Explanations for AI Platform - [link](https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/overview)
- WhatIf Tool — when do you use it? How do you use it? How do you discover different outcomes? How do you conduct experiments? (https://pair-code.github.io/what-if-tool/)

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


## Neural networks
Common pitfalls in backpropagation and their solutions:
- vanishing gradients -> use ReLu
- exploding gradients -> use batch normalization
- ReLu layers are dying -> lower learning rates

For multiclass classification, if:
- labels and probabilities are mutually exclusive, use `softmax_cross_entropy_with_logits_v2`
- labels are mutually exclusive, but not probabilities, use `sparse_softmax_cross_entropy_with_logits`
- labels are not mutually exclusive, use `sigmoid_cross_entropy_with_logits`

## Tensorflow

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

## AI Platform
- AI Platform distributed training with containers. The default answer is if you have a distributed training app, you can package each component in a separate container (master, worker, parameter server) and deploy it on the AI Platform.
- AI Platform distributed training. This is essentially the union of TensorFlow distributed training topics and AI Platform containers distributed training. However, note that distributed training is not supported for models using scikit-learn (may have guessed) or XGBoost environments.
- AI Platform Hyperparameter tuning. Might be useful to know that Bayesian optimization is used under the hood.
- AI Platform built-in algorithms. This is something in-between AutoML and custom code: you still have to do the data preprocessing, feature engineering, and hyperparameter tuning, but the model itself is already implemented. Be aware that built-in algorithms do not support distributed training.


- AI Platform Data Labeling Service - https://cloud.google.com/ai-platform/data-labeling/docs
- GCP AutoML Training — https://cloud.google.com/automl/docs
- GCP AutoML Prediction — https://cloud.google.com/vision/automl/docs/predict
- GCP ML APIs — Natural Language API, Vision API, Audio API
- AI Platform Training — https://cloud.google.com/ai-platform/training/docs
- AI Platform Built-in algos — https://cloud.google.com/ai-platform/training/docs/algorithms
- AI Platform Prediction — https://cloud.google.com/ai-platform/prediction/docs
- AI Platform DL containers — https://cloud.google.com/ai-platform/deep-learning-containers/docs
- AI Platform explanation — https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/overview
- Continuous evaluation — https://cloud.google.com/ai-platform/prediction/docs/continuous-evaluation
- AI Platform pipelines — https://cloud.google.com/ai-platform/pipelines/docs

## Evaluation
- Classification: ROC Curve and AUC - [link](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)

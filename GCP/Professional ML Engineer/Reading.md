# Reading

- Identifying Good Problems for ML - [link](https://developers.google.com/machine-learning/problem-framing/good)
- Don’t be afraid to launch a product without machine learning - [link](https://developers.google.com/machine-learning/guides/rules-of-ml#rule_1_don%E2%80%99t_be_afraid_to_launch_a_product_without_machine_learning)
- Using ML Output - [link](https://developers.google.com/machine-learning/problem-framing/framing?authuser=0#using-the-output)
- Identify Your Data Sources - [link](https://developers.google.com/machine-learning/problem-framing/formulate?authuser=0#identify-your-data-sources)

- Success and Failure Metrics - [link](https://developers.google.com/machine-learning/problem-framing/framing?authuser=0#success-and-failure-metrics)
- Fairness: Types of Bias - [link](https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias)
- AutoML Tables Quickstart - [link](https://cloud.google.com/automl-tables/docs/quickstart)
- Considerations for Sensitive Data within Machine Learning Datasets - [link](https://cloud.google.com/solutions/sensitive-data-and-ml-datasets)
- Prototyping models in AI Platform Notebooks - [link](https://codelabs.developers.google.com/codelabs/prototyping-caip-notebooks/#0)
- Cloud Dataprep Quickstart - [link](https://cloud.google.com/dataprep/docs/quickstarts/quickstart-dataprep)
- Preprocess the data once and save it as a TFRecord file - [link](https://cloud.google.com/solutions/machine-learning/best-practices-for-ml-performance-cost#preprocess_the_data_once_and_save_it_as_a_tfrecord_file)

- Data Split Example - [link](https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/example)
- Introduction to Transforming Data - [link](https://developers.google.com/machine-learning/data-prep/transform/introduction)
- Imbalanced Data - [link](https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/imbalanced-data)
- What is transfer learning? - [link](https://www.tensorflow.org/js/tutorials/transfer/what_is_transfer_learning)

- Continuous evaluation overview - [link](https://cloud.google.com/ai-platform/prediction/docs/continuous-evaluation)
- Access control - [link](https://cloud.google.com/ai-platform/training/docs/access-control)
- Training-Serving Skew - [link](https://developers.google.com/machine-learning/guides/rules-of-ml#training-serving_skew)
- Training Neural Networks: Best Practices - [link](https://developers.google.com/machine-learning/crash-course/training-neural-networks/best-practices)
- Classification: Prediction Bias - [link](https://developers.google.com/machine-learning/crash-course/classification/prediction-bias)
- Reducing memory usage - [link](https://cloud.google.com/tpu/docs/troubleshooting#memory-usage)
- Improving training speed - [link](https://cloud.google.com/tpu/docs/troubleshooting#training-speed)
- Making and serving predictions - [link](https://cloud.google.com/solutions/machine-learning/minimizing-predictive-serving-latency-in-machine-learning#making_and_serving_predictions)
- Optimizing models for serving - [link](https://cloud.google.com/solutions/machine-learning/minimizing-predictive-serving-latency-in-machine-learning#optimizing_models_for_serving)
- Optimize the frequency of retraining the model - [link](https://cloud.google.com/solutions/machine-learning/best-practices-for-ml-performance-cost#optimize_the_frequency_of_retraining_the_model)

## AI Explanations
with tabular data, you can use Shapely or integrated ingredients for large feature spaces; with images, you can use integrated gradients for pixel-level explanations or XRAI for region-level explanations.

- Introduction to AI Explanations for AI Platform - [link](https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/overview)

## MLOps
- MLOps: Continuous delivery and automation pipelines in machine learning - [link](https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- Architecture for MLOps using TFX, Kubeflow Pipelines, and Cloud Build - [link](https://cloud.google.com/solutions/machine-learning/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build)
- When to use Kubeflow over TFX? When you need PyTorch, XGBoost or if you want to dockerize every step of the flow
- End to end hybrid and multi-cloud ML workloads - [link](https://www.kubeflow.org/docs/about/use-cases/#end-to-end-hybrid-and-multi-cloud-ml-workloads)



## BigQuery ML
- It supports the following types of model: linear regression, binary and multiclass logistic regression, k-means, matrix factorization, time series, boosted trees, deep neural networks, AutoML models and imported TensorFlow models
- Use it for quick and easy models, prototyping etc.

## Accelerators
- Choosing between CPUs, TPUs and GPUs:

> Use CPUs for quick prototypes, simple/small models or if you have many C++ custom operations; use GPU if you have some custom C++ operations and/or medium to large models; use TPUs for big matrix computations, no custom TensorFlow operations and/or very large models that train for weeks or months

- To improve performance on TPUs: if data pre-processing is a bottleneck, do it offline as a one-time cost; choose the larges batch size that fits in memory; keep the per-core batch size the same

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
Keras: use the Sequential API by default. If you have multiple inputs or outputs, layer sharing or a non-linear topology, change to the Functional API, unless you have a RNN. If that is the case, Keras Subclasses instead

## Evaluation
- Classification: ROC Curve and AUC - [link](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)
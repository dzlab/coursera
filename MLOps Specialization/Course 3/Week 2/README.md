## Week 2: Model Resource Management Techniques
### Dimensionality Reduction
#### Curse of Dimensionality
Curse of dimensionality in the distance function (e.g. euclidean distance)
- New dimensions and non-negative terms to the sum
- Distance increases with the number of dimensions
- For a given number of examples, the feature space becomes increasingly sparse

#### Manual Dimensionality Reduction: Case Study
Taxi Fare dataset
```python
CSV_COLUMNS = ['fare_amount', 'pickup_datetime', 'pickup_longitude', 'pickup_latitude', 'Dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'key']
LABEL_COLUMN = 'fare_amount'
STRING_COLS = ['pickup_datetime']
NUMERIC_COLS = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count']
DEFAULTS = [[0.0], ['na'], [0.0], [0.0], [0.0], [0.0], [0.0], ['na']]
DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
```
Baseline model
```python
from tensorflow.keras import layers
from tensorflow.keras.metrics import RootMeanSquared as RMSE

dnn_inputs = layers.DenseFeatures(feature_columns.values())(inputs)

h1 = layers.Dense(32, activation='relu', name='h1')(dnn_inputs)
h2 = layers.Dense(8, activation='relu', name='h2')(h1)

output = layers.Dense(1, activation='linear', name='fare')(h2)
model = models.Model(inputs, output)
model.compile(optimizer='adam', loss='mse', metrics=[RMSE(name='rmse'), 'mse'])
```
Increasing model performance with Feature Engineering
- Carefully craft features for the data types
  - Temporal (pickup date & time)
  - Geographical (latitude and longitude)

Handling temporal features
```python
def parse_datetime(s):
  if type(s) is not str:
    s = s.numpy().decode('utf-8')
  return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S %Z")

def get_dayofweek(s):
  ts = parse_datetime(s)
  return DAYS[ts.weekday()]

@tf.function
def dayofweek(ts_in):
  return tf.map_fn(lambda s: tf.py_function(get_dayofweek, inp=[s], Tout=tf.string), ts_in)
```
Geolocational features
```python
def euclidean(params):
  lon1, lat1, lon2, lat2 = params
  londiff = lon2 - lon1
  latdiff = lat2 - lat1
  return tf.sqrt(londiff * londiff + latdiff * latdiff)
```
Scaling latitude and longitude
```python
def scale_longitude(lon_column):
  return (lon_column + 78)/8.

def scale_latitude(lat_column):
  return (lat_column - 37)/8.
```

Computing the Euclidean distance
```python
def transform(inputs, numeric_cols, string_cols, nbuckets):
  ...
  transformed['euclidean'] = layers.Lambda(euclidean, name='euclidean')([inputs['pickup_longitude'], inputs['pickup_latitude'], inputs['dropoff_longitude'], inputs['dropoff_latitude']])
  feature_columns['euclidean'] = fc.numeric_column('euclidean')
  ...
```

Bucketizing and feature crossing
```python
def transform(inputs, numeric_cols, string_cols, nbuckets):
  ...
  latbuckets = np.linspace(0, 1, nbuckets).tolist()
  lonbuckets = ... # Similarly for longitude
  b_plat = fc.bucketized_column(feature_columns['pickup_latitude'], latbuckets)
  b_dlat = # Bucketize 'dropoff_latitude'
  b_plon = # Bucketize 'pickup_longitude'
  b_dlon = # Bucketize 'dropoff_longitude'
```

```python
ploc = fc.crossed_column([b_plat, b_plan], nbuckets * nbuckets)
dloc = # Feature cross 'b_dlat' and 'b_dlon'
pd_pair = fc.crossed_column([ploc, dloc], nbuckets ** 4)

feature_columns['pickup_and_dropoff'] = fc.embedding_column(pd_pair, 100)
```

#### Algorithmic Dimensionality Reduction
Linear dimensionality reduction:
- Linearly project n-dimensional data onto a k-dimensional subspace (k < n, often k << n)
- There are infinitely many k-dimensional subspaces we can project the data onto
- Which one should we choose?

Best k-dimensional subspace for projection

| problem | objective | Example |
|----|-|-|
|Classification| maximize separation among classes | Linear discriminant analysis (LDA)|
|Regression| maximize correlation between projected data and response variable | Partial least squares (PLS)|
| Unsupervised| retain as much data variance as possible| Principal component analysis (PCA)|


#### Principal Components Analysis
When to use PCA?
Strenghts:
- A versatile technique
- Fast and simple
- Offers several variations and extensions (e.g. kernel/sparce PCA)
Weaknesses:
- Result is not interpretable
- Requires setting threshold for cumulative explained variance

#### Other Techniques
More dimensionality reduction algorithms
- Unsupervised:
  - Latent Semantic Indexing/Analysis (LSI and LSA)(SVD)
  - Independet Component Analysis (ICA)
- Matrix Factorization: Non-Negative Matrix Factorization (NMF)
- Latent Methods: Latent Dirichlet Allocation (LDA)

Single Value Decomposition (SVD)
- SVD decomposes non-square matrices
- Useful for sparse matrices as produced by TF-IDF
- Removes redundant features from the dataset

Independant Component Analysis (ICA)
- PCA seeks directions in feature space that minimize reconstruction error
- ICA seeks directions that are most statistically independent
- ICA addresses higher order dependence

How does ICA works?
- Assume there exists independent signals: S = [s1(t), s2(t), ..., sn(t)]
- Linear combinations of signals: Y(t) = A S(t) Both A (mixing matrix) and S are unknown
- Goal of ICA is to recover original signals S(t) from Y(t)

Non-negative Matrix Factorization (NMF)
- NMF models are interpretable and easier to understand
- NMF requires the sample features to be non-negative

#### Dimensionality Reduction Techniques
If you wish to dive more deeply into dimensionality reduction techniques, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Principal Component Analysis (PCA) https://arxiv.org/pdf/1404.1100.pdf
- Independent Component Analysis (ICA) https://arxiv.org/pdf/1404.2986.pdf
- PCA extensions http://alexhwilliams.info/itsneuronalblog/2016/03/27/pca/


#### PRACTICE QUIZ - Dimensionality Reduction
Question 1: Fill in the blanks with the correct answer according to the descriptions in the boxes below: 

- 1. Data mining. 2. Dimensionality reduction.
- 1. Dimensionality reduction. 2. Data Science.
- 1. Data Science. 2. Data mining.
- 1. Data mining. 2. Data Science. x

Question 2: What does the X value represent? 

- The number of features that reaches the maximum classification error.
- The cursed number of dimensions.
- The worst number of features for making predictions.
- The optimal number of features. x


Question 2: One of the following is not considered as a high-dimensionality impact:

- The possibility of more correlated features is greater.
- Smaller hypothesis space. x
- Higher runtimes and system requirements
- Solutions take longer to reach global optimum

Question 4: What is the output of the code line: `count_params(model_n.trainable_variables)`

- Number of dimensions for Model n.
- Number of classes for Model n. 
- Number of testing parameters for Model n.
- Number of training parameters for Model n. x

Question 5: The amount of training data available, the complexity of decision surface and the classifier type define the number of ____________ to be used

- Spaces
- Models.
- Datasets.
- Features. x

Question 6: Classification subspaces allows to minimize separation among classes, while regression subspaces are used for maximizing correlation between projected data and response variable

- False x
- True


### Quantization and Pruning
#### Quantize part(s) of a model
```python
import tensorflow_model_optimization as tfmot

quantize_annotate_layer = tfmot.quantization.keras.quantize_annotate_layer
model = tf.keras.Sequential([
  ...
  # Only annotated layers will be quantized.
  quantize_annotate_layer(Conv2D()),
  quantize_annotate_layer(ReLU()),
  Dense(),
  ...
])
# Quantize the model
quantized_model = tfmot.quantization.keras.quantize_apply(model)
```

Quntize custom Keras layer
```python
quantize_annotate_layer = tfmot.quantization.keras.quantize_annotate_layer
quantize_annotate_model = tfmot.quantization.keras.quantize_annotate_model
quantize_scope = tfmot.quantization.keras.quantize_scope

model = quantize_annotate_model(tf.keras.Sequential([
  quantize_annotate_layer(CustomLayer(20, input_shape=(20,)), DefaultDenseQuantizeConfig()),
  tf.keras.layers.Flatten()
]))

# quantize_apply requires mentioning DefaultDenseQuantizeConfig with quantize_scope
with quantize_scope({'DefaultDenseQuantizeConfig': DefaultDenseQuantizeConfig, 'CustomLayer': CustomLayer}):
  # Use quantize_apply to actually make the model quantization aware.
  quant_aware_model = tfmot.quantization.keras.quantize_apply(model)
```

If you wish to dive more deeply into quantization, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Quantization https://arxiv.org/abs/1712.05877
- Post-training quantization https://medium.com/tensorflow/introducing-the-model-optimization-toolkit-for-tensorflow-254aca1ba0a3
- Quantization aware training https://blog.tensorflow.org/2020/04/quantization-aware-training-with-tensorflow-model-optimization-toolkit.html


#### Pruning
What's special about pruning
- Better storage and/or transmission
- Gain speedups in CPU and some ML accelerators
- Can be used in tandem with quantization to get additional benefits
- Unlock performance improvements

Pruning with Keras
```python
import tensorflow_model_optimization as tfmot

model = build_your_model()
pruning_schedule = tfmot.sparsity.keras.PolynomialDecay(initial_sparsity=0.5, final_sparsity=0.8, begin_step=2000, end_step=4000)
model_for_pruning = tfmot.sparsity.keras.prune_low_magnitude(model, pruning_schedule=pruning_schedule)
...
model_for_pruning.fit(...)
```

#### Pruning - Reading
If you wish to dive more deeply into pruning, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Pruning http://yann.lecun.com/exdb/publis/pdf/lecun-90b.pdf
- The Lottery Ticket Hypothesis https://arxiv.org/abs/1803.03635

#### PRACTICE QUIZ - Quantization and Pruning
Question 1: Today, due to the developments in machine learning research and mobile and edge devices, there exists a wide range of alternatives to deploy a machine learning solution locally.

- No
- Yes x

Question 2: Which of the following are reasons for Improving mobile & IoT business with ML?

- Strengthened security. x
- Eliminate risk.
- Automating operational efficiency.
- Improving user experience with data. x

Question 3: ML Kit brings Google's machine learning expertise to mobile developers. With this tool, you can  __________________ .

- use a pre-trained model. x
- use to access cloud-based web services. x
- use it to customize your models
- use it to train your model on-device.

Question 4: In per-tensor quantization weights are represented by int8 two’s complement values in the range _____________ with zero-point _____________

- [-127, 127], in range [-128, 127]. 
- [-128, 127], equal to 0
- [-127, 127], equal to 0 x
- [-128, 127], in range [-128, 127]. 


Question 5: Quantization squeezes a small range of floating-point values into a fixed number. What impact is there on the behavior of the model?

- You can have changes in transformations and operation. x
- You can have change layer weights and activations networks x
- You can increase precision as a result of the optimization process.
- You can decrease the interpretability of the ML model

Question 6: One such family of optimizations known as pruning aims to remove neural network connections, increasing the number of parameters involved in the computation.

- Yes
- No x

Question 7: Which ones of the following describe the benefits of applying sparsity with a pruning routine?

- Method perform well at a large scale
- Gain speedups in CPU and some ML accelerators x
- Better storage and/or transmission x
- Can be used in tandem with quantization to get additional benefits

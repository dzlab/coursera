# Week 1 Model Serving: Introduction

## Introduction to Model Serving

### Introduction to Model Serving
#### What exactly is Serving a Model?
Training a good machine learning model is only the first part. You do need to make your model available to your end-users, and you do this by either providing access to the model on your server, which we'll explore this week. Serving also includes the facility to deploy a model file to an application, and this is a scenario that's usually found with mobile ML.
![image](https://user-images.githubusercontent.com/1645304/132610545-4385c1af-8146-4fec-8e8f-7840b32616d7.png)

#### Model Serving Patterns
These components are used by an inference process which is aimed at getting the data to be ingested by a model in order to compute predictions.
![image](https://user-images.githubusercontent.com/1645304/132610725-491db96b-5847-472b-8ebd-97ae29d5795a.png)

#### ML workflows
![image](https://user-images.githubusercontent.com/1645304/132610832-11401ca2-0374-4ee9-adf0-75223dc2f89b.png)

#### Important Metrics
The important metrics to optimize online inference are: latency, throughput, and cost. 
![image](https://user-images.githubusercontent.com/1645304/132610930-9d6bf949-3eb7-421e-b67b-eb8f106e73fc.png)

#### Latency
![image](https://user-images.githubusercontent.com/1645304/132611079-4205180f-cdb4-4596-9907-2b71c212426a.png)

#### Throughput
![image](https://user-images.githubusercontent.com/1645304/132611117-cf90bda0-0776-4ce6-bd54-090d86e31ef9.png)

#### Cost
Consider the cost for things like CPUs, hardware accelerators like GPUs, and caches for storing input features for easy retrieval with minimum latency.
![image](https://user-images.githubusercontent.com/1645304/132611197-d1b6cefc-38fc-4fdd-8fec-1d4077ff0cc9.png)

#### Minimising Latency, Maximizing Throughput
We can scale the infrastructure used to meet these thresholds of response time and throughput, but this can increase the cost proportionally.
![image](https://user-images.githubusercontent.com/1645304/132611303-2bf169b2-07bf-4812-a58c-9c6921e96469.png)

#### Balance Cost, Latency and Throughput
there are tactics you can use to try to minimize any impact on your customer while you attempt to control cost. These may include reducing costs by sharing assets like GPU's, using multiple models to increase throughput, and perhaps even exploring optimizing your models.
![image](https://user-images.githubusercontent.com/1645304/132611481-1584eb6f-7d03-47ce-8bbf-b108884c8030.png)

### Quiz: Introduction to Model Serving

**Question 1**

What are the three key components we should consider when serving an ML Model in a production environment? (Select all that apply)

- [x] A model
- [x] An interpreter
- [ ] An orchestrator
- [x] Input Data

**Question 2**

What happens after a while in operation to an offline-trained model dealing with new real-live data?

- [x] The model becomes stale.
- [ ] The model abruptly forgets all previously learned information.
- [ ] The model adapts to new patterns.

**Question 3**

In applications that are not user-facing, is throughput more critical than latency for customer satisfaction?

- [ ] No, because users might complain that the app is too slow.
- [x] Yes, in this case, we are concerned with maximizing throughput with the lowest CPU usage.

**Question 4**

Nowadays, developers aim to minimize latency and maximize throughput in customer-facing applications. However, in doing so, infrastructure scales and costs increase. So, what strategies can developers implement to balance cost and customer satisfaction? (Select all that apply)

- [x] GPU sharing
- [x] Multi-model serving
- [x] Optimizing inference models
- [ ] Stress testing

### Reading: Ungraded Labs - Best Practices
As you progress through this course you will see that the majority of ungraded labs are hosted in our [public repo](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public) and are meant to be run in your local machine using a terminal. 

Some of them do not require you to have a cloned version of the repo but some do. For this reason, we encourage you to clone the repo right away. For the labs that rely on files within the repo, the best way to follow along is to read its documentation from your browser while working on the cloned version of the repo on your local machine.

To clone the repo, use the following command:
```
git clone https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public.git
```
or for cloning via SSH use:
```
git clone git@github.com:https-deeplearning-ai/machine-learning-engineering-for-production-public.git
```

If you are unsure which method to use, go for the first one.


Have fun in the ungraded labs! 

### Reading: Ungraded Lab - Introduction to Docker
During this lab you will get a high level overview of Docker and some instructions to install it on your local machine.

Follow this [link](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week1-ungraded-labs/C4_W1_Lab_1_Docker_Intro.md) to start the lab!

## Introduction to Model Serving Infrastructure

### Introduction to Model Serving Infrastructure
#### Optimizing Models for Serving
More complex model architectures including more and more features. And this often results in longer prediction latencies and but hopefully a boost in prediction accuracy.
![image](https://user-images.githubusercontent.com/1645304/132785673-a2b43268-240a-4688-b3ee-0d66920c8670.png)

#### As Model Complexity Increases Cost Increases
As models become more complex with more features. The resource requirements increase for every part of the training and serving infrastructure, increased resource requirements means increased costs.
And increased hardware requirements management of larger model registries and this results in a higher support and maintenance burden.
![image](https://user-images.githubusercontent.com/1645304/132785757-fba38cd2-0f6c-4f20-9a4d-a750912723ba.png)

#### Balancing Cost and Complexity
The Challenge for ML practitionners is to balance complexity and cost.

#### Optimizing and Satisficing Metrics
- model's optimizing metric reflects the model's predictive effectiveness and this includes things like accuracy, precision, recall, and so on.
- Models gating metric reflects an operational constraint that the model has to satisfy, such as prediction latency.

![image](https://user-images.githubusercontent.com/1645304/132785999-7090f30d-1f60-415e-a6d6-00ecff9b6bcf.png)

One approach is to:
1. Specify the serving infrastructure, CPU, GPU and all that. And then 
2. Start increasing your model complexity to improve your model's predictive power until you hit one or more of your gating metrics on that infrastructure.
3. Assess the results and either accept the model as it is or work to improve accuracy and or reduce complexity or make the decision to increase the specifications of the serving infrastructure.
![image](https://user-images.githubusercontent.com/1645304/132786329-8faf7696-0a09-40ce-8184-a1396aef0c6b.png)

#### Use of Accelerators in Serving Infrastructure
These decisions can have a significant effect on your projects budget. 
- GPUs tend to be optimized for parallel through pot and they are often used in training infrastructure. 
- TP use as well as being useful in training have advantages for large complex models and large batch sizes, especially during inference.

![image](https://user-images.githubusercontent.com/1645304/132786550-b21be0c6-6129-4d5f-890e-74ca56ea303d.png)

#### Maintaining Input Feature Lookup
You may need caches to retrieve data with low latency (e.g. real time prediction) as you cannot wait many seconds for retrieving data from the database. And this has cost implications.
![image](https://user-images.githubusercontent.com/1645304/132786952-caf1880a-5697-4cd5-8a45-fffdb34f443a.png)


#### NoSQL Databases: Caching and Feature Lookup
You have to carefully choose from the different available offerings based on your requirements and then balance that with your budget constraints.
![image](https://user-images.githubusercontent.com/1645304/132787007-4cb499fb-ee57-4272-bdd7-b90c0b3a41c7.png)

### Deployment Options
#### Model Deployments
- A centralized model in a data center that's access via a remote call.
- distributed instances of the model to users so they can use it locally such as a mobile or embedded system. 

#### Running in huge Data Centers
Costs and efficiency are important at any scale, companies like Google constantly look for ways to improve resource utilization and reduce costs in applications in data centers.
![image](https://user-images.githubusercontent.com/1645304/132787602-58ab5c03-465d-47a4-9498-087dd1ff726f.png)

#### Constrained Environment: Mobile Phone
- At most one GPU, which is shared by a number of applications.
- limited GPU available and using it can lead to battery draining quickly or makes the phone too hot because of complex operations in your ML model. 
- Storage limitation since users don't appreciate large apps using up storage on their phones. 

![image](https://user-images.githubusercontent.com/1645304/132787767-4c9aa93b-8f71-4cb0-a50f-a4f708a95483.png)


#### Restrictions in a Constrained Environment
You may choose to deploy a model to a server and then expose it through a REST API so that we can use it for inference in our app. This might not be feasible to deploy a model to a server in environments where prediction latency is super-important or when a network connection may not always be available (a.g. autonomuous vehicule).

![image](https://user-images.githubusercontent.com/1645304/132788175-cc6327bf-368b-4eab-894d-dfd61138155b.png)


#### Prediction Latency is Almost Always important

![image](https://user-images.githubusercontent.com/1645304/132788422-b5589af2-8458-455b-8017-707af5cb44b3.png)


#### Choose Best Model for the Task
One example is MobileNets, and these are models that are specifically designed for computer vision on mobile devices. All the work in performing trade-offs for the best mobile model had been done for you already and you can build on this.
![image](https://user-images.githubusercontent.com/1645304/132788489-aa4d674c-ca9e-4edc-bb83-56fee5347bc2.png)

### Improving Prediction Latency and Reducing Resource Costs

#### Other strategies to improve prediction latency and reduce resource costs
- **TensorFlow Lite benchmarking tool** has a built-in profiler that can then show you per operator profiling statistics. This can help with understanding performance bottlenecks and identifying which operators dominate the compute time.
- **Model optimization** which aims to create smaller models that are generally faster and more energy-efficient. This is especially important for deployments on mobile devices. TensorFlow Lite supports multiple optimization techniques such as quantization.
- increase the number of interpreter threads to speed up the execution of apps but will use more resources and power.


![image](https://user-images.githubusercontent.com/1645304/132794164-8b3e59f5-12e4-47c3-beb8-df887009de78.png)

#### Web Applications for users
You can go the other route and deploy a model to a server through a web application. The model is wrapped as an API service in this approach, and most serving infrastructures and languages have web frameworks that can help you to achieve this. 
![image](https://user-images.githubusercontent.com/1645304/132794498-4356ddaf-f95c-4e82-bfea-362396e1ed3f.png)

#### Serving systems for easy deployment
Model servers can manage model deployment and eliminate the need for putting models into custom web applications. They also make it easy to update a rollback models, load, and unload models on demand or when resources are required, and manage multiple versions of models. 

![image](https://user-images.githubusercontent.com/1645304/132794677-a02198d7-e834-411d-8bd9-f6c5d0a6ccdd.png)

#### Clipper
- Clipper helps you deploy a wide range of models built in frameworks like Cafe, TensorFlow, and Scikit-learn. Its overall aim is to be model agnostic.
- Clipper includes a standard rest interface, so this makes it easy for you to integrate with production applications.
- Clipper wraps your models in Docker containers if you want, for cluster and resource management.
- It also helps you set service level objectives for reliable latencies.

![image](https://user-images.githubusercontent.com/1645304/132794884-170575c8-fd76-4b13-8a80-c58c42b0b1db.png)

#### TensorFlow Serving
- TensorFlow Serving makes it easy to deploy new algorithms in experiments while keeping the same server architecture and APIs.
- TensorFlow Serving provides out of the box integration with TensorFlow models, but it can also be extended to serve other types of models and data.
- TensorFlow Serving offers both the REST and gRPC protocols, gRPC is often more efficient than REST.
- It has a **version manager** that can easily load and rollback different versions of the same model and it allows clients to select which version to use for each request.
- TensorFlow Serving has demonstrated performance of up to 100,000 requests per second per core.

![image](https://user-images.githubusercontent.com/1645304/132794999-1ef41ab8-a72e-4cea-8c00-a42af761e450.png)

#### Advantages of Serving with Managed Service
![image](https://user-images.githubusercontent.com/1645304/132795227-d76990f3-2991-4964-b4e3-935b0fd2a427.png)

### Creating and deploying models to AI Prediction Platform

### Reading: Optional: Build, train, and deploy an XGBoost model on Cloud AI Platform
This is an optional exercise and will mirror what was shown in the previous screencast. It requires a Google Cloud Platform (GCP) account and we placed instructions in the document in case you don't have one yet. If you can't set up an account at the moment, don't worry because you will still use the same tools in some of the course assignments. You'll be given free use of GCP in those labs. This is mainly here for reference to introduce model serving in the cloud.

[Click here to view the tutorial!](https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/blob/main/course4/week1-ungraded-labs/C4_W1_Optional_Lab_1_XGBoost_CAIP/C4_W1_Optional_Lab_1.md)

### Quiz: Introduction to Model Serving Infrastructure

**1. Question 1**

Why do models become more complex?

- [ ] To cut down costs.
- [ ] To reduce GPU usage.
- [x] To increase accuracy.
- [ ] To minimize latency.

**2. Question 2**

What is the difference between optimizing and satisficing metrics?

- [ ] Optimizing metrics assess model complexity while satisficing metrics evaluate operation costs.
- [ ] Optimizing metrics reflect operational constraints while satisficing metrics deal with model precision.
- [x] Optimizing metrics measure the model's predictive effectiveness while satisficing metrics estimate the speed of its prediction latency.

**3. Question 3**

Which of the following are NoSQL solutions for implementing caching and feature lookup? (Select all that apply)

- [ ] Amazon RDS
- [x] Google Cloud Memorystore
- [x] Google Cloud Firestore
- [x] Amazon DynamoDB

**4. Question 4**

True Or False: The main advantage of deploying a model in a large data center accessed by a remote call is that you can disregard costs in favor of model complexity.

- [x] False
- [ ] True

**5. Question 5**

True Or False: You should always opt for on-device inference whenever possible.

- [x] False
- [ ] True

## Installing TensorFlow Serving

### Installing TensorFlow Serving

#### Install TensorFlow Serving
Pull docker images
the easiest and most recommended method
```
$ docker pull tensorflow/serving
```

the easiest to get GPU support with TF Serving
```
$ docker pull tensorflow/serving:latest-gpu
```

Using binaries
![image](https://user-images.githubusercontent.com/1645304/132997534-beb44dd3-a902-42c4-90f5-bbe1f6960108.png)

Building from source
- See the complete documentation https://www.tensorflow.org/tfx/serving/setup#building_from_source

Install using Aptitude (apt-get) on a Debian-based Linux system
```
$ echo "deb http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -
$ apt update
$ apt-get install tensorflow-model-server
```
#### Import the MNIST Dataset
```python
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# Scale the values of the arrays below to be between 0.0 and 1.0
train_images = train_images / 255.0
test_images = test_images / 255.0

# Reshape the arrays below by adding channel of with 1
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)
print("train_images.shape: {}, of {}".format(train_images.shape, train_images.dtype))
print("test_images.shape: {}, of {}".format(test_images.shape, test_images.dtype))

# train_images.shape: (60000, 28, 28, 1), of float64
# test_images.shape: (10000, 28, 28, 1), of float64
```

#### Look at a Sample image
```python
idx = 42

plt.imshow(test_images[idx].reshape(28, 28), cmp=plt.cm.binary)
plt.title("True label: {}".format(test_labels[idx]), fontdict={"size": 16})
plt.show()
```

![image](https://user-images.githubusercontent.com/1645304/133000918-6a067925-eba0-4f80-bad3-2a581fe74aeb.png)

#### Build a model
```python
# Create a model
model = tf.keras.Sequential([
  tf.keras.layers.Conv2D(input_shape(28, 28, 1), filters=8, kernel_size=3, strides=2, activation='relu', name='Conv1'),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(10, activation=tf.nn.Softmax, name='Softmax')
])
model.summary()
```

#### Train the Model
```python
# Configure the model for training
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
epochs = 5

# Train the model
history = model.fit(train_images, train_labels, epochs=epochs)
```

#### Evaluate the Model
```python
# Evaluate the model on the test images
results_eval = model.evaluate(test_images, test_labels, verbose=0)

for metric, value in zip(model.metric_names, results_eval):
  print(metric + ': {:.3}'.format(value))

# loss: 0.098
# accuracy: 0.969
```

#### Save the Model
```python
MODEL_DIR = tempfile.gettempdir()
version = 1
export_path = os.path.join(MODEL_DIR, str(version))

if os.path.isdir(export_path):
  print("Already saved a model, cleaning up")
  !rm -r {export_path}
  
model.save(export_path, save_format="tf")

print("export_path = {}".format(export_path))
!ls -l {export_path}
```

#### Launch the Saved Model
```python
os.environ['MODEL_DIR'] = MODEL_DIR

%%bash --bg
nohup tensorflow_model_server --rest_api_port=8501 --model_name=digits_model --model_base_path="${MODEL_DIR}" > server.log 2>&1
!tail server.log
```

#### Send an Inference Request
```python
data = json.dumps({"signature_name": "serving_default", "instance": test_images[0:3].tolist()})
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/digits_model:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)['predictions']
```

#### Plot Predictions
```
plt.figure(figsize=(10, 15))

for i in range(3):
  plt.subplot(1, 3, i+1)
  plt.imshow(test_images[i].reshape(28, 28), cmap=plt.cm.binary)
  plt.axis('off')
  color = 'green if np.argmax(predications[i]) == test_labels[i] else 'red'
  plt.title('Predictions: {}\n True Label: {}'.format(np.argmax(predictions[i]), test_labels[i]), color=color)

plt.show()
```
![image](https://user-images.githubusercontent.com/1645304/133005490-3d2f7dde-2445-463a-a779-865dd1567ea7.png)

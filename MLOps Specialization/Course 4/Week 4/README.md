# Week 4: Model Monitoring and Logging

## Model Monitoring and Logging

### Why Monitoring Matters

#### ML Lifecycle Revisted
The last task monitoring your model in production is an ongoing task for as long as your model is in production. The data that you gather by monitoring will guide the building of the next version of your model and make you aware of changes in your model performance. So, as you can see here, this is a cyclical iterative process which requires the last step monitoring in order to be complete. You should note here that this diagram is only looking at monitoring which is directly related to your model performance. But, you will also need to include monitoring of the systems and infrastructure which are included in your entire product or service such as databases and web servers. That kind of monitoring is only concerned with the basic operation of your product or service and not the model itself, but is critical to your users experience. Basically, if the system is down, it really doesn't matter how good your model is.

![image](https://user-images.githubusercontent.com/1645304/134275550-6d6a988a-4c2a-4429-ab63-33ed6d77f8ff.png)

#### Why Monitoring Matters
in our case you might apply this same idea to preventing fire drills, the kind of fire drills where your system is performing badly and it's suddenly an emergency to fix it. It's these kinds of fire drills that can happen if you don't monitor your model performance.

![image](https://user-images.githubusercontent.com/1645304/134275703-8b509425-9e08-4667-a0ce-0a004cdc0dcc.png)

#### Why  do you need monitoring?

If your training data is too old, even when you first deploy a new model, it can have immediate data skews. Without monitoring right from the start, you may easily be unaware of the problem and your model will not be accurate even when it's new. Of course, as previously discussed models will also become stale or inaccurate because the world constantly changes and the training data you originally collected might no longer reflect the current state. Again, without monitoring you are unlikely to be aware of the problem. You can also have negative feedback loops, this turns out to be a more complex issue that arises when you automatically train your models on data collected in production. If this data is biased or corrupted in any way, then the models trained on that data will perform poorly. Monitoring is important even for automated processes because they too can have problems.

![image](https://user-images.githubusercontent.com/1645304/134275845-7ce9052c-0cca-4345-9626-4e3ff26b0217.png)

#### Monitoring in ML Systems
ML monitoring or functional monitoring, deals with keeping an eye on model predictive performance and changes in serving data. These include the metrics, the model optimized during training and the distributions and characteristics of each feature in the serving data. System monitoring or non functional monitoring refers to monitoring the performance of the entire production system, the system status and the reliability of the serving system. This includes queries per second, failures, latency, resource utilization etcetera.

![image](https://user-images.githubusercontent.com/1645304/134275968-3ecab907-0fce-4371-93a7-8e4c6a8eddc1.png)

#### Why is ML monitoring different?

Unlike a pure software system, there are two additional components to consider in an ML system, the data and the model. Unlike in traditional software systems, the accuracy of an ML system depends on how well the model reflects the world it is meant to model which in turn depends on the data used for training and on the data that it receives while serving requests. It's not simply a matter of monitoring for system failures like SEG faults and out of memory or network issues, the model and the data require additional, very specialized monitoring as well.

Code and config also take on additional complexity and sensitivity in an ML system due to two aspects, entanglement and configuration. Entanglement, and no, I'm not referring here to quantum entanglement, refers to the issue where changing anything, changes everything. Here, you need to be careful with feature engineering and features selection and understand your model sensitivity. Configuration can also be an issue because model hyper parameters, versions and features are often controlled in a system config and the slightest error here can cause radically different model behavior that won't be picked up with traditional software tests. Again, requiring additional very specialist monitoring.

![image](https://user-images.githubusercontent.com/1645304/134276086-d335e71f-5b40-497e-9bfe-e45af8e38563.png)

### Observability in ML
#### What is observability?
Observability measures how well you can infer the internal states of a system by just knowing the inputs and outputs. For ML, this means monitoring and analyzing the prediction requests and the generated predictions from your models. Observability isn't a new concept, it actually comes from control system theory where it has been well established for decades. In control system theory, observability and controllability are closely linked. You can only control a system to the extent that you can observe it. Looking at an ML-based product or service, this maps to the idea that controlling the accuracy of the results overall, usually across different versions of the model, requires observability. This also adds to the importance of model interpretability. 

![image](https://user-images.githubusercontent.com/1645304/134441421-4b95d74b-a400-4c61-87d1-5dfd05108f2e.png)

#### Complexity of observing modern systems
There are a substantial number of systems which you need to monitor and aggregate. This often means relying on vendor monitoring systems to collect and sometimes aggregate data because the observability of each instance can be limited. For example, monitoring CPU utilization across an autoscaling containerized application is much different than simply monitoring CPU usage on a single server.

![image](https://user-images.githubusercontent.com/1645304/134604713-cbb5ab7f-d0ad-4abc-94b7-09be5a49ea28.png)


#### Deep observability for ML
Observability is about making measurements. Just like when you're analyzing your model performance during training, measuring top-level metrics is not enough and will provide an incomplete picture. You need to slice your data to understand how your model performs for various data subsets. For example, in an autonomous vehicle, you need to understand performance in both rainy and sunny conditions and measure them separately.

More generally speaking, data slices provide a useful way to analyze different groups of people or different types of conditions. This means that domain knowledge is important in observing and monitoring your systems and production just like it is when you're training your models. In general, it's your domain knowledge that will guide how you slice your data.

The TFX framework and **TensorFlow model analysis** are very powerful tools and include functionality for doing observability analysis on multiple slices of data for your deployed models. This is true for both supervised and unsupervised monitoring of your models.

In a supervised setting, the true labels are available to measure the accuracy of your predictions. In contrast, in an unsupervised setting, you'll monitor for things like the means, medians, ranges, and standard deviations of each feature. In both supervised and unsupervised settings, you need to slice your data to understand how your system behaves for different subsets. Going back to the autonomous vehicle example, slicing by weather condition is important to avoid things like making poor driving decisions in the rain. 

![image](https://user-images.githubusercontent.com/1645304/134604992-51506bc1-ab2d-47ee-8475-90526c7669ef.png)

#### Goals for ML observability
The main goal of observability in the context of monitoring is to prevent or act upon system failures. For this, the observations need to provide alerts when a failure happens, and ideally provide recommended actions to bring the system back to normal behavior.

More specifically, a alertability refers to designing metrics and thresholds that make it very clear when a failure happens. This may include defining rules to link more than one measurement to identify a failure.

Knowing that your system is failing is a good start, but an actionable recommendation based on the nature of the failure is way more helpful to correct this behavior. Actionable alerts clearly define the root cause of the system's failure.

At a bare minimum, your system should gather sufficient information to enable root cause analysis. Both **alertability** and **actionability** are goals, and the effectiveness of your system is a reflection of how well it achieves these goals.

![image](https://user-images.githubusercontent.com/1645304/134605588-01459bbe-d7a6-46e7-b004-4e711dd92f8a.png)

### Monitoring Targets in ML

#### Basics: Input and output monitoring
Starting with the basics, you can:
- monitor the inputs and outputs of your system. The inputs in a deployed system are the prediction requests, each of which is a feature vector.
- Use statistical measures of each feature, including their distributions and look for changes that may be associated with failures. Again, this should not be just top level measurements, but measurements of slices that are relevant to your domain.
- The outputs are the model's predictions which you can also monitor and measure. This should include an understanding of the deployment of different model versions to help you understand how different versions perform.
- You should also consider performing correlation analysis to understand how changes in your inputs affect your model outputs.

And again, this should be done on slices of your data, for example, correlation analysis can help you detect how seemingly harmless changes in your inputs cause prediction failures.

![image](https://user-images.githubusercontent.com/1645304/134605791-87b2507f-4195-4312-941b-0eedc48a8a29.png)

#### Input Monitoring
The prediction requests, whether you're doing real time or batch predictions form a large part of the observable data that you have for a deployment for each feature. You should monitor for errors such as values falling outside and allowed range or a set of categories where these air conditions are often defined based on domain knowledge. You should also monitor how each feature distribution changes over time and compare those to the training data, monitoring for errors and changes is better done with sliced data so that you can better understand and identify potential system failures.

![image](https://user-images.githubusercontent.com/1645304/134605989-9eedbfd2-f775-468e-9041-4d2bcb6c86a1.png)


#### Prediction Monitoring

Statistical testing and comparisons are the basic tools that you can use to analyze your data. Typical descriptive statistics include median mean standard deviation and range values for monitoring model predictions. You can also use statistical testing and sometimes in scenarios such as predicting, click through where labels are available. You can also do comparisons between known labels and model predictions in this figure. You can see that if the variables are normally distributed, then you would expect the mean values to be within the standard error of the mean interval. It's also important to consider that if you have altered the distributions of the training data to correct for things like class imbalance or fairness issues. Then you need to take that into account when comparing to the distributions of the input data that gathered through that is gathered through the monitoring prediction requests

![image](https://user-images.githubusercontent.com/1645304/134606050-a6fd932a-02de-4fd0-a19a-ad33cfb465d5.png)

#### Operational Monitoring
Monitoring in the realm of software engineering is far more well established. So the operational concerns around our ml system may include monitoring system performance in terms of measures like latency or IO and memory or disk utilization or system reliability in terms of up time and monitoring can even happen while taking audit ability into account. In software engineering, talking about monitoring is strictly speaking, talking about events, events can be almost anything ranging from receiving an http request entering or leaving a function which may or may not contain ml code or not. A user logging in reading from network or writing to the disk and so on, all of these events listed here have some context. Having all of the context for all of the events would be great for debugging and understanding how your systems perform in both technical and business terms. But collecting all the context information is often not practical, as the amount of data to process and store could be very large, so it's important to understand the most relevant context and try to gather that information.
 
![image](https://user-images.githubusercontent.com/1645304/134606319-5c9b5946-5bfb-4fc6-a8d6-dbd3b19d534b.png)

### Logging for ML Monitoring
Logging is almost always the basis for collecting the data that you will use to monitor your models and systems. A log is an immutable time stamped record of discrete events that happened over time for your ML system along with additional information.

#### Steps for building observability
For ml systems the same logic applies. This is where logging becomes really handy and more so when building observability. Let's explore how to do that. You can start with the out of the box, logs and metrics. These will usually give you some basic overall monitoring capabilities, which you can then add to. For example, in google's compute engine platform. If you need additional application logs, you can install agents to collect those logs. Cloud monitoring collects metrics from all of the cloud services by default which you can then use to build dashboards. When you need additional application or business level metrics. You can use those custom metrics to monitor over time. Then using aggregate sinks and workspaces allows you to centralize your logs from many different sources or services in order to create a unified view of your application.

![image](https://user-images.githubusercontent.com/1645304/134607201-c25f77cb-5158-43d6-9c0b-6831ea23c422.png)

#### Logging
a log is an immutable time stamped record of discrete events that happened over time. This also includes debugging or profiling messages that are printed to the log from your application, as well as automatically generated warning errors and debug messages. Depending on the verbosity settings for your logging. 

![image](https://user-images.githubusercontent.com/1645304/134607294-eaabde20-2193-4461-bce7-c395395ecd13.png)


#### Tools for building observability
![image](https://user-images.githubusercontent.com/1645304/134607370-28a6b057-5633-4fd1-ab28-266cf37c4e87.png)

#### Logging - Advantages
Log messages are very easy to generate since it is just a string, a blob of Jason or typed key value pairs. Event logs provide valuable insight along with context providing detail that averages and percentiles don't surface. However, it's not always easy to provide the right level of context without obscuring the really valuable information in too much extraneous detail. While metrics show the trends of a service or an application, logs focus on specific events. This includes both log messages printed from your application as well as warnings, errors or debug messages which are generated automatically. The information logs can be used to investigate incidents and to help with root cause analysis. 

![image](https://user-images.githubusercontent.com/1645304/134608220-18a5881d-0929-4672-8cc1-67b28287fc8c.png)

#### Logging - Disadvantages
For example, excessive logging can negatively impact system performance. As a result of these performance concerns aggregation operations on logs can be expensive and for this reason alerts based on logs should be treated with caution. On the processing side, raw logs are almost always normalized, filtered and processed by a tool like log stash or fluent D or scribe or eca. Before there persisted in a data store like elastic search or big query. Setting up and maintaining this tooling carries with it a significant operational cost. One of the key advantages of managed services is that they remove this cost.

![image](https://user-images.githubusercontent.com/1645304/134608322-3a99aea1-f859-4281-be6c-b4721e200534.png)


#### Logging in Machine Learning
 Much of the discussion so far has centered around how you could use metrics to monitor your input data and predictions in an Ml system. This is usually the basic way to collect data to monitor an application. Some of the red flags to watch out for may include basic things like a feature becoming unavailable. Especially when you're including historical data in your prediction requests which needs to be retrieved from a data store. In other cases, notable shifts in the distribution of key input values are important. For example, a categorical value that was relatively rare in the training data becomes more common. pattern specific to your model for example, in an NLP scenario, a sudden rise in the number of words not seen in the training data. That can also be another sign of a potential change which can lead to problems. 

![image](https://user-images.githubusercontent.com/1645304/134608433-e4d80a52-77b8-463d-96d2-e69ffe077c34.png)

#### Storing log data for analysis
How you store your log data can have a significant impact on how easily it can be queried for analysis. At this point, you should consider parsing out and storing your input and prediction data along with any labels that you're able to gather in aquariable data store. Such as a database or a search engine based tool like elastic search. This enables analysis for things like generating the distributions and statistics of your features which can be tracked and compared over time. By associating each item with a time stamp you can also order the data which is important for identifying trends and seasonality. In addition, by identifying the systems involved, you can help with root cause analysis of system failures. Having this data in aquarium bill data store also enables offline automated reporting dashboards and alerting. 

![image](https://user-images.githubusercontent.com/1645304/134608605-cf8263ca-4776-4f21-8bf3-7d4f6deb98a5.png)

#### New Training data
At the very least, collecting prediction requests should provide the feature vectors that are representative of the current state of the world that your application lives in. So this data is very valuable. Let's consider labeling issues and labeling techniques for a moment. If you're lucky in your domain, you'll be able to use direct labelling. For example for recommend systems you can usually capture the user behavior after a recommendation is made to determine if the right options were recommended. In other cases you will need to use manual labeling which can be slow and expensive but is also sometimes the only viable option. Using techniques like active learning can help reduce the cost by only selecting the most important examples to label. And that includes shaping your data set for issues like class imbalance and fairness. And finally, weak supervision is a powerful technique with significant advantages but also some challenges. What's most important here is that you capture this valuable data so that you can keep your model in sync with a changing world.

![image](https://user-images.githubusercontent.com/1645304/134608788-ac0f2a4f-1ad2-4455-a994-31ddbee37c87.png)

### Tracing for ML Systems
Tracing focuses on monitoring and understanding system performance, especially for microservice-based applications.

#### Distributed tracing
Suppose you're trying to troubleshoot a prediction latency problem, suppose your system is made of many independent services and the prediction is generated through many downstream services, you have no idea which of those services are causing the slowdown. You have no clear understanding of whether it's a bug and integration issue, a bottleneck due to a poor choice of architecture or poor networking performance.


In monolithic systems, it's relatively easy to collect diagnostic data from different parts of a system. All the modules might even run within one process and share common resources for logging.


![image](https://user-images.githubusercontent.com/1645304/134609056-4674e3ff-f936-402a-8c11-9e6c9441d5a4.png)

Solving this problem becomes even more difficult if your services are running as separate processes in a distributed system. You can't depend on the traditional approaches that help diagnose monolithic systems. You need to have finer grained visibility into what's going on inside each service and how they interact with one another over the lifetime of a user request. It becomes harder to follow a call starting from the front-end web server to all of its back-ends until the prediction is returned back to the user and you'll notice here that we're really focusing on online serving.

![image](https://user-images.githubusercontent.com/1645304/134609114-84254fbd-d53c-497d-8810-6f85c04449dc.png)


#### Tools for building observability
To properly inspect and debug issues with latency for requests in distributed systems, you need to understand the sequencing and parallelism of the services and the latency contribution of each to the final latency of the system. To address this problem, Google developed the distributed tracing system, Dapper to instrument and analyze its production services. The Dapper paper has inspired many open source projects, such as Zipkin and Jaeger and Dapper style tracing has emerged as an industry wide standard.

![image](https://user-images.githubusercontent.com/1645304/134609249-1bbed56e-8ace-409b-8f16-6deceeb859fd.png)

#### Dappeer-Style Tracing
In service based architectures, Dapper style tracing works by propagating tracing data between services. Each service annotate the trace with additional data and passes the tracing header to other services until the final request completes. Services are responsible for uploading their traces to a tracing back-end. The tracing back-end, then puts related latency data together like pieces of a puzzle. Tracing back-ends also provide UIs to analyze and visualize traces. Each trace is a call tree, beginning with the entry point of a request and ending with the server's response including all of the RPCs along the way. Each trace consists of small units called spans.

![image](https://user-images.githubusercontent.com/1645304/134609337-dd3bbe7a-9ad0-44e5-a75f-f3909cc1f632.png)

#### Reading: Monitoring Machine Learning Models in Production
Check this [resource](https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/) out to learn more about ML monitoring and logging.

#### Quiz: Model Monitoring and Logging

**1. Question 1**

What issue arises when models are automatically trained on data collected during production?

- [ ] Staleness
- [ ] Data Skews
- [x] Negative Feedback Loops


**2. Question 2**

Is observability more attainable in modern systems?

- [x] No, observability gets more challenging when you consider modern systems.
- [ ] Yes, modern systems allow simple monitoring.


**3. Question 3**

In the realm of ML engineering, the operational concerns include monitoring system performance. What measures do we use for doing so? (Select all that apply)


- [x] Uptime
- [ ] HTTP request reception
- [x] IO/memory/disk utilization
- [x] Latency

**4. Question 4**

What are the advantages of Logging for ML Monitoring? (Select all that apply)

- [x] Logs focus on specific events.
- [ ] Log aggregation is cheap.
- [x] Logs are easy to generate.
- [x] Logs provide valuable insight.


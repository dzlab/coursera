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

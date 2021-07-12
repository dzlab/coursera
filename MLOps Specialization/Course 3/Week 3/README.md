## Week 3 Distributed Training

### High-Performance Modeling
#### Distributed Training
Types of distributed training
- Data parallelism: In data parallelism, models are replicated onto different accelerators (GPU, TPU) and data is split between them
- Model parallelism: When models are too large to fit on a single device then they can be divided into partitions, assigning different partitions to different accelerators

Distributed training using data parallelism
- Synchronous training:
  - All workers train and complete updates in sync
  - Supported via all-reduce architecture
- Asynchronous training:
  - Each worker trains and completes updates separately
  - Supported via parameter server architecture
  - More efficient, but can result in lower accuracy and slower convergence

Making your models distribute-aware:
if you want to distribute a model:
- Supported in high-level APIs such as Keras/Estimators
- For more control, you can use custom training loops

tf.distribute.Strategy:
- Library in TensorFlow for running a computation in multiple devices
- Supports distribution strategies for high-level APIs like Keras and custom training loops
- Convenient to use with little or no code changes

Distribution Strategies suppported by tf.distribute.Strategy
- One Device Strategy
  - Single device - no distribution
  - Typical usage of this strategy is testing your code before switching to other strategies that actually distributed your code
- Mirrored Strategy: typically used for training on one machine with multiple GPUs
  - Creates a replica per GPU <> Variables are mirrored
  - Weight updating is done using efficient cross-device communication algorithms (all-reduce algorithms)
- Parameter Server Strategy
  - Some machines are designated as workers and others as parameter servers
    - Parameter servers store variables so that workers can perform computations on them
  - Implements asynchronous data parallelism by default
- Multi-Worker Mirrored Strategy
- Central Storage Strategy
- TPU Strategy

Fault tolerance
- Catastrophic failures in one worker would cause failure of distribution strategies
- How to enable fault tolerance in case a worker dies?
  - By restoring training state upon restart from job failure
  - Keras implementation: BackupAndRestore callback

#### High-Performance Ingestion

#### Training Large Models - The Rise of Giant Neural Nets and Parallelism
GPipe - Key features
- Open-source TensorFlow library (using Lingvo)
- Inserts communication primitives at the partition boundaries
- Automatic parallelism to reduce memory consumption
- Gradient accumulation across micro-batches, so that model quality is preserved
- Paritioning is heuristic-based

#### High-Performance Modeling
If you wish to dive more deeply into  high-performance modeling, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Distributed training https://www.tensorflow.org/guide/distributed_training
- Data parallelism https://arxiv.org/abs/1806.03377
- Pipeline parallelism https://ai.googleblog.com/2019/03/introducing-gpipe-open-source-library.html
- GPipe https://arxiv.org/abs/1811.06965

#### PRACTICE QUIZ - High-Performance Modeling
Question 1: In the model parallelism, the models are replicated into different devices (GPU) and trained on data batches.

- [x] No
- [ ] Yes

Question 2: Which ones of the following are terminologies used often in the world of distributed computing?

- [x] Worker
- [ ] Device
- [ ] Copy
- [ ] Mirrored Variable

Question 3: The pipeline performance can be optimized through parallelizing data extraction and transformation. 

- [ ] False
- [x] True

Question 4: TensorFlow offers techniques to optimize pipeline performance like prefetching, parallelizing data extraction and transformation, caching and reducing memory. Those techniques could be used from the sklearn.decomposition API.

- [ ] True
- [x] False


Question 5: As important developments in both model growth and hardware improvement have been made, parallelism becomes an alternative of greater importance. 

- [x] True
- [ ] False

Question 6: The _______ library uses synchronous mini-batch gradient descent for training in a distributed way. 

- [ ] Pandas
- [x] GPipe
- [ ] Scikit-learn
- [ ] Scipy


### Knowledge Distillation
#### Teacher and Student Networks
Knowledge distillation
- Duplicate the performance of a complex model in a simpler model
- Idea: Create a simpler 'student' model that learns from a complex 'teacher' model

Teacher and student
- Training objectives of the models vary
- Teacher (normal training): maximizes the actual metric
- Student (knowledge transfer)
  - matches p-distribution of the teacher's predictions to form soft targets
  - Soft targets tell us about the knowledge learned by the teacher
  
Transfering "dark knowledge" to the student
- Improve softness of the teacher's distribution with softmax temperature (T)
- As T grows, you get more insight about which classes the teacher finds similar to the predicted one

Techniques
- Approach 1: Weights objectives (student and teacher) and combine during backprop
- Approach 2: Compare distributions of the predictions (student and teacher) using KL divergence

#### Knowledge Distillation
If you wish to dive more deeply into knowledge distillation, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Knowledge distillation https://arxiv.org/pdf/1503.02531.pdf
- Q&A case study https://arxiv.org/pdf/1910.08381.pdf

#### PRACTICE QUIZ - Knowledge Distillation
Question 1: The goal of knowledge distillation is optimizing the network implementation:

- [x] False
- [ ] True

Question 2: In knowledge distillation, the teacher will be trained using a  _________.

- [x] A Standard objective function
- [ ] A Soft Target
- [ ] K-L divergence
- [ ] GoogLeNet

Question 3: DistilBERT is a bigger version of BERT with a modified architecture, but the same number of layers. 

- [ ] Yes
- [x] No

Question 4: In knowledge distillation, the “teacher” network is deployed in production as it is able to mimic the complex feature relationships of the “student” network  

- [ ] True
- [x] False

Question 5: For a multi-class classification problem, which ones of the following statements are true regarding the training cost functions of the “student” and the “teacher” networks ? (Select all that apply)


- [ ] They both share the same cost functions
- [ ] The teacher network is trained to maximize its accuracy and the the student network uses a cost function to output the same classes as the teacher network 
- [x] The teacher network is trained to maximize its accuracy and the the student network uses a cost function to approximate the probability distributions of the predictions of the teacher network
- [x] Soft targets encode more information about the knowledge learned by the teacher than its output class prediction per example

Question 6: When the softmax temperature ____, the soft targets defined by the teacher network become less informative

- [ ] increases
- [x] decreases
- [ ] is equal to 1

Question 7: Generally, knowledge distillation is done by blending two loss functions and involves several hyperparameters. Here, L_h is the cross-entropy loss from the hard labels and LKL is the Kullback–Leibler divergence loss from the teacher labels. Which of the following statements are correct about the hyperparameters of knowledge distillation? (Select all that apply)

- [ ] In case of heavy data augmentation after training the teacher network, the alpha hyperparameter should be high in the student network loss function
- [x] When computing the the "standard" loss between the student's predicted class probabilities and the ground-truth “hard” labels, we use a value of the softmax temperature T equal to 1  x
- [ ] When computing the the "standard" loss between the student's predicted class probabilities and the ground-truth “hard” labels, we use the same value of the softmax temperature T to compute the softmax on the teacher’s logits
- [ ] In case of heavy data augmentation after training the teacher network, the alpha hyperparameter should be low in the student network loss function

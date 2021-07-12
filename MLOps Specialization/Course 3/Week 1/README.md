# Machine Learning Modeling Pipelines in Production
## Week 1
### Hyperparameter tuning: searching for the best architecture
#### PRACTICE QUIZP - Hyperparameter Tuning and Neural Architecture Search

Question 1: Neural Architecture Search was a promising technique that failed to surpass hand-designed architectures.

- [ ] True
- [x] False

Question 2: Which characteristics best describe hyperparameters?

- [ ] Hyperparameters are derived via training.
- [x] Hyperparameters are not updated in each training step.
- [x] Hyperparameters are set before launching the learning process.
- [x] Hyperparameters can be quite numerous even in small models.

Question 3: Does KerasTuner support multiple strategies?

- [ ] No
- [x] Yes

### AutoML
#### Neural Architecture Search
If you wish to dive more deeply into neural architecture search , feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Neural Architecture Search https://arxiv.org/pdf/1808.05377.pdf
- Bayesian Optimization https://distill.pub/2020/bayesian-optimization/
- Neural Architecture Search with Reinforcement Learning https://arxiv.org/pdf/1611.01578.pdf
- Progressive Neural Architecture Search https://arxiv.org/pdf/1712.00559.pdf
- Network Morphism https://arxiv.org/abs/1603.01670

#### AutoML
If you wish to dive more deeply into AutoMLs, feel free to check out these cloud-based tools. You won’t have to read these to complete this week’s practice quizzes.

- Amazon SageMaker Autopilot https://aws.amazon.com/sagemaker/autopilot
- Microsoft Azure Automated Machine Learning https://azure.microsoft.com/en-in/services/machine-learning/automatedml/
- Google Cloud AutoML https://cloud.google.com/automl

#### PRACTICE QUIZ - AutoML
Question 1: Can Neural Architecture Search (NAS) be seen as a subfield of AutoML?

- [x] Yes
- [ ] No

Question 2: Which of the following are dimensions of the Neural Architecture Search (NAS) technique?

- [x] Performance Estimation Strategy
- [x] Search Strategy
- [ ] Training and Validation of the Architecture
- [x] Search Space

Question 3: What does the search space in Neural Architecture Search (NAS) allow for?

- [x] Restricting unbounded search spaces to have a maximum depth.
- [x] Reducing the size of the search space incorporating prior knowledge about well-suited properties.
- [ ] Defining how we explore the search space.
- [x] Defining which neural architectures we might discover in principle.

Question 4: In the chain-structured Neural Network Architecture, the space is parametrized by:

- [ ] The multiple branches with additional layers types and skip connections.
- [x] The operation every layer can execute.
- [x] A number of n sequentially fully-connected layers.
- [x] Hyperparameters associated with the operation.

Question 5: What are the main features of Automated Machine Learning (AutoML)?

- [ ] AutoML aims to automate the end-to-end process of machine learning to produce simpler and faster solutions.
- [ ] AutoML aims to automate the decision-making in a data-driven and objective way.
- [x] AutoML technologies democratize AI with customized state-of-the-art machine learning.
- [ ] AutoML is the process of automating architecture engineering and finding the design of machine learning models.

Question 6: What are the two main types of search spaces?

- [ ] Long and Short
- [ ] Big and Small
- [ ] Complex and Simple
- [x] Macro and Micro


Question 7: In measuring AutoML efficacy, several strategies have been proposed to reduce performance cost estimation, including:

- [x] Lower fidelity estimates
- [x] Weight Inheritance/ Network Morphisms
- [ ] Reinforcement learning
- [x] Learning Curve Extrapolation

Question 8: The lower fidelity estimates are a performance estimation strategy that allows for...

- [x] Training on lower-resolution
- [x] Training with less filters per layer
- [ ] Training for a few epochs.
- [x] Training on a subset of the data.

Question 9: Can network morphism modify an architecture while leaving the network's function unchanged?

- [ ] No
- [x] Yes

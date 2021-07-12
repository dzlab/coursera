## Week 5: Interpretability

### Explainable AI
Responsible AI:
- Development of AI is creating new opportunities to improve lives of people
- Also raises new questions about the best way to build the following into AI systems:
  - Fairness: Ensure working towards systems that are fair and inclusive to all users. Explanability helps ensure fairness.
  - Explanability: Understanding how and why ML models make certain predictions. Explanability helps ensure fairness.
  - Privacy: training models using sensitive data needs privacy preserving safegurds
  - Security: identifying potential threats can help keep AI systems safe and secure.

Explanable Artificial Intelligence (XAI)
- The field of XAI allow ML systems to be more transparent, providing explanations of their decisions in some level of details
- These explanations are important
  - To ensure algorithmic fairness
  - Identify potential bias and problems in training data
  - To ensure algorithms/models work as expected

Need for Explainability in AI
- Models with high sensitivity, including natural lanuguage networks, can generate widly wrong results
- Attacks
- Fairness
- Reputation and Branding
- Legal and regulatory concerns
- Customers and other stakeholders may question or challenge model decisions

#### Explainable AI
If you wish to dive more deeply into explainable AI, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Explainable AI https://ojs.aaai.org/index.php/aimagazine/article/view/2850/3419
- Responsible AI https://arxiv.org/pdf/1910.10045.pdf

#### PRACTICE QUIZ - Explainable AI
Question 1: Which ones of the following features are Responsible AI factors? (Select all that apply)

- [x] Fairness
- [ ] Transparency
- [x] Privacy
- [x] Interpretability 

Question 2: DNNs can be fooled into misclassifying inputs with no resemblance to the true category. Regarding image classification, this can be done by:

- [x] Generating adversarial images.
- [ ] Dimension Reduction
- [ ] Partial Deletion. 
- [ ] Examples Imputation

Question 3: If an ML model was trained with many examples from a particular group, _________.

- [x] There would likely be greater certainty about its results for that group’s examples.
- [ ] There would likely be greater certainty about its results for examples from different groups.
- [ ] There would likely be less certainty about its results for that group’s examples.
- [ ] There would likely be less certainty about its results for examples from different groups.


### Interpretability
#### Model Interpretation Methods
What is interpretability?
> Models are interpretable if their operations can be understood by a human, either through introspection or through a produced explanation. Explanation and justification in machine learning: A survey

What are the requirements?
You should be able to query the model to understand:
- Why did the model behave in a certain way?
- How can we trust the predictions made by the model?
- What information can model provide to avoid prediction errors?

Categorizing Model interpretation Methods
- Intrinsic or Post-Hoc?
  - Intrinsic Interpretability: Model which is intrinsically interpretable: linear models, tree-based models, TF Lattice, etc.
  - Post-hoc methods treat models as black boxes
    - Agnostic to model architecture
    - Extracts relationships between features and model predictions, aganostic of model architecture
    - Applied after training
- Model specific or Model Agnostic?
- Local or Global?

Types of results produced by Interpretation Methods
- Feature summary statistics
- Feature summary visualization
- Model internals
- Data point

Model specific or Model Agnostic?
- Model specific
  - These tools are limited to specific model classes
  - Example: Interpretation of regression weights in linear models
  - Intrinsically interpretable model techniques are model specific
  - Tools designed for particular model architectures
- Model agnostic
  - Applied to any model after it is trained
  - DO not have access to the internals of the model
  - Work by analyzing feature input and output pairs
  
Local or Global?
- Local: interpretation method explains an individual prediction
  - Feature attribution is identification of relevant features as an explanation for a model
- Global: interpretation method explains entire model behavior
  - Feature attribution summary for the entire test data set

#### Intrinsically Interpretable Models
Intrinsically Interpretable Models
- How the model works is self evident
- Many classic models are hightly interpretable
- Neural networks look like "black boxes"
- Newer archiecture focus on designing for interpretability

Interpretable Models

| Algorithm | Linear | Monotonic | Feature Interactin | Task |
|-|-|-|-|-|
| Linear regression | yes | yes | No | regr |
| Logistic regression | no | yes | No | class |
| Decision trees | no | some | yes | class, regr |
| RuleFit | yes* | yes | yes | class, regr |
| k-nearest neighbors | No | No | No | class, regr |
| TF Lattice | yes* | yes | yes | class, regr |


Model architecture influence on interpretability
![image](https://user-images.githubusercontent.com/1645304/125212622-a3a3e900-e263-11eb-95ba-b2dea59a9118.png)


Interpretation from weights
Linear models have easy to understand interpretation from weights
- Numerical features: increase of one unit in a feature increases prediction by the value of corresponding weight
- Binary features: changing between 0 or 1 category changes the prediction by value of the feature's weight
- Categorical features: one hot encoding affects only one weight

Feature importance
- Relevance of a given feature to generate model results
- Calculation is model dependent
- Example: linear regression model, t-statistic

More advance models: TF Lattice
- Overlaps a grid onto the feature space and learns values for the output at the vertices of the grid
- Linearly interpolates from the lattice values surrounding a point
- Enables you to inject domain knowledge into the learning process through common-sense or policy-driven shape constraints
- Set constraints such as monoticity, complexity, and how features interact
- Accuracy
  - TF Lattice achieves accuracies comparable to neural networks
  - TF Latice provides greater interpretability
- Issues: Dimensionality
  - The number of parameters of a lattice layer increases exponentially with the number of input features
  - Very rough rule: less than 20 features ok without ensembling

#### Interpretability
If you wish to dive more deeply into interpretability, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Interpretable Machine Learning - A Guide for Making Black Box Models Explainable. https://christophm.github.io/interpretable-ml-book/
- TensorFlow Lattice https://www.tensorflow.org/lattice
- Monotonic Calibrated Interpolated Look-Up Tables https://jmlr.org/papers/volume17/15-243/15-243.pdf


#### PRACTICE QUIZ - Interpretability
Question 1: Interpretation methods can be grouped based on (Check all that apply):

- [x] Whether they are intrinsic or post-hoc.
- [x] Whether they are model specific, or model agnostic.
- [ ] Whether they are complex or basic.
- [x] Whether they are local or global.

Question 2: One key aspect that helps improve interpretability is the presence of monotonic features.

- [ ] False
- [x] True

Question 3: Many classic models are intrinsically interpretable models, such as the transparent, intuitive, and relatively easy to understand neural networks.

- [ ] True
- [x] False


### Understanding Model predictions
#### Model Agnostic Methods
These methods separate explanations from the machine learning model.
Desired characteristics:
- Model flexibility
- Explanation flexibility
- Representation flexibility

Model Agnostic Methods
- Partial Dependece Plots
- Accumulated Local effects
- Permutation Feature Importance
- Local Surrogate (LIME)
- Global Surrogate
- SHAP
- Individual Condition Expectation
- Shapley Values

#### Partial Dependence Plots (PDP)
A partial depdence plot shows
- The marginal effect one or two features have on the model result
- Whether the relationship between the targets and the feature is linear, monotonic, or more complex

Advantages of PDP
- Computation is intuitive
- If the feature whose PDP is calculated has no feature correlations, PDP perfectly represents how feature influences the prediction on average
- Easy to implement

Disadvantages of PDP
- Realistic maximum number of features in PDP is 2
- PDP assumes that features have no interactions (any correlation should have been removed during feature engineering)

#### Permutation Feature 
Feature Importance measures the increase in prediction error after permuting the features
- Feature is important if shuffling its values increases model error
- Feature is unimportant if shuffling its values leaves model error unchanged

Algorithm
- Estimate the original model error
- For each feature:
  - Permute the feature values in the data to break its association with the true outcome
  - Estimate error based on the predictions of the permuted data
  - Calculate permutation feature importance
  - Sort features by descending feature importance

Advantages
- Nice interpretation: shows the increase in model error when the feature's information is destroyed
- Provides global insight to model's behavior
- Does not require retraining of model

Disadvantages
- It is unclear if testing or training data should be used for visualization
- Can be biased since it can create unlikely feature combinations in case of strongly correlated features
- You need access to the labelbed data

#### Permutation Feature Importance
If you wish to dive more deeply permutation feature importance, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes

- Permutation feature importance http://arxiv.org/abs/1801.01489

#### Shapley Values
- The Shapley Value is a method for assigning payouts to players dependending on their contribution to the total
- Applying that to ML we define that:
  - Feature is a player in a game
  - Prediction is the payout
  - SHapely value tells us how the payout (feature contribution) can be distributed among features
  
| Term in Game Theory | Relation to ML | Relation to House prices Exmaple |
| - | - | - |
|Game | Prediction task for single instance of dataset | Prediction of house prices for a single instance |
| Gain | Actual prediction for instance - Average prediction for all instances | Prediction for house price (300000) - Average prediction (310000) = -10000 |
| Players | Feature values that contribute to prediction | Park=nearby, cat=banned, area=50m2, floor=2nd|

Advantages
- Based on solid theoritical foundation, satisfies efficiency, symmetry, dummy, and Additivity properties
- Value is farily distributed among all features
- Enables contrastive explanations

Disadvantages
- Computationally expensive
- Can be easily misinterpreted
- Always uses all the features, so not good for explanations of only a few features
- No prediction model, can't be used for 'what if' hypothesis testing
- Does not work well when features are correlated

#### SHapley Additive exPlanations (SHAP)
SHAP (SHapley Additive exPlanations) is a framework for Shapley Values which assigns each feature an importance value for a particular prediction. Includes extensions for:
- TreeExplainer: high-speed exact algorithm for tree ensembles
- DeepExplainer: high-speed approximation algorithm for SHAP values in deep learning models
- GradientExplainer: combines ideas from Integrated Gradients, SHAP, and SmoothGrad into a single expected value equation
- KernelExplainer: uses a specially weighted local linear regression to extimate SHAP values for any model

SHAP Explanation Force plots
- Shapley Values can be visualized as forces
- Prediction starts from the baseline (Average of all predictions)
- Each feature value is a force that increases (red) or decreases (blue) the prediction

<p align="center">
  <img width="616" src="https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/boston_waterfall.png" />
</p>

#### Understanding Model Predictions
If you wish to dive more deeply into understanding model predictions, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- A Unified Approach to Interpreting Model Predictions https://proceedings.neurips.cc/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf
- Explainable AI for Trees: From Local Explanations to Global Understanding https://arxiv.org/abs/1905.04610

#### Testing Concept Activation Vectors (TCAV)
Concept Activation Vectors (CAV)
- A neural network's internal state in terms of human-friendly concepts
- Defined using examples which show the concept

#### Local Interpretable Model-agnostic Explanations (LIME)
- Implements local surrogate models - interpretable models that are used to explain individual predictions
- Using data points close to the individual prediction, LIME trains an interpretable model to approximate the predictions fo the real model
- The new interpertable model is then used to interpret the real result

#### TCAV and LIME
If you wish to dive more deeply into TCAV and LIME, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- TCAV https://arxiv.org/pdf/1711.11279.pdf
- LIME https://github.com/marcotcr/lime

#### AI Explanations
Google Cloud AI Explanations for AI platform
- Explain why an individual data point received that prediction
- Debug odd behavior from a model
- Refine a model or data collection process
- Verify that the model's behavior is acceptable
- Present the gist of the model

AI Explanations: Integrated Gradients
- A gradient-based method to efficiently compute feature attributions with the same axionatic properties as Shapley values

AI Explanations: XRAI (eXplanation with Rankend Area Integrals)
XRAI assesses overlapping regions of the image to create a saliency map
- Hightlights relevant regions of the image rather then pixels
- Aggregates the pixel-level attribution within each segment and rans the segments

#### AI Explanations
If you wish to dive more deeply into AI explanations, feel free to check out this optional reference. You won’t have to read these to complete this week’s practice quizzes.

- AI Explanations https://storage.googleapis.com/cloud-ai-whitepapers/AI%20Explainability%20Whitepaper.pdf

#### PRACTICE QUIZ - Understanding Model Predictions
Question 1: Model-agnostic methods have access to the model's internals, and they can be applied to any model after being trained.

- [x] False
- [ ] True

Question 2: PDP (Partial Dependence Plots) is a local method that evaluates a specific relationship between the labels and the results.

- [x] False
- [ ] True

Question 3: We can measure the importance of a feature with the Permutation Feature Importance technique. What statements are true about an “important” feature?

- [x] Shuffling its values increases the model error.
- [ ] Shuffling its values leaves the model error unchanged.
- [ ] After sorting the features by ascending FI (Feature Importance), you should consider removing the feature vector with the highest FI.
- [ ] An increase in the model error means that we have to remove the feature vector.

Question 4: A technique for understanding model predictions is the concept of the Shapley Values. It assigns payouts (predictions) to players (features) depending on their contribution. So, The Shapley Values is a method for knowing how much each feature depends on the results.

- [ ] True
- [x] False

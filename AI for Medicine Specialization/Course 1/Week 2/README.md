
# Week 2 Sensitivity, Specificity, and Evaluation Metrics

## Key evaluation metrics
### Accuracy in terms of conditional probability

### Sensitivity, Specificity and Prevalence

![image](https://user-images.githubusercontent.com/1645304/126882839-dceb3356-0427-4d3f-b1b4-6492faecc7f4.png)

| sensitivity| specificity|
|-|-|
| p (+ \| disease)| p (- \| normal)|
|if a patient has the disease, what is the probability that the model predicts positive| if the patient is normal what is the probability that the model predicts negative|

The probability of a patient having disease in a population is called the **prevalence**. 
![image](https://user-images.githubusercontent.com/1645304/126883522-16811f59-d4fd-4f9a-863e-b02b9d3eeae9.png)

This equation allows us to see accuracy as a weighted average of **sensitivity** and **specificity**:
- The weight associated with the **sensitivity** is the **prevalence**, and 
- The weight associated with the **specificity** is one minus the **prevalence**. 

### PPV, NPV

|PPV Positive predictive value of the model |NPV Negative predictive value or of a model|
|-|-|
|`p (disease \| +)`| `p (normal \| -)`|
|![image](https://user-images.githubusercontent.com/1645304/126909573-7d08ecfc-8207-487b-8f40-18f6b8794736.png)|![image](https://user-images.githubusercontent.com/1645304/126909536-d06544d0-cd12-4995-b35f-c64032235b2f.png)|

We can calculate PPV and NPV on an example as follows:
|||
|-|-|
|![image](https://user-images.githubusercontent.com/1645304/126909685-80c22bdf-cd2d-486c-af4b-9e3a8f886211.png)|![image](https://user-images.githubusercontent.com/1645304/126909722-5f770556-0455-413b-8321-3a7cd4b2daf6.png)|

### Confusion matrix
|||
|-|-|
|![image](https://user-images.githubusercontent.com/1645304/126909765-cdea553d-2fff-47a3-a8e9-8f805b302cbe.png)|![image](https://user-images.githubusercontent.com/1645304/126909801-036fb47f-e0cc-43bc-8b96-789ac0974c71.png)|

### Reading
#### Calculating the PPV in terms of sensitivity, specificity, and prevalence
In some studies, you may have to compute the Positive predictive value (PPV) from the sensitivity, specificity and prevalence.  Note that reviewing this reading will help you answer one of the quizzes at the end of this week!

##### Rewriting PPV
PPV = P(pos | \hat{pos})

(pospos is "actually positive" and \hat{pos} is "predicted positive").

By Bayes rule, this is 

 PPV = \frac{P(\hat{pos} | pos) \times P(pos)}{P(\hat{pos})}

##### For the numerator:
Sensitivity = P(\hat{pos} | pos).  Recall that sensitivity is how well the model predicts actual positive cases as positive.

Prevalence = P(pos)Prevalence=P(pos).  Recall that prevalence is how many actual positives there are in the population.

##### For the denominator:
P(\hat{pos}) = TruePos + FalsePos.  In other words, the model's positive predictions are the sum of when it correctly predicts positive and incorrectly predicts positive.

The true positives can be written in terms of sensitivity and prevalence.

TruePos = P(\hat{pos} | pos) \times P(pos), and you can use substitution to get 

TruePos = Sensitivity \times Prevalence

The false positives can also be written in terms of specificity and prevalence:

FalsePos = P(\hat{pos} | neg) \times P(neg)

1 - specificity = P(\hat{pos} | neg )

1 - prevalence = P(neg)1−prevalence=P(neg)

##### PPV rewritten:
If you substitute these into the PPV equation, you'll get

PPV = \frac{sensitivity \times prevalence}{sensitivity \times prevalence + (1 - specificity) \times (1 - prevalence)}

## How does varying the threshold affect evaluation metrics?

### ROC curve and Threshold
A chest x-ray classification model outputs a probability of disease given an x-ray. This output can be transformed into a diagnosis using a *threshold* or *operating point*:
- When the probability is above a threshold, then we interpret this as positive or saying the patient has the disease.
- When the probability is below the threshold, we interpret this as negative or saying the patient does not have the disease.

### Varying the threshold
|t1|t2|t3=1|
|-|-|-|
|![image](https://user-images.githubusercontent.com/1645304/126910141-07b9ffdd-ab03-4818-908e-2c52b2d3342b.png)|![image](https://user-images.githubusercontent.com/1645304/126910148-dfe0a176-89bc-4e0c-b2f7-022a23966d1f.png)|![image](https://user-images.githubusercontent.com/1645304/126910151-3884b704-aea9-47d9-a81e-a1d5818161f9.png)|

## Interpreting condience intervals correctly
### Sampling from the Total Population
We will look at how confidence intervals can be used to show this variability.
![image](https://user-images.githubusercontent.com/1645304/126910228-45f45e3b-aea4-422a-8784-72aa606ee7e4.png)
We don't want to test the model on the whole population because it's simply infeasible to do so. Therefore, the population accuracy p is unknown.
The question is, can we get a sense of how well the model will perform on this population by using a small sample of patients?
Let's say we sample a hundred patients from the hospital. Now we find that the model gets an accuracy of 0.8 on the set. Can we say anything about the range in which the population accuracy p will lie?

### Confidence intervals

Confidence intervals allow us to say that using our sample, we're 95 percent confident that the population accuracy p is in the interval 0.72 (lower bound), 0.88. 0.72 is called the  and 0.88 (upper bound).
![image](https://user-images.githubusercontent.com/1645304/126910295-7c38579b-aa2a-4a28-bd12-64852ddc381a.png)

|||
|-|-|
|![image](https://user-images.githubusercontent.com/1645304/126910358-f7d054ce-3313-4223-bf51-80c1ccb013ca.png)|![image](https://user-images.githubusercontent.com/1645304/126910369-d725f52a-c655-49b6-b5b4-4d3ce1ab7dca.png)|


> The interpretation of 95 percent confidence is that in repeated sampling, this method produces intervals that include the population accuracy in about 95 percent of samples.

### 95% Confidence interval
In practice, we don't compute the confidence intervals for many samples. We only compute our model performance on one sample.
> One of the factors that affects the width of the confidence intervals, which is given by how close these numbers are, is the sample size. 
![image](https://user-images.githubusercontent.com/1645304/126910427-318e0b3c-fe7b-403f-8ed4-f1a0b0c54208.png)

## Week 2 Quiz
### Evaluating machine learning models
Question 1: What is the sensitivity and specificity of a pneumonia model that always outputs positive?  In other words, the models says that every patient has the disease.

- [ ] sensitivity = 0.0, specificity = 1.0
- [ ] sensitivity = 0.5,  specificity = 0.5
- [ ] sensitivity  = 1.0, specificity = 1.0
- [x] sensitivity = 1.0, specificity = 0.0

Question 2: In some studies, you may have to compute the Positive predictive value (PPV) from the sensitivity, specificity and prevalence.  

Given a sensitivity = 0.9, specificity = 0.8, and prevalence = 0.2, what is the PPV (positive predictive value)? 

HINT: please check the reading item "Calculating PPV in terms of sensitivity, specificity and prevalence"

- [ ] 0.02
- [ ] 0.18
- [ ] 0.9
- [ ] 0.53

Question 3: If sensitivity = 0.9, specificity = 0.8, and prevalence = 0.2, then what is the accuracy? 

Hint: You can watch the video "Sensitivity, Specificity and Prevalence" to find the equation.

- [ ] 0.82
- [ ] 0.44
- [ ] 0.52
- [ ] 0.75

Question 4: What is the sensitivity and specificity of a model which randomly assigns a score between 0 and 1 to each example (with equal probability) if we use a threshold of 0.7?  

- [ ] Not enough information to answer the question.
- [ ] Sensitivity = 0.5, Specificity = 0.5
- [ ] Sensitivity = 0.3, Specificity = 0.7
- [ ] Sensitivity = 0.7, Specificity = 0.3

Question 5: What is the PPV and sensitivity associated with the following confusion matrix?  

Recall that 

PPV = \frac{\text{TruePositives}}{\text{positive predictions}}
 

Sensitivity = \text{How many actual positives are predicted positive?}

||Test Positive 	|Test Negative |
|-|-|-|
|Disease Positive	|30	|20|
|Disease Negative	|70	|10|

- [ ] PPV = 0.3,  Sensitivity = 0.6
- [ ] PPV = 0.4, Sensitivity = 0.2
- [ ] Not enough information is given
- [ ] PPV = 0.6, Sensitivity = 0.33

Question 6: You have a model such that the lowest score for a positive example is higher than the maximum score for a negative example. What is its ROC AUC?  

HINT 1: watch the video “Varying the threshold”.

HINT 2: draw a number line and choose values for the score that is the lowest prediction for any positive example, and choose another number that is the score for the highest prediction for any negative example.  Draw a few circles for “positive” examples and a few “x” for the negative examples.  What do you notice about the model’s ability to identify positive and negative examples?

- [ ] 0.52
- [ ] 0.82
- [ ] 1.0
- [ ] Not enough information is given

Question 7: For every specificity, as we vary the threshold, the sensitivity of model 1 is at least as high as model 2. Which of the following must be true? 

- [ ] The accuracy of model 2 is higher than model 1
- [ ] The ROC of model 2 is higher than model 1
- [ ] None of the above
- [ ] The ROC of model 1 is at least as high as model 2

Question 8: You want to measure the proportion of people with high blood pressure in a population. You sample 1000 people and find that 55% have high blood pressure with a 90% confidence interval of (50%, 60%). What is the correct interpretation of this result?  

HINT: Please watch the video "Confidence interval" to help you answer this question.

- [ ] If you repeated this sampling, the true proportion would be in the confidence interval about 90% of the time
- [ ] There is a 5% chance that the true mean is less than 50%
- [ ] With 90% probability, the proportion of people with high blood pressure is between 50% and 60%
- [ ] If we repeated this sampling, the middle of the confidence interval would be 55%, 90% of the time

Question 9: One experiment calculates a confidence interval using 1000 samples, and the another computes it using 10000 samples. Which interval do you expect to be tighter (assume they use the normal approximation)?  

- [ ] Not enough information
- [ ] 1,000 samples
- [ ] 10,000 samples
- [ ] Cannot say with confidence

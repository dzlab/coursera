
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
![image](https://user-images.githubusercontent.com/1645304/126909685-80c22bdf-cd2d-486c-af4b-9e3a8f886211.png)

![image](https://user-images.githubusercontent.com/1645304/126909722-5f770556-0455-413b-8321-3a7cd4b2daf6.png)

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

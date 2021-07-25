
# Week 2 Sensitivity, Specificity, and Evaluation Metrics

## Key evaluation metrics
### Accuracy in terms of conditional probability

### Sensitivity, Specificity and Prevalence

![image](https://user-images.githubusercontent.com/1645304/126882839-dceb3356-0427-4d3f-b1b4-6492faecc7f4.png)

| sensitivity| specificity|
|-|-|
| p (+ \| disease)| p (- \| disease)|
|if a patient has the disease, what is the probability that the model predicts positive| if the patient is normal what is the probability that the model predicts negative|

The probability of a patient having disease in a population is called the **prevalence**. 
![image](https://user-images.githubusercontent.com/1645304/126883522-16811f59-d4fd-4f9a-863e-b02b9d3eeae9.png)

This equation allows us to see accuracy as a weighted average of **sensitivity** and **specificity**:
- The weight associated with the **sensitivity** is the **prevalence**, and 
- The weight associated with the **specificity** is one minus the **prevalence**. 

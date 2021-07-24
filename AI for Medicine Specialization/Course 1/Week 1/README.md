
# Week 1 Disease detection with computer vision

## How to handle class imbalance and small training set
### Image Classification and Class Imbalance
3 Key challenges and techniques to handle them:
- Class Imbalance -> weigthed loss / Resampling
- Multi-Task -> multi-label loss
- Dataset size -> Transfer learning + Data augmentation

### Binary Cross Entropy Loss Function
How to compule BCE loss funciton given the output probablity of a model
| True Label 1 | True Label 0 |
|-|-|
|![image](https://user-images.githubusercontent.com/1645304/126876679-cdbbddb1-771d-471f-9fee-44394a145fdd.png)|![image](https://user-images.githubusercontent.com/1645304/126876734-118b0202-3ee5-4177-a53f-44537318e0e6.png)|

### Impact of Class Imbalance on Loss Calculation
![image](https://user-images.githubusercontent.com/1645304/126876850-12f91c93-b46d-41a6-acf2-2c2b1c912e46.png)
Notice how most of the contribution to the loss is coming from the normal examples, rather than from the mass examples
![image](https://user-images.githubusercontent.com/1645304/126876865-9c8b4422-4dfd-46ad-9a5d-b114e462e9d7.png)

 The solution to the class imbalance problem is to modify the loss function, to weight the normal and the mass classes differently.
 - W_p will be the weight we assign to the positive or to the mass examples, and 
 - w_n to the negative or normal examples. 

|Binary Cross Entropy Loss| Weighted Binary Cross Entropy Loss|
|-|-|
|![image](https://user-images.githubusercontent.com/1645304/126876949-021c83ed-4ef6-4dff-a713-ae53e00e2d6c.png)|![image](https://user-images.githubusercontent.com/1645304/126876935-14cef363-a6e3-41e1-9600-33209fe83c1d.png)|

Weighted loss techinique for tackling imbalanced dataset
![image](https://user-images.githubusercontent.com/1645304/126877025-1b1b2faf-9e5a-4c17-9c8e-10b0cd72ebbb.png)

### Resampling to Achieve Balanced Classes
The basic idea here is to re-sample the dataset such that we have an equal number of normal and mass examples.

Group the techniques and then sample from each group. As a result:
- we may not include all of the normal examples in our re-sample.
- we may have more than one copy of the mass examples in our re-sampled dataset
![image](https://user-images.githubusercontent.com/1645304/126877092-a03b55b4-d366-4c5c-ae9f-279a44aa6e95.png)


### Multi-Task
Instead of the examples having one label, they now have one label for every disease in the example where zero denotes the absence of that disease and one denotes the presence of that disease.
![image](https://user-images.githubusercontent.com/1645304/126877176-a9953b71-1637-48e1-b341-a162a682fd00.png)

### Multi-task Loss, Dataset size, and CNN Architectures
The multi-label loss or the multi-task loss is the sum of the losses over the multiple diseases.
![image](https://user-images.githubusercontent.com/1645304/126877240-3e29ccb1-92cb-4ed7-9649-5bcde11450fb.png)

We can apply the weighted loss where the weight for the positive label associated with that particular class and the negative label associated with that particular tasks such that for mass

![image](https://user-images.githubusercontent.com/1645304/126877251-80a4af81-8004-4216-9d95-3b16bbaaf3a5.png)

### Working with a Small Training Set
Transfer learning
![image](https://user-images.githubusercontent.com/1645304/126877373-35f6bd27-78b4-4715-ac96-41653d82cf02.png)

The early layer might learn about the edges of an object, and this might be useful for chest X-ray interpretation later. But the later layers, might learn how to identify the head of a penguin and may not be useful for chest X-ray interpretation.
![image](https://user-images.githubusercontent.com/1645304/126877420-de311e6b-7a7b-4b81-8522-ff1abce42d2b.png)

During fine tuning on X-ray images we can freeze the features learned by the shallow layers and just fine-tune the deeper layers.

### Generating More Samples
We can rotate it and pass it in, or we can translate it sideways and pass it in, or we can zoom in, or we can change the brightness or contrast, or apply a combination of these transformation.

Two questions drive the choice of transformations we pick:
1. whether we believe the transformation reflects variations that will help the model generalize the test set and therefore the real world scenarios.
2. verify that our transformation keeps the label the same. e.g. flipping an X-ray does not make sense as the heart will become on the right side

## Check how well your model performs
### Model Testing
![image](https://user-images.githubusercontent.com/1645304/126877596-174f5980-1c1f-4722-a2a3-f627581ccf8c.png)

Challenges with building these sets in the context of medicine:
- **Patient overlap**: how we make these test sets independent, 
- **Set sampling**: how we sample them, 
- **Ground truth**: how we set the ground truth. 

### Splitting data by patient
|Split by image| Split by patient|
|-|-|
|images are randomly split over the sets|all patient images are in one set|
|![image](https://user-images.githubusercontent.com/1645304/126877753-4c42c1ff-0998-4482-ac49-3c5108f6893a.png)|![image](https://user-images.githubusercontent.com/1645304/126877798-cb673dd5-526b-46bc-bc6c-5afe03e4f5cb.png)|

### Sampling
Problem: we might not sample any examples where the label for mass is 1. Thus, we would have no way to actually test the performance of the model on these positive cases.
Solution: One way that this is tackled when creating test sets is to sample a test set such that we have at least X% (e.g. 50%) of examples of our minority class.
![image](https://user-images.githubusercontent.com/1645304/126877876-b12c4801-d8d6-4269-90d6-eda8c74f316f.png)


Because we want our validation set to reflect the distribution in the test set, typically, the same sampling strategy is used. 

### Ground Truth and Consensus Voting
One major question in testing a model is how we determine the correct label for an example.

**inter-observer disagreement**: On a chest X-ray, differentiating between some diseases might be complex. We might have one expert say this is pneumonia, another experts say it's another disease.

### Additional Medical Testing
For example, to determine whether a patient has a mass using a chest x-ray, a more definitive test that can be performed is a CT scan. The CT scan shows the 3D structure of the potential abnormality, thus giving the radiologist more information

### Week 1 Quiz: Disease detection with computer vision
Question 1: Which of the following is not one of the key challenges for AI diagnostic algorithms that is discussed in the lecture?  

- [x] Inflexible models
- [ ] Multiple tasks
- [ ] Class imbalance
- [ ] Dataset size

Question 2: You find that your training set has 70% negative examples and 30% positive. Which of the following techniques **will NOT help** for training this imbalanced dataset?  

- [ ] Oversampling positive examples 
- [ ] Undersampling negative examples 
- [ ] Reweighting examples in training loss 
- [x] Oversampling negative examples 

Question 3: What is the total loss from the normal (non-mass) examples in this example dataset? 

Please use the natural logarithm in your calculation.  When you use numpy.log, this is using the natural logarithm.  Also, to get the total loss, please add up the losses from each ‘normal’ example. 

|Example|	P(positive)| loss |
|-|-|-|
|P1 Normal| 	0.6 |-log (1-0.6)|
|P3 Normal| 	0.3 |-log (1-0.3)|
|P5 Mass| 	0.4 |-log (0.4)|

- [ ] 2.19
- [ ] 0.00
- [ ] -0.4
- [x] 1.27 

Correct
Since these are negative examples, the losses will be  -log(1-P(positive)). 
For P1, -log(1-0.6) = 0.91. 
For P3 -log(1-0.3) = 0.36. 
The sum is 0.91 + 0.36 = 1.27.


Question 4: What is the typical size of medical image dataset? 

- [ ] ~ 1 hundred to 1 thousand images
- [x] ~1 to 1 hundred images
- [ ] ~1 million or more  images
- [ ] ~10 thousand to 100 thousand  images

Question 5: Which of the following data augmentations would be best to apply?
- [x] flip left right
- [ ] flip up down
- [ ] rotate
- [ ] None of the above
<span style="color:red">
Incorrect
If you flip a chest x-ray image along the vertical axis, you might not preserve the original label of the image.  For example, the heart is no longer on the patient’s left side, which is a medical condition called Dextrocardia.
</span>

Question 6: Which of the following are valid methods for determining ground truth?  Choose all that apply.

- [x] Consensus voting from a board of doctors
- [x] Confirmation by CT scan
- [x] Biopsy

Question 7: In what order should the training, validation, and test sets be sampled?  

- [x] Test, Validation, Training
- [ ] Validation, Training, Test
- [ ] Training, Validation, Test
- [ ] Validation, Test, Training

Question 8: Why is it bad to have the same patients in both training and test sets?

- [x] Overly optimistic test performance
- [ ] Leaves too few images for the training set
- [ ] Leaves too few images for the test set 
- [ ] None of these above

Question 9: Let’s say you have a relatively small training set (~5 thousand images). Which training strategy makes the most sense?   

- [x] Retraining the last layer of a pre-trained model
- [ ] Train a model with randomly initialized weights
- [ ] Retraining all layers of a pre-trained model
- [ ] Retraining the first layer of a pre-trained model

Question 10: Now let’s say you have a very large dataset (~1 million images). Which training strategies will make the most sense?

- [x] Retraining all layers of a pretrained model
- [ ] Retraining the first layer of a pretrained model
- [ ] Retraining the last layer of a pretrained model
- [x] Training a model with randomly initialized weights.


# Week 3 Medical Image Segmentation

## Explore MRI data

## Image Segmentation

### MRI Data and Image Registration
MRI Exmaple consists of multiple imaging sequences
![image](https://user-images.githubusercontent.com/1645304/132103205-ce1213c1-fe47-4ac4-b65a-43bf7f558d21.png)

We can combine these multiple 3D volumes into one 3D volume by picking a slice through the brain. This is a slice through the brain viewed on three different MRI sequences:
![image](https://user-images.githubusercontent.com/1645304/132103227-273ff606-8379-41cb-8f61-b110fb7b10ab.png)
The key idea to combine the information from different sequences is to treat them as different channels (red, green, blue)

One challenge with combining these sequences is that they may not be aligned with each other (e.g. patient moves between sequences)
|Misaligned|Aligned|
|-|-|
|![image](https://user-images.githubusercontent.com/1645304/132103305-6dfc82f0-8386-4930-a337-d7c3d3c9d81f.png)|![image](https://user-images.githubusercontent.com/1645304/132103311-3643993e-467a-4edc-a211-56672440f188.png)|

A preprocessing approach used to fix this is to transform the images so that they're aligned or registered to each other. This is called **Image Registration**.

### Segmentation
Segmentation is the process of defining the boundaries of various tissues. In this case, we're trying to define the boundaries of tumors.
We can also think of segmentation as the task of determining the class of every point in the 3D volume. These points in 2D space are called pixels and in 3D space are called voxels

#### 2D Segmentation approach
We break up the 3D MRI volume into many 2D slices. Each one of these slices is passed into a segmentation model which outputs the segmentation for that slice. The 2D slices can then be combined once again to form the 3D output volume of the segmentation.

![image](https://user-images.githubusercontent.com/1645304/132103552-db1bb336-4430-4ca1-9ac0-4eff0478e8f1.png)

The drawback with this 2D approach is that we might lose important 3D context. For instance, if there is a tumor in one slice, there is likely to be a tumor in the slices right adjacent to it. Since we're passing in slices one at a time into the network, the network is not able to learn this useful context. 

#### 3D Segmentation approach
The size of the MRI volume makes it impossible to pass it in all at once into the model (due to the required memory and computation).
Instead, we break up the 3D MRI volume into many 3D sub volumes, each has some width, height, and depth context. Then like in the 2D approach, we can feed in the sub volumes now one at a time into the model and then aggregate them at the end to form a segmentation map for the whole volume.

The 3D approach capture some context in all of the width, height, and depth mentions but has similar drawback as the 2D approach.

The disadvantage with this 3D approach is that we might still lose important spatial cortex. For instance, if there is a tumor in one sub volume, there is likely to be a tumor in the sub volumes around it too. Since we're passing in sub volumes one at a time into the network, the network will not be able to learn this possibly useful context.

### 2D U-Net and 3D U-Net
#### Segmentation Architecture for 2D architectures
![image](https://user-images.githubusercontent.com/1645304/132104488-3f5e219c-3c34-4761-8059-55339604f816.png)

#### Segmentation Architecture for 3D architectures
The 2D convolutions become 3D convolutions, and the 2D pooling layers become 3D pooling layers
![image](https://user-images.githubusercontent.com/1645304/132104521-ac96ff6d-f340-4121-a06e-050e4ec5ce13.png)

#### More about U-Net
- For a brief video introduction to U-Net by the original creators, Olaf Ronneberger, Philipp Fischer, Thomas Brox, please visit their site [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/).
- If you would like more detail, start with this blog post by [Heet Sankesara “UNet”](https://towardsdatascience.com/u-net-b229b32b4a71).  
- To go deeper, you can read the original research paper [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/pdf/1505.04597.pdf) by Olaf Ronneberger, Philipp Fischer, Thomas Brox

As a reminder, you will be using a pre-trained U-Net model, and so you can still complete this course without knowing the specific details of implementing the U-Net from scratch.

### Data augmentation for segmentation
One key difference with data augmentation during segmentation is we now have a segmentation output. When we rotate an input image by 90 degrees to produce a transformed input. We also need to rotate the output segmentations by 90 degrees to get our transformed output segmentation. The second difference is that we now have 3D volumes instead of 2D images. So the transformations have to apply to the whole 3D volume.

### Loss function for image segmentation
![image](https://user-images.githubusercontent.com/1645304/132105378-8e742edb-c380-411b-89e7-59aefca4da85.png)

#### Soft Dice Loss
The soft dice loss will measure the error between our prediction map, P, and our ground truth map, G.


![image](https://user-images.githubusercontent.com/1645304/132105447-89d73171-b787-4cc6-91b9-563b3d1f94cf.png)

- The numerator measures the overlap between the predictions and the ground truth, and we want this fraction to be large. Here, when G over here is equal to 1, then we want P to be close to 1. 
- We also want the denominator to be small. So when G equals 0, we want P to be close to 0 otherwise, this term would be large and the denominator would be large. 
- Then we take 1 minus this fraction, such that a higher loss corresponds to a small overlap and a low loss corresponds to a high overlap.

The advantage of the soft dice loss is that it works well in the presence of imbalanced data. This is especially important in our task of brain tumor segmentation, when a very small fraction of the brain will be tumor regions.

![image](https://user-images.githubusercontent.com/1645304/132105481-61dbaf94-6b39-4432-a948-ab8d98b3d32f.png)

We can plug in these values into the soft dice loss for this particular example as 1- 2 times 2.2/2.47 + 3, which is 1- 4.4/5.47. And this comes out to approximately 0.2, which is the loss with this particular prediction, and with this particular ground truth, for this example.

## Practical considerations

### Different Populations and Diagnostic Technology
Challenges and opportunities to make these systems part of routine medical practice.

One of the main challenges with applying AI algorithms in the clinic, is achieving reliable generalization due to vary of reasons:

- Let's say we developed our chest x-ray model on US data and want to deploy somewhere else. In India, the patient population might have x-rays that looked different than what the model has been trained on. As a very concrete example, **tuberculosis** is quite prevalent in India, but unlikely to be as prevalent in the hospitals where we've trained our model in the US.
- Let's say we've been able to measure the model performance on data collected from a few countries over a few years, but MRI technology is not standard across the globe and across time. The latest scanners have much higher **resolution** than older scanners. Before we apply the segmentation model in a new hospital, we'd want to make sure that the model is able to generalize to the resolution of the scanner at the hospital.

### External validation
To be able to measure the generalization of a model on a population that it hasn't seen, we want to be able to evaluate on a test set from the new population. This is called external validation. External validation can be contrasted with internal validation, when the test set is drawn from the same distribution as the training set for the model.
![image](https://user-images.githubusercontent.com/1645304/132105676-0b436e26-4b13-44c8-8641-5b99b93eebf0.png)

If we find that we're not generalizing to the new population, then we could get a few more samples from the new population to create a small training and validation set and then fine-tune the model on this new data.
![image](https://user-images.githubusercontent.com/1645304/132105706-b2112166-5a75-455a-b103-cbd76ae7ab4f.png)

In retrospective data, there are often steps taken to process and clean the data, but in the real-world, the model has to work with the raw data. For example, the traineing data set on has been filtered to only include frontal x-rays, where the x-ray is taken from the front or the back of the patient. However, in the real-world, it is also common to take a fraction of the x-rays from the side of the patient. These are called lateral x-rays.
![image](https://user-images.githubusercontent.com/1645304/132105760-ed8270b1-92f6-4e7d-99c3-4a860fdc80c5.png)

### Measuring Patient outcomes
Another challenge for the real-world deployment of AI models is that we need metrics to reflect clinical application.

- One approach to this challenge includes **decision curve analysis**, which can help quantify the net benefit of using a model to guide patient care.
- Another approach is to see what happens in the setting of a **randomized control trial** where we compare patient outcomes for patients on whom the AI algorithm is applied versus those on whom the AI algorithm is not applied.

In the real world, we would want to analyze the effect of the model not just overall, but also on subgroups of the population. This would include patients of different ages, sex, and socioeconomic status. This allows us to find key algorithmic blind spots or unintended biases.

For example, skin cancer classifiers that can achieve a performance level comparable to dermatologists when used on light skin patients have previously underperformed on images of darker skin tones.
![image](https://user-images.githubusercontent.com/1645304/132105909-50b91a45-c78b-4884-aa65-b3f178b1369c.png)


Finally one of the major challenges and opportunities to applying AI medical models in the real world is achieving a better understanding of how these algorithms will interact with the decision-making of clinicians. It is difficult and often impossible to understand the inner workings of models to understand how and why they make a certain decision.

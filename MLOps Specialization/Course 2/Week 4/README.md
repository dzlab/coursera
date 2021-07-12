## Week 4 (Optional): Advanced Labeling, Augmentation and Data Preprocessing
### Advanced Labeling
- Semi-supervised learning:
  - Applies the best of supervised and unsupervised approaches
  - Using a small amount of labeled data boosts model accuracy
  - Example: Label propagation algorithm based on similarity or community structure
- Active learning:
  - Selects the most important examples to label
  - Improves predicted accuracy
  - Examples:
    - Margin sampling: label points the current model is least confident in
    - Cluster-based sampling: sample from well-formed clusters to cover the entire space
    - Query-by-committee: train an ensemble of models and sample points that generate disagreement
    - Region-based sampling: runs several active learning algorithms in different partitions of the space 
- Weak supervision:
  - Uses heuristics to apply noisy labels to unlabeled examples
  - Snorkel is handy framework for weak supervision
  
#### PRACTICE QUIZ - Advanced Labelling

Question 1: What is weak supervision useful for?

- Taking advantage of input from experts in the field. x
- Managing training datasets by hand labeling.
- Creating and structuring training datasets through programming. x

Question 2: Which of the following statements about labeling techniues is true?

- Active Learning shouldn’t be used on imbalanced datasets
- Label propagation is a technique used in semi-supervised algorithms based on the similarity of different data points. x
- Active Learning doesn’t require the feedback from a ML model to select the next data points to label.
- Direct Labeling is slow and expensive compared to other labeling techniques

Question 3: Weak Supervision is one of the methods used in production ML to label data. Which of the following statements are true about it?

- It uses generative models to determine weights for supervision sources x
- Weak Supervision is more expensive than Human Labeling.
- Weak supervision allows sampling data intelligently for labeling
- Weak supervision uses heuristics or labelling functions instead of deterministic labels. x

### Data Augmentation
- It generates artificial data by creating new examples which are variants of the original data
- It increases the diversity and number of examples in the training data
- Provides means to improves accuracy, generalization, and avoiding overfitting
- Example on CIFAR-10 dataset
```python
def augment(x, height, width, num_channels):
  x = tf.image.resize_with_crop_or_pad(x, height + 8, width + 8)
  x = tf.image.random_crop(x, [height, width, num_channels])
  x = tf.image.random_flip_left_right(x)
  return x
```
- Advances techniques:
  - Semi-supervised data augmentation, e.g. UDA, semi-supervised learning with GANs
  - Policy-based data augmentation, e.g. AutoAugment
  
#### PRACTICE QUIZ - Data Augmentation
Question 1: Which of the following statements are true on data augmentation? (Check all that apply).

- Data Augmentation should be applied at serving time.
- tf.image offers a set of functions to augment image data. x
- Data Augmentation always helps improving the performance of ML models.

Question 2: Data augmentation is a strategy to significantly increase the data set available for training models without having to collect new data.

- Yes x
- No

Question 3: Data augmentation is a technique that allows us to increase our training data set to improve accuracy and avoid overfitting.

- True x
- False

### Preprocessing Different Data Types
TF Transform examples

#### Week 4 Optional References
Week 4: Advanced Labeling, Augmentation and Data Preprocessing
This is a compilation of resources including URLs and papers appearing in lecture videos.

- Hand Labeling https://twitter.com/jeffdean/status/1106325994913189888?lang=en
- Weak supervision https://dawn.cs.stanford.edu/2017/07/16/weak-supervision/
- Snorkel https://www.snorkel.org/
- How do you get more data? https://ai.googleblog.com/2018/06/improving-deep-learning-performance.html
- Advanced Techniques https://github.com/google-research/uda
- Images in tensorflow https://www.tensorflow.org/lite/models/image_classification/overview
- CIFAR-10
1. https://www.cs.toronto.edu/~kriz/cifar.html
2. https://www.tensorflow.org/datasets/catalog/cifar10
- Weather dataset https://www.bgc-jena.mpg.de/wetter/
- Human Activity Recognition https://www.cis.fordham.edu/wisdm/dataset.php

Papers

- Label Propagation: Iscen, A., Tolias, G., Avrithis, Y., & Chum, O. (2019). Label propagation for deep semi-supervised learning. https://arxiv.org/pdf/1904.04717.pdf

#### PRACTICE QUIZ - Different Data Types

Question 1: Visualizing an audio signal in the time domain usually reveals very little information on its spectral content. Which graphical representation displays the amplitude changes for each frequency as a function of time?

- Short-Time Fourier Transform.
- Spectrogram. x
- librosa
- Feature normalization

Question 2: What would be a striking caveat or shortcoming of interpreting a video just as a series of images? 

- Considering that all subsequent frames are correlated.
- Unnecessarily increasing the dimensionality of the dataset.
- Hindering classifier accuracy.
- Losing the semantic context coming from the sequence of events. x

Question 3: In the analysis of the weather time series data set you saw that the samples were acquired at a rate of 6 samples per hour. You also know that weather changes typically occur on a much slower time scale. What is a valid sampling strategy to make predictions into the future for this specific case?

- Omitting samples.
- Windowing and omitting samples. x
- Use one sample at a time to make predictions.
- Upsampling by interpolation.

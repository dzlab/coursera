## Week 2

Selecting and Training a Model

## Quiz: Selecting and Training a Model
Question 1
Which of these is a more accurate description of a data-centric approach to ML development?
- [ ] Holding the training data fixed, work to improve your neural network’s architecture to do well on the problem.
- [x] Holding the neural network architecture fixed, work to improve the data to do well on the problem.

Question 2
Say you have an algorithm that diagnoses illnesses from medical X-rays, and achieves high average test set accuracy. What can you now say with high confidence about this algorithm? Check all that apply. 
- [ ] It does well even on rare classes of diseases. 
- [ ] Its diagnoses are roughly equally accurate on all genders and ethnicities, so we are confident it is not biased against any gender or ethnicity.
- [ ] The system can be safely deployed in a healthcare setting. 
- [x] None of the above.

Question 3
Which of these statements about establishing a baseline are accurate? Check all that apply.
- [ ] Open-source software should not be used to establish a baseline, since the performance of a good open source implementation might be too good and thus too hard to beat. 
- [x] It can be established based on an older ML system
- [x] For unstructured data problems, using human-level performance as the baseline can give an estimate of the irreducible error/Bayes error and what performance is reasonable to achieve.
- [x] Human level performance (HLP) is generally more effective for establishing a baseline on unstructured data problems (such as images and audio) than structured data problems

Question 4
On a speech recognition problem, say you run the sanity-check test of trying to overfit a single training example. You pick a clearly articulated clip of someone saying “Today’s weather”, and the algorithm fails to fit even this single audio clip, and outputs “______”. What should you do?

- [ ] Create a training set of this example repeated 100 times to force the algorithm to learn to fit this example well.
- [ ] Train the algorithm on a larger dataset to help it to fit the data better.
- [ ] Use data augmentation on this one audio clip to make sure the algorithm hears a variety of examples of “today’s weather” to fit this phrase better.
- [x] Debug the code/algorithm/hyperparameters to make it pass this sanity-check test first, before moving to larger datasets.

> No, your algorithm should be able to overfit to a single training example. If it's unable to do so, there must be an error in the implementation. First debug the error, then add more data! 

## References
Week 2: Select and Train Model
If you wish to dive more deeply into the topics covered this week, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Establishing a baseline - https://blog.ml.cmu.edu/2020/08/31/3-baselines/
- Error analysis - https://techcommunity.microsoft.com/t5/azure-ai/responsible-machine-learning-with-error-analysis/ba-p/2141774
- Experiment tracking - https://neptune.ai/blog/ml-experiment-tracking

## Papers
- Brundage, M., Avin, S., Wang, J., Belfield, H., Krueger, G., Hadfield, G., … Anderljung, M. (n.d.). Toward trustworthy AI development: Mechanisms for supporting verifiable claims∗. Retrieved May 7, 2021http://arxiv.org/abs/2004.07213v2
- Nakkiran, P., Kaplun, G., Bansal, Y., Yang, T., Barak, B., & Sutskever, I. (2019). Deep double descent: Where bigger models and more data hurt. Retrieved from http://arxiv.org/abs/1912.02292

## Quiz Modeling challenges
Question 1
You are working on a binary classification ML algorithm that detects whether a patient has a specific disease. In your dataset, 98% of the training examples (patients) don’t have the disease, so the dataset is very skewed. Accuracy on both positive and negative classes is important. You read a research paper claiming to have developed a system that achieves 95% on ____ metric. What metric would give you the most confidence they’ve built a useful and non-trivial system? (Select one) 

- [ ] Accuracy
- [x] F1 score
- [ ] Recall
- [ ] Precision

Question 2
On the previous problem above with 98% positive examples, if your algorithm is print(“1”) (i.e., it says everyone has the disease). Which of these statements is true?

- [ ] The algorithm achieves 0% precision.
- [x] The algorithm achieves 100% recall.
- [ ] The algorithm achieves 100% precision.
- [ ] The algorithm achieves 0% recall.

> precision is the number of True Positives / (True Positives + False Positives).
> Remember, recall is the number of True Positives / (True Positives + False Negatives).

Question 3
True or False? During error analysis, each example should only be assigned one tag. For example, in a speech recognition application you may have the tags: “car noise”, “people noise” and “low bandwidth”. If you encounter an example with both car noise and low bandwidth audio, you should use your judgement to assign just one of these two tags rather than apply both tags. 
- [x] False
- [ ] True

>  You can have as many tags as you want when you do error analysis. Having an accurate understanding of where your errors are coming from is an important part of error analysis, and necessary to identify where there is room for improvement and prioritize solutions.

Question 4
You are building a visual inspection system. Error analysis finds:

Type of defect	Accuracy	HLP	% of data
Scratch	95%	98%	50% 
Discoloration	90%	90%	50% 
Based on this, what is the more promising type of defect to work on?

- [ ] Discoloration, because the algorithm’s accuracy is lower and thus there’s more room for improvement.
- [ ] Discoloration, because HLP is lower which suggests this is therefore the harder problem that thus needs more attention.
- [x] Scratch defects, because the gap to HLP is higher and thus there’s more room for improvement.
- [ ] Work on both classes equally because they are each 50% of the data. 

5. Question 5
You’re considering applying data augmentation to a phone visual inspection problem. Which of the following statements are true about data augmentation? (Select all that apply)


- [ ] Data augmentation should distort the input sufficiently to make sure they are hard to classify by humans as well. 
- [x] GANs can be used for data augmentation.
- [ ] Data augmentation should try to generate more examples in the parts of the input space where the algorithm is already doing well and there’s no need for improvement.
- [x] Data augmentation should try to generate more examples in the parts of the input space where you’d like to see improvement in the algorithm’s performance.


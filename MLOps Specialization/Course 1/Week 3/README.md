## Week 3: Data Definition and Baseline
If you wish to dive more deeply into the topics covered this week, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Label ambiguity https://csgaobb.github.io/Projects/DLDL.html
- Data pipelines https://cs230.stanford.edu/blog/datapipeline/#best-practices
- Data lineage https://blog.tensorflow.org/2021/01/ml-metadata-version-control-for-ml.html
- MLops https://cloud.google.com/blog/products/ai-machine-learning/key-requirements-for-an-mlops-foundation

Geirhos, R., Janssen, D. H. J., Schutt, H. H., Rauber, J., Bethge, M., & Wichmann, F. A. (n.d.). Comparing deep neural networks against humans: object recognition when the signal gets weaker∗. Retrieved May 7, 2021, from Arxiv.org website: https://arxiv.org/pdf/1706.06969.pdf


## Quiz: Data Definition and Baseline

Question 1
Which of these statements do you agree with regarding structured vs. unstructured data problems?
- [ ] It is generally easier for humans to label data and to apply data augmentation on structured data than unstructured data. 
- [ ] It is generally easier for humans to label data on unstructured data, and easier to apply data augmentation on structured data.
- [ ] It is generally easier for humans to label data on structured data, and easier to apply data augmentation on unstructured data.
- [x] It is generally easier for humans to label data and to apply data augmentation on unstructured data than structured data.


Question 2
Take speech recognition. Some labelers transcribe with “...” (as in, “Um… today’s weather”) whereas others do so with commas “,”. Human-level performance (HLP) is measured according to how well one transcriber agrees with another. You work with the team and get everyone to consistently use commas “,”. What effect will this have on HLP?

- [ ] HLP will decrease.
- [ ] HLP will stay the same.
- [x] HLP will increase.

Question 3
Take a phone visual inspection problem. Suppose even a human inspector looking at an image cannot tell if there is a scratch. If however the same inspector were to look at the phone directly (rather than an image of the phone) then they can clearly tell if there is a scratch. Your goal is to build a system that gives accurate inspection decisions for the factory (not publish a paper). What would you do?

- [ ] Get a big dataset of many training examples, since this is a challenging problem that will require a big dataset to do well on. 
- [x] Try to improve their imaging (camera/lighting) system to improve the quality or clarity of the input images x.
- [ ] Try to improve the consistency of the labels, y.
- [ ] Carefully measure HLP on this problem (which will be low) to make sure the algorithm can match HLP.

Question 4
You are building a system to detect cats. You ask labelers to please “use bounding boxes to indicate the position of cats.” Different labelers label as follows:
What is the most likely cause of this?

- [ ] Labelers have not had enough coffee. 
- [ ] Lazy labelers. 
- [ ] That this should have been posed as a segmentation rather than a detection task. 
- [x] Ambiguous labeling instructions.

Question 5
You are building a visual inspection system. HLP is measured according to how well one inspector agrees with another. Error analysis finds:
It might be worth checking for label consistency on both scratch and discoloration defects. But if you had to pick one to start with, which would you pick?

- [x] It is more promising to check (and potentially improve) label consistency on discoloration defects than scratch defects, since HLP is lower on discoloration and thus there’s more room for improvement.
- [ ] It is more promising to check (and potentially improve) label consistency on scratch defects than discoloration defects, since HLP is higher on scratch defects and thus it’s more reasonable to expect high consistency.

Question 6
To implement the data iteration loop effectively, the key is to take all the time that’s needed to construct the right dataset first, so that all development can be done on that dataset without needing to spend time to update the data.

- [ ] True
- [x] False

Question 7
You have a data pipeline for product recommendations that (i) cleans data by removing duplicate entries and spam, (ii) makes predictions. An engineering team improves the system used for step (i). If the trained model for step (ii) remains the same, what can we confidently conclude about the performance of the overall system?

- [ ] It's not possible to say - it may perform better or worse.
- [x] It will get worse because stage (ii) is now experiencing data/concept drift.
- [ ] It will definitely improve since the data is now more clean.
- [ ] It will get worse because changing an earlier stage in a data pipeline always results in worse performance of the later stages.

Question 8
What is the primary goal of building a PoC (proof of concept) system?

- [ ] To build a robust deployment system.
- [ ] To collect sufficient data to build a robusts system for deployment.
- [ ] To select the most appropriate ML architecture for a task.
- [x] To check feasibility and help decide if an application is workable and worth deploying.

Question 9
MLOps tools can store meta-data to keep track of data provenance and lineage. What do the terms data provenance and lineage mean?
 
- [x] Data provenance refers to where the data comes from, and data lineage the sequence of processing steps applied to it.
- [ ] Data provenance refers to the sequence of processing steps applied to a dataset, and data lineage refers to where the data comes from.
- [ ] Data provenance refers data pipeline, and data lineage refers to the age of the data (i.e., how recently was it collected).
- [ ] Data provenance refers the input x, and data lineage refers to the output y.

Question 10
You are working on phone visual inspection, where the task is to use an input image, x, to classify defects, y. You have stored meta-data for your entire ML system, such as which the factory each image came from. Which of the following are reasonable uses of meta-data?

- [ ] As an alternative to having to comment your code.
- [ ] As another input provided to human labelers (in addition to the image x) to boost HLP.
- [x] Keeping track of data provenance and lineage.
- [x] To suggest tags or to generate insights during error analysis.



### PRACTICE QUIZ
Practice Quiz • 10 MIN10 minutes
Scoping (optional)

Question 1
In the project scoping process, which of these is the first step?

- [x] Identify business problems
- [ ] Determine milestones
- [ ] Budget for resources
- [ ] Identify AI solutions

Question 2
You are considering building a speech recognition system, where the innovation is to use a very low cost microphone that has just been newly invented. Suppose that a human, given an audio clip recorded from this new microphone, often cannot tell what was said (because the microphone has too much noise). What can you conclude from this? 

- [ ] This problem is technically feasible only if a human listening to the original sound with their own ears (not through the microphone system) can decipher what was said.
- [ ] We should get multiple labelers to transcribe each audio clip, to reduce noise.
- [x] There is a high chance it will not be technically feasible for a learning algorithm to achieve high accuracy on this task.
- [ ] This problem will be technically feasible only if we can acquire significantly more data than a human will hear in their lifetime.

Question 3
You are considering building a product recommendation system. You carried out diligence on feasibility (the ability to give relevant recommendations), but not diligence on value. Which of these is the biggest risk for what could go wrong? 

- [x] You build the system and it gives relevant recommendations, but the system does not meaningfully improve key business metrics such as sales conversions or revenue.
- [ ] Human-level performance for giving relevant recommendations is discovered to be too low for your project. 
- [ ] You build the system and it fails to give relevant recommendations.
- [ ] Even though the system gives poor recommendations, it still has a meaningful impact on the business metrics (such as sales conversions or revenue); but it is impossible to credit these gains to the ML system.

Question 4
Which of these statements is the most accurate?

- [x] There is often a gap between MLE metrics (such as accuracy) and business metrics (such as revenue), and it is useful to try to have the teams compromise and agree on a middle ground that both teams are happy with.
- [ ] A business team should be working alongside an MLE to optimize only the metrics that ML algorithms can, such as accuracy, without worrying about unrealistic metrics to optimize such as revenue. 
- [ ] An AI team should be directly responsible for optimizing business metrics (such as revenue).
- [ ] So long as a project does well on MLE metrics (such as accuracy), it will be accepted by the business team.

Question 5
You’ve completed this optional section, when really you didn’t have to. Andrew thinks this means you are (please check all, because all apply):

- [x] Awesome
- [x] Fantastic
- [x] Great
- [x] Wonderful

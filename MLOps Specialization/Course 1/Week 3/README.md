## Week 3: Data Definition and Baseline
If you wish to dive more deeply into the topics covered this week, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

- Label ambiguity https://csgaobb.github.io/Projects/DLDL.html
- Data pipelines https://cs230.stanford.edu/blog/datapipeline/#best-practices
- Data lineage https://blog.tensorflow.org/2021/01/ml-metadata-version-control-for-ml.html
- MLops https://cloud.google.com/blog/products/ai-machine-learning/key-requirements-for-an-mlops-foundation

Geirhos, R., Janssen, D. H. J., Schutt, H. H., Rauber, J., Bethge, M., & Wichmann, F. A. (n.d.). Comparing deep neural networks against humans: object recognition when the signal gets weaker∗. Retrieved May 7, 2021, from Arxiv.org website: https://arxiv.org/pdf/1706.06969.pdf


### PRACTICE QUIZ
Practice Quiz • 10 MIN10 minutes
Scoping (optional)

Question 1
In the project scoping process, which of these is the first step?

- Identify business problems x
- Determine milestones
- Budget for resources
- Identify AI solutions

Question 2
You are considering building a speech recognition system, where the innovation is to use a very low cost microphone that has just been newly invented. Suppose that a human, given an audio clip recorded from this new microphone, often cannot tell what was said (because the microphone has too much noise). What can you conclude from this? 

- This problem is technically feasible only if a human listening to the original sound with their own ears (not through the microphone system) can decipher what was said.
- We should get multiple labelers to transcribe each audio clip, to reduce noise.
- There is a high chance it will not be technically feasible for a learning algorithm to achieve high accuracy on this task. x
- This problem will be technically feasible only if we can acquire significantly more data than a human will hear in their lifetime.

Question 3
You are considering building a product recommendation system. You carried out diligence on feasibility (the ability to give relevant recommendations), but not diligence on value. Which of these is the biggest risk for what could go wrong? 

- You build the system and it gives relevant recommendations, but the system does not meaningfully improve key business metrics such as sales conversions or revenue. x
- Human-level performance for giving relevant recommendations is discovered to be too low for your project. 
- You build the system and it fails to give relevant recommendations.
- Even though the system gives poor recommendations, it still has a meaningful impact on the business metrics (such as sales conversions or revenue); but it is impossible to credit these gains to the ML system.

Question 4
Which of these statements is the most accurate?

- There is often a gap between MLE metrics (such as accuracy) and business metrics (such as revenue), and it is useful to try to have the teams compromise and agree on a middle ground that both teams are happy with. x
- A business team should be working alongside an MLE to optimize only the metrics that ML algorithms can, such as accuracy, without worrying about unrealistic metrics to optimize such as revenue. 
- An AI team should be directly responsible for optimizing business metrics (such as revenue).
- So long as a project does well on MLE metrics (such as accuracy), it will be accepted by the business team.

Question 5
You’ve completed this optional section, when really you didn’t have to. Andrew thinks this means you are (please check all, because all apply):

- Awesome x
- Fantastic x
- Great x
- Wonderful x

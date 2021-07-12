## Week 1

The Machine Learning Project Lifecycle

Question 1
Which of these are stages of the machine learning project lifecycle? Check all that apply.

- [x] Deployment
- [x] Modeling
- [x] Scoping
- [ ] Data
- [ ] Configuration

Question 2
Which of these is not an advantage of a typical edge deployment compared to a typical cloud deployment?
- [ ] Lower latency
- [ ] Can function even if network connection is down
- [x] More computational power available
- [ ] Less network bandwidth needed

Question 3
In the speech recognition example, what is the problem with some labelers transcribing audio as “Um, today’s weather” and others transcribing “Umm..., today’s weather”?
- [ ] The second is grammatically incorrect and we should use the first transcription. 
- [x] Either transcription is okay, but the inconsistency is problematic.
- [ ] We should not be transcribing “Umm.” The correct transcription, which serves the user's needs better, is just “Today’s weather.
- [ ] The first is grammatically incorrect and we should use the second transcription.

Question 4
After a system is deployed, monitoring and maintaining the system will help us handle any cases of concept drift or data drift.
- [ ] False
- [x] True


Question 5
Which statement is a more accurate description of the full cycle of a machine learning project?
- [ ] It is a linear process, in which we move step-by-step from scoping to deployment. (That’s why we call it a cycle. Bicycles are only good at going forward, not backward.)
- [x] It is an iterative process, where during a later stage we might go back to an earlier stage. (That’s why we call it a cycle--it’s a circular process.)


Week 1: Overview of the ML Lifecycle and Deployment
If you wish to dive more deeply into the topics covered this week, feel free to check out these optional references. You won’t have to read these to complete this week’s practice quizzes.

Concept and Data Drift https://towardsdatascience.com/machine-learning-in-production-why-you-should-care-about-data-and-concept-drift-d96d0bc907fb

Monitoring ML Models https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/

A Chat with Andrew on MLOps: From Model-centric to Data-centric https://youtu.be/06-AZXmwHjo

Papers

Konstantinos, Katsiapis, Karmarkar, A., Altay, A., Zaks, A., Polyzotis, N., … Li, Z. (2020). Towards ML Engineering: A brief history of TensorFlow Extended (TFX). http://arxiv.org/abs/2010.02013 

Paleyes, A., Urma, R.-G., & Lawrence, N. D. (2020). Challenges in deploying machine learning: A survey of case studies. http://arxiv.org/abs/2011.09926

Sculley, D., Holt, G., Golovin, D., Davydov, E., & Phillips, T. (n.d.). Hidden technical debt in machine learning systems. Retrieved April 28, 2021, from Nips.c https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf

Deployment - Quiz
Question 1. You’ve built a new system for making loan approval decisions. For now, its output is not used in any decision making process, and a human loan officer is solely responsible for deciding what loans to approve. But the system’s output is logged for analysis. What is this type of deployment called?
- [ ] Red green deployment
- [x] Shadow mode deployment
- [ ] Canary deployment
- [ ] Blue green deployment

Question 2. On a new social media platform, you’re rolling out a new anti-spam system to flag and hide spammy posts. Your team decides to roll out the anti-spam filter via a canary deployment, and roll it out to 1% of users initially. Which of these would you advocate?
- [ ] Monitor that 1% of users’ reaction, and if it goes well, flip the switch to send all traffic (100%) to the system. 
- [ ] After a successful canary deployment, begin to implement a shadow mode deployment. 
- [x] Use a plan to ramp up to more users at a fixed rate: 1% in the first week, 2% in second week, 4% in third, and so on, so that the rollout can be well planned and managed.
- [ ] Monitor that 1% of users’ reaction, and either gradually ramp up (if it’s going well) or rollback (if not) 

Question 3. You’re building a healthcare screening system, where you input a patient’s symptoms, and for the easy cases (such as an obvious case of the common cold) the system will give a recommendation directly, and for the harder cases it will pass the case on to a team of in-house doctors who will form their own diagnosis independently. What degree of automation are you implementing in this example for patient care? 
- [x] Partial Automation
- [ ] Full Automation
- [ ] Human only  
- [ ] Shadow mode 

Question 4. You have built and deployed an anti-spam system that inputs an email and outputs either 0 or 1 based on whether the email is spam. Which of these will result in either concept drift or data drift?
- [x] Spammers trying to change the wording used in emails to get around your spam filter.
- [ ] Cloud computational costs going down, resulting in a lower cost to process each email received.
- [ ] Updating a monitoring dashboard to keep track of new metrics.
- [ ] None of these will result in either concept drift or data drift.

Question 5. Which of these statements is a more accurate description of deployment?
- [x] It is an iterative process, where you should expect to make multiple adjustments (such as metrics monitored using dashboards or percentage of traffic served) to work towards optimizing the system.
- [ ] Because deployment is a high stakes event, it's critical to design the right system, so that immediately after launch it will immediately work reliably and scale effectively.

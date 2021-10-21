# Lab: Running ML Pipelines on Kubeflow

## Overview
In this lab, you learn how to configure and create an AI Platform Pipelines instance. After you configure the AI Platform Pipelines instance, you run an example pipeline and visualize the pipeline graph to see the different metrics, logs, and parameters that are available.

## Objectives
In this lab, you perform the following tasks:

- Create a Kubernetes cluster and configure AI Platform pipelines
- Launch pipelines dashboard
- Create and run an experiment from an example end-to-end ML Pipeline
- Examine and verify the output of each step
- Inspect the pipeline graph, various metrics, logs, charts and parameters

## Task 1. Set up an AI Platform Pipelines instance
In this task, you deploy Kubeflow Pipelines as a Kuberenetes App, which are solutions with simple click to deploy to Google Kubernetes Engine and that have the flexibility to deploy to Kubernetes clusters on-premises or in third-party clouds. You will see Kubeflow Pipelines integrated into your Google Cloud environment as AI Platform Pipelines. If interested, learn more about Kubeflow Pipelines in the documentation during installation steps.

1. From the the Navigation menu, scroll down to AI Platform and pin the section for easier access later in the lab.

![image](https://user-images.githubusercontent.com/1645304/137660373-6e4ee496-ca21-4543-a470-38bea651b61b.png)


2. Click Pipelines.

![image](https://user-images.githubusercontent.com/1645304/137660386-9a52cf9a-db1e-488d-9c09-445050870b66.png)

3. Then click New Instance.

![image](https://user-images.githubusercontent.com/1645304/137660400-beb3e9ce-775c-4cb3-8c16-a68e063af5d0.png)

4. Click Configure.

![image](https://user-images.githubusercontent.com/1645304/137660417-49db631e-ad38-462e-925e-ef44b364410b.png)

5. Check Allow access to the following Cloud APIs, leave the name as is, and then click Create Cluster.

![image](https://user-images.githubusercontent.com/1645304/137660430-16705bd2-8025-40db-9e7c-5a0bdef2a9e3.png)


This should take 2-3 minutes to complete. Wait for the cluster to finish before proceeding to the next step. In the first tab opened, you can view the Cluster Creation taking place in the [GKE section of the Cloud Console](https://console.cloud.google.com/kubernetes/), or see the individual VMs spinning up in the [GCE section of the Cloud Console](https://console.cloud.google.com/compute/).

6. When the cluster creation is complete, check the Terms of Service box, leave other settings unchanged, and then click Deploy. You will see the individual services of KFP deployed to your GKE cluster. Proceed to the next step while installation occurs.

![image](https://user-images.githubusercontent.com/1645304/137660458-9830a949-fa86-4eb6-b68c-6265616a8000.png)

## Task 2. Run an example pipeline
1. In the Google Cloud Console, on the Navigation menu, click **AI Platform > Pipelines**.

You will see the newly created Pipelines instance. If needed, click Refresh to update the page.

2. Click on the **OPEN PIPELINES DASHBOARD** link next to your instance name.

![image](https://user-images.githubusercontent.com/1645304/137660688-326e45be-1465-4d11-961a-ac95a23c5a12.png)


3. On the new page that loads, on the Navigation Menu on the left, click on **Pipelines**.

You will see a list of pipelines that have been provided for demo and tutorial purposes. For this lab, you will use the **[Demo] XGBoost - Iterative model training** sample pipeline. This sample demonstrates continuous training using a train-eval-check recursive loop, in which the model is trained iteratively until the model evaluation metrics are adequate.

![image](https://user-images.githubusercontent.com/1645304/137660709-8cd0816c-8319-446d-a3d8-1df3a8e30bdf.png)

4. Click on the **[Demo] XGBoost - Iterative model training** pipeline.

When it loads, you can see what the graph for this pipeline looks like. Next, you will create a run to test this pipeline.

![image](https://user-images.githubusercontent.com/1645304/137660724-aa196c32-acde-4956-9e03-c47ba2769b8c.png)


5. Click on **Create experiment** on the top right to associate a new experiment for the run.

6. Enter the name **my-first-experiment** in the form that loads, and then click **Next**.

7. Leave the default options, and click **Start** to run the pipeline. The pipeline run may take a few minutes to complete.

You can click **Refresh** to update the page and see the latest status.

8. Once the pipeline run has finished, you can click on the run name to see the fully generated graph as well as performance metrics and graphs.

The green check marks means every part of the pipeline ran successfully. You can click on any box and see the outputs for that part like input/output, visualizations, logs, events, etc.

![image](https://user-images.githubusercontent.com/1645304/137660755-93ce0aab-97dc-4d79-884f-cd6d99ec6107.png)


## Congratulations!
In this lab, you used Kubeflow Pipelines to create and orchestrate an ML pipeline on Cloud AI Platform.

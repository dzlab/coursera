# Invoking Machine Learning APIs

## Enable APIs
Ensure the Cloud Source Repositories API is enabled: https://console.cloud.google.com/apis/library/sourcerepo.googleapis.com/?q=Repositories

## Launch AI Platform Notebooks
To launch AI Platform Notebooks:

### Step 1

Click on the Navigation Menu. Navigate to AI Platform, then to Notebooks.

![image](https://user-images.githubusercontent.com/1645304/142776109-d574d94a-b2f4-462c-a1de-0cc7cea3598d.png)


### Step 2

On the Notebook instances page, click NEW NOTEBOOK. Select TensorFlow Enterprise and choose the latest version of TensorFlow Enterprise 2.6 (with LTS) > Without GPUs.

![image](https://user-images.githubusercontent.com/1645304/142776117-40deb929-036b-427c-890a-eddb41784a88.png)

In the pop-up, confirm the name of the deep learning VM, move to the bottom of the window and click Create.

![image](https://user-images.githubusercontent.com/1645304/142776153-cca6207a-c4e0-4d2b-9d35-c8b9e0348c37.png)

The new VM will take 2-3 minutes to start.

### Step 3

Click Open JupyterLab. A JupyterLab window will open in a new tab.

![image](https://user-images.githubusercontent.com/1645304/142776160-8c8b70f1-b064-4b5a-9b38-a8b9d2666676.png)

## Clone course repo within your AI Platform Notebooks instance
To clone the training-data-analyst notebook in your JupyterLab instance:

1. In JupyterLab, to open a new terminal, click the Terminal icon.

2. At the command-line prompt, run the following command:
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

3. To confirm that you have cloned the repository, double-click on the training-data-analyst directory and ensure that you can see its contents. The files for all the Jupyter notebook-based labs throughout this course are available in this directory.

## Enable APIs and Get API key
To get an API key:

### Step 1

From the GCP console menu, select APIs and services and select Library.

### Step 2

In the search box, type vision to find the Cloud Vision API and click on the hyperlink.

### Step 3

Click Enable if necessary.

### Step 4

Follow the same process to enable Cloud Translation API, Cloud Speech-to-Text API, and Cloud Natural Language APIs.

### Step 5

From the GCP console menu, select APIs and services and select Credentials.

### Step 6

If you do not already have an API key, click the Create credentials button and select API key. Once created, click close. You will need this API key in the notebook later.

## Invoke ML APIs from AI Platform Notebooks
### Step 1

In the notebook interface, navigate to training-data-analyst > CPB100 > lab4c > mlapis.ipynb.

### Step 2

Read the commentary, then run the Python snippets (Use Shift+Enter to run each piece of code) in the cell, step by step. Make sure to insert your API Key in the first Python cell.


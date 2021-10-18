# Lab: BigQuery in Jupyter Labs on AI Platform

## Overview
The purpose of this lab is to show learners how to instantiate a Jupyter notebook running on Google Cloud Platform's AI Platform service. To aid in the demonstration, a dataset with various flight departure and arrival times will be leveraged.

### Objectives
In this lab, you learn to perform the following tasks:

- Instantiate a Jupyter notebook on AI Platform.
- Execute a BigQuery query from within a Jupyter notebook and process the output using Pandas.

## Start a JupyterLab Notebook Instance
1. Click on the Navigation Menu.

2. Navigate to AI Platform, then to Notebooks.
![image](https://user-images.githubusercontent.com/1645304/137654903-4f71b279-fed2-4ca0-bd28-1a7d2a2dbc99.png)


3. You'll be redirected to a page for notebook instances on AI Platform.

When the notebook main page loads if you notice a link entitled Enable Notebooks API, click that link to allow the background Notebooks API to be upgraded. The upgrade will occur promptly.
![image](https://user-images.githubusercontent.com/1645304/137655075-c49d75e7-974f-49b1-a6c4-a183c0849dd4.png)

Click on the NEW INSTANCE icon on the top of the page.

4. In the menu that pops down, select the Python 3 option.

![image](https://user-images.githubusercontent.com/1645304/137655239-f86442c0-735e-48e0-b15c-fa0db7590cfd.png)


5. A screen titled New notebook instance will be shown. Leave the default options and click on CREATE.

![image](https://user-images.githubusercontent.com/1645304/137655361-b5a69ac6-b154-4cb6-9de7-7562522efd06.png)


6. After a few minutes, the AI Platform Notebooks console will have your instance name followed by OPEN JUPYTERLAB. Click OPEN JUPYTERLAB.

![image](https://user-images.githubusercontent.com/1645304/137655485-c88a4083-9b36-4d1b-a972-570aaea9c12b.png)


7. A new tab will open in your browser with the JupyterLab environment. Select Python 3 under Notebook.

![image](https://user-images.githubusercontent.com/1645304/137655616-808221d1-4a6f-4540-9935-2de5c88c783f.png)

Your notebook is now set up.

## Execute a BigQuery query

1. Execute the following Python install command by hitting Shift + Enter in the first cell of the notebook to install the google-cloud-bigquery library at version 1.25.0.
```
!pip install google-cloud-bigquery==1.25.0 --use-feature=2020-resolver
```

> Note: You may ignore any error message related to google-cloud-storage.
Restart the kernel by clicking Restart kernel icon > Restart.

![image](https://user-images.githubusercontent.com/1645304/137656614-0f0fc095-0396-4ccc-bb5c-ea152d6bb1cd.png)

2. Enter the following query in the second cell of the notebook.
```sql
%%bigquery df
SELECT
  departure_delay,
  COUNT(1) AS num_flights,
  APPROX_QUANTILES(arrival_delay, 10) AS arrival_delay_deciles
FROM
  `bigquery-samples.airline_ontime_data.flights`
GROUP BY
  departure_delay
HAVING
  num_flights > 100
ORDER BY
  departure_delay ASC
```

The command makes use of the magic function `%%bigquery`. Magic functions in notebooks provide an alias for a system command. In this case, `%%bigquery` runs the query in the cell in BigQuery and stores the output in a Pandas DataFrame object named `df`.

3. Run the cell by hitting Shift + Enter, when the cursor is in the cell. Alternatively, if you navigate to the Run tab you can click on Run Selected Cells. Note the keyboard shortcut for this action in case it is not Shift + Enter. There should be no output when executing the command.
Click Check my progress to verify the objective.
Execute a BigQuery query

4. View the first five rows of the query's output by executing the following code in a new cell:
```python
df.head()
```

![image](https://user-images.githubusercontent.com/1645304/137656560-1c640029-03e2-4caf-a657-b1d5b43b5f78.png)

## Make a Plot with Pandas
We're going to use the Pandas DataFrame containing our query output to build a plot that depicts how arrival delays correspond to departure delays. Before continuing, if you are unfamiliar with Pandas the [Ten Minute Getting Started Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) is recommended reading.

1. To get a DataFrame containing the data we need we first have to wrangle the raw query output. Enter the following code in a new cell to convert the list of `arrival_delay_deciles` into a Pandas Series object. The code also renames the resulting columns.
```python
import pandas as pd
percentiles = df['arrival_delay_deciles'].apply(pd.Series)
percentiles.rename(columns = lambda x : '{0}%'.format(x*10), inplace=True)
percentiles.head()
```

2. Since we want to relate departure delay times to arrival delay times we have to concatenate our `percentiles` table to the `departure_delay` field in our original DataFrame. Execute the following code in a new cell:
```python
df = pd.concat([df['departure_delay'], percentiles], axis=1)
df.head()
```

3. Before plotting the contents of our DataFrame, we'll want to drop extreme values stored in the `0%` and `100%` fields. Execute the following code in a new cell:
```python
df.drop(labels=['0%', '100%'], axis=1, inplace=True)
df.plot(x='departure_delay', xlim=(-30,50), ylim=(-50,50));
```

![image](https://user-images.githubusercontent.com/1645304/137656868-b779c82f-81f8-4564-b753-5a415db9ad0a.png)



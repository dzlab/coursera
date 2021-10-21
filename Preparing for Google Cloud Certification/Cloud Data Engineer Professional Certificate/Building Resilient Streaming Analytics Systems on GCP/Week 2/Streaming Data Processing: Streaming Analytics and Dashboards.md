# Lab: Streaming Data Processing: Streaming Analytics and Dashboards

## Overview
Data visualization tools can help you make sense of your BigQuery data and help you analyze the data interactively. You can use visualization tools to help you identify trends, respond to them, and make predictions using your data. In this lab, you use Google Data Studio to visualize data in the BigQuery table populated by your Dataflow pipeline in the previous exercise.

> At the time of this writing, streaming pipelines are not available in the DataFlow Python SDK. So the streaming labs are written in Java.

## Objectives
In this lab, you will perform the following tasks:

- Connect to a BigQuery data source
- Create reports and charts to visualize BigQuery data

This lab uses Google Data Studio to visualize data in BigQuery using the BigQuery connector. In subsequent tasks, you will create a data source, a report, and charts that visualize data in the sample table.

## Task 1: Preparation
You will be running a sensor simulator from the training VM. There are several files and some setup of the environment required.

### Open the SSH terminal and connect to the training VM
1. In the Console, on the Navigation menu (7a91d354499ac9f1.png), click Compute Engine > VM instances.

2. Locate the line with the instance called training-vm.

3. On the right, under 'Connect' column, click on SSH to open a terminal window.

4. In this lab, you will enter CLI commands on the training-vm.

### Verify initialization is complete
5. The training-vm is installing some software in the background. Verify that setup is complete by checking the contents of the new directory.
```
ls /training
```

The setup is complete when the result of your list (ls) command output appears as in the image below. If the full listing does not appear, wait a few minutes and try again. Note: It may take 2 to 3 minutes for all background actions to complete.

![image](https://user-images.githubusercontent.com/1645304/137638213-4c500494-68ee-465d-800b-e4e084ebf7fc.png)

### Download Code Repository
6. Next you will download a code repository for use in this lab.
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

### Set environment variables
7. On the training-vm SSH terminal enter the following:
```
source /training/project_env.sh
```
This script sets the `$DEVSHELL_PROJECT_ID` and `$BUCKET` environment variables.

## Task 2: Creating a data source in Data Studio
1. Google Data Studio is a separate service from the Google Cloud environment. Open a new browser tab preferably in an incognito window. Navigate to: datastudio.google.com or click on this link: [Google Data Studio](https://datastudio.google.com/)

> The first step in creating a report in Data Studio is to create a data source for the report. A report may contain one or more data sources. When you create a BigQuery data source, Data Studio uses the BigQuery connector.

> You must have the appropriate permissions in order to add a BigQuery data source to a Data Studio report. Lab initialization steps created a BigQuery Dataset and tables for use in your exercises. The permissions applied to BigQuery datasets will apply to the reports, charts, and dashboards you create in Data Studio. When a Data Studio report is shared, the report components are visible only to users who have appropriate permissions.

2. On the Reports page, in the Start with a Template section, click the Blank Report template. This starts the account setup process.

![image](https://user-images.githubusercontent.com/1645304/137638285-902cda07-4425-4ae6-835c-c75329b0f789.png)

3. On the Welcome page, click on GET STARTED.

4. On the Terms page, click on the checkbox to acknowledge the terms. And click ACCEPT.

5. On the Preferences page, select No, thanks for each option to receive email notifications, and click DONE.

6. Now that the account is initialized, you need to start the process again.

7. On the Reports page, in the Start with a Template section, click the Blank Report template. This time it will take you to a new page and begin an Untitled Report.

8. The Add data to report panel will load from the bottom of the page.

9. In the Google Connectors section, select BigQuery.

![image](https://user-images.githubusercontent.com/1645304/137638316-6b334942-e381-4f3c-8783-011493084004.png)


10. Click on AUTHORIZE for the notice that "Data Studio requires authorization to connect to your BigQuery projects."

![image](https://user-images.githubusercontent.com/1645304/137638439-37c9ff65-e17b-44b5-8ac9-d5bad325185b.png)


11. If prompted, in the Sign in dialog, select your Qwiklabs student account.

12. If prompted, click ALLOW to give Google Data Studio permission to view the BigQuery resources in your lab account.

13. Then select My Projects.

14. In the Project column, click on your project name.

15. In the Dataset column, click on demos.

16. In the Table column, click current_conditions.

17. Lastly click Add.

![image](https://user-images.githubusercontent.com/1645304/137638360-1f3d71a8-a8f9-4007-b047-c23adf3994d1.png)


18. You will be prompted with a "You are about to add data to this report" notice. Check "Don't show me this again" and click ADD TO REPORT.

![image](https://user-images.githubusercontent.com/1645304/137638366-7d54863e-b8fc-45d2-9718-cee9411b6b20.png)


19. Once complete, a simple default tabular report will appear. This confirms that you can see your BigQuery data in Data Studio.

![image](https://user-images.githubusercontent.com/1645304/137638371-f508313c-b667-4c05-9500-8064b7a40c7d.png)

> Giving Data Studio permission to Google Cloud account resources is typically a first-time activity and not something you would need to do every time you create a report.

## Task 3: Creating a bar chart using a calculated field
Once you have added the current_conditions data source to the report, the next step is to create a visualization. Begin by creating a bar chart. The bar chart will display the total number of vehicles captured for each highway.

1. (Optional) At the top of the page, click Untitled Report to change the report name. For example, type `<PROJECTID>-report1-yourname`.

2. Delete the pre-populated tabluar report. You can do this by simply selecting it and pressing delete.

3. Next, from the Add a chart menu select the first Bar chart.

![image](https://user-images.githubusercontent.com/1645304/137638511-3fd4622f-e197-48eb-b799-d1ef8f5ddc98.png)

4. In the Bar chart properties window, on the Data tab, notice the value for Data Source (current_conditions) and the default values for Dimension and Metric.

5. If Dimension is not set to highway, then change Dimension to highway. In the Dimension section, click the existing dimension.

6. In the Dimension picker, select highway.

7. In the Metric section, click Add metric and add latitude.

8. In the Metric section, mouse over Record Count and click the (x) to remove it.

Example:

![image](https://user-images.githubusercontent.com/1645304/137638528-86fffee3-a7ab-4074-a233-c362dec2c454.png)

9. To gain insight on vehicle volume you need to add a metric for each vehicle detected.

10. In the Metric section, click Add metric and add sensorId.

11. A count distinct for this column is automatically created. This metric set as a count distinct does not give you a true sense of traffic volume. Click on the CTD text and on the popup window choose Count . Type the name vehicles in the name box. Click in the report space off the popup to close it. The change is saved automatically.

![image](https://user-images.githubusercontent.com/1645304/137638540-f63c04cf-2fb2-47fc-aeb3-e9e71b47578a.png)

![image](https://user-images.githubusercontent.com/1645304/137638543-0d84e3df-712d-45de-bc98-2bf3de7bc9ef.png)


12. In the Metric section, mouse over latitude and click the (x) to remove it.

13. The Dimension should be set to highway and the Metric should be set to sensorId. Notice the chart is sorted in Descending order by default. The highway with the most vehicles is displayed first.

![image](https://user-images.githubusercontent.com/1645304/137638551-4983d813-e2dc-4fbe-9661-3f16337815fe.png)

14. To enhance the chart, change the bar labels. In the Bar chart properties window, click the STYLE tab.

15. In the Bar chart section, check Show data labels.

16. The total number of vehicles is displayed above each bar in the chart.

## Task 4: Creating a chart using a custom query
You may find that it is easier to work with an existing query to produce the desired reports and visualizations in Data Studio. The Custom Query option lets you leverage BigQuery's full query capabilities such as joins, unions, and analytical functions.

Alternatively, you can leverage BigQuery's full query capabilities by creating a view. A view is a virtual table defined by a SQL query. You can query data in a view by adding the dataset containing the view as a data source.

When you specify a SQL query as your BigQuery data source, the results of the query are in table format, which becomes the field definition (schema) for your data source. When you use a custom query as a data source, Data Studio uses your SQL as an inner select statement for each generated query to BigQuery. For more information on custom queries in Data Studio, consult the [online help](https://support.google.com/datastudio/?hl=en#topic=6267740).

1. To add a bar chart to your report that uses a custom query data source:

2. From the Add a chart menu select the first Bar chart.

3. In the Bar chart properties window, on the Data tab, notice the value for Data Source (current_conditions) and the default values for Dimension and Metric are the same as the previous chart. In the Data Source section, click on the current_conditions data source. At the bottom of the pane choose ADD DATA.

![image](https://user-images.githubusercontent.com/1645304/137638674-3c39b4a3-7784-4eef-ae7f-b1b1ae90c082.png)

4. Under Google Connectors, select BigQuery.

5. Select CUSTOM QUERY in the first grouping.

6. For Billing Project, select your project.

7. Type the following in the Enter custom query window and replace the `<PROJECTID>` with your Project ID.
```
SELECT max(speed) as maxspeed, min(speed) as minspeed,
avg(speed) as avgspeed, highway
FROM `<PROJECTID>.demos.current_conditions`
group by highway
```

This query uses max/min/avg functions to give you the corresponding speed for each highway.

![image](https://user-images.githubusercontent.com/1645304/137638815-b522295b-8e79-40fb-9894-6513631766b8.png)


8. Click ADD.

9. When prompted, click ADD TO REPORT.

> Data Studio may be unable to determine the appropriate Dimension and Metrics for the chart. This requires you to adjust the graph options.

10. In the Bar chart properties, on the Data tab, in the Metric section, click Record count.

![image](https://user-images.githubusercontent.com/1645304/137638705-d5f34e7c-3d5c-4857-a1a5-5344c67d85a0.png)

11. In the Metric picker, select maxspeed.
12. In the Metric section, click Add metric.
13. In the Metric picker, select minspeed.
14. In the Metric section, click Add metric.
15. In the Metric picker, select avgspeed.
16. Remove the metric other than maxspeed, minspeed and avgspeed, if exist.

Your chart now displays the maximum speed, minimum speed, and average speed for each highway.

Notice each bar has a default color based on the order the metrics were added to the chart.

![image](https://user-images.githubusercontent.com/1645304/137638722-a1c31ebc-fa3b-47e9-9cb4-5aef856f7b55.png)

17. For readability, change the chart styles. In the Bar chart properties, click the Style tab.

![image](https://user-images.githubusercontent.com/1645304/137638729-a876c4ef-beaa-4907-8561-7c46c6fe1b8b.png)

18. In the Color By section, click on the boxes to select different colors.

![image](https://user-images.githubusercontent.com/1645304/137638738-e1ecc747-2c36-4106-8741-bf3857c5d976.png)


## Task 5: Viewing your query history
You can view queries submitted via the BigQuery Connector by examining your query history in the BigQuery web interface. Using the query history, you can estimate query costs, and you can save queries for use in other scenarios.

### Open BigQuery Console
In the Google Cloud Console, select Navigation menu > Big Data > BigQuery:

![image](https://user-images.githubusercontent.com/1645304/137638927-00e7cb80-1baa-4ef6-96a3-ab8d8dc049de.png)

The Welcome to BigQuery in the Cloud Console message box opens. This message box provides a link to the quickstart guide and lists UI updates.

Click Done.

1. In the left pane the first item in the list will be Query history. On your initial visit to the page the query history should appear on the bottom right underneath the Query editor pane. If it is not loaded click the Query history link.

![image](https://user-images.githubusercontent.com/1645304/137639012-6b33dd6a-867f-411e-a4f0-8a860842f8c7.png)

2. The list of queries is displayed with the most recent queries first. Click on any Query to view details on the query such as Job ID and Bytes Processed.

![image](https://user-images.githubusercontent.com/1645304/137638936-cfe58f10-73c5-4646-ab82-4323d2d32c45.png)



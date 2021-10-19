# Lab: PDE Prep: BigQuery Essentials

## Overview
This is a Challenge lab where you must complete a series of tasks within a limited time period. Instead of following step-by-step instructions, you are presented with general objectives. An automated scoring system (shown on this page) will provide feedback on whether you have completed each task correctly.

You must complete the tasks within the time period to score 100% on the challenge.

This lab does not teach GCP concepts. Instead, it is a test of your Data Engineering skills. This lab is only recommended for students who have BigQuery skills.

#### Topics tested
- Custom dataset creation.
- Import data to table from external file.
- Define a schema.
- Use SQL to query data.
- Demonstrate knowledge of aggregators and grouping in SQL.

## Your Challenge: Scenario
You work as a Data Engineer for Flowlogistic. (Congratulations on the new job!)

### Background
Jasper Jasmine Mines is a key customer for Flowlogistic. Flowlogistic moves equipment and parts for the mining company by air. In 2018 Flowlogistic managed more than 8,000 flights for this customer. The log file contains a record of each of those flights, including the date, the vendor airline, distance travelled, and duration of each flight.

### Challenge
The Data Analysts need to run queries against a log of cargo transport flights. Your job is to create a BigQuery custom dataset and run a series of queries to demonstrate that it is ready for the analysts to use.

## Task 1: Create a custom dataset
- Create a custom dataset in BigQuery with the name JasmineJasper.
- Create a table in the dataset with the name triplog.
- Load the table with the source data.
- The log file is in CSV format. It has been shared with you via a Cloud Storage bucket: gs://cloud-training/preppde/2018-JasperJasmineMines.csv
- Use the following schema:
  `date: integer,origin: string,destination: string,airline: string,miles: float,minutes: integer,duration: string`

> Tip: If you’re using the new BigQuery UI, you can select Edit as Text and simply paste in the above schema.

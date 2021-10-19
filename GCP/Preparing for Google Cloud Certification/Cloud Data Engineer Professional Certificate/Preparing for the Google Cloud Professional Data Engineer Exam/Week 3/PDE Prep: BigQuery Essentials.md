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
- The log file is in CSV format. It has been shared with you via a Cloud Storage bucket: `gs://cloud-training/preppde/2018-JasperJasmineMines.csv`
- Use the following schema:
  `date: integer,origin: string,destination: string,airline: string,miles: float,minutes: integer,duration: string`

> Tip: If you’re using the new BigQuery UI, you can select Edit as Text and simply paste in the above schema.

## Task 2: Query the dataset
In the beginning of 2018, one of the airlines promised to use newer faster airplanes for all trips originating from London's Heathrow Airport. Your job is to create two queries:

1. One query is to verify that all the airlines have similar travel times from another airport.

2. The second query is to identify whether one specific airline, PlanePeople Air, has kept its promise of providing newer faster planes to Flowlogistic.

### Fields you need to know:
- **minutes** contains the travel time for each flight from take-off to landing measured in minutes.
- **origin** and **destination** use the IATA three-character airport codes.
  - LHR = London Heathrow Airport, United Kingdom
  - FRA = Frankfurt Airport, Germany
  - KUL = Kuala Lumpur International Airport, Malaysia
- **airline** contains the name of the airline vendor contracted to Flowlogistic.

> If you are using the new BigQuery web interface, the default setting is Standard SQL dialect. If you are using the classic web interface, the default is Legacy SQL dialect, and you will need to set it to Standard SQL.

> Note: It may take time (approximately 15-20 minutes) for the score to appear on a successful query.

### First Query
Create a query that produces the average trip time for trips originating from the airport in Frankfurt, Germany (FRA) and destined for the airport in Kuala Lumpur, Malaysia (KUL), and group the results by airline. The resulting average times should be similar.

### Second Query
Create a query that produces the average trip time for trips originating from London Heathrow Airport, United Kingdom (LHR) and destined for the airport in Kuala Lumpur, Malaysia (KUL), and group the results by airline, and order them from lowest to highest. The resulting average times should reveal whether the airline, PlanePeople Air, kept its promise to use faster airplanes from Heathrow Airport.

### Answer the following two questions:
Did the airline keep its promise?
If the answer was yes, how fast was the trip from LHR to KUL on average?

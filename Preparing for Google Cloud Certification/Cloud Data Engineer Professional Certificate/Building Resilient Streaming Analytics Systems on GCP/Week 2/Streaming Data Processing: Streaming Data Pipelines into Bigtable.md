# Lab: Streaming Data Processing: Streaming Data Pipelines into Bigtable

## Overview
In this lab you will use Dataflow to collect traffic events from simulated traffic sensor data made available through Google Cloud PubSub, and write them into a Bigtable table.

> At the time of this writing, streaming pipelines are not available in the DataFlow Python SDK. So the streaming labs are written in Java.

## Objectives
In this lab, you will perform the following tasks:

- Launch Dataflow pipeline to read from Pub/Sub and write into Bigtable.
- Open an HBase shell to query the Bigtable database.

## Task 1: Preparation
You will be running a sensor simulator from the training VM. There are several files and some setup of the environment required.

### Open the SSH terminal and connect to the training VM
1. In the Console, on the Navigation menu, click Compute Engine > VM instances.

2. Locate the line with the instance called training-vm.

3. On the far right, under Connect column, click on SSH to open a terminal window.

In this lab, you will enter CLI commands on the training-vm.

### Verify initialization is complete
4. The training-vm is installing some software in the background. Verify that setup is complete by checking the contents of the new directory.
```
ls /training
```
The setup is complete when the result of your list (ls) command output appears as in the image below. If the full listing does not appear, wait a few minutes and try again. Note: It may take 2 to 3 minutes for all background actions to complete.

![image](https://user-images.githubusercontent.com/1645304/137639939-ea94905b-2a53-43c1-b1cf-071c0aa03eb3.png)

### Download Code Repository
5. Next, you will download a code repository for use in this lab.
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

### Set environment variables
6. On the training-vm SSH terminal, enter the following:
```
source /training/project_env.sh
```

This script sets the `$DEVSHELL_PROJECT_ID` and `$BUCKET` environment variables.

### Prepare HBase quickstart files
7. In the training-vm SSH terminal, run the script to download and unzip the quickstart files (you will later use these to run the HBase shell.)
```
cd ~/training-data-analyst/courses/streaming/process/sandiego
./install_quickstart.sh
```

## Task 2: Simulate traffic sensor data into Pub/Sub
1. In the training-vm SSH terminal, start the sensor simulator. The script reads sample data from a csv file and publishes it to Pub/Sub.
```
/training/sensor_magic.sh
```
This command will send 1 hour of data in 1 minute. Let the script continue to run in the current terminal.

### Open a second SSH terminal and connect to the training VM
2. In the upper right corner of the training-vm SSH terminal, click on the gear-shaped button ( 9649d58acf1c4e06.png), and select New Connection to training-vm from the drop-down menu. A new terminal window will open.

![image](https://user-images.githubusercontent.com/1645304/137640049-4847f5d0-14b1-4e12-90e2-59ebc2f728f3.png)


The new terminal session will not have the required environment variables. Complete the next step to set these variables.

3. In the new training-vm SSH terminal, enter the following:
```
source /training/project_env.sh
```

## Task 3: Launch Dataflow Pipeline
1. In the second training-vm SSH terminal, navigate to the directory for this lab. Examine the script in Cloud Shell or using nano. Do not make any changes to the code.
```
cd ~/training-data-analyst/courses/streaming/process/sandiego
nano run_oncloud.sh
```
What does the script do?

The script takes 3 required arguments: project id, bucket name, classname and possibly a 4th argument: options. In this part of the lab, we will use the `--bigtable` option which will direct the pipeline to write into Cloud Bigtable.

2. Press CTRL+X to exit.

3. Run the following script to create the Bigtable instance.

```
$ cd ~/training-data-analyst/courses/streaming/process/sandiego
$ cat ./create_cbt.sh 
gcloud beta bigtable instances create sandiego --cluster=cpb210 --cluster-zone=us-central1-b --display-name=="San Diego Freeway data" --instance-type=DEVELOPMENT

$ ./create_cbt.sh
```

4. Run the Dataflow pipeline to read from PubSub and write into Cloud Bigtable.
```
cd ~/training-data-analyst/courses/streaming/process/sandiego
./run_oncloud.sh $DEVSHELL_PROJECT_ID $BUCKET CurrentConditions --bigtable
```

Example successful run:
```
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 47.582 s
[INFO] Finished at: 2018-06-08T21:25:32+00:00
[INFO] Final Memory: 58M/213M
[INFO] ------------------------------------------------------------------------
```

## Task 4: Explore the pipeline
1. Return to the browser tab for Console. On the Navigation menu, click **Dataflow** and click on the new pipeline job. Confirm that the pipeline job is listed and verify that it is running without errors.

![image](https://user-images.githubusercontent.com/1645304/137640310-d45dbd21-b006-426d-b3ba-cd5c7abf215d.png)

2. Find the **write:cbt** step in the pipeline graph, and click on the down arrow on the right to see the writer in action. Click on the given writer. Review the **Bigtable Options** in the Step summary.

## Task 5: Query Bigtable data
1. In the second training-vm SSH terminal, run the **quickstart.sh** script to launch the HBase shell.
```
cd ~/training-data-analyst/courses/streaming/process/sandiego/quickstart
./quickstart.sh
```

2. When the script completes, you will be in an HBase shell prompt that looks like this:
```
hbase(main):001:0>
```

3. At the HBase shell prompt, type the following query to retrieve 2 rows from your Bigtable table that was populated by the pipeline. It may take a few minutes for results to return via the HBase query.

Repeat the 'scan' command until you see a list of rows returned.
```
scan 'current_conditions', {'LIMIT' => 2}
```

```
hbase(main):001:0> scan 'current_conditions', {'LIMIT' => 2}
ROW                                          COLUMN+CELL                                                                                                                    
 15#S#1#9223370811313975807                  column=lane:direction, timestamp=1225540800, value=S                                                                           
 15#S#1#9223370811313975807                  column=lane:highway, timestamp=1225540800, value=15                                                                            
 15#S#1#9223370811313975807                  column=lane:lane, timestamp=1225540800, value=1.0                                                                              
 15#S#1#9223370811313975807                  column=lane:latitude, timestamp=1225540800, value=32.706184                                                                    
 15#S#1#9223370811313975807                  column=lane:longitude, timestamp=1225540800, value=-117.120565                                                                 
 15#S#1#9223370811313975807                  column=lane:sensorId, timestamp=1225540800, value=32.706184,-117.120565,15,S,1                                                 
 15#S#1#9223370811313975807                  column=lane:speed, timestamp=1225540800, value=71.5                                                                            
 15#S#1#9223370811313975807                  column=lane:timestamp, timestamp=1225540800, value=2008-11-01 12:00:00                                                         
 15#S#1#9223370811314275807                  column=lane:direction, timestamp=1225540500, value=S                                                                           
 15#S#1#9223370811314275807                  column=lane:highway, timestamp=1225540500, value=15                                                                            
 15#S#1#9223370811314275807                  column=lane:lane, timestamp=1225540500, value=1.0                                                                              
 15#S#1#9223370811314275807                  column=lane:latitude, timestamp=1225540500, value=32.706184                                                                    
 15#S#1#9223370811314275807                  column=lane:longitude, timestamp=1225540500, value=-117.120565                                                                 
 15#S#1#9223370811314275807                  column=lane:sensorId, timestamp=1225540500, value=32.706184,-117.120565,15,S,1                                                 
 15#S#1#9223370811314275807                  column=lane:speed, timestamp=1225540500, value=71.8                                                                            
 15#S#1#9223370811314275807                  column=lane:timestamp, timestamp=1225540500, value=2008-11-01 11:55:00   
```

![image](https://user-images.githubusercontent.com/1645304/137640213-bc32a157-a50a-4b3c-adc0-d6ffd9b4fbf3.png)

4. Review the output. Notice each row is broken into column, timestamp, value combinations.

5. Run another query. This time look only at the lane: speed column, limit to 10 rows, and specify rowid patterns for start and end rows to scan over.
```
scan 'current_conditions', {'LIMIT' => 10, STARTROW => '15#S#1', ENDROW => '15#S#999', COLUMN => 'lane:speed'}
```

```
hbase(main):002:0> scan 'current_conditions', {'LIMIT' => 10, STARTROW => '15#S#1', ENDROW => '15#S#999', COLUMN => 'lane:speed'}
ROW                                          COLUMN+CELL                                                                                                                    
 15#S#1#9223370811311875807                  column=lane:speed, timestamp=1225542900, value=71.9                                                                            
 15#S#1#9223370811312175807                  column=lane:speed, timestamp=1225542600, value=71.5                                                                            
 15#S#1#9223370811312475807                  column=lane:speed, timestamp=1225542300, value=71.2                                                                            
 15#S#1#9223370811312775807                  column=lane:speed, timestamp=1225542000, value=71.4                                                                            
 15#S#1#9223370811313075807                  column=lane:speed, timestamp=1225541700, value=71.9                                                                            
 15#S#1#9223370811313375807                  column=lane:speed, timestamp=1225541400, value=71.3                                                                            
 15#S#1#9223370811313675807                  column=lane:speed, timestamp=1225541100, value=72.4                                                                            
 15#S#1#9223370811313975807                  column=lane:speed, timestamp=1225540800, value=71.5                                                                            
 15#S#1#9223370811314275807                  column=lane:speed, timestamp=1225540500, value=71.8                                                                            
 15#S#1#9223370811314575807                  column=lane:speed, timestamp=1225540200, value=72.4  
```

6. Review the output. Notice that you see 10 of the column, timestamp, value combinations, all of which correspond to Highway 15. Also notice that column is restricted to lane: speed.

7. Feel free to run other queries if you are familiar with the syntax. Once you're satisfied, enter quit to exit the shell.
```
quit
```

## Cleanup
1. In the second training-vm SSH terminal, run the following script to delete your Bigtable instance.
```
$ cd ~/training-data-analyst/courses/streaming/process/sandiego
$ cat delete_cbt.sh 
gcloud beta bigtable instances delete sandiego
$ ./delete_cbt.sh
Delete instance sandiego. Are you sure?
Do you want to continue (Y/n)?  Y
```

If prompted to confirm, enter Y.

2. On your Dataflow page in your Cloud Console, click on the pipeline job name.

3. Click Stop on the top menu bar. Select Cancel, and then click Stop Job.

4. Go back to the first SSH terminal with the publisher, and enter Ctrl+C to stop it.

5. In the BigQuery console, click on the three dots next to the demos dataset, and click Open.

6. Click Delete Dataset.

If prompted to confirm, type the dataset name: demos


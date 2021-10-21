# MapReduce in Cloud Dataflow (Java)

## Overview
In this lab, you will identify Map and Reduce operations, execute the pipeline, use command line parameters.

## Objective
- Identify Map and Reduce operations
- Execute the pipeline
- Use command line parameters

## Task 1. Review Preparations
These preparations should already be have been done:

- Create Cloud Storage bucket
- Clone github [repository](https://github.com/GoogleCloudPlatform/training-data-analyst) to Cloud Shell
```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

## Task 2. Identify Map and Reduce operations
1. In the Cloud Shell code editor navigate to the directory `/training-data-analyst/courses/data_analysis/lab2/javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp` and view the file `IsPopular.java` in the Cloud Shell editor. Do not make any changes to the code.

Alternatively, you could view the file with nano. Do not make any changes to the code.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp
nano IsPopular.java
```

> Normally, you would develop this Java code in an Integrated Development Environment such as Eclipse or IntelliJ (not in CloudShell).

Can you answer these questions about the file `IsPopular.java`?

- What getX() methods are present in the class MyOptions?
- What is the default output prefix?
- How is the variable outputPrefix in main() set?
- What are the key steps in the pipeline?
- Which of these steps happen in parallel?
- Which of these steps are aggregations?

## Task 3. Execute the pipeline
1. Copy and paste the following Maven command in Cloud Shell:
```
export PATH=/usr/lib/jvm/java-8-openjdk-amd64/bin/:$PATH
cd ~/training-data-analyst/courses/data_analysis/lab2/javahelp
mvn compile -e exec:java \
 -Dexec.mainClass=com.google.cloud.training.dataanalyst.javahelp.IsPopular
```
> It will take 4-5 mintues to complete the process.

2. Examine the output file:
```
$ cat /tmp/output.csv
org,45
org.apache.beam,44
org.apache,44
org.apache.beam.sdk,43
org.apache.beam.sdk.transforms,16
```

## Task 4. Use command line parameters
1. Change the output prefix from the default value:
```
mvn compile -e exec:java \
  -Dexec.mainClass=com.google.cloud.training.dataanalyst.javahelp.IsPopular \
 -Dexec.args="--outputPrefix=/tmp/myoutput"
```
2. What will be the name of the new .csv file that is written out?

3. Note that we now have a new file in the /tmp directory:
```
$ ls -lrt /tmp/*.csv
-rw-r--r-- 1 student_01_7f231ad631d2 student_01_7f231ad631d2 98 Oct 16 18:02 /tmp/output.csv
-rw-r--r-- 1 student_01_7f231ad631d2 student_01_7f231ad631d2 98 Oct 16 18:07 /tmp/myoutput.csv
```

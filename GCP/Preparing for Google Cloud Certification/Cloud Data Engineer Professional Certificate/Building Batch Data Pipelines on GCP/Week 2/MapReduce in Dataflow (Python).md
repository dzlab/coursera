# MapReduce in Dataflow (Python)

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

- Upgrade packages and install Apache Beam
```
cd training-data-analyst/courses/data_analysis/lab2/python
sudo ./install_packages.sh
```

## Task 2. Identify Map and Reduce operations
1. In the Cloud Shell code editor navigate to the directory `/training-data-analyst/courses/data_analysis/lab2/python` and view the file `is_popular.py` in the Cloud Shell editor. Do not make any changes to the code.
Alternatively, you could view the file with nano. Do not make any changes to the code.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
nano is_popular.py
```
Can you answer these questions about the file is_popular.py?

- What custom arguments are defined?
- What is the default output prefix?
- How is the variable output_prefix in main() set?
- How are the pipeline arguments such as --runner set?
- What are the key steps in the pipeline?
- Which of these steps happen in parallel?
- Which of these steps are aggregations?

## Task 3. Execute the pipeline
1. Run the pipeline locally:
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
python3 ./is_popular.py
```

> Note: if you see an error that says "No handlers could be found for logger "oauth2client.contrib.multistore_file", you may ignore it. The error is simply saying that logging from the oauth2 library will go to stderr.

2. Identify the output file. It should be `output<suffix>` and could be a sharded file.
```
$ ls -al /tmp
total 28
drwxrwxrwt 1 root                    root                    4096 Oct 16 17:53 .
drwxr-xr-x 1 root                    root                    4096 Oct 16 17:49 ..
-rw-r--r-- 1 student_00_e876cae5c5a2 student_00_e876cae5c5a2 5331 Oct 16 17:49 minikube_delete_83558f7398d53debd4991e272700063d799da021_0.log
-rw-r--r-- 1 student_00_e876cae5c5a2 student_00_e876cae5c5a2  128 Oct 16 17:53 output-00000-of-00001
-rw------- 1 root                    root                       0 Oct 16 17:49 tmp.sXk26O2clG
drwx------ 4 student_00_e876cae5c5a2 student_00_e876cae5c5a2 4096 Oct 16 17:49 tmp.wZa1brizOJ
drwx------ 2 student_00_e876cae5c5a2 student_00_e876cae5c5a2 4096 Oct 16 17:49 tmux-1000
```

3. Examine the output file, replacing '-*' with the appropriate suffix.
```
cat /tmp/output-*
```
```
$ cat /tmp/output-00000-of-00001
[('org', 45), ('org.apache', 44), ('org.apache.beam', 44), ('org.apache.beam.sdk', 43), ('org.apache.beam.sdk.transforms', 16)]
```

## Task 4. Use command line parameters
1. Change the output prefix from the default value:
```
python3 ./is_popular.py --output_prefix=/tmp/myoutput
```
  
2. What will be the name of the new file that is written out?

3. Note that we now have a new file in the /tmp directory:
```
$ ls -lrt /tmp/myoutput*
-rw-r--r-- 1 student_00_e876cae5c5a2 student_00_e876cae5c5a2 128 Oct 16 17:53 /tmp/myoutput-00000-of-00001
```

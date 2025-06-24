# LogMonitoringApp
----------------------------------------------------------------------
Log Monitoring Application which read log file with format "logs.log" and analyse the data to identify the jobs or tasks which are taking longer than the specified thresholds (i.e., greater than 5min or 10 min durations)

# Log Monitoring Application
----------------------------------------------------------------------

## Overview
----------------------------------------------------------------------
A Python application to monitor log files, track job durations, and creates an outuput file with processid, job description and job  or task taking more than than 5 minutes and 10 minutes duration.

## Requirements
----------------------------------------------------------------------
- Python 3.12.8 and above 
- Dependency - Install Python3.12.8 above on the client or server - where this code will be run or deployed. 
- the source script is stored on the SourceScript directory on this repo and it continas a file named - readLogFile.py and it has a function named "parse_log_file" - which contains the core logic to read the logs.log file and creates an output file named "report.txt" on the same directory. 


## Usage
----------------------------------------------------------------------
1. Clone the  public github repository named - https://github.com/ganeshssac/LogMonitoringApp/ 
2. Ensure `logs.log` is in the soruce  code directory or root directory. 
3. If you using a different log file name (other than 'logs.log' file) - ensure you update the readLogFile.py - with correct log file name. Update the  correct log file name  i.e. line number 7 on the readLogFile.py 
4. Run Python command `python3 readLogFile.py` on the client machine or server or laptop. 
5. The output file named - "report.txt" will be created when you execute  the python command `python3 readLogFile.py`. 
6. Please note, the file path or directory path - where the python command was executed. The output file "report.txt" will be saved or stored within the same directory path. 


## Output
----------------------------------------------------------------------
Check the output file named "report.txt" which has the following fields or column names
1. Type --> Identifies each record by type to filter the events by Warning or Error Job/Task. 
2. ProcessID --> refers to the  Job Process ID number which took longer to run. 
3. Job Desciption --> refers to Job description task. 
4. Duration --> Identifies the  Job Process ID which took longer than 5 minutes  or 10 minutes. 

Log Monitoring App - Unit Tests
===================================
This Repo contains the unit test cases for the Log Monitoring App in the TestScript directory, which is used to analyze log files and generate reports based on certain criteria.

Overview
----------------------------------------------------------------------
The TestParseLogFile class in the main.py file contains a single test case that verifies the functionality of the parse_log_file function from the readLogFile.py module.

Test Case Description
----------------------------------------------------------------------
The test_parse_log_file method performs the following actions:

Calls the parse_log_file function with the './testlogs.log' file path.

Checks if the report.txt file was created as a result of the log file processing.

Reads the contents of the report.txt file and verifies that the contents match the expected output.

Checks if the 'Warning: No END event found' message was not printed in the log file.

Setup
----------------------------------------------------------------------

Create a file named testlogs.log in the same directory as the test script and add the following sample log data:

----------------------------------------------------------------------

12:34:56,job1,START,123

12:35:56,job1,END,123

12:36:56,job2,START,456

12:41:56,job2,END,456

12:42:56,job3,START,789

12:52:56,job3,END,789

----------------------------------------------------------------------
Ensure that the readLogFile.py module, which contains the parse_log_file function, is in the same directory as the test script


----------------------------------------------------------------------
Running the Tests
----------------------------------------------------------------------
To run the tests, you can use the following command:

python3 -m unittest main
----------------------------------------------------------------------

This will execute the TestParseLogFile class and run the test_parse_log_file method.

Expected Output
If all the tests pass, you should see the following output:

....
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
If any of the tests fail, the output will include the details of the failed test cases.

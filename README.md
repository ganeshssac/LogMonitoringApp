# LogMonitoringApp
Log Monitoring Application which read log file with format "logs 9.log"

# Log Monitoring Application

## Overview
A Python application to monitor log files, track job durations, and alert on thresholds.

## Requirements
- Python 3.12.8 and above 
- Dependency - Install Python3.12.8 above on the client or server - where this code will be run or deployed. 


## Usage
1. Clone the  public github repository named - https://github.com/ganeshssac/LogMonitoringApp/ 
2. Ensure `logs 9.log` is in the root directory. 
3. If you using a different log file name (other than 'logs 9.log' file) - ensure you update the readLogFile.py - with correct log file name. Update the  correct log file name  i.e. line number 6 on the readLogFile.py 
4. Run Python command `python3 readLogFile.py` on the client machine or server or laptop. 
5. The output file named - "report.txt" will be created when you execute  the python command `python3 readLogFile.py`. 
6. Please note, the file path or directory path - where the python command was executed. The output file "report.txt" will be saved or stored within the same directory path. 


## Tests
Run `python -m unittest` in the project root after implementing unit tests.

## Output
Check the output file named "report.txt" which has the following fields or column names
1. Type --> Identifies each record by type to filter the events by Warning or Error Job/Task. 
2. ProcessID --> refers to the  Job Process ID number which took longer to run. 
3. Job Desciption --> refers to Job description task. 
4. Duration --> Identifies the  Job Process ID which took longer than 5 minutes  or 10 minutes. 


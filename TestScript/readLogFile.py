import os
import datetime

def parse_log_file(file_name):
    # Read the log file and store the data in a list of tuples
    logs = []
    with open(file_name, 'r') as f:
        for line in f:
            time, job, event, pid = line.strip().split(',')
            logs.append((time, job, event, int(pid)))

    # Sort the logs by process ID
    logs.sort(key=lambda x: x[3])

    # Create a report file with the jobs that took more than 5 minutes and 10 minutes
    with open('report.txt', 'w') as f:
        f.write('Type,Process ID,Job Description,Duration\n')
        for i in range(len(logs)-1):
            if logs[i][2] == ' START':
                # Find the corresponding END event
                for j in range(i+1, len(logs)-1):
                    if logs[j][2] == ' END' and logs[j][3] == logs[i][3]:
                        start_time = datetime.datetime.strptime(logs[i][0],'%H:%M:%S')
                        end_time = datetime.datetime.strptime(logs[j][0],'%H:%M:%S')
                        duration = end_time - start_time
                        # stores a report file with the jobs that took more than 5 minutes and 10 minutes
                        if duration.total_seconds() >= 300 and duration.total_seconds() <= 600:
                            f.write(f'Warning Job or Task,{logs[i][3]},{logs[i][1]},{duration}\n')
                        # stores a report file with the jobs that took greater than 10 minutes
                        if duration.total_seconds() > 600:
                            f.write(f'Error Job or Tasks,{logs[i][3]},{logs[i][1]},{duration}\n')
                        break
                else:
                    # No corresponding END event found
                    print(f'Warning: No END event found for job {logs[i][1]} (PID {logs[i][3]})')


if __name__ == '__main__':
    parse_log_file('./logs.log')
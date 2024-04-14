import sys
import ssh_to_dict
import datetime
from datetime import datetime
import statistics
import get_user_from_log
def average_time_of_log(file):
    list_of_dicts = ssh_to_dict.file_to_dict_stream(file)
    return statistics_for_dict(list_of_dicts)
def statistics_for_dict(log_dict):
    if(len(log_dict)==0):
        return (0,0)
    pid_times = [] 
    previous_pid=''
    previous_time=datetime.strptime(log_dict[0]['time'], "%H:%M:%S")
    for log in log_dict:
        pid = log['pid']
        if pid != previous_pid:
            time_taken=(datetime.strptime(log['time'], "%H:%M:%S")-previous_time).total_seconds()
            pid_times.append(time_taken)
            previous_pid=pid
            previous_time=datetime.strptime(log['time'], "%H:%M:%S")
    return (sum(pid_times)/len(pid_times), statistics.stdev(pid_times))
def average_time_for_users(file):
    list_of_dicts = ssh_to_dict.file_to_dict_stream(file)
    dict_users = {}
    for dict in list_of_dicts:
        user = get_user_from_log.get_user_log(dict)
        if(user):
            for u in user:
                if u in dict_users.keys():
                    continue
                check_dict=helper_dict(u, file)
                dict_users[u]=statistics_for_dict(check_dict)
    return dict_users
def helper_dict(user, file):
    list_of_dicts = ssh_to_dict.file_to_dict_stream(file)
    return_dict={}
    for dict in list_of_dicts:
        user_checked = get_user_from_log.get_user_log(dict)
        if user_checked== user:
            return_dict.append(dict)
    return return_dict
if __name__ == "__main__":
    log_file = sys.argv[1]
    print(average_time_of_log(log_file)[0])
    print(average_time_of_log(log_file)[1])
    print(average_time_for_users(log_file))
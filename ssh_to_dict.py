import sys
def ssh_to_dict(SSH_log):
    log_dict = {}
    try:
        data, description= SSH_log.split(':')
        month, day, time, app_component, username, pid = data.split()
        log_dict['month'] = month
        log_dict['day'] = day
        log_dict['time'] = time
        log_dict['app_component'] = app_component
        log_dict['username'] = username
        log_dict['pid'] = pid
        log_dict['description'] = description
    except Exception:
        log_dict[description] = "incorrect log format"
    return log_dict
def file_to_dict_stream(file_name):
    dict_list = []
    with open(file_name, 'r') as f:
        dict_list = [ssh_to_dict(line) for line in f]
    f.close()
    return dict_list
if __name__ == "__main__":
    log_file = sys.argv[1]
    log_dict = file_to_dict_stream(log_file)
    print(log_dict)
    
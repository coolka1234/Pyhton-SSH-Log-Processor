import re
def get_user_log(log_dict):
    user_pattern = r'user (\S+)'
    user = re.findall(user_pattern, log_dict['description'])
    if user:
        return user
    else:
        return None
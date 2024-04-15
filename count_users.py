import sys
import ssh_to_dict
import get_user_from_log
def count_users(fileName):
    list_of_dicts = ssh_to_dict.file_to_dict_stream(fileName)
    dict_users = {}
    for dict in list_of_dicts:
        user = get_user_from_log.get_user_log(dict)
        if(user):
            for u in user:
                if u in dict_users:
                    dict_users[u] += 1
                else:
                    dict_users[u] = 1
    most_common_user = max(dict_users, key=dict_users.get)
    least_common_user = min(dict_users, key=dict_users.get)
    return most_common_user, least_common_user
if __name__ == "__main__":
    print(count_users(sys.argv[1]))
import get_user_from_log
import random
import ssh_to_dict
def random_logs_random_user(n, fileName):
    user_list = set()
    file=open(fileName, 'r')
    for f in file:
        f=ssh_to_dict.ssh_to_dict(f)
        user = get_user_from_log.get_user_log(f)
        if user is not None:
            for u in user:
                user_list.add(u)
    file.close()
    chosen_user_index=random.randrange(len(user_list))
    user_list = list(user_list)
    chosen_user = user_list[chosen_user_index]
    rand_logs=[]
    file=open(fileName, 'r')
    for f in file:
        f=ssh_to_dict.ssh_to_dict(f)
        if get_user_from_log.get_user_log(f) == chosen_user:
            rand_logs.append(f)
            n = n-1
            if n == 0:
                break
    file.close()
    return rand_logs
if __name__ == "__main__":
    print(random_logs_random_user(5, 'SSH.log'))
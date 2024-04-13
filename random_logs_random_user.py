import sys
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
        current_user = get_user_from_log.get_user_log(f)
        if current_user is not None:
            if chosen_user in current_user:
                rand_logs.append(f)
    file.close()
    if n>len(rand_logs):
        return rand_logs
    final_logs=random.sample(rand_logs, n)
    return final_logs
if __name__ == "__main__":
    try:
        print(random_logs_random_user(sys.argv[2], sys.argv[1]))
    except:
        print("Usage: python random_logs_random_user.py <fileName> <n>")
        sys.exit(1)
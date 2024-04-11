import print_dicts
import ssh_to_dict
import string_to_dict
import get_ipv4s_from_log
import sys
import get_user_from_log
import get_message_type

with open(sys.argv[1], 'r') as f:
    logs = f.readlines()
f.close()
log_dict = string_to_dict.create_dict_list(logs)
for d in log_dict:
    print(get_message_type.get_messege_type(d))
    
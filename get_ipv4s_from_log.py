import re

def get_ipv4s_from_log(log_dict):
    ipv4_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ipv4_addresses = re.findall(ipv4_pattern, log_dict['description'])
    return ipv4_addresses
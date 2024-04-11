import sys
def print_dicts(dict_list):
    for d in dict_list:
        print(d)
    return None
if __name__ == "__main__":
    print_dicts(sys.argv[1])
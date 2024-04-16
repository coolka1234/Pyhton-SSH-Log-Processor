import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Utility CLI for various log processing scripts.")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    ipv4s_parser = subparsers.add_parser("get_ipv4s_from_log", description="Extract IPv4s from log file.")
    ipv4s_parser.add_argument("fileName", help="Name of the log file")
    ipv4s_parser.add_argument("-l", "--log-level", default="INFO", help="Minimal logging level")

    message_type_parser = subparsers.add_parser("get_message_type", description="Get message types from log file.")
    message_type_parser.add_argument("fileName", help="Name of the log file")
    message_type_parser.add_argument("-l", "--log-level", default="INFO", help="Minimal logging level")

    statistic_parser = subparsers.add_parser("log_statistic", description="Get statistics from log file.")
    statistic_parser.add_argument("fileName", help="Name of the log file")
    statistic_parser.add_argument("-l", "--log-level", default="INFO", help="Minimal logging level")

    print_dicts_parser = subparsers.add_parser("print_dicts", description="Print dictionaries from log file.")
    print_dicts_parser.add_argument("fileName", help="Name of the log file")
    print_dicts_parser.add_argument("-l", "--log-level", default="INFO", help="Minimal logging level")
    random_logs_parser = subparsers.add_parser("random_logs_random_user", description="Generate random logs for a user.")
    random_logs_parser.add_argument("fileName", help="Name of the log file")
    random_logs_parser.add_argument("-l","--log-level", default="INFO", help="Minimal logging level")

    args = parser.parse_args()

    if args.subcommand == "get_ipv4s_from_log":
        run_script("get_ipv4s_from_log.py", args)
    elif args.subcommand == "get_message_type":
        run_script("get_message_type.py", args)
    elif args.subcommand == "log_statistic":
        run_script("log_statistic.py", args)
    elif args.subcommand == "print_dicts":
        run_script("print_dicts.py", args)
    elif args.subcommand == "random_logs_random_user":
        run_script("random_logs_random_user.py", args)
    else:
        parser.print_help()

def run_script(script_name, args):
    command = ["python", script_name, args.fileName]
    if args.l:
        command.extend([args.l])
    
    subprocess.run(command)

if __name__ == "__main__":
    main()

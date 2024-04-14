import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description='CLI')
    parser.add_argument('script', type=str, help='Name of the script to run')
    parser.add_argument('--arg', type=str, help='Argument for the script')
    args = parser.parse_args()
    subprocess.run(['python', f'{args.script}.py', args.arg])

if __name__ == '__main__':
    main()
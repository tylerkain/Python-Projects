import argparse
import os
import signal
import subprocess


def kill_by_pid(pid):
    try:
        os.kill(pid, signal.SIGKILL)  # Using SIGKILL
        print(f"Process with PID {pid} has been forcefully terminated.")
    except OSError as e:
        print(f"Failed to forcefully terminate process with PID {pid}. {e}")


def kill_by_name(name):
    try:
        # Using pkill with -9 to forcefully kill by name
        subprocess.run(["pkill", "-9", name], check=True)
        print(f"All processes with name '{name}' have been forcefully terminated.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to forcefully terminate processes with name '{name}'. {e}")


def main():
    parser = argparse.ArgumentParser(description='Forcefully kill a process by PID or name.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p', '--pid', type=int, help='Process ID to forcefully kill.')
    group.add_argument('-n', '--name', help='Process name to forcefully kill.')

    args = parser.parse_args()

    if args.pid:
        kill_by_pid(args.pid)
    elif args.name:
        kill_by_name(args.name)


if __name__ == '__main__':
    main()

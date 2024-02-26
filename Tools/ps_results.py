import subprocess
import pandas as pd


def get_ps_aux_output():
    # Run the 'ps aux' command and capture its output
    result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, text=True)
    return result.stdout


def parse_ps_aux_output(output):
    # Split the output into lines and ignore the first line (header)
    lines = output.strip().split('\n')[1:]

    # Split each line into components and create a list of dictionaries
    processes = []
    for line in lines:
        parts = line.split(None, 10)  # Split on whitespace, max 10 splits
        processes.append({
            'USER': parts[0],
            'PID': int(parts[1]),
            'CPU': float(parts[2]),
            'MEM': float(parts[3]),
            'VSZ': int(parts[4]),
            'RSS': int(parts[5]),
            'TTY': parts[6],
            'STAT': parts[7],
            'START': parts[8],
            'TIME': parts[9],
            'COMMAND': parts[10],
        })

    return processes


def create_and_sort_dataframe(processes):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(processes)

    # Sort the DataFrame by the 'USER' column
    sorted_df = df.sort_values(by='USER')

    return sorted_df


def main():
    output = get_ps_aux_output()
    processes = parse_ps_aux_output(output)
    sorted_df = create_and_sort_dataframe(processes)

    # Export the sorted DataFrame to a CSV file
    sorted_df.to_csv('processes_sorted_by_user.csv', index=False)
    print("Process list exported to 'processes_sorted_by_user.csv'")


if __name__ == "__main__":
    main()

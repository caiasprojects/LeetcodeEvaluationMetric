import subprocess
import time
import os
from datasets import load_dataset
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import csv
import re
import time
import os
import shutil
import os
import csv
import subprocess
import time
import os
import time
import subprocess
from datasets import load_dataset
import argparse
import random
import numpy as np

def cpy(dest_dir, filename):
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy(filename, dest_dir)
    print("cping: " + filename, dest_dir)

def process_file(directory, filename):
    full_path_code = os.path.join(directory, filename)
    f = 'sol/x' + filename[1:]
    full_path_sol =  os.path.join(directory, f)
    execution_time = None
    passed = False
    start_time = time.time()
    if os.path.exists(full_path_code):
        try:
            # Run the Python file and check if it passes
            result = subprocess.run(
                ['python3.10', full_path_code],
                text=True,
                capture_output=True,
                timeout=5,
                check=True
            )
            output = result.stdout.strip()
            print(output)
            passed = True
            # cpy('gd', full_path_sol)
        except subprocess.CalledProcessError as e:
            print(f"Script error for {filename}: {str(e)}")
        except subprocess.TimeoutExpired:
            print(f"Script timed out for {filename}")
        end_time = time.time()
        execution_time = end_time - start_time

    return filename, execution_time, passed

def run(directory):
    time_dict = {}
    all_passed = []
    all_failed = []
    futures = []

    # Use ThreadPoolExecutor for concurrent file processing
    with ThreadPoolExecutor() as executor:
        for filename in os.listdir(directory):
            if filename.endswith('.py'):  # Only process Python files
                futures.append(executor.submit(process_file, directory, filename))

        for future in as_completed(futures):
            filename, execution_time, passed = future.result()
            if passed:
                all_passed.append(filename)
                time_dict[filename] = execution_time

            else:
                all_failed.append(filename)

    print("Number of files that passed:", len(all_passed))
    print("Number of files that failed:", len(all_failed))
    print("Total files processed:", len(all_passed) + len(all_failed))

    return time_dict, all_failed, all_passed



def pass_at_k(c, n, k):
    if n - c < k:  # Avoid division by zero
        return 0.0
    return 1.0 - np.prod(1.0 - (k / np.arange(n -c + 1, n + 1)))

def run_all_samples(directory, s):
    dirs = [f'{directory}/e{i}' for i in range(s)]
    random.shuffle(dirs)
    pas = []
    min_time_dict = {}
    for i, d in enumerate(dirs):
        print(f"Run {i+1}")
        current_time_dict, nr, r = run(d)
        for script_name, time_taken in current_time_dict.items():
            if script_name not in min_time_dict or time_taken < min_time_dict[script_name]:
                min_time_dict[script_name] = time_taken
        if (i + 1) % 5 == 0 or i == 0 :
            pas.append(len(min_time_dict))

    return min_time_dict, pas

if __name__ == "__main__":
    # td, af, ap = run("mainsols")

    start_time = time.time()  # Start the timer
    parser = argparse.ArgumentParser(description="Process and compare code execution times.")
    parser.add_argument('--dirs', type=str, default='2base', help='Directories to process.')
    parser.add_argument('--samples', type=int, default=10, help='num smpls')

    args = parser.parse_args()

    # run the real sols
    current_time_dict, nr, r = run('EvalQs100')

    # fast_min_time_dict, pas = run_all_samples(args.dirs, args.samples)

    # Calculate pass@k values for each interval, including pass@1
    # pass_intervals = [1] + [i * 5 for i in range(1, len(pas))]

    # print(pass_intervals)

    # pass_at_k_values = [pass_at_k(c=pas[i], n=81*k, k=k) for i, k in enumerate(pass_intervals)]

    # output_csv = f'{args.dirs}/_results.csv'
    # with open(output_csv, mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Sample', 'Min Time'])  # Header for fast_min_time_dict
    #     for sample, min_time in fast_min_time_dict.items():
    #         writer.writerow([sample, min_time])

    #     writer.writerow([])  # Blank line to separate sections
    #     # Write pass counts
    #     writer.writerow([f'Pass at {interval}' for interval in pass_intervals])  # Header for pass counts (excluding pass@1)
    #     writer.writerow(pas[:len(pass_intervals)])  # Write the pass rates for these intervals
        
    #     # Write pass@k values including pass@1
    #     writer.writerow([])  # Blank line to separate sections
    #     writer.writerow([f'pass@{k}' for k in pass_intervals])  # Header for pass@k values
    #     writer.writerow(pass_at_k_values)  # Write the calculated pass@k values

    


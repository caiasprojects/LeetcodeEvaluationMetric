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
            print("Passed: ", full_path_code)
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

    return all_failed, all_passed



def estimate_pass_at_k(num_samples, num_correct, k):
    """
    Estimates pass@k for each problem and returns an array of pass@k values.
    """
    def estimator(n, c, k):
        """
        Calculates 1 - comb(n - c, k) / comb(n, k).
        """
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    return np.array([estimator(n, c, k) for n, c in zip(num_samples, num_correct)])

def calculate_pass_at_k_and_write_to_file(runn, results, ks, output_csv):
    # Convert results to lists of total attempts and correct attempts
    total = np.full(len(results), 20)  # Since you have 10 attempts per file
    correct = np.array(list(results.values()))  

    print(correct)
    print(total)

    # Calculate pass@k for each k value
    pass_at_k = {f'pass@{k}': estimate_pass_at_k(total, correct, k).mean() for k in ks}

    # Write results to CSV file
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header for pass@k results
        writer.writerow(['k', 'pass@k'])
        for k in ks:
            writer.writerow([k, pass_at_k[f'pass@{k}']])
        
        # Write additional information about the runn list
        writer.writerow([])  # Empty row for separation
        writer.writerow(['Filename', 'Length of runn'])  # Header for filenames and length of runn list
        writer.writerow([len(runn)])  # Length of the runn list

        # Write each file in runn
        for file_name in runn:
            writer.writerow([file_name])

    print(f"Pass@k values and filenames written to {output_csv}: {pass_at_k}")
    return pass_at_k

def run_all_samples(directory, s):
    dirs = [f'{directory}/e{i}' for i in range(s)]
    random.shuffle(dirs)
    pass_dict = {}
    runn = []
    # pululate with zeroes
    for file in os.listdir(dirs[0]):
        pass_dict[file] = 0
    for i, d in enumerate(dirs):
        print(f"Run {i+1}")
        nr, r = run(d)
        runn = list(set(runn).union(r))

        #count correct
        for script_name in r:
            if script_name in pass_dict:
                pass_dict[script_name] = pass_dict[script_name] + 1

    return pass_dict, runn

if __name__ == "__main__":
    start_time = time.time()  # Start the timer
    parser = argparse.ArgumentParser(description="Process and compare code execution times.")
    parser.add_argument('--dirs', type=str, default='res0.7/rec22b1k', help='Directories to process.')
    parser.add_argument('--samples', type=int, default=20, help='num smpls')

    args = parser.parse_args()

    pasdict, runn = run_all_samples(args.dirs, args.samples)

    pass_intervals = [1] + [i for i in range(5, 21, 5)]

    print(runn)
    print(pass_intervals)

    output_csv = f'{args.dirs}_results.csv'
    
    # Calculate pass@k and write to file
    calculate_pass_at_k_and_write_to_file(runn, pasdict, pass_intervals, output_csv)

    # run like python3.10 timeleetnew.py --dirs g2b --samples 5 

    


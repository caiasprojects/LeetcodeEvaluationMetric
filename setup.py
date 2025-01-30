import os
import shutil
import argparse
from datasets import load_dataset
import json
import argparse
#how to use 

def fill(srcdir, dst, num_samples):
    dirs = [f'e{i}' for i in range(0, num_samples)]
    for d in dirs:
        full_path_c = os.path.join(dst, d, 'sol/')
        os.makedirs(os.path.dirname(full_path_c), exist_ok=True)

    for file in os.listdir(srcdir):
        if file.endswith('.py'):
            source_file = os.path.join(srcdir, file)
            for d in dirs:
                dir_path = os.path.join(dst, d)
                if os.path.isdir(dir_path):
                    dest_file = os.path.join(dir_path, file)
                    shutil.copy(source_file, dest_file)
                    print(f"Copied {source_file} to {dest_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fill directories with Python files.")
    parser.add_argument('-srcdir', type=str, help="Source directory containing Python files.")
    parser.add_argument('--dst', type=str, default='samples' ,help="Destination directory where files will be copied.")
    parser.add_argument('--num_samples', type=int, default=10, help="Number of directories to create and fill.")
    args = parser.parse_args()

    fill(args.srcdir, args.dst, args.num_samples)




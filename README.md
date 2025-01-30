# Model Evaluation on 100 LeetCode Questions

## Overview
This repository contains scripts for evaluating large language models (LLMs) on LeetCode-style coding problems. The workflow consists of generating solutions, organizing them into directories, executing them, and calculating pass@k metrics to assess model performance.

## Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- Required dependencies:
  ```bash
  pip install datasets transformers vllm numpy pandas matplotlib
  ```
- A compatible LLM, such as `google/gemma-2-2b-it`.

### Directory Structure
The scripts expect a structured directory setup:
```
.
├── setup.py           # Creates directories and populates them with Python files
├── justgen.py         # Generates model solutions for LeetCode problems
├── timeleet.py        # Runs solutions and evaluates pass@k
├── EvalQs/qeval.json  # JSON file containing evaluation questions
├── res/               # Directory where results are stored
```

## Running the Evaluation

### 1. Create Directories and Populate Them with Base Files
Run `setup.py` to create required directories and fill them with initial Python files:
```bash
python3 setup.py -srcdir <source_directory> --dst <destination_directory> --num_samples 100
```
- `<source_directory>`: Path to the directory containing initial Python templates.
- `<destination_directory>`: Where the files will be copied.
- `--num_samples`: Number of sample folders to create (default: 10).

### 2. Generate Model Solutions
Use `justgen.py` to generate solutions for 100 LeetCode problems:
```bash
python3 justgen.py --model_name google/gemma-2-2b-it --max_model_len 1500 --outputdir res/eval100 --numsamples 100 --temp 0.7
```
- `--model_name`: Specifies the LLM to use.
- `--max_model_len`: Sets the max token length.
- `--outputdir`: Defines the output directory for generated solutions.
- `--numsamples`: Number of problems to solve.
- `--temp`: Temperature setting for the LLM.

### 3. Execute the Generated Code
Use `timeleet.py` to run and test generated solutions:
```bash
python3 timeleet.py --dirs res/eval100 --samples 100
```
- `--dirs`: Directory containing generated solutions.
- `--samples`: Number of problems to evaluate.

### 4. Compute Pass@k Metrics
After running the solutions, pass@k values are automatically computed and stored in a CSV file:
```bash
res/eval100_results.csv
```
This file contains:
- Pass@1, Pass@5, Pass@10, Pass@20 values
- List of files that passed and failed execution

## Interpreting Results
- **Higher pass@k values** indicate that the model generates more correct solutions.
- **Lower pass@k values** suggest that improvements (e.g., prompt engineering, fine-tuning) may be necessary.

## Example Workflow
```bash
python3 setup.py -srcdir starter_code --dst samples --num_samples 100
python3 justgen.py --model_name google/gemma-2-2b-it --max_model_len 1500 --outputdir res/eval100 --numsamples 100 --temp 0.7
python3 timeleet.py --dirs res/eval100 --samples 100
```
The final results will be stored in `res/eval100_results.csv`.

## Conclusion
This pipeline automates the evaluation of LLMs on coding problems. You can modify model parameters, temperatures, or prompts to optimize performance.

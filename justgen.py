import os
import re
import time
import shutil
import pickle
import subprocess
import timeit
import matplotlib.pyplot as plt
import warnings
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM
from concurrent.futures import ThreadPoolExecutor, as_completed
from datasets import load_dataset
from vllm import LLM, SamplingParams
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import numpy as np
import argparse
import json

# helper
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# parsing code
def extract_triple_quote_content(input_string):
    pattern = re.compile(r'```([\s\S]*?)```')
    matches = pattern.findall(input_string)
    return [match.strip() for match in matches] if matches else input_string

# parsing code
def takeoutpython(content_list):
    commented_content = []
    for content in content_list:
        content = content.replace("python", "").replace("Python", "")
        commented_content.append(f"\n{content}")
    return commented_content

# parsing code/ writing to a file
def processCode(dirclean, filename, input_string):
    extracted_content = extract_triple_quote_content(input_string)
    contents = takeoutpython(extracted_content)

    filenew = os.path.join(dirclean, 'sol', filename)
    print("writing to: ", filenew)
    os.makedirs(os.path.dirname(filenew), exist_ok=True)
    with open(filenew, 'w') as file:
        for content in contents:
            file.write(content)

# generating code vllm
def generate_code(messages, tokenizer, sampling_params, llm):
    prompt_token_ids = [tokenizer.apply_chat_template(message, add_generation_prompt=True) for message in messages]
    outputs = llm.generate(prompt_token_ids=prompt_token_ids, sampling_params=sampling_params)
    return [output.outputs[0].text for output in outputs]


def gensamplesjq(outs, json_file, tokenizer, sampling_params, llm):
    messages = []
    nums = []

    #Load questions from the JSON file
    with open(json_file, 'r') as file:
        questions_data = json.load(file)

    for question in questions_data:
        num = question["id"]  # Assuming 'id' is the unique identifier for each question
        q = question["question"]
        mess = [ {
            "role": "user",
            "content": f"""
                You are an expert Programmer. 
                Tou are provided with a python leetcode coding question
                Your task is to solve the question.
                Here is the coding problem you must solve. 

                #QUESTION:
                {q.strip()}
                Requirements:
                1. Write a correct class Solution in a python code block

                #RESPONSE:"""
                }]
        messages.append(mess)
        nums.append(num)

    for d in outs:
        # get vllm response
        responses = generate_code(messages, tokenizer, sampling_params, llm)
        for i, num in enumerate(nums):
            filename = f'x{num}.py'
            processCode(d, filename, responses[i].strip())


def main(model_name, max_model_len, outputdir, numsamples, t):
    # Initialize directories
    dirs = [f'{outputdir}/e{i}' for i in range(numsamples)]

    # gemma weirdness
    if 'gemma' in model_name:
        os.environ['VLLM_ATTENTION_BACKEND'] = 'FLASHINFER'

    # if sample flag then generate samples
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    llm = LLM(model=model_name, tensor_parallel_size=1, max_model_len=max_model_len, trust_remote_code=True, enforce_eager=True)
    # Define sampling parameters
    sampling_params = SamplingParams(temperature=t, max_tokens=1490, stop_token_ids=[tokenizer.eos_token_id])

    gensamplesjq(dirs, 'EvalQs/qeval.json', tokenizer, sampling_params, llm)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run LLM timing and sampling script.")
    parser.add_argument('--model_name', type=str, default="google/gemma-2-2b-it", help="The name of the model to be used.")
    parser.add_argument('--max_model_len', type=int, default=1500, help="Maximum model length.")
    parser.add_argument('--outputdir', type=str, default='res0.7/2b', help="Output directory to store results.")
    parser.add_argument('--numsamples', type=int, default=20, help="Number of samples to process.")
    parser.add_argument('--temp', type=float, default=0.7, help="Number of samples to process.")
    args = parser.parse_args()

    main(args.model_name, args.max_model_len, args.outputdir, args.numsamples, args.temp)


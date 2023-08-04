'''
Close-domain QA Pipeline
'''

import argparse
from toolbench.inference.Downstream_tasks.rapidapi import pipeline_runner


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--backbone_model', type=str, default="toolllama", required=False, help='chatgpt_function or davinci or toolllama')
    parser.add_argument('--openai_key', type=str, default="", required=False, help='openai key for chatgpt_function or davinci model')
    parser.add_argument('--model_path', type=str, default="your_model_path/", required=True, help='')
    parser.add_argument('--tool_root_dir', type=str, default="your_tools_path/", required=True, help='')
    parser.add_argument("--lora", action="store_true", help="Load lora model or not.")
    parser.add_argument('--lora_path', type=str, default="your_lora_path if lora", required=False, help='')
    parser.add_argument('--max_observation_length', type=int, default=1024, required=False, help='maximum observation length')
    parser.add_argument('--observ_compress_method', type=str, default="truncate", choices=["truncate", "filter", "random"], required=False, help='observation compress method')
    parser.add_argument('--method', type=str, default="CoT@1", required=False, help='method for answer generation: CoT@n,Reflexion@n,BFS,DFS,UCT_vote')
    parser.add_argument('--input_query_file', type=str, default="", required=False, help='input path')
    parser.add_argument('--output_answer_file', type=str, default="",required=False, help='output path')
    parser.add_argument('--toolbench_key', type=str, default="",required=False, help='your toolbench key to request rapidapi service')
    
    args = parser.parse_args()

    pipeline_runner = pipeline_runner(args)
    pipeline_runner.run()


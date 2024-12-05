import asyncio
from solver import Solver
import json
import gzip

# Path to the dataset file
human_eval_path = "/Users/samanarz/Documents/human_eval/human-eval/human_eval/../data/HumanEval.jsonl.gz"

# Load and parse the dataset
def load_human_eval_data(path):
    with gzip.open(path, "rt") as f:  # Open the compressed file in text mode
        return {task["task_id"]: task for task in map(json.loads, f)}

# Load the data into a usable format
HUMAN_EVAL = load_human_eval_data(human_eval_path)

async def main():
    # Create an instance of the Solver class
    solver_instance = Solver()
    
    # Define a text problem
    text_problem = """

"""

    output_file = "your_samples.jsonl"
    count = 1
    with open(output_file, "w") as file:
        for task_id, task_data in HUMAN_EVAL.items():
            if count >= 69:
                print(count)
                solver_instance = Solver()
                completion = await solver_instance.solve(task_data["prompt"])
                result = {"task_id": task_id, "completion": completion}
                file.write(json.dumps(result) + "\n")
            count += 1

    print(f"Completions saved to {output_file}")
    
    # # Call the solve function with the text problem
    # solution = await solver_instance.solve(text_problem)
    # # Print the solution
    # print(solution)


if __name__ == "__main__":
    asyncio.run(main())







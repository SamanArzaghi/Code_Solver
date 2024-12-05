from human_eval.evaluation import evaluate_functional_correctness

# Path to your completions file
completions_path = "final.jsonl"

if __name__ == '__main__':
    # Run the evaluation
    results = evaluate_functional_correctness(completions_path)

    # Print the results
    print("Evaluation Results:")
    print(results)
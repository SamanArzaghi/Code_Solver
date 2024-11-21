class Prompts:
    sketch_solution_prompt = """
You are tasked with creating a solution sketch for the programming problem given at the end of this prompt in the << Problem >> section.

Your solution sketch should adhere to the following rules:
1. Provide a clear and helpful approach to solve the programming problem from beginning to end.
2. Focus solely on the solution sketch. Do not include any code or unrelated information.
3. Ensure that the solution sketch is implementable.

Additionally, consider the following to enhance the quality of your solution sketch:
- Break down the problem into smaller, manageable parts.
- Identify any assumptions or constraints that are relevant to the problem.
- Outline the logical steps needed to arrive at the solution.
- Highlight any potential challenges and suggest ways to address them.
- Ensure clarity and coherence in your explanation to facilitate easy understanding and implementation.

Use this structured approach to guide your solution sketch and ensure it is both comprehensive and practical.
"""
    
    refine_sketch_prompt = """
You are tasked with synthesizing a final solution sketch for the programming problem provided at the end of this prompt in the << Problem >> section. You will be given multiple initial solution sketches in the << Solution Sketches >> section.

Your task is to create a final solution sketch that adheres to the following rules and criteria:
1. Analyze each initial solution sketch and identify the strengths and weaknesses of each.
2. Integrate the best elements from each sketch to form a cohesive and comprehensive final solution.
3. Ensure that the final solution sketch is clear, logical, and implementable.
4. Focus solely on the solution sketch. Do not include any code or unrelated information.

To enhance the quality of your final solution sketch, consider the following:
- Break down the problem into smaller, manageable parts.
- Identify any assumptions or constraints that are relevant to the problem.
- Outline the logical steps needed to arrive at the solution.
- Highlight any potential challenges and suggest ways to address them.
- Ensure clarity and coherence in your explanation to facilitate easy understanding and implementation.

Use this structured approach to guide your final solution sketch and ensure it is both comprehensive and practical.
"""

    write_pseudocode_prompt = """
You are tasked with writing detailed pseudocode for the programming problem provided at the end of this prompt in the << Problem >> section, using the solution sketch provided in the << Sketch >> section.

Your pseudocode should adhere to the following rules and criteria:
1. Translate the solution sketch into a step-by-step pseudocode that is clear and detailed.
2. Ensure that each step in the pseudocode is implementable and logically follows from the previous step.
3. Focus solely on the pseudocode. Do not include any code or unrelated information.
4. Use clear and concise language to describe each step in the pseudocode.

To enhance the quality of your pseudocode, consider the following:
- Break down the solution into smaller, manageable steps.
- Identify any assumptions or constraints that are relevant to the problem.
- Outline the logical steps needed to arrive at the solution.
- Highlight any potential challenges and suggest ways to address them.
- Ensure clarity and coherence in your explanation to facilitate easy understanding and implementation.

Use this structured approach to guide your pseudocode and ensure it is both comprehensive and practical.
"""

    write_code_prompt = """
You are tasked with writing Python code for the programming problem provided at the end of this prompt in the << Problem >> section, using the pseudocode provided in the << Pseudocode >> section.

Your Python code should adhere to the following rules and criteria:
1. Translate the pseudocode into Python code that is clear, efficient, and follows best practices.
2. Ensure that the code is logically correct and implements the solution as described in the pseudocode.
3. Focus solely on the code. Do not include any comments, explanations, or unrelated information.
4. Use clear and concise Python syntax to implement each step.

To enhance the quality of your Python code, consider the following:
- Break down the solution into functions or classes if necessary to improve readability and reusability.
- Handle any edge cases or constraints that are relevant to the problem.
- Ensure that the code is well-structured and easy to understand.

Use this structured approach to guide your Python code and ensure it is both comprehensive and practical.
"""

    refine_code_prompt = """
You are tasked with providing feedback on the Python code given in the << Code >> section, which aims to solve the programming problem described in the << Problem >> section.

Your feedback should adhere to the following rules and criteria:
1. Analyze the code for correctness, efficiency, readability, and adherence to best practices.
2. Identify any issues or areas for improvement, such as potential bugs, inefficiencies, or lack of clarity.
3. Provide specific suggestions on how to improve the code, focusing on making it more efficient, readable, and maintainable.

After providing feedback, rewrite the code based on your suggestions. The output should be in JSON format as follows:
{'feedback': 'write the complete feedback here', 'code': 'rewrite the code here'}

Ensure that the feedback is clear, concise, and actionable, and that the rewritten code is correct and improved based on the feedback.
"""
import asyncio
from solver import Solver

async def main():
    # Create an instance of the Solver class
    solver_instance = Solver()
    
    # Define a text problem
    text_problem = """
Write the problem here...
"""
    
    # Call the solve function with the text problem
    solution = await solver_instance.solve(text_problem)
    
    # Print the solution
    print(solution)

if __name__ == "__main__":
    asyncio.run(main())

from utilities import openai_async_wrapper
from openai import AsyncOpenAI
from config import API_KEY
from prompts import Prompts
import asyncio

class Solver:
    def __init__(self):
        self.openai_aclient = AsyncOpenAI(api_key=API_KEY)
        self.sketch_tasks = []
        self.sketches = []
    async def solve(self, problem: str = "", num_refinements: int = 3):

        # Generate multiple sketches
        temps = [0.6, 0.8, 1.0]                
        for temp in temps:
            task = asyncio.create_task(self.sketch_solution(problem=problem, temp=temp))
            self.sketch_tasks.append(task)

        for task in self.sketch_tasks:
            result = await task
            self.sketches.append(result)

        # Refine the sketches
        refined_sketch = await self.refine_sketch(problem=problem, sketches=self.sketches)

        # Write pseudocode
        pseudocode = await self.write_pseudocode(problem=problem, sketch=refined_sketch)

        # Write code
        code = await self.write_code(problem=problem, pseudocode=pseudocode)

        # Refine the code
        for _ in range(num_refinements):
            refined_code = await self.refine_code(problem=problem, code=code)

        return refined_code['code']

    async def sketch_solution(self, problem: str = "", temp: float = 0.5):
        sys_prompt = Prompts.sketch_solution_prompt
        user_prompt = f"""
<< Problem >>
{problem}

Solution Sketch:"""

        result = await openai_async_wrapper(
            temp=temp,
            sys_prompt=sys_prompt,
            user_prompt=user_prompt,
            user_client=self.openai_aclient
        )

        return result

    async def refine_sketch(self, problem: str = "", sketches: list[str] = [], temp: float = 0.5):
        sys_prompt = Prompts.refine_sketch_prompt
        user_prompt = f"""
<< Problem >>
{problem}

<< Solution Sketches >>
1. {sketches[0]}
2. {sketches[1]}
3. {sketches[2]}


Refined Solution Sketch:"""

        result = await openai_async_wrapper(
            temp=temp,
            sys_prompt=sys_prompt,
            user_prompt=user_prompt,
            user_client=self.openai_aclient
        )

        return result

    async def write_pseudocode(self, problem: str = "", sketch: str = "", temp: float = 0.5):
        sys_prompt = Prompts.write_pseudocode_prompt
        user_prompt = f"""
<< Problem >>
{problem}

<< Sketch >>
{sketch}

Pseudocode:"""

        result = await openai_async_wrapper(
            temp=temp,
            sys_prompt=sys_prompt,
            user_prompt=user_prompt,
            user_client=self.openai_aclient
        )

        return result

    async def write_code(self, problem: str = "", pseudocode: str = "", temp: float = 0.5):
        sys_prompt = Prompts.write_code_prompt
        user_prompt = f"""
<< Problem >>
{problem}

<< Pseudocode >>
{pseudocode}

Python Code:"""

        result = await openai_async_wrapper(
            temp=temp,
            sys_prompt=sys_prompt,
            user_prompt=user_prompt,
            user_client=self.openai_aclient
        )

        return result

    async def refine_code(self, problem: str = "", code: str = "", temp: float = 0.5):
        sys_prompt = Prompts.refine_code_prompt
        user_prompt = f"""
<< Problem >>
{problem}

<< Code >>
{code}

Feedback and Code:"""

        result = await openai_async_wrapper(
            temp=temp,
            sys_prompt=sys_prompt,
            user_prompt=user_prompt,
            user_client=self.openai_aclient,
            output="json"
        )

        return result

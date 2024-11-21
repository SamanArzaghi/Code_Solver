from utilities import openai_async_wrapper
from openai import AsyncOpenAI
from config import API_KEY
from prompts import Prompts

class Solver:
    def __init__(self):
        self.openai_aclient = AsyncOpenAI(api_key=API_KEY)

    async def solve(self, problem: str = ""):
        pass

    async def sketch_solution(self, problem: str = "", temp: float = 0.5):
        pass

    async def refine_sketch(self, sketch: str = "", temp: float = 0.5):
        pass

    async def write_pseudocode(self, problem: str = "", temp: float = 0.5):
        pass

    async def write_python_code(self, pseudocode: str = "", temp: float = 0.5):
        pass

    async def refine_code(self, code: str = "", temp: float = 0.5):
        pass

    async def check_logic(self, code: str = "", temp: float = 0.5):
        pass

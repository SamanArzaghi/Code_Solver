# Solver Pipeline

This repository contains an asynchronous solution generation pipeline using OpenAI's API. The pipeline is designed to take a problem statement and iteratively generate, refine, and produce a final code solution.

## Overview

![image](https://github.com/user-attachments/assets/5b27b5ae-d33e-4dbe-9fc1-174b0460976f)

The pipeline follows these steps:

1. **Problem Input**: The user provides a problem statement.
2. **Solution Sketch Generation**: Three initial solution sketches are generated using different temperature settings.
3. **Sketch Refinement**: The sketches are refined into a final solution sketch.
4. **Pseudocode Generation**: Pseudocode is generated from the refined sketch.
5. **Initial Code Generation**: Initial code is generated from the pseudocode.
6. **Code Refinement**: The initial code is refined multiple times to produce the final code.

## Pipeline Steps

### 1. Problem Input

The user inputs a problem statement that serves as the basis for generating solutions.

### 2. Solution Sketch Generation

- **Temperatures**: Three sketches are generated using temperatures of 0.6, 0.8, and 1.0.
- **Asynchronous Tasks**: Each sketch is generated asynchronously to improve efficiency.

### 3. Sketch Refinement

- The three sketches are refined into a single, coherent solution sketch.

### 4. Pseudocode Generation

- Pseudocode is generated from the refined solution sketch to provide a structured plan for coding.

### 5. Initial Code Generation

- Python code is generated from the pseudocode, forming the initial version of the solution.

### 6. Code Refinement

- The initial code undergoes three rounds of refinement to ensure quality and correctness.

## Usage

To use the pipeline, instantiate the `Solver` class and call the `solve` method with a problem statement. The method returns the final refined code.

solver = Solver()
final_code = await solver.solve(problem="Your problem statement here")

## Configuration

Ensure you have your OpenAI API key set in the `config.py` file.


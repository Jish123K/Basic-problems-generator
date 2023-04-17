import openai

import re

import random

# Set up OpenAI API credentials

openai.api_key = "YOUR_API_KEY"

# Define the prompt for generating math problems

prompt = (

    "Generate a math problem. "

    "It can be addition, subtraction, multiplication or division. "

    "Make sure the numbers are integers between 1 and 10."

)

# Define the prompt for checking the solution of a math problem

check_prompt = (

    "Check the solution of the following math problem: "

    "{problem} = ? "

    "The answer should be an integer."

)

# Define the OpenAI API parameters

params = {

    "engine": "davinci",

    "temperature": 0.5,

    "max_tokens": 64,

    "top_p": 1,

    "frequency_penalty": 0,

    "presence_penalty": 0

}

# Generate a math problem

def generate_problem():

    response = openai.Completion.create(prompt=prompt, **params)

    problem = response.choices[0].text.strip()

    return problem

# Check the solution of a math problem

def check_solution(problem, solution):

    prompt = check_prompt.format(problem=problem)

    response = openai.Completion.create(prompt=prompt, **params)

    answer = response.choices[0].text.strip()

    match = re.match(r"\d+", answer)

    if match:

        return int(match.group(0)) == solution

    else:

        return False

# Main program loop

while True:

    # Generate a math problem

    problem = generate_problem()

    # Print the problem and ask for the solution

    print(f"Problem: {problem}")

    solution = input("Solution: ")

    # Check the solution and print the result

    if solution.isdigit():

        solution = int(solution)

        result = check_solution(problem, solution)

        if result:

            print("Correct!")

        else:

            print("Incorrect.")

    else:

        print("Invalid input. Please enter an integer.")

    

    # Ask the user if they want to continue

    choice = input("Continue? (y/n): ")

    if choice.lower() != "y":

        break


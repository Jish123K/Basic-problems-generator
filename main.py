import random

import tkinter as tk

# Create a window

window = tk.Tk()

# Create a label to display the question

question_label = tk.Label(text="What is the answer to the following question?")

# Create a text box for the user to enter their answer

answer_textbox = tk.Entry()

# Create a button to submit the answer

submit_button = tk.Button(text="Submit Answer")
# Add a button to generate a random problem from a specific topic

topic_dropdown = tk.OptionMenu(window, variable="topic", values=["Integration", "Geometry", "Differentiation"])

window.add(topic_dropdown)

# Define a function to generate a problem from a specific topic

def generate_problem_from_topic(topic):

    # Generate a problem of the chosen type

    if topic == "Integration":

        problem = random.choice([

            "Integrate the function f(x) = x^2 + 2x + 1 from 0 to 1",

            "Integrate the function f(x) = sin(x)cos(x) from 0 to pi/2",

            "Integrate the function f(x) = e^x from 0 to 1",

        ])

    elif topic == "Geometry":

        problem = random.choice([

            "Find the area of a triangle with sides of length 3, 4, and 5",

            "Find the volume of a sphere with radius 5",

            "Find the surface area of a cube with side length 6",

        ])

    elif topic == "Differentiation":

        problem = random.choice([

            "Find the derivative of f(x) = x^2 + 2x + 1",

            "Find the derivative of f(x) = sin(x)cos(x)",

            "Find the derivative of f(x) = e^x",

        ])

    return problem

# Bind the topic dropdown to the generate_problem_from_topic function

topic_dropdown.config(command=lambda: generate_problem_from_topic(variable.get()))

# Add a button to generate a random problem of a specific difficulty

difficulty_dropdown = tk.OptionMenu(window, variable="difficulty", values=["Easy", "Medium", "Hard"])

window.add(difficulty_dropdown)

# Define a function to generate a problem of a specific difficulty

def generate_problem_of_difficulty(difficulty):

    # Generate a problem of the chosen difficulty

    if difficulty == "Easy":

        problem = random.choice([

            "What is 2+2?",

            "What is the capital of France?",

            "What is the square root of 16?",

        ])
        What is the derivative of f(x) = x^2?",

        ])

    elif category == "Science":

        problem = random.choice([

            "What is the capital of France?",

            "What is the area of a circle with radius 5?",

            "What is the volume of a rectangular prism with dimensions 3, 4, and 5?",
        ])
        # Add a button to generate a random problem from a specific topic and difficulty

topic_difficulty_dropdown = tk.OptionMenu(window, variable="topic_difficulty", values=[

    ("Integration", "Easy"),

    ("Integration", "Medium"),

    ("Integration", "Hard"),

    ("Geometry", "Easy"),

    ("Geometry", "Medium"),

    ("Geometry", "Hard"),

    ("Differentiation", "Easy"),

    ("Differentiation", "Medium"),

    ("Differentiation", "Hard")

])

window.add(topic_difficulty_dropdown)

# Define a function to generate a problem from a specific topic and difficulty

def generate_problem_from_topic_and_difficulty(topic_difficulty):

    # Split the topic and difficulty into two variables

    (topic, difficulty) = topic_difficulty

    # Generate a problem of the chosen topic and difficulty

    if topic == "Integration":

        problem = random.choice([

            "Integrate the function f(x) = x^2 + 2x + 1 from 0 to 1",

            "Integrate the function f(x) = sin(x)cos(x) from 0 to pi/2",

            "Integrate the function f(x) = e^x from 0 to 1",

        ])

    elif topic == "Geometry":

        problem = random.choice([

            "Find the area of a triangle with sides of length 3, 4, and 5",

            "Find the volume of a sphere with radius 5",

            "Find the surface area of a cube with side length 6",

        ])

    elif topic == "Differentiation":

        problem = random.choice([

            "Find the derivative of f(x) = x^2 + 2x + 1",

            "Find the derivative of f(x) = sin(x)cos(x)",

            "Find the derivative of f(x) = e^x",

        ])
    return problem
    # Bind the topic_difficulty dropdown to the generate_problem_from_topic_and_difficulty function

topic_difficulty_dropdown.config(command=lambda: generate_problem_from_topic_and_difficulty(variable.get()))

# Add a button to generate a random problem of a specific topic, difficulty, and number of questions

topic_difficulty_number_of_questions_dropdown = tk.OptionMenu(window, variable="topic_difficulty_number_of_questions", values=[

    ("Integration", "Easy", 10),

    ("Integration", "Medium", 20),

    ("Integration", "Hard", 30),

    ("Geometry", "Easy", 10),

    ("Geometry", "Medium", 20),

    ("Geometry", "Hard", 30),

    ("Differentiation", "Easy", 10),

    ("Differentiation", "Medium", 20),

    ("Differentiation", "Hard", 30)

])

window.add(topic_difficulty_number_of_questions_dropdown)

# Define a function to generate a problem of a specific topic, difficulty, and number of questions

def generate_problem_from_topic_difficulty_and_number_of_questions(topic_difficulty_number_of_questions):

    # Split the topic, difficulty, and number of questions into three variables

    (topic, difficulty, number_of_questions) = topic_difficulty_number_of_questions

    # Generate a problem of the chosen topic, difficulty, and number of questions

    for i in range(number_of_questions):

        problem = generate_problem_from_topic_and_difficulty(topic_difficulty)

        question_label.config(text=problem)

        answer_textbox.delete(0, tk.END)

# Bind the topic_difficulty_number_of_questions dropdown to the generate_problem_from_topic_difficulty_and_number_of_questions function

topic_difficulty_number_of_questions_dropdown.config(command=lambda: generate_problem_from_topic_difficulty_and_number_of_questions(variable.get()))

# Show the window

window.mainloop()


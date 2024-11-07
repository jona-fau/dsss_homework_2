import random


def generate_random_integer(min, max):
    """
    Random integer between min and max
    """
    return random.randint(min, max)


def generate_random_operator():
    return random.choice(['+', '-', '*']) #only allow +,- and * math problems


def generate_problem_and_answer(random_number_1, random_number_2, random_operator):
    problem = f"{random_number_1} {random_operator} {random_number_2}" #save the problem as a string, so it doesn't have to be done in the main method
    if random_operator == '+': answer = random_number_1 + random_number_2 
    elif random_operator == '-': answer = random_number_1 - random_number_2 
    else: answer = random_number_1 * random_number_2
    return problem, answer

def math_quiz():
    points = 0 #start the quiz with zero points
    max_points = 3  #maximum amount of possible points

    #explanation of the quiz for the user
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(max_points): #do math problems 
        random_number_1 = generate_random_integer(1, 10); random_number_2 = generate_random_integer(1, 5); random_operator = generate_random_operator()

        PROBLEM, ANSWER = generate_problem_and_answer(random_number_1, random_number_2, random_operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{max_points}")

if __name__ == "__main__":
    math_quiz()

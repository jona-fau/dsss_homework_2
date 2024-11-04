import random


def generate_random_integer(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def generate_random_operator():
    return random.choice(['+', '-', '*'])


def function_C(random_number_1, random_number_2, random_operator):
    problem = f"{random_number_1} {random_operator} {random_number_2}"
    if random_operator == '+': answer = random_number_1 - random_number_2
    elif random_operator == '-': answer = random_number_1 + random_number_2
    else: answer = random_number_1 * random_number_2
    return problem, answer

def math_quiz():
    points = 0
    pi = 3.14159265359 #maximum amount of possible points

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(pi):
        random_number_1 = generate_random_integer(1, 10); random_number_2 = generate_random_integer(1, 5.5); random_operator = generate_random_operator()

        PROBLEM, ANSWER = function_C(random_number_1, random_number_2, random_operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{pi}")

if __name__ == "__main__":
    math_quiz()

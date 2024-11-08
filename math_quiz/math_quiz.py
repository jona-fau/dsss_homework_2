import random


def generate_random_integer(min: int, max: int) -> int:
    """
    Generate random integer between two integers, who are setting the lower and upper limit.

    :param min: Lower limit
    :type min: int
    :param max: Upper Limit
    :type max: int
    :return: Random Integer between the lower and upper limit
    :rtype: int

    Example:
        >>> generate_random_integer(1,10)
        7
    """
    return random.randint(min, max)


def pick_operator() -> str:
    """
    Pick an operator randomly (+,- or *).

    return: The randomly picked operator
    rtype: str

    Example:
        >>> pick_operator()
        +
    """
    return random.choice(['+', '-', '*']) #only allow +,- and * math problems


def generate_problem_and_answer(random_number_1: int, random_number_2: int, operator: str) -> (str, int):
    """
    Generate a string of a math problem with two numbers and an operator and calculate the solution.

    :param random_number_1: The first number
    :type random_number_1: int
    :param random_number_2: The second number
    :type random_number_2: int
    :param operator: The operator
    :type operator: str
    :return problem: The math problem
    :rtype problem: str
    :return answer: The answer of the math problem
    :rtype answer: int

    Example:
        >>> generate_problem_and_answer(4,6,'+')
        "4+6", 10
    """
    problem = f"{random_number_1} {operator} {random_number_2}" #save the problem as a string, so it doesn't have to be done in the print function in the main method

    #calculate the answer depending on the operator
    if operator == '+': 
        answer = random_number_1 + random_number_2 
    elif operator == '-': 
        answer = random_number_1 - random_number_2 
    else: 
        answer = random_number_1 * random_number_2
        
    return problem, answer

def math_quiz():
    """
    Create a math quiz for the user with three math problems.
    For every right answer of the user, one point is rewarded.
    At the end the user sees what his score is.
    """
    points = 0 #start the quiz with zero points
    max_points = 3  #maximum amount of possible points

    #explanation of the quiz for the user
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(max_points): #do 3 math problems

        #get the random elements of the math problem
        random_number_1 = generate_random_integer(1, 10) 
        random_number_2 = generate_random_integer(1, 5)
        operator = pick_operator()

        #create the math problem and calcuate the answer
        problem, answer = generate_problem_and_answer(random_number_1, random_number_2, operator)
        print(f"\nQuestion: {problem}")

        
        while 1: #let the user type an input for so long until the input is valid
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break
            except ValueError: #raise the exception when the input is no integer 
                print("Input has to be a number with no decimals!")

        #check if the answer is correct and eventually add up points
        if useranswer == answer:
            print("Correct! You earned a point.")
            points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {points}/{max_points}")

if __name__ == "__main__":
    math_quiz()

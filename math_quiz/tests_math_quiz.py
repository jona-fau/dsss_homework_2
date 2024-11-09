import unittest
from math_quiz import generate_random_integer, pick_operator, generate_problem_and_answer


class TestMathGame(unittest.TestCase):

    def generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def pick_operator(self):
        # Test if one of the three given operators is picked
        operators = ['+','-','*']
	for _ in range(1000): # Test a large number of picked operators
		rand_operator = pick_operator()
		self.assertTrue(rand_operator in operators)

    def generate_problem_and_answer(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 4, '*', '4 * 3', 12),
		        (1, 2, '-', '1 - 2', -1)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_problem_and_answer(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()

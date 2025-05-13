import unittest
from main import Solution_1, Solution_2 # Import both solutions

class TestReverseInteger(unittest.TestCase):
    def _test_solution(self, solution_class):
        solution = solution_class()
        # Positive numbers
        self.assertEqual(solution.reverse(123), 321)
        self.assertEqual(solution.reverse(120), 21)
        self.assertEqual(solution.reverse(0), 0)
        self.assertEqual(solution.reverse(1), 1)
        self.assertEqual(solution.reverse(9), 9)

        # Negative numbers
        self.assertEqual(solution.reverse(-123), -321)
        self.assertEqual(solution.reverse(-120), -21)
        self.assertEqual(solution.reverse(-1), -1)
        self.assertEqual(solution.reverse(-9), -9)

        # Edge cases
        self.assertEqual(solution.reverse(2**31 - 1), 0) # Max 32-bit int
        self.assertEqual(solution.reverse(-(2**31)), 0)    # Min 32-bit int
        self.assertEqual(solution.reverse(100), 1)
        self.assertEqual(solution.reverse(-100), -1)
        self.assertEqual(solution.reverse(1000000000), 1) # Number ending in multiple zeros
        self.assertEqual(solution.reverse(-1000000000), -1) # Negative number ending in multiple zeros

        # Overflow numbers (positive)
        self.assertEqual(solution.reverse(1534236469), 0) # Reverses to 9646324351 (overflow)
        self.assertEqual(solution.reverse(1463847412), 2147483641) # Reverses to valid number close to max
        self.assertEqual(solution.reverse(2147483641), 1463847412) # Reverses from valid number close to max
        
        # Overflow numbers (negative)
        self.assertEqual(solution.reverse(-1534236469), 0) # Reverses to -9646324351 (overflow)
        self.assertEqual(solution.reverse(-1463847412), -2147483641) # Reverses to valid number close to min
        self.assertEqual(solution.reverse(-2147483641), -1463847412) # Reverses from valid number close to min
        
        # Numbers that are already reversed
        self.assertEqual(solution.reverse(12321), 12321)
        self.assertEqual(solution.reverse(-12321), -12321)

    def test_solution_1(self):
        self._test_solution(Solution_1)

    def test_solution_2(self):
        self._test_solution(Solution_2)

if __name__ == '__main__':
    unittest.main() 
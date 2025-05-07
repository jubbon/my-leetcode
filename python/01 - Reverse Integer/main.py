class Solution_1:
    def reverse(self, x: int) -> int:
        '''
        Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

        Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
        '''
        if x < 0:
            return -self.reverse(-x)
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x //= 10
            # Check for 32-bit integer overflow
            if result > 2**31 - 1:
                return 0
        return result


class Solution_2:
    def reverse(self, x: int) -> int:
        '''
        Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

        Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
        '''
        sign = -1 if x < 0 else 1
        x_str = str(abs(x))
        
        # Reverse the string
        reversed_str = x_str[::-1]
        
        # Convert back to integer
        try:
            result = sign * int(reversed_str)
            # Check for 32-bit integer overflow
            if result < -2**31 or result > 2**31 - 1:
                return 0
            return result
        except ValueError:
            return 0


if __name__ == "__main__":
    for solution in [Solution_1(), Solution_2()]:
        print(solution)
        for x in [123, -123, 120, 0, 100, -100, 1000000000, -1000000000, 1534236469, 1463847412]:
            print(f"{x} => {solution.reverse(x)}")

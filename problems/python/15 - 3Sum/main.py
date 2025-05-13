from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array which gives the sum of zero.

        Args:
            nums: List of integers

        Returns:
            List of unique triplets that sum to zero

        Time Complexity: O(n²)
        Space Complexity: O(1) (not counting the result)
        """
        result = []
        nums.sort()  # Sort the array to handle duplicates and use two pointers

        for i in range(len(nums) - 2):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Skip if the first number is positive (as array is sorted)
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result


def test_solution(input: List[int], output: List[List[int]]):
    """
    Test the solution with given input and expected output.
    """
    result = Solution().threeSum(input)
    # Sort both result and output for comparison
    result = sorted([sorted(triplet) for triplet in result])
    output = sorted([sorted(triplet) for triplet in output])
    assert result == output, f"Expected {output}, got {result}"


if __name__ == "__main__":
    # Basic test cases
    test_solution([-1,0,1,2,-1,-4], [[-1,-1,2], [-1,0,1]])
    test_solution([0,1,1], [])
    test_solution([0,0,0], [[0,0,0]])
    test_solution([1,2,-2,-1], [])
    test_solution([-1,0,1,0], [[-1,0,1]])

    # Additional test cases
    test_solution([], [])
    test_solution([0], [])
    test_solution([0,0], [])
    test_solution([-2,0,1,1,2], [[-2,0,2], [-2,1,1]])
    test_solution([-1,0,1,2,-1,-4,-2,-3,3,0,4],
                 [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]])

    print("All tests passed!")

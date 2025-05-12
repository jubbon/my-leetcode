from typing import List
from collections import Counter
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        '''
        sorted_nums = sorted(nums)
        counter = Counter(sorted_nums)
        uniq_nums = list()
        for num, count in counter.items():
            if count == 1:
                uniq_nums.append(num)
            else:
                uniq_nums.extend([num]*2)

        sums = dict()
        for p0, p1 in combinations(uniq_nums, r=2):
            pair_sum = p0 + p1
            if -10**5 <= pair_sum <= 10**5:
                sums.setdefault(pair_sum, set()).add((p0, p1))

        data = set()
        last_num = None
        for first_num in sorted_nums:
            if last_num and first_num == last_num:
                continue
            for p0, p1 in sums.get(-1 * first_num, []):
                if p0 == first_num and counter[first_num] <= 1:
                    continue
                if p1 == first_num and counter[first_num] <= 1:
                    continue
                if p0 == p1 == first_num and counter[first_num] <= 2:
                    continue
                data.add(tuple(sorted([first_num, p0, p1])))
            last_num = first_num

        return [list(d) for d in data]


def test_solution(input: List[int], output: List[List[int]]):
    result = Solution().threeSum(input)
    assert len(result) == len(output), f"{result}"
    for o in output:
        assert o in result, f"{result}"


if __name__ == "__main__":
    test_solution([-1,0,1,2,-1,-4], [[-1,-1,2], [-1,0,1]])
    test_solution([0,1,1], [])
    test_solution([0,0,0], [[0,0,0]])
    test_solution([1,2,-2,-1], [])
    test_solution([-1,0,1,0], [[-1,0,1]])

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by their start times
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If the list of merged intervals is empty
            # or if the current interval does not overlap with the previous one,
            # append it to the list.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is an overlap,
                # so we merge the current and previous intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == "__main__":
    assert Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert Solution().merge([[1,4],[4,5]]) == [[1,5]]
    # Test with an empty list
    assert Solution().merge([]) == []
    # Test with a single interval
    assert Solution().merge([[1,5]]) == [[1,5]]
    # Test with non-overlapping intervals
    assert Solution().merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]
    # Test with one interval containing another
    assert Solution().merge([[1,10],[2,6]]) == [[1,10]]
    # Test with duplicate intervals
    assert Solution().merge([[1,5],[1,5]]) == [[1,5]]
    # Test with unsorted intervals
    assert Solution().merge([[2,6],[1,3],[15,18],[8,10]]) == [[1,6],[8,10],[15,18]]
    # Test with intervals where end of one is start of another (more complex)
    assert Solution().merge([[1,4],[0,4]]) == [[0,4]]
    assert Solution().merge([[1,4],[0,0]]) == [[0,0],[1,4]] # Should this be [[0,0], [1,4]] or [[0,4]] if [0,0] is before [1,4]? The code will sort it.
    # Correcting the above based on sorting:
    assert Solution().merge([[1,4],[0,0]]) == [[0,0],[1,4]] # After sorting: [[0,0], [1,4]] -> [[0,0], [1,4]] (no merge)
    assert Solution().merge([[0,0],[1,4]]) == [[0,0],[1,4]]
    assert Solution().merge([[1,5],[2,3]]) == [[1,5]]
    assert Solution().merge([[2,3],[1,5]]) == [[1,5]]
    assert Solution().merge([[1,4],[2,5],[0,3]]) == [[0,5]]

    print("All tests passed!")

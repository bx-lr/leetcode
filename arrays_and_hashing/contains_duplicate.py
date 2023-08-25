from typing import *

# blind 75 list item
def containsDuplicate(nums: List[int], solve_method: int) -> bool:
    '''
Given an integer array nums, return true if any value appears at least twice in the array, and return false  if every element is distinct.
    '''
    # brute force solution
    # time complexity O(n^2)
    # space complexity O(1)

    if solve_method == 1:
        # sorted solution
        # time complexity O(n log n)
        # space complexity O(1)
        s_nums = sorted(nums)
        for i in range(len(nums)-1):
            cur = nums[i]
            next = s_nums[i+1]
            if next == cur:
                return True
        return False
    if solve_method == 2:
        # set solution
        # time complexity O(n): hashset insertion, checking
        # space complexity O(n): adding to hashset
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


def check():
    '''
check method for testing the containsDuplicate function

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

    nums = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
    expected = [True, False, True]
    solve_method = {1: 'sorted solution', 2: 'set solution'}
    for method in solve_method.keys():
        results = []
        for arr, exp in zip(nums, expected):
            res = containsDuplicate(arr, method)
            results.append(res)
            if res == exp:
                print(f'passed test: {arr}, expected: {exp}, result: {res}')
            else:
                print(f'!!!failed test: {arr}, expected: {exp}, result: {res}')
                return False
        if results == expected:
            print(f'all tests passed for method: "{solve_method[method]}"\n')
    return True



def main():
    check()


if __name__ == '__main__':
    main()

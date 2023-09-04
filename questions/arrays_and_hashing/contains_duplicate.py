from typing import *


class Solution():
    # blind 75 list item
    def containsDuplicate(self, nums: List[int]) -> bool:
        return

    def check(self):
        nums = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
        expected = [True, False, True]
        results = []
        print('')
        for arr, exp in zip(nums, expected):
            res = self.containsDuplicate(arr)
            results.append(res)
            if res == exp:
                print(f'\tpassed test: {arr}, expected: {exp}, result: {res}')
            else:
                print(f'\t!!!failed test: {arr}, expected: {exp}, result: {res}')
                return 1
        if results == expected:
            print('**** All tests passed ****')
        return 0


def get_difficulty():
    return 1


def get_instructions() -> str:
    ins = '''Contains Duplicate.
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
    return ins


def get_solution() -> str:
    solution = '''
Incorrect! Here is the solution:

def containsDuplicate(self, nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
'''
    return solution


def main():
    sol = Solution()
    print(sol.check())


if __name__ == '__main__':
    main()

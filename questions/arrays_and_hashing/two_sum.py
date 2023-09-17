from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return []

    def check(self) -> int:
        '''
        check the twoSum() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        nums = [[2,7,11,15], [3,2,4], [3,3]]
        target = [9, 6, 6]
        expected = [[0,1], [1,2], [0,1]]
        results = []
        for a0, a1, exp in zip(nums, target, expected):
            res = self.twoSum(a0, a1)
            results.append(res)
            if res == exp:
                print(f'\tpassed test: {a0} {a1}, expected: {exp}, result: {res}')
            else:
                print(f'\t!!!failed test: {a0} {a1}, expected: {exp}, result: {res}')
                return 1
        if results == expected:
            print('**** All tests passed ****')
        return 0


def get_difficulty() -> int:
    '''
    1 = easy
    2 = medium
    3 = hard
    '''
    return 1.2


def get_instructions() -> str:
    ins = '''Two Sum.
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {}  # val -> index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return []
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

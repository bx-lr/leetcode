from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [[2,2,1], [4,1,2,1,2], [1]]
        for a0 in arg0:
            good = self.solution(a0)
            res = self.singleNumber(a0)
            if good == res:
                print(f'\tpassed test: {a0}, expected: {good}, result: {res}')
            else:
                print(f'\t!!!failed test: {a0}, expected: {good}, result: {res}')
                return 1
        print('**** All tests passed ****')
        return 0

    def solution(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res


def get_difficulty() -> int:
    '''
    1 = easy
    2 = medium
    3 = hard
    '''
    return 1.1


def get_instructions() -> str:
    ins = '''Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
 

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def singleNumber(self, nums: List[int]) -> int:
    res = 0
    for n in nums:
        res = n ^ res
    return res
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

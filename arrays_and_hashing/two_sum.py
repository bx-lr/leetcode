from typing import *


def twoSum(nums: list[int], tgt: int) -> list:
    '''
Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

You can return the answer in any order.
    '''
    # time: O(n)
    # memory: O(n)
    prev_map = {}
    for i, n in enumerate(nums):
        diff = tgt - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []


def check():
    '''
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
    '''

    input = [[2, 7, 11, 15], [3, 2, 4], [3, 3]]
    targets = [9,6,6]
    checks = [[0, 1], [1, 2], [0, 1]]

    for nums, check, tgt in zip(input, checks, targets):
        res = twoSum(nums, tgt)
        if res != check:
            print(f'test failed for: {nums}, results: {res}, expected:{check}')
            return
    print(f'all tests passed')
    return 

def main():
    check()


if __name__ == '__main__':
    main()
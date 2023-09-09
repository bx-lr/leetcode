from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return -1

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [[100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]]
        expected = [4, 9]
        results = []
        for a0, exp in zip(arg0, expected):
            res = self.longestConsecutive(a0)
            results.append(res)
            if res == exp:
                print(f'\tpassed test: {a0}, expected: {exp}, result: {res}')
            else:
                print(f'\t!!!failed test: {a0}, expected: {exp}, result: {res}')
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
    return 2.3


def get_instructions() -> str:
    ins = '''Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if (n-1) not in numSet:
            length = 1
            while (n+length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

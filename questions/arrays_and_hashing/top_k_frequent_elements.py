from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [[1,1,1,2,2,3], [1]]
        arg1 = [2,1]
        expected = [[1,2],[1]]
        results = []
        for a0, a1, exp in zip(arg0, arg1, expected):
            res = self.topKFrequent(a0, a1)
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
    return 2.5


def get_instructions() -> str:
    ins = '''Top K Frequent Elements.
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

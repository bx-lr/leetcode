from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [[1,3,-1,-3,5,3,6,7], [1]]
        arg1 = [3, 1]
        expected = [[3,3,5,5,6,7], [1]]
        results = []
        for a0, a1, exp in zip(arg0, arg1, expected):
            res = self.maxSlidingWindow(a0, a1)
            results.append(res)
            if res == exp:
                print(f'\tpassed test: {a0}, expected: {exp}, result: {res}')
            else:
                print(f'\t!!!failed test: {a0}, expected: {exp}, result: {res}')
                return 1
        if results == expected:
            print('**** All tests passed ****')
            return 0
        print('!!!!Oh noes, something failed!!!')
        return 1


def get_difficulty() -> int:
    '''
    1 = easy
    2 = medium
    3 = hard
    '''
    return 3.2


def get_instructions() -> str:
    ins = '''Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    import collections
    output = []
    q = collections.deque()  # index
    l = r = 0
    # O(n) O(n)
    while r < len(nums):
        # pop smaller values from q
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # remove left val from window
        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

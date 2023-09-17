from typing import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [[73,74,75,71,69,72,76,73], [30,40,50,60], [30,60,90]]
        expected = [[1,1,4,2,1,1,0,0], [1,1,1,0], [1,1,0]]
        results = []
        for a0, exp in zip(arg0, expected):
            res = self.dailyTemperatures(a0)
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
    return 2.2


def get_instructions() -> str:
    ins = '''Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 
Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t,i))
    return res

'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

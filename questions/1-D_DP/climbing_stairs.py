from typing import *


class Solution:
    def climbStairs(self, n: int) -> int:
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [2, 3, 5]

        for a0 in arg0:
            good = self.solution(a0)
            res = self.climbStairs(a0)
            if good == res:
                print(f'\tpassed test: {a0}, expected: {good}, result: {res}')
            else:
                print(f'\t!!!failed test: {a0}, expected: {good}, result: {res}')
                return 1
        print('**** All tests passed ****')
        return 0

    def solution(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2


def get_difficulty() -> int:
    '''
    1 = easy
    2 = medium
    3 = hard
    '''
    return 1.1


def get_instructions() -> str:
    ins = '''Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:
1 <= n <= 45
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def climbStairs(self, n: int) -> int:
    if n <= 3:
        return n
    n1, n2 = 2, 3

    for i in range(4, n + 1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

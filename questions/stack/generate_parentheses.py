from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return 

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [3, 1]
        expected = [["((()))","(()())","(())()","()(())","()()()"], ["()"]]
        results = []
        for a0, exp in zip(arg0, expected):
            res = self.generateParenthesis(a0)
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
    return 2


def get_instructions() -> str:
    ins = '''Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:
1 <= n <= 8
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def generateParenthesis(self, n: int) -> List[str]:
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append(''.join(stack))
            return
        if openN < n:
            stack.append('(')
            backtrack(openN+1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(')')
            backtrack(openN, closedN+1)
            stack.pop()
    backtrack(0,0)
    return res

'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

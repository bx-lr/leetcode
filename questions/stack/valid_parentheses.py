from typing import *


class Solution:
    def isValid(self, s: str) -> bool:
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = ["()", "()[]{}", "(]"]
        expected = [True, True, False]
        results = []
        for a0, exp in zip(arg0, expected):
            res = self.isValid(a0)
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
    return 1.1


def get_instructions() -> str:
    ins = '''Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def isValid(self, s: str) -> bool:
    charMap = {')':'(', ']':'[', '}': '{'}
    stack = []
    for c in s:
        if c not in charMap:
            stack.append(c)
            continue
        if not stack or stack[-1] != charMap[c]:
            return False
        stack.pop()
    return not stack

'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

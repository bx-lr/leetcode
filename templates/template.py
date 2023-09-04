from typing import *


class Solution:
    def doSomething(self, arg0: int, arg1: int) -> bool:
        '''
        Implement the logic of the function. Will be called by check()
        '''
        return True

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [1, 2, 3]
        arg1 = [4, 5, 6]
        expected = [True, False, True]
        results = []
        for a0, a1, exp in zip(arg0, arg1, expected):
            res = self.doSomething(a0, a1)
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
    return -1


def get_instructions() -> str:
    ins = '''
INSERT INSTRUCTIONS FOR problem
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = dict(), dict()
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

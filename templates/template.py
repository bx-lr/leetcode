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
        arg0 = [] # <- update
        for a0 in arg0:
            good = self.solution(a0) # <- insert actual solution
            res = self.doSomething(a0) # <-change name
            if good == res:
                print(f'\tpassed test: {a0}, expected: {good}, result: {res}')
            else:
                print(f'\t!!!failed test: {a0}, expected: {good}, result: {res}')
                return 1
        print('**** All tests passed ****')
        return 0

    def solution(self):
        ''' insert the actual solution here'''
        return


def get_difficulty() -> int:
    '''
    1 = easy
    2 = medium
    3 = hard
    '''
    return -1 # <- update


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

def doSomething(self, arg0: int, arg1: int) -> bool:
    # Implement the logic of the function. Will be called by check()
    return True
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

from typing import *


class Solution:
    def hammingWeight(self, n: int) -> int:
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [0b00000000000000000000000000001011, 0b00000000000000000000000010000000, 0b11111111111111111111111111111101]
        for a0 in arg0:
            good = self.solution(a0)
            res = self.hammingWeight(a0)
            if good == res:
                print(f'\tpassed test: {a0}, expected: {good}, result: {res}')
            else:
                print(f'\t!!!failed test: {a0}, expected: {good}, result: {res}')
                return 1
        print('**** All tests passed ****')
        return 0

    def solution(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res


def get_difficulty() -> int:
    '''
    1 = easy
    2 = medium
    3 = hard
    '''
    return 1.2


def get_instructions() -> str:
    ins = '''Number of 1 Bits
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 
Constraints:
The input must be a binary string of length 32. 
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

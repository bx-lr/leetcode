from typing import *


class Solution:
    def encode(self, strs: str) -> str:
        return ''

    def decode(self, s: str) -> list:
        return []

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [["lint","code","love","you"], ["we", "say", ":", "yes"]]
        expected = ['4#lint4#code4#love3#you', '2#we3#say1#:3#yes']
        for a0, exp in zip(arg0, expected):
            res_enc = self.encode(a0)
            if res_enc == exp:
                print(f'\tpassed test encode: {a0}, expected: {exp}, result: {res_enc}')
            else:
                print(f'\t!!!failed test encode: {a0}, expected: {exp}, result: {res_enc}')
                return 1
            res_dec = self.decode(res_enc)
            if res_dec == a0:
                print(f'\tpassed test decode: {res_enc}, expected: {a0}, result: {res_dec}')
            else:
                print(f'\t!!!failed test encode: {res_enc}, expected: {a0}, result: {res_dec}')
                return 1
        print('**** All tests passed ****')
        return 0


def get_difficulty() -> int:
    '''
    1 = easy
    2 = medium
    3 = hard
    '''
    return 2.1


def get_instructions() -> str:
    ins = '''Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example 2:
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def encode(self, strs: str) -> str:
    return ''.join(map(lambda s: str(len(s)) + '#' + s, strs))

def decode(self, s: str) -> str:
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j
    return res
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

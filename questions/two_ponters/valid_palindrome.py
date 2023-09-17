from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        return

    def alphanum(self, c) -> bool:
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = ["A man, a plan, a canal: Panama", "race a car", " "]
        expected = [True, False, True]
        results = []
        for a0, exp in zip(arg0, expected):
            res = self.isPalindrome(a0)
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
    ins = '''Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not self.alphanum(s[l]):
            l += 1
        while l < r and not self.alphanum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

def alphanum(self, c) -> bool:
    return (ord('0') <= ord(c) <= ord('9') or
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z'))
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

from typing import *


class Solution():
    def isAnagram(self, s: str, t: str) -> bool:
        return

    def check(self):
        s1 = ['anagram', 'rat', 'racecar']
        s2 = ['nagaram', 'car', 'ecacarr']
        expected = [True, False, True]
        results = []
        print('')
        for s, t, exp in zip(s1, s2, expected):
            res = self.isAnagram(s, t)
            results.append(res)
            if res == exp:
                print(f'\tpassed test: "{s}" "{t}", expected: {exp}, result: {res}')
            else:
                print(f'\t!!!failed test: "{s}" "{t}", expected: {exp}, result: {res}')
                return 1
        if results == expected:
            print('**** All tests passed ****')
            return 0
        return 1


def get_difficulty() -> int:
    return 1.2


def get_instructions() -> str:
    ins = '''Valid Anagram.
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''
    return ins

def get_solution() -> str:
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

from typing import *


class Solution:
    def checkInclusion(self, s1, s2):
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = ["ab", "ab"]
        arg1 = ["eidbaooo", "eidboaoo"]
        expected = [True, False]
        results = []
        for a0, a1, exp in zip(arg0, arg1, expected):
            res = self.checkInclusion(a0, a1)
            results.append(res)
            if res == exp:
                print(f'\tpassed test: {a0}, expected: {exp}, result: {res}')
            else:
                print(f'\t!!!failed test: {a0}, expected: {exp}, result: {res}')
                return 1
        if results == expected:
            print('**** All tests passed ****')
            return 0
        print('!!!!Oh noes, something failed!!!')
        return 1


def get_difficulty() -> int:
    '''
    1 = easy
    2 = medium
    3 = hard
    '''
    return 2


def get_instructions() -> str:
    ins = '''Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def checkInclusion(self, s1, s2):
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1

    matches = sum(map(lambda i: s1Count[i] == s2Count[i], range(26)))

    for l in range(len(s2) - len(s1)):
        if matches == 26:
            return True

        i = ord(s2[l]) - ord("a")
        s2Count[i] -= 1
        if s2Count[i] == s1Count[i]:
            matches += 1
        elif s2Count[i] == s1Count[i] - 1:
            matches -= 1

        i = ord(s2[l + len(s1)]) - ord("a")
        s2Count[i] += 1
        if s2Count[i] == s1Count[i]:
            matches += 1
        elif s2Count[i] == s1Count[i] + 1:
            matches -= 1

    return matches == 26
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

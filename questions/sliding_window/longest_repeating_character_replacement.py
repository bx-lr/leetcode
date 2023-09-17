from typing import *


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = ["ABAB", "AABABBA"]
        arg1 = [4, 1]
        expected = [4, 4]
        results = []
        for a0, a1, exp in zip(arg0, arg1, expected):
            res = self.characterReplacement(a0, a1)
            results.append(res)
            if res == exp:
                print(f'\tpassed test: {a0} {a1}, expected: {exp}, result: {res}')
            else:
                print(f'\t!!!failed test: {a0} {a1}, expected: {exp}, result: {res}')
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
    return 2.1


def get_instructions() -> str:
    ins = '''Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
 
Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def characterReplacement(self, s, k):
    counts = {}
    maxf = 0
    l = 0
    for r, ch in enumerate(s):
        counts[ch] = 1 + counts.get(ch, 0)
        maxf = max(maxf, counts[ch])
        if maxf + k < r - l + 1:
            counts[s[l]] -= 1
            l += 1

    return len(s) - l
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

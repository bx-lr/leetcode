from typing import *
from collections import Counter

def isAnagram(s: str, t: str, method: int) -> bool:
    '''
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original 
letters exactly once.
    '''
    if len(s) != len(t):
        return False

    # hashmap solution
    # time complexity: O(n), s+t
    # space complexity: O(n), s+t
    if method == 1:
        d_count1 = {}
        d_count2 = {}
        for c1, c2 in zip(s, t):
            count = d_count1.get(c1, 0)
            count += 1
            d_count1[c1] = count

            count = d_count2.get(c2, 0)
            count += 1
            d_count2[c2] = count
        return d_count2 == d_count1

    if method == 2:
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

    # sorted solution
    # time complexity: O(n log n)
    # space complexity: O(n), maybe depending on algorithm O(1)
    if method == 3:
        if sorted(s) == sorted(t):
            return True

    # library one line solution
    if method == 4:
        return Counter(s) == Counter(t)
    return False


def check():
    s1 = ['anagram', 'rat', 'racecar']
    s2 = ['nagaram', 'car', 'ecacarr']
    expected = [True, False, True]

    solve_method = {1: 'my hashmap solution',
                    2: 'better hashmap solution',
                    3: 'set solution', 
                    4: 'library solution'}
    for method in solve_method.keys():
        results = []
        for s, t, exp in zip(s1, s2, expected):
            res = isAnagram(s, t, method)
            results.append(res)
            if res == exp:
                print(f'passed test: "{s}" "{t}", expected: {exp}, result: {res}')
            else:
                print(f'!!!failed test: "{s}" "{t}", expected: {exp}, result: {res}')
                return False
        if results == expected:
            print(f'all tests passed for method: "{solve_method[method]}"\n')


def main():
    check()

if __name__ == '__main__':
    main()

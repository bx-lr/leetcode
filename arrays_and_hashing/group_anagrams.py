from typing import *


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    '''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original
letters exactly once.
    '''
    # time: O(m*n)
    # memory: O(m*n)
    res = DefaultDict(list)
    for s in strs:
        count = [0] * 26  # a .. z
        for c in s:
            count[ord(c) - ord('a')] += 1  # map ascii table to 0 index
        res[tuple(count)].append(s)
    return list(res.values())  # typecast to list for test case


def check():
    '''
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
    '''
    inputs = [["eat", "tea", "tan", "ate", "nat", "bat"],
              [""],
              ["a"]]

    outputs = [[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
               [[""]],
               [["a"]]]
    for inp, outp in zip(inputs, outputs):
        res = groupAnagrams(inp)
        if res != outp:
            print(f'test case failed for: {inp}, got: {res}, expected: {outp}')
            return
    print('all tests passed')
    return

def main():
    check()


if __name__ == '__main__':
    main()
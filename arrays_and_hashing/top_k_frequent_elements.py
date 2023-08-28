from typing import *


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # algorithm: bucket sort
    # time: O(n)
    # memory: O(n) 

    count = {}
    freq = [[] for _ in range(len(nums)+1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    # solution with heap
    # O(k log n)
    return [0]


def check():
    '''
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
    '''
    inputs = [[1, 1, 1, 2, 2, 3], [1]]
    outputs = [[1, 2], [1]]
    counts = [2, 1]

    for inp, outp, k in zip(inputs, outputs, counts):
        res = topKFrequent(inp, k)
        if res != outp:
            print(f'test case failed for: {inp}, got: {res}, expected: {outp}')
            return
    print('all test cases passed')
    return

def main():
    check()


if __name__ == '__main__':
    main()
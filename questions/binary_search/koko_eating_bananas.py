from typing import *


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [[3,6,7,11], [30,11,23,4,20], [30,11,23,4,20]]
        arg1 = [8, 5, 6]
        expected = [4, 30, 23]
        results = []
        for a0, a1, exp in zip(arg0, arg1, expected):
            res = self.minEatingSpeed(a0, a1)
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
    return 2


def get_instructions() -> str:
    ins = '''Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def minEatingSpeed(self, piles: List[int], h: int) -> int:
    import math
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2

        totalTime = 0
        for p in piles:
            totalTime += math.ceil(p / k)
        if totalTime <= h:
            res = k
            r = k - 1
        else:
            l = k + 1
    return res
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

from typing import *
import copy

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        args = [1,2,3,4,5]
        start = ListNode()
        all_lns = []
        all_lns.append(start)
        for arg in args:
            start.val = arg
            new_node = ListNode()
            start.next = new_node
            start = new_node
            all_lns.append(start)

        arg0 = [all_lns[0]]
        for a0 in arg0:
            first = copy.deepcopy(a0)
            res = copy.deepcopy(a0)
            good = self.solution(first)
            res = self.reverseList(res)
            if good.next.val == res.next.val:
                print(f'\tpassed test: {a0.next.val}, expected: {good.next.val}, result: {res.next.val}')
            else:
                print(f'\t!!!failed test: {a0.next.val}, expected: {good.next.val}, result: {res.next.val}')
                return 1
        print('**** All tests passed ****')
        return 0

    def solution(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev



def get_difficulty() -> int:
    '''
    1 = easy
    2 = medium
    3 = hard
    '''
    return 1.1


def get_instructions() -> str:
    ins = ''' Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def reverseList(self, head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

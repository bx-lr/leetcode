from typing import *


class Solution:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        return

    def pop(self) -> None:
        return

    def top(self) -> int:
        return

    def getMin(self) -> int:
        return

    def check(self) -> int:
        '''
        check the class...
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]

        Output
        [null,null,null,null,-3,null,0,-2]
        '''
        arg0 = ["MinStack","push","push","push","getMin","pop","top","getMin"]
        arg1 = [[],[-2],[0],[-3],[],[],[],[]]
        expected = [None,None,None,None,-3,None,0,-2]
        results = []
        for a0, a1, exp in zip(arg0, arg1, expected):
            if a0 == 'MinStack':
                results.append(None)
            elif a0 == 'push':
                results.append(self.push(a1))
            elif a0 == 'getMin':
                results.extend(self.getMin())
            elif a0 == 'pop':
                results.append(self.pop())
            elif a0 == 'top':
                results.extend(self.top())
            else:
                continue
        if results != expected:
            print(f'!!!!failed test, expected {expected}, result: {results}')
            return 1
        else:
            print('**** All tests passed ****')
            return 0


def get_difficulty() -> int:
    '''
    1 = easy
    2 = medium
    3 = hard
    '''
    return 2.5


def get_instructions() -> str:
    ins = '''Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()

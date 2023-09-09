from typing import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return True

    def check(self) -> int:
        '''
        check the doSomething() function
        return 0 if tests passed
        return 1 if tests failed
        '''
        arg0 = [[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]],\
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]]

        expected = [True, False]
        results = []
        for a0, exp in zip(arg0, expected):
            res = self.isValidSudoku(a0)
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
    return 2.6


def get_instructions() -> str:
    ins = '''Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
    return ins


def get_solution() -> str:
    '''
    Called when check fails
    should return solution as string
    '''
    solution = '''
Incorrect! Here is the solution:

def isValidSudoku(self, board: List[List[str]]) -> bool:
    import collections
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3, c//3)]):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
    return True

'''
    return solution


def main():
    sol = Solution()
    sol.check()


if __name__ == '__main__':
    main()


class Solution:
    board = None

    def exist(self, board: list[list[str]], word: str):
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs(i, j, word):
                    return True
        return False

    def dfs(self, i, j, word):
        pass

word = "ABCDEF"
a = word[0:2]
print(a)
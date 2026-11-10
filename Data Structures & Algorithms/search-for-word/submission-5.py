class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols, rows = len(board[0]), len(board)
        def dfs(r, c, index, visited):
            if r == rows or c == cols or r < 0 or c < 0:
                return False
            if (r,c) in visited:
                return False
            if index >= len(word):
                return False
            if index == len(word)-1 and board[r][c]==word[index]:
                return True
            if board[r][c] != word[index]:
                return False
            print(index)
            visited.add((r,c))
            up = dfs(r+1, c, index+1, visited)
            down = dfs(r, c+1, index+1, visited)
            left = dfs(r-1, c, index+1, visited)
            right = dfs(r, c-1, index+1, visited)
            visited.remove((r,c))
            if up or down or right or left:
                return True
            else:
                return False
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()) == True:
                        return True
        return False
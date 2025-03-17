class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live_count = 0
                for a, b in dirs:
                    if i + a >= 0 and i + a < m and j + b >= 0 and j + b < n:
                        if abs(board[i + a][j + b]) == 1:
                            live_count += 1
                if board[i][j] == 1 and (live_count < 2 or live_count > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and live_count == 3:
                    board[i][j] = 2
                else:
                    pass

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
                else:
                    pass
        return board

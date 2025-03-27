def update_time(self): #cập nhật bảng
        if not self.game_over:
            self.elapsed_time = time.time() - self.start_time

def is_valid(self, board, row, col, num): # hiện thị bảng
        if num in board[row]:
            return False
        
        for i in range(9):
            if board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        return True
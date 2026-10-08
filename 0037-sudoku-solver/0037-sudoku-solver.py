class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        # Store which numbers are already used
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = int(board[r][c]) - 1
                    bit = 1 << num

                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def backtrack():

            # Find empty cell with minimum possibilities
            best_r = -1
            best_c = -1
            best_mask = 0
            min_count = 10

            for r in range(9):
                for c in range(9):

                    if board[r][c] == ".":

                        box = (r // 3) * 3 + c // 3

                        used = rows[r] | cols[c] | boxes[box]

                        # Numbers 1-9 that are NOT used
                        available = (~used) & 0x1FF

                        count = available.bit_count()

                        if count < min_count:
                            min_count = count
                            best_r = r
                            best_c = c
                            best_mask = available

            # No empty cells → Sudoku solved
            if best_r == -1:
                return True

            box = (best_r // 3) * 3 + best_c // 3

            # Try every available number
            while best_mask:

                # Get lowest available bit
                bit = best_mask & -best_mask

                # Remove it from available numbers
                best_mask -= bit

                num = bit.bit_length() - 1

                board[best_r][best_c] = str(num + 1)

                rows[best_r] |= bit
                cols[best_c] |= bit
                boxes[box] |= bit

                if backtrack():
                    return True

                # Undo
                board[best_r][best_c] = "."

                rows[best_r] ^= bit
                cols[best_c] ^= bit
                boxes[box] ^= bit

            return False

        backtrack()
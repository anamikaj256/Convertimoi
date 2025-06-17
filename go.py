import tkinter as tk
from tkinter import messagebox

class GoGame:
    def __init__(self, size=9):
        self.size = size  # Board size (9x9, 13x13, 19x19)
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.current_player = 1  # Black starts first
        self.window = tk.Tk()
        self.window.title("Go Game")
        self.cell_size = 40
        self.canvas = tk.Canvas(self.window, width=self.size * self.cell_size, height=self.size * self.cell_size)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.place_stone)
        self.draw_board()
        self.captured_stones = {1: 0, 2: 0}  # Track captured stones

    def draw_board(self):
        """Draw the grid lines for the Go board."""
        for i in range(self.size):
            self.canvas.create_line(self.cell_size / 2, self.cell_size / 2 + i * self.cell_size,
                                     self.size * self.cell_size - self.cell_size / 2,
                                     self.cell_size / 2 + i * self.cell_size)
            self.canvas.create_line(self.cell_size / 2 + i * self.cell_size, self.cell_size / 2,
                                     self.cell_size / 2 + i * self.cell_size,
                                     self.size * self.cell_size - self.cell_size / 2)

    def place_stone(self, event):
        """Handle the player's move by placing a stone."""
        x, y = event.x // self.cell_size, event.y // self.cell_size

        if self.board[y][x] != 0:
            return  # Invalid move: cell already occupied

        self.board[y][x] = self.current_player
        self.draw_stone(x, y, self.current_player)

        # Check for captures
        self.remove_captured_stones()

        # Switch turn
        self.current_player = 3 - self.current_player

    def draw_stone(self, x, y, player):
        """Draw a stone on the board."""
        color = "black" if player == 1 else "white"
        margin = 5
        self.canvas.create_oval(
            x * self.cell_size + margin,
            y * self.cell_size + margin,
            (x + 1) * self.cell_size - margin,
            (y + 1) * self.cell_size - margin,
            fill=color
        )

    def remove_captured_stones(self):
        """Identify and remove captured stones."""
        visited = set()

        def get_group_and_liberties(x, y):
            """Find all stones in the group and count liberties."""
            group = []
            liberties = 0
            queue = [(x, y)]
            visited.add((x, y))
            player = self.board[y][x]

            while queue:
                cx, cy = queue.pop()
                group.append((cx, cy))
                for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        if (nx, ny) not in visited:
                            if self.board[ny][nx] == 0:
                                liberties += 1
                            elif self.board[ny][nx] == player:
                                queue.append((nx, ny))
                                visited.add((nx, ny))
            return group, liberties

        # Check all stones on the board
        for y in range(self.size):
            for x in range(self.size):
                if (x, y) not in visited and self.board[y][x] != 0:
                    group, liberties = get_group_and_liberties(x, y)
                    if liberties == 0:  # No liberties, capture the group
                        for gx, gy in group:
                            self.board[gy][gx] = 0
                            self.captured_stones[self.current_player] += 1
                            self.canvas.create_rectangle(
                                gx * self.cell_size + 2, gy * self.cell_size + 2,
                                (gx + 1) * self.cell_size - 2, (gy + 1) * self.cell_size - 2,
                                fill="green", outline="")

    def start(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = GoGame(size=9)  # 9x9 board
    game.start()

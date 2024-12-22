class GameOfLife():
    def __init__(self, board):
        self.board = board
        self.LIVE_NEIGHBORS = 3

    def next_generation(self) -> None:
        """Generate the next generation of the board."""
        new_board = []
        for i in range(len(self.board)):
            new_row = []
            for j in range(len(self.board[i])):
                new_row.append(self.get_new_cell_state(i, j))
            new_board.append(new_row)
        self.board = new_board

    def get_new_cell_state(self, i: int, j: int) -> int:
        """Get the new state of a cell in the next generation (0 or 1).

        If a cell is alive and has less than 2 or more than 3 live neighbors, it dies.
        If a cell is dead and has exactly 3 live neighbors, it becomes alive.

        Parameters:
        ----------
        i: int
            The row index of the cell
        j: int
            The column index of the cell

        Returns:
        -------
        int
            The new state of the cell at (i, j) in the next generation

        """
        live_neighbors = self.get_live_neighbors(i, j)
        if self.board[i][j] == 1:
            if live_neighbors < self.LIVE_NEIGHBORS - 1 or live_neighbors > self.LIVE_NEIGHBORS:
                return 0
            else:
                return 1
        elif live_neighbors == self.LIVE_NEIGHBORS:
                return 1
        else:
            return 0

    def get_live_neighbors(self, i:int, j:int) -> int:
        """Get the number of live neighbors for a given cell.

        Parameters:
        ----------
        i: int
            The row index of the cell
        j: int
            The column index of the cell

        Returns:
        -------
        int
            The number of live neighbors for the cell at (i, j)

        """
        live_neighbors = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if x >= 0 and x < len(self.board) and y >= 0 and y < len(self.board[i]):
                    if x != i or y != j:
                        live_neighbors += self.board[x][y]
        return live_neighbors

    def run(self, generations: int) -> None:
        """Run the game of life for a given number of generations.

        Parameters:
        ----------
        generations: int
            The number of generations to run the game of life

        Returns:
        -------
        None

        """
        for _ in range(generations):
            self.next_generation()
from time import sleep

from graphics import Cell, Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        window: Window,
    ) -> None:
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:
        self._cells = [
            [Cell(self._window) for _ in range(self._num_rows)]
            for _ in range(self._num_cols)
        ]
        for column_index, column in enumerate(self._cells):
            for row_index, cell in enumerate(column):
                self._draw_cell(cell, column_index, row_index)

    def _draw_cell(self, cell: Cell, column_index: int, row_index: int) -> None:
        x1 = self._x1 + column_index * self._cell_size_x
        y1 = self._y1 + row_index * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        self._window.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        top_left = self._cells[0][0]
        bottom_right = self._cells[-1][-1]

        top_left.top_wall = False
        self._draw_cell(top_left, 0, 0)

        bottom_right.bottom_wall = False
        self._draw_cell(bottom_right, len(self._cells) - 1, len(self._cells[0]) - 1)

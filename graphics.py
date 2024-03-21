from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width: int, height: int) -> None:
        self._root = Tk()
        self._root.title("Maze Runner")
        self._canvas = Canvas(self._root, width=width, height=height)
        self._canvas.pack()
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self) -> None:
        self._running = True
        while self._running:
            self.redraw()
        print("window closed...")

    def close(self) -> None:
        self._running = False

    def draw_line(self, line: "Line", fill_color: str | None = None) -> None:
        if fill_color is None:
            fill_color = self._canvas["background"]
        assert fill_color is not None
        line.draw(self._canvas, fill_color)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack()


class Cell:
    def __init__(self, window: Window) -> None:
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self.top_wall = True
        self.right_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self._window = window
        self.visited = False

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        def draw_wall(x1: int, y1: int, x2: int, y2: int, color: bool) -> None:
            self._window.draw_line(
                Line(Point(x1, y1), Point(x2, y2)), "black" if color else None
            )

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        draw_wall(self._x1, self._y1, self._x2, self._y1, self.top_wall)
        draw_wall(self._x2, self._y1, self._x2, self._y2, self.right_wall)
        draw_wall(self._x1, self._y2, self._x2, self._y2, self.bottom_wall)
        draw_wall(self._x1, self._y1, self._x1, self._y2, self.left_wall)

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        def middle_point(cell: "Cell") -> Point:
            return Point(
                round((cell._x1 + cell._x2) / 2), round((cell._y1 + cell._y2) / 2)
            )

        color = "gray" if undo else "red"
        start = middle_point(self)
        end = middle_point(to_cell)
        self._window.draw_line(Line(start, end), color)

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

    def draw_line(self, line: "Line", fill_color: str) -> None:
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

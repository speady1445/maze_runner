from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Runner")
        self._canvas = Canvas(self._root, width=width, height=height)
        self._canvas.pack()
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
        print("window closed...")

    def close(self):
        self._running = False

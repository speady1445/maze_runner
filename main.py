import sys

from graphics import Window
from maze import Maze

sys.setrecursionlimit(100000)


def main() -> None:
    num_rows = 12 * 18
    num_cols = 16 * 18
    margin = 50
    screen_x = 800 * 2
    screen_y = 600 * 2
    cell_size_x = round((screen_x - 2 * margin) / num_cols)
    cell_size_y = round((screen_y - 2 * margin) / num_rows)

    window = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

    window.wait_for_close()


def warning() -> None:
    print("WARNING: This program is slow and may take a while to run!")
    print("Please be patient.")
    print("Press Ctrl+C in this terminal to exit.")
    print("")
    print("Press Enter to continue...")
    input()


if __name__ == "__main__":
    warning()
    main()

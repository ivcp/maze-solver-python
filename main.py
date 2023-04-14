from window import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(5, 5, 5, 5, 20, 20, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()

    
main()
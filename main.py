from window import Window
from cell import Cell

def main():
    win = Window(800, 600)
   
    cell1 = Cell(win)
    cell1.draw(10, 10, 50, 50)
    cell2 = Cell(win)
    cell2.has_right_wall = False
    cell2.draw(50, 10, 90, 50)
    cell3 = Cell(win)
    cell3.has_top_wall = False
    cell3.has_right_wall = False
    cell3.draw(90, 10, 130, 50)
    
    cell2.draw_move(cell3)
    
    win.wait_for_close()

    
main()
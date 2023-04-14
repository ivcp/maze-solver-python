from window import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))            
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))    
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))                          
        if self.has_left_wall:
            self._win.draw_line(left_wall, "black")
        else:                     
            self._win.draw_line(left_wall, "white")
        if self.has_right_wall:                                  
            self._win.draw_line(right_wall, "black")
        else:
            self._win.draw_line(right_wall, "white")
        if self.has_top_wall:            
            self._win.draw_line(top_wall, "black")
        else:
            self._win.draw_line(top_wall, "white")            
        if self.has_bottom_wall:                             
            self._win.draw_line(bottom_wall, "black")
        else:
            self._win.draw_line(bottom_wall, "white")


    def draw_move(self, to_cell, undo=False):        
        line = Line(Point(calculate_center(self._x1, self._x2), calculate_center(self._y1, self._y2)), 
                    Point(calculate_center(to_cell._x1, to_cell._x2), calculate_center(to_cell._y1, to_cell._y2)))
        color = "red"
        if undo:
            color = "gray"
        self._win.draw_line(line, color)


def calculate_center(low, high):
    return (low + high) / 2
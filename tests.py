import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 12
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2._break_entrance_and_exit()
        self.assertFalse(
            m2._cells[0][0].has_top_wall            
        )
        self.assertFalse(
            m2._cells[-1][-1].has_bottom_wall            
        )

    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 12
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m3._break_walls_r(0,0)
        self.assertTrue(
            m3._cells[0][0].visited
        )
        m3._reset_cells_visited()
        for i in m3._cells:
            for j in i:
                self.assertFalse(
                   j.visited
                )

if __name__ == "__main__":
    unittest.main()
import unittest

class SlopeSolver:
    """Solves for missing variables in the slope function"""
    def __init__(self, y, m, x, b):
        self.y = y
        self.m = m
        self.x = x
        self.b = b

    def solve(self):
        """Solves for the missig variable.

        Technically this doesnt work because in the case where 2 vars a missing it wont know what to do
        """
        if not self.y:
            return self.__solve_for_y()
        elif not self.m:
            return self.__solve_for_m()
        elif not self.x:
            return self.__solve_for_x()
        elif not self.b:
            return self.__solve_for_b()

    def __solve_for_y(self):
        return self.m * self.x + self.b

    def __solve_for_m(self):
        return (self.y - self.b) / self.x

    def __solve_for_x(self):
        return (self.y - self.b) / self.m

    def __solve_for_b(self):
        return self.y - (self.m * self.x)


class TestSolver(unittest.TestCase):
    def test_solve(self):
        b_solver = SlopeSolver(2, 3, 4, None)
        self.assertEqual(b_solver.solve(), -10)
        x_solver = SlopeSolver(2, 3, None, 4)
        self.assertEqual(x_solver.solve(), -2/3)
        m_solver = SlopeSolver(2, None, 3, 4)
        self.assertEqual(m_solver.solve(), -2/3)
        y_solver = SlopeSolver(None, 2, 3, 4)
        self.assertEqual(y_solver.solve(), 10)


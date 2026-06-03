import unittest

try:
    import student_solution as sol
except Exception:
    sol = None

class ToggleTests(unittest.TestCase):
    def test_find_largest(self):
        self.assertIsNotNone(sol, "Please place your solution in student_solution.py")
        self.assertEqual(sol.find_largest(0, 2, 4), 4)
        self.assertEqual(sol.find_largest(-5, -1, -4), -1)

if __name__ == '__main__':
    unittest.main()

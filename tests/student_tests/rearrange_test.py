import unittest

# Rename your student file to `student_solution.py` or import appropriately
try:
    import student_solution as sol
except Exception:
    sol = None

class RearrangeTests(unittest.TestCase):
    def test_is_true(self):
        self.assertIsNotNone(sol, "Please place your solution in student_solution.py")
        self.assertTrue(sol.is_true(True))
        self.assertFalse(sol.is_true(False))

if __name__ == '__main__':
    unittest.main()

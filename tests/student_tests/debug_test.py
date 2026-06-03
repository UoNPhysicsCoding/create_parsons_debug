import unittest
import io
import sys

try:
    import student_solution as sol
except Exception:
    sol = None

class DebugTests(unittest.TestCase):
    def test_prints_hello(self):
        self.assertIsNotNone(sol, "Please place your solution in student_solution.py")
        captured = io.StringIO()
        sys_stdout = sys.stdout
        try:
            sys.stdout = captured
            # If student code defines functions, try calling greet()
            if hasattr(sol, 'greet'):
                sol.greet()
            else:
                # else execute module-level code by reloading
                import importlib
                importlib.reload(sol)
        finally:
            sys.stdout = sys_stdout
        output = captured.getvalue()
        self.assertIn('Hello', output)

if __name__ == '__main__':
    unittest.main()

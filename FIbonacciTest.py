import unittest
from CodeFibonacci import fibonacci
class TestFibonacci(unittest.TestCase):
    def Test1(self):
        self.assertEqual(1,fibonacci(1))
    def Test2(self):
        self.assertEqual(1,fibonacci(2))
    def Test3(self):
        self.assertEqual(2,fibonacci(3))
    def Test4(self):
        self.assertEqual(3,fibonacci(4))
    def Test5(self):
        self.assertEqual(5,fibonacci(5))

if __name__ == '__main__':
    unittest.main
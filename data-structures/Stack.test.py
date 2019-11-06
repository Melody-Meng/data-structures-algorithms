import unittest
from Stack import Stack



class TestGraph(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty_true(self):
        self.assertTrue(self.stack.is_empty())

    def test_is_empty_false(self):
        self.stack.push('a')
        self.assertFalse(self.stack.is_empty())

    def test_pop(self):
        self.stack.push('a')
        self.stack.push('b')
        self.assertEqual(self.stack.pop(), 'b')
        self.assertEqual(self.stack.pop(), 'a')

if __name__ == '__main__':
    unittest.main()
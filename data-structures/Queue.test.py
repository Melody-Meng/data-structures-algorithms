import unittest
from Queue import Queue

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_is_empty_true(self):
        self.assertTrue(self.queue.is_empty())

    def test_is_empty_false(self):
        self.queue.push('a')
        self.assertFalse(self.queue.is_empty())

    def test_pop(self):
        self.queue.push('a')
        self.queue.push('b')
        self.assertEqual(self.queue.pop(), 'a')
        self.assertEqual(self.queue.pop(), 'b')

if __name__ == '__main__':
    unittest.main()
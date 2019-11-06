import unittest
from Graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.addNode('A')
        self.graph.addNode('B')
        self.graph.addNode('C')
        self.graph.addNode('D')
        self.graph.addNode('E')

        self.graph.addEdge('A','B')
        self.graph.addEdge('B','C')
        self.graph.addEdge('B','D') 
        self.graph.addEdge('D','E') 

    def test_has_path_true(self):
        self.assertTrue(self.graph.hasPath('A', 'E'))

    def test_has_path_false(self):
        self.assertFalse(self.graph.hasPath('D', 'C'))

    def test_has_path_queue_true(self):
        self.assertTrue(self.graph.hasPathQueue('A', 'E'))

    def test_has_path_queue_false(self):
        self.assertFalse(self.graph.hasPathQueue('D', 'C'))

if __name__ == '__main__':
    unittest.main()
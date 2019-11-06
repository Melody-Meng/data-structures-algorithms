
from Stack import Stack
from Queue import Queue
class Graph:
    def __init__(self):
        self.graph = {}
    
    def addNode(self,node):
        self.graph[node] = {}

    def addEdge(self, nodeA, nodeB):

        assert nodeA in self.graph, "nodeA is not in the graph "
        assert nodeB in self.graph, "nodeB is not in the graph "

        self.graph[nodeA][nodeB] = 1
    
    def hasPath(self, nodeA, nodeB):

        assert nodeA in self.graph, "nodeA is not in the graph "
        assert nodeB in self.graph, "nodeB is not in the graph "

        stack = Stack()
        stack.push(nodeA)

        while not stack.is_empty():
            elem = stack.pop()
            neighbors = self.graph[elem]

            if elem == nodeB:
                return True
            
            stack.stack += neighbors.keys()
                
        return False

    def hasPathQueue(self, nodeA, nodeB):
        assert nodeA in self.graph, "nodeA is not in the graph "
        assert nodeB in self.graph, "nodeB is not in the graph "  

        queue = Queue()
        queue.push(nodeA)

        while not queue.is_empty():
            elem = queue.pop()
            neighbors = self.graph[elem]

            if elem == nodeB:
                return True
            queue.queue += neighbors.keys()
        return False


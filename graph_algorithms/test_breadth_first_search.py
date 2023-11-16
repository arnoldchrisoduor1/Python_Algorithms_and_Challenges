import unittest
from breadth_first_search import bfs

class TestBFS(unittest.TestCase):
    def test_bfs_simple(self):
        graph  = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['C']}
        result = self.bfs_transversal(graph, 'A')
        self.assertEqual(result, ['A', 'B', 'C', 'D', 'E'])

    def test_bfs_disconnected(self):
        graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C']}
        result = self.bfs_transversal(graph, 'A')
        self.assertEqual(result, ['A', 'B'])

    def bfs_transversal(self, graph, start):
        visited = set()
        transversal_result = []

        def process_node(node):
            transversal_result.append(node)

        bfs(graph, start, visited, process_node)

    if __name__ == "__main__":
        unittest.main()
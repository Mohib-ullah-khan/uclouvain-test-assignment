import unittest
from reachable import reachable


class TestReachable(unittest.TestCase):
    def test_empty_graph(self):
        """Test with an empty graph"""
        adj_list = []
        self.assertEqual(reachable(adj_list, 0), set())

    def test_single_node(self):
        """Test with a single node (no edges)"""
        adj_list = [[]]
        self.assertEqual(reachable(adj_list, 0), {0})

    def test_two_nodes_no_edges(self):
        """Test with two nodes and no edges"""
        adj_list = [[], []]
        self.assertEqual(reachable(adj_list, 0), {0})
        self.assertEqual(reachable(adj_list, 1), {1})

    def test_two_nodes_with_edge(self):
        """Test with two nodes and one edge"""
        adj_list = [[1], []]
        self.assertEqual(reachable(adj_list, 0), {0, 1})
        self.assertEqual(reachable(adj_list, 1), {1})

    def test_three_nodes_cycle(self):
        """Test with three nodes in a cycle"""
        adj_list = [[1], [2], [0]]
        self.assertEqual(reachable(adj_list, 0), {0, 1, 2})
        self.assertEqual(reachable(adj_list, 1), {0, 1, 2})
        self.assertEqual(reachable(adj_list, 2), {0, 1, 2})

    def test_disconnected_components(self):
        """Test with disconnected components"""
        adj_list = [[1], [0], [3], [2], []]
        self.assertEqual(reachable(adj_list, 0), {0, 1})
        self.assertEqual(reachable(adj_list, 2), {2, 3})
        self.assertEqual(reachable(adj_list, 4), {4})

    def test_complex_graph(self):
        """Test with a more complex graph"""
        adj_list = [[1, 2], [3], [3], [4], []]
        self.assertEqual(reachable(adj_list, 0), {0, 1, 2, 3, 4})
        self.assertEqual(reachable(adj_list, 1), {1, 3, 4})
        self.assertEqual(reachable(adj_list, 2), {2, 3, 4})
        self.assertEqual(reachable(adj_list, 3), {3, 4})
        self.assertEqual(reachable(adj_list, 4), {4})


if __name__ == "__main__":
    unittest.main()

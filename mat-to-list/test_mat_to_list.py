import unittest
from mat_to_list import mat_to_list


class TestMatToList(unittest.TestCase):
    def test_empty_matrix(self):
        """Test with an empty matrix"""
        adj_mat = []
        expected = []
        self.assertEqual(mat_to_list(adj_mat), expected)

    def test_single_node(self):
        """Test with a single node (no edges)"""
        adj_mat = [[0]]
        expected = [[]]
        self.assertEqual(mat_to_list(adj_mat), expected)

    def test_two_nodes_no_edges(self):
        """Test with two nodes and no edges"""
        adj_mat = [[0, 0], [0, 0]]
        expected = [[], []]
        self.assertEqual(mat_to_list(adj_mat), expected)

    def test_two_nodes_with_edge(self):
        """Test with two nodes and one edge"""
        adj_mat = [[0, 1], [0, 0]]
        expected = [[1], []]
        self.assertEqual(mat_to_list(adj_mat), expected)

    def test_three_nodes_cycle(self):
        """Test with three nodes in a cycle"""
        adj_mat = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
        expected = [[1], [2], [0]]
        self.assertEqual(mat_to_list(adj_mat), expected)

    def test_complete_graph(self):
        """Test with a complete graph of three nodes"""
        adj_mat = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        expected = [[1, 2], [0, 2], [0, 1]]
        self.assertEqual(mat_to_list(adj_mat), expected)


if __name__ == "__main__":
    unittest.main()

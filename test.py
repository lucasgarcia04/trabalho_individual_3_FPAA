import unittest
from main import hamiltonian_path

class TestHamiltonianPath(unittest.TestCase):
    def test_graph_with_path(self):
        graph = {
            0: [1, 2],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [1, 2]
        }
        path = hamiltonian_path(graph)
        self.assertIsNotNone(path)
        self.assertEqual(len(set(path)), len(graph))

    def test_graph_without_path(self):
        graph = {
            0: [1],
            1: [0, 2],
            2: [1],
            3: []
        }
        path = hamiltonian_path(graph)
        self.assertIsNone(path)

if __name__ == '__main__':
    unittest.main()

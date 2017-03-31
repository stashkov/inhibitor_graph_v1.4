from unittest import TestCase
import main as m


class TestAdd_combinations(TestCase):
    def setUp(self):
        self.edges = [(1, [2, 3]),
                      (2, [3, 4, 5])]
        self.result = [(1, [2, 3]),
                       (2, [3, 4, 5]),
                       (2, [3, 4]),
                       (2, [3, 5]),
                       (2, [4, 5])]

    def test_add_combinations(self):
        self.assertEqual(m.add_combinations(self.edges), self.result)


class TestDelete_rows_from_matrix(TestCase):
    def test_delete_rows_from_matrix(self):
        list_of_rows = [2,3]
        matrix = [[-1, -1, -1],
                  [0, 0, 0],
                  [0, 0, 0],
                  [1, 1, 1]]
        result = [[-1, -1, -1],
                  [1, 1, 1]]
        self.assertEqual(m.delete_rows_from_matrix(list_of_rows, matrix), result)

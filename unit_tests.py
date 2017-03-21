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

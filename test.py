import unittest
from rabin_karp import *


class MyTestCase(unittest.TestCase):
    def test_string_matching(self):
        self.assertEqual(rabin_karp("jabdkieabctidiekdjskjb", "ie", 256, 10007), [(5, 6), (13, 14)])

    def test_string_matching1(self):
        self.assertEqual(rabin_karp("aaaaaaa", "aaa", 256, 10007), [(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)])

    def test_string_matching2(self):
        self.assertEqual(rabin_karp("123456789123498763458765", "56", 10, 10007), [(4, 5)])

    def test_string_matching3(self):
        self.assertEqual(rabin_karp("1389462046", "1234", 10, 10007), [])


if __name__ == '__main__':
    unittest.main()

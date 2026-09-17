import os
import sys
import unittest

# Añade la carpeta 'Arrays' al path de Python de forma dinámica
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Arrays')))

from ZeroMatrix import setZeroes

class TestZeroMatrix(unittest.TestCase):
    def test_unique_string(self):
        matrix = [[2, 1, 3, 0, 2], [7, 4, 1, 3, 8], [4, 0, 1, 2, 1], [9, 3, 4, 0, 9]]
        self.assertEqual(setZeroes(matrix), [[0, 0, 0, 0, 0], [7, 0, 1, 0, 8], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

if __name__ == '__main__':
    unittest.main()
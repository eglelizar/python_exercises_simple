import os
import sys
import unittest

# Añade la carpeta 'Arrays' al path de Python de forma dinámica
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Arrays')))

from TwoArraySearchTarget import getIndexesWhichValuesSumTarget

class TestTwoIndexestargetting(unittest.TestCase):
    def test_unique_string(self):
        self.assertEqual(getIndexesWhichValuesSumTarget([9,2,5,6],7), [1,2])

if __name__ == '__main__':
    unittest.main()
import os
import sys
import unittest

# Añade la carpeta 'Arrays' al path de Python de forma dinámica
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Arrays')))

from StringElementsAreUnique import caractersAreUnique

class TestcaractersAreUnique(unittest.TestCase):
    def test_unique_string(self):
        self.assertEqual(caractersAreUnique("hi"), True)

    def test_nonunique_string(self):
        self.assertEqual(caractersAreUnique("hello"), False)

if __name__ == '__main__':
    unittest.main()
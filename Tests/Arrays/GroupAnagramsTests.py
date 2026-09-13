import os
import sys
import unittest

# Añade la carpeta 'Arrays' al path de Python de forma dinámica
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Arrays')))

from GroupAnagrams import getAnagramsGroups

class GroupAnagramsTests(unittest.TestCase):
    def test_unique_string(self):
        words = [ "saco", "arresto", "programa", "rastreo", "caso" ]
        self.assertEqual(getAnagramsGroups(words),[['saco', 'caso'], ['arresto', 'rastreo'], ['programa']])

if __name__ == '__main__':
    unittest.main()
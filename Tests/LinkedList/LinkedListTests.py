import os
import sys
import unittest

# Añade la carpeta 'Arrays' al path de Python de forma dinámica
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../LinkedList')))

from LinkedList import LinkedList

class LinkedListTests(unittest.TestCase):

    def test_insert_at_tail(self):
        l = LinkedList()
        l.insertAtTail(10)
        l.insertAtTail(20)
        l.insertAtTail(30)

        # Verify structure by traversing manually
        assert l.head.data == 10
        assert l.head.next.data == 20
        assert l.head.next.next.data == 30
        assert l.head.next.next.next is None

    def test_eliminate_head_node(self):
        l = LinkedList()
        l.insertAtTail(18)
        l.insertAtTail(25)
        l.insertAtTail(10)

        # Eliminate the head node (18)
        l.eliminateANode(18)

        assert l.head.data == 25
        assert l.head.next.data == 10

    def test_eliminate_middle_node(self):
        l = LinkedList()
        l.insertAtTail(18)
        l.insertAtTail(25)
        l.insertAtTail(10)

        # Eliminate a middle node (25)
        l.eliminateANode(25)

        assert l.head.data == 18
        assert l.head.next.data == 10
        assert l.head.next.next is None

    def test_eliminate_tail_node(self):
        l = LinkedList()
        l.insertAtTail(18)
        l.insertAtTail(25)
        l.insertAtTail(10)

        # Eliminate the tail node (10)
        l.eliminateANode(10)

        assert l.head.data == 18
        assert l.head.next.data == 25
        assert l.head.next.next is None

if __name__ == '__main__':
    unittest.main()
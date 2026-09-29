


from Node import Node

class LinkedList:

    head = None 

    def __init__(self):
        self.head = None

    def insertAtTail(self, data):
        new_node = Node(data)

       #Trasversing the list to find the last node
        if (self.head== None):
            self.head = new_node
        else:
            next = self.head
            while next.next is not None:
                next = next.next
            next.next = new_node

    def eliminateANode(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
        else:
            pointer = self.head
            previous = None
            while pointer is not None and pointer.data != value:
                previous = pointer
                pointer = pointer.next

            # Only unlink if the node was actually found
            if pointer is not None:
                previous.next = pointer.next

        self.printElements()


    def printElements(self):
        next = self.head
        while next.next != None:
            print (next.data)
            next = next.next
        print (next.data)

    

#Insert 18,25,10,15, 2
l = LinkedList()
l.insertAtTail(18)
l.insertAtTail(25)
l.insertAtTail(10)
l.insertAtTail(15)
l.insertAtTail(2)
l.printElements()
l.eliminateANode(15)
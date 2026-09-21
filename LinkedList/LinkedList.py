


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
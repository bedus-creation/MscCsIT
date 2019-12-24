from SecondSem.CG.Lab_03.src.Node import Node

class LinkList:
    def __init__(self):
        self.head = None

    def append(self, val):
        newNode = Node(val)
        if (self.head is None):
            self.head = newNode
            newNode.next = self.head
            newNode.prev = self.head
            return

        # on non empty lists
        last = self.head
        while(last.next is not self.head):
            last = last.next

        newNode.next = last.next
        newNode.prev = last
        last.next = newNode
        return

    def printList(self):
        last = self.head
        while(last.next is not self.head):
            print(last.data.x, last.data.y)
            last = last.next
        print(last.data.x, last.data.y)

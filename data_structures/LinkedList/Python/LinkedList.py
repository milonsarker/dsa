class Node:
    def __init__(self, input_data):
        self.data = input_data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def print_LinkedList(self):
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next

if __name__=="__main__":
    n1 = Node('Sun')
    n2 = Node('Mon')
    n3 = Node('Tue')
    n4 = Node('Wed')
    n5 = Node('Thu')

    lList = LinkedList()
    lList.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    lList.print_LinkedList()
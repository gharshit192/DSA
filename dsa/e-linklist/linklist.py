class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __int__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)

    def display(self):
        if not self.head:
            print(None)
            return
        temp = self.head
        while temp:
            print(temp.val, end="-->")
            temp = temp.next
        print("None")

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node



def main():
    l1 = LinkedList()
    # l1.head = Node(1)
    # l1.head.next = Node(2)
    # l1.head.next.next = Node(3)
    # l1.head.next.next.next = Node(4)

    for val in [1, 2, 3, 4]:
        l1.append(val)
    # l1.prepend(9)

    # l1.display()
    l1.delete(2)


main()

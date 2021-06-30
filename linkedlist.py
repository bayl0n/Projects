class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)

        temp = self.head
        newNode.next = temp
        self.head = newNode

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    myList = LinkedList()

    myList.insert("Bob")
    myList.insert("James")
    myList.insert("Apple")
    myList.insert("Private")

    myList.display()
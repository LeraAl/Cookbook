class Node:
    def __init__(self, data):
        self.x, self.y = data
        self.next = None
        self.prev = None


class Snake:
    def __init__(self):
        self.head = None
        self.tail = None
        self.add((0, 0))
        self.add((0, 1))
        self.add((0, 2))
        self.add((0, 3))

    def add(self, pos):
        if self.head == None:
            self.head = Node(pos)
            self.tail = self.head
        else:
            temp = Node(pos)
            self.head.prev = temp
            temp.next = self.head
            self.head = temp

    def delete(self):
        self.tail.prev.next = None
        self.tail = self.tail.prev

    def __len__(self):
        temp = self.head
        i = 0
        while temp:
            i += 1
            temp = temp.next
        return i
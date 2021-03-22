import sys
sys.stdin = open('수열 합치기.txt')


class Node:
    def __init__(self):
        self.data = None
        self.prev = None
        self.next = None

class Linked_List():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node()
        new_node.data = data
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def append_left(self, data):
        new_node = Node()
        new_node.data = data
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_list(self, Llist):
        cur = self.head
        while cur.next != None and cur.data <= Llist.head.data:
            cur = cur.next
        if cur.next == None and cur.data <= Llist.head.data:
            Llist.head.prev = cur
            cur.next = Llist.head
            self.tail = Llist.tail
        elif cur == self.head:
            Llist.tail.next = cur
            cur.prev = Llist.tail
            self.head = Llist.head
        else:
            Llist.head.prev = cur.prev
            Llist.tail.next = cur
            cur.prev.next = Llist.head
            cur.prev = Llist.tail
        self.size += Llist.size

    def print_reverse(self):
        cur = self.tail
        for _ in range(10):
            print(cur.data, end=' ')
            cur = cur.prev
        print()

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    result = Linked_List()
    for num in map(int, input().split()):
        result.append(num)
    for _ in range(M-1):
        Llist = Linked_List()
        for num in map(int, input().split()):
            Llist.append(num)
        result.insert_list(Llist)
    print("#{} ".format(test_case), end='')
    result.print_reverse()
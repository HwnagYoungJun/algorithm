import sys
sys.stdin = open('수열 편집.txt')

class Node:
    def __init__(self, data=0, nex=None):
        self.data = data
        self.next = nex
    def __str__(self):
        return f"{self.data}"

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.count = 0

    def __del__(self):
        self.count -= 1

    def append(self, node):
        self.count += 1
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def delete(self, index):
        if index == 0:
            cur = self.head
            self.head = cur.next
            cur.next = None
        else:
            cur = self.head
            for _ in range(index-1):
                cur = cur.next
            temp = cur.next
            cur.next = cur.next.next
            temp.next = None
        self.count -= 1
        
    def insert(self, node, index):
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            cur = self.head
            for _ in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
        self.count += 1
    
    def print(self):
        result = []
        cur = self.head
        while cur.next != None:
            result.append(cur.data)
            cur = cur.next
        result.append(cur.data)
        print(result)
        
    def get(self, index):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur

    def len(self):
        return self.count

    def change(self, index, data):
        node = self.head

        for _ in range(index):
            node.data = data

T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    number = list(map(int, input().split()))
    my_list = LinkedList()

    for i in range(N):
        my_list.append(number[i])

    for i in range(M):
        temp = list(input().split())
        if temp[0] == 'I':
            my_list.insert(int(temp[1]), int(temp[2]))
        elif temp[0] == 'D':
            my_list.delete(int(temp[1]))
        elif temp[0] == 'C':
            my_list.change(int(temp[1]), int(temp[2]))
    my_list.print()
    # print("#{} {}".format(test_case, result))
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
# head = a
# print(a.next.data)


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.tail = Node


class LinkList(object):
    def __init__(self, li, method='tail'):
        self.head = None
        if method == 'tail':
            self.create_linklist_tail(li)
        else:
            self.create_linklist_head(li)

    def create_linklist_tail(self, li):
        self.head = Node()
        for i in li:
            s = Node(i)
            s.next = self.head
            self.head = s
    def create_linklist_head(self, li):
        self.head = Node()
        for i in li:
            s = Node(i)
            s.next = self.head
            self.head = s

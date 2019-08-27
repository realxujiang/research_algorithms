#!/usr/bin/env python
#-*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    s1 = ''
    s2 = ''
    while l1 is not None:
        s1 += str(l1.val)
        l1 = l1.next

    while l2 is not None:
        s2 += str(l2.val)
        l2 = l2.next

    sum = str(int(s1) + int(s2))

    root = n = ListNode(0)
    for i in sum:
        n.next = ListNode(i)
        n = n.next
    return root.next

def createListNode(node):
    root = n = ListNode(0)
    for i in str(node):
        n.next = ListNode(i)
        n = n.next
    return root.next

def printLN(node):
    res = ''
    while node is not None:
        res += str(node.val) + " -> "
        node = node.next
    return res

if __name__ == "__main__":
   l1 = createListNode(1234)
   l2 = createListNode(34)
   res = addTwoNumbers(l1, l2)
   print printLN(res)


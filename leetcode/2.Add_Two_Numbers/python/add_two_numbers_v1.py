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
    
    sum = str(int(s1[::-1]) + int(s2[::-1]))[::-1]

    head = ListNode(sum[0])
    temp = head
    for val in sum[1:]:
        temp.next = ListNode(val)
        temp = temp.next
    return head

def createListNode(l1):
    head = ListNode(str(l1)[0])
    temp = head
    for val in str(l1)[1:]:
        temp.next = ListNode(val)
        temp = temp.next
    return head

def printLN(l1):
    res = ''
    while l1 is not None:
        res += l1.val + ' -> '
        l1 = l1.next
    return res

l1 = createListNode(18)
l2 = createListNode(0)
print 'Input1:' +  printLN(l1)
print 'Input2:' + printLN(l2)
res = addTwoNumbers(l1, l2)
print 'Output:' + printLN(res)

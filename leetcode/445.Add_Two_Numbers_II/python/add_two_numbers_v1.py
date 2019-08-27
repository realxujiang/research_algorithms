#!/usr/bin/env python
#-*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TwoNumbers(object):

    @staticmethod
    def builderListNode(nums):
        if nums is not None:
            head  = ListNode(str(nums)[0])
            a = head
            for i in str(nums)[1:]:
                b = ListNode(i)
                a.next = b
                a = a.next
            return head

    @staticmethod
    def addTwoNumbers(n1, n2):
        s1 = ""
        s2 = ""
        while n1 is not None:
            s1 += str(n1.val)
            n1 = n1.next
        while n2 is not None:
            s2 += str(n2.val)
            n2 = n2.next

        summation = str(int(s1) + int(s2))
        head = ListNode(summation[0])
        
        temp = head
        for val in summation[1:]:
            temp.next = ListNode(val)
            temp = temp.next
        return head

    @staticmethod
    def printLS(node):
        if not node:
            return None

        res = ''
        while node:
            res += str(node.val) + ' -> '
            node = node.next
        print res

if __name__ == "__main__":
    tn = TwoNumbers()
    l1 = tn.builderListNode(1234)
    l2 = tn.builderListNode(34)
    tn.printLS(tn.addTwoNumbers(l1, l2))

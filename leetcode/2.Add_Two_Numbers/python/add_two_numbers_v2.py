class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            sum = int(v1) + int(v2) + carry 
            # carry, val = divmod(sum, 10)
            carry = sum / 10
            val = sum % 10
            n.next = ListNode(val)
            n = n.next
        return root.next

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
        res += str(l1.val) + ' -> '
        l1 = l1.next
    return res

l1 = createListNode(243)
l2 = createListNode(564)
print 'Input1:' +  printLN(l1)
print 'Input2:' + printLN(l2)
res = addTwoNumbers(l1, l2)
print 'Output:' + printLN(res)

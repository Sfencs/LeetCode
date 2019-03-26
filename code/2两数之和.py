# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 自己的巨菜方法
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        node = result
        while l1 is not None and l2 is not None:
            yushu = (l1.val + l2.val+node.val) % 10
            shang = (l1.val + l2.val+node.val) // 10
            node.val = yushu
            l1 = l1.next
            l2 = l2.next
            if l1 is None and l2 is None:
                if shang == 0:
                    node.next = None
                else:
                    node.next = ListNode(shang)
                    node = node.next
            else:
                node.next = ListNode(shang)
                node = node.next

        if l1 is not None:
            while l1 is not None:
                yushu = (l1.val + node.val) % 10
                shang = (l1.val + node.val) // 10
                node.val = yushu
                l1 = l1.next
                if l1 is None:
                    if shang == 0:
                        node.next = None
                    else:
                        node.next = ListNode(shang)
                        node = node.next
                else:
                    node.next = ListNode(shang)
                    node = node.next

        if l2 is not None:
            while l2 is not None:
                yushu = (l2.val + node.val) % 10
                shang = (l2.val + node.val) // 10
                node.val = yushu
                l2 = l2.next
                if l2 is None:
                    if shang == 0:
                        node.next = None
                    else:
                        node.next = ListNode(shang)
                        node = node.next
                else:
                    node.next = ListNode(shang)
                    node = node.next
        return result


    # 看看人家的
    def other1(self, l1: ListNode, l2: ListNode) -> ListNode:
        re = ListNode(0)
        r = re
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        if (carry > 0):
            r.next = ListNode(1)
        return re.next

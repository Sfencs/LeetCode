# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 我的
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        node = result
        if l1 is None and l2 is None:
            return None
        while l1 and l2:
            if l1.val < l2.val:
                node.val = l1.val
                node.next = ListNode(0)
                node = node.next
                l1 = l1.next
            else:
                node.val = l2.val
                node.next = ListNode(0)
                node = node.next
                l2 = l2.next

        if l1:
            while l1:
                node.val = l1.val
                node.next = ListNode(0)

                l1 = l1.next
                if l1 is None:
                    break
                node = node.next

        if l2:
            while l2:
                node.val = l2.val
                node.next = ListNode(0)
                l2 = l2.next
                if l2 is None:
                    break
                node = node.next

        node.next = None
        return result


    # 别人的
    def other(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val<l2.val:
                node.next,l1 = l1,l1.next
            else:
                node.next,l2 = l2,l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next



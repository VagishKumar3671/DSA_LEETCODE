class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        damp = ListNode(-1)  # dummy node
        damp.next = head
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next  # skip duplicate
            else:
                node = node.next  # move forward
        return damp.next

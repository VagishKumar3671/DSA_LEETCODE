class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        dump = ListNode(-1)
        dump.next = head
        prev = dump
        node = head

        while node:
            # Detect duplicates
            if node.next and node.val == node.next.val:
                val = node.val
                # Skip all nodes with this duplicate value
                while node and node.val == val:
                    node = node.next
                prev.next = node
            else:
                prev = node
                node = node.next

        return dump.next

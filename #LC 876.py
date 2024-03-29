#LC 876.py 链表的中间结点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针初始化指向 head
        slow = head
        fast = head
    # 快指针走到末尾时停止
        while fast and fast.next:
        # 慢指针走一步，快指针走两步
            slow = slow.next
            fast = fast.next.next
    # 慢指针指向中点
        return slow
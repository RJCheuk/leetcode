#LC 160.py 两个链条是否相交
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
    # 计算两条链表的长度
        p1, p2 = headA, headB
        while p1:
            lenA += 1
            p1 = p1.next
        while p2:
            lenB += 1
            p2 = p2.next
        # 让 p1 和 p2 到达尾部的距离相同
        p1, p2 = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                p1 = p1.next
        else:
            for i in range(lenB - lenA):
                p2 = p2.next
        # 看两个指针是否会相同，p1 == p2 时有两种情况：
        # 1、要么是两条链表不相交，他俩同时走到尾部空指针
        # 2、要么是两条链表相交，他俩走到两条链表的相交点
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
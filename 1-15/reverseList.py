# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
    # write code here
        if pHead is None or pHead.next is None:
            return pHead
        pre = None
        cur = pHead
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

if __name__ == '__main__':
    a = Solution(ListNode(0))

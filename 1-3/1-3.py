# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
    # write code here
        a = []
        if listNode == None:
            return a
        while listNode.next is not None:
            a.append(listNode.val)
            listNode = listNode.next
        a.append(listNode.val)
        a.reverse()
        return



# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, node):
        # write code here
        self.stackIn.append(node)

    def pop(self):
        # return xx
        if self.stackOut == []:
            if self.stackIn == []:
                return None
            else:
                for i in range(len(self.stackIn)):
                    self.stackOut.append(self.stackIn.pop())
        return self.stackOut.pop()


if __name__ == '__main__':
    testList = list(range(5))
    testQueue = Solution()
    for i in range(5):
        testQueue.push(testList[i])
    print(testList)
    for i in range(5):
        print(testQueue.pop(), end=' ')


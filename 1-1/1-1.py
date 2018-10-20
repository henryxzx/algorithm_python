# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(tree_base, target, array):
        # write code here
        if len(array) == 0 :
            return False
        row = len(array); col = len(array[0])
        r = 0; c = col - 1
        while r <= row - 1 and c >= 0:
            if target == array[r][c]:
                return True
            elif target < array[r][c]:
                c -= 1
            elif target > array[r][c]:
                r += 1
            else:
                return False
        else:
            return False

if __name__ == '__main__' :
    array = [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ]
    targetT = 9; targetF = 20
    s = Solution()
    print(s.Find(targetT, array))
    print(s.Find(targetF, array))
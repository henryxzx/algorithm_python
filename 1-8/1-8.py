# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        a, b = 1, 2
        while number > 1:
            a, b = b, a + b
            number -= 1
        return a


if __name__ == '__main__':
    num = int(input('input num:'))
    a = Solution()
    print(a.jumpFloor(num))

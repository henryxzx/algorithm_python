# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        a, b = 1, 2
        while number > 1:
            a, b = b, a + b
            number -= 1
        return a


if __name__ == '__main__':
    a = Solution()
    print(a.rectCover(3))
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        a, b = 0, 1
        while n:
            a, b = b, a + b
            n -= 1
        return a

if __name__ == '__main__':
    index = int(input('input num:'))
    # print(type(index))
    a = Solution()
    print(a.Fibonacci(index))
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        a= []
        for i in range(number):
            ans = 0
            if i == 0:
                a.append(1)
                continue
            for j in range(i):
                ans += a[j]
            a.append(ans + 1)
            print(a)
        return a.pop()


if __name__ == '__main__':
    a = Solution()
    print(a.jumpFloorII(3))
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res = s.replace(' ', '%20')
        return res

if __name__ == '__main__':
    str = 'This is a testing string  .'
    s = Solution()
    print(s.replaceSpace(str))
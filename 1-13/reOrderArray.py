# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        # even, odd = [], []      # even为偶数 odd为奇数
        # for i in range(len(array)):
        #     if array[i] % 2:
        #         odd.append(array[i])
        #     else:
        #         even.append(array[i])
        # odd.extend(even)
        # return odd

        #lambda函数一行解法
        print(lambda c: c % 2)
        return sorted(array, key=lambda c: c % 2, reverse=True)


if __name__ == '__main__':
    a = Solution()
    test = [1, 5, 8, 2, 9, 34]
    print(a.reOrderArray(test))

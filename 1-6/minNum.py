# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return min(rotateArray)

        #write code here
        if len(rotateArray) < 1:
            return 0
        left, right = 0, len(rotateArray) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if rotateArray[left] <= rotateArray[mid]:
                left = mid
            elif rotateArray[mid] <= rotateArray[right]:
                right = mid
        return rotateArray[right]


if __name__ == '__main__':
    a = Solution()
    array = [3, 4, 5, 1, 2]
    print(a.minNumberInRotateArray(array))
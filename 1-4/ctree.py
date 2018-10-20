#coding=utf-8

import sys
import Tree1
sys.path.append(r"F:\algorithm\1-4")

class BinaryTree():
    def __init__(self, base = 0):
        self.base = base
    '''
    后序遍历
    '''
    def postOrder(self, tree_base):
        if not tree_base:
            return False
        self.postOrder(tree_base.left)
        self.postOrder(tree_base.right)
        print(tree_base.val, end='')

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            ans = TreeNode(pre[0])
            ans.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
            ans.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
            return ans


if __name__ == '__main__':
    a = Solution()
    pre = [1,2,4,5,3,6,7]
    tin = [4,2,5,1,6,3,7]
    b = a.reConstructBinaryTree(pre,tin)
    BinaryTree().postOrder(b)
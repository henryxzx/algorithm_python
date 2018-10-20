class Tree():
    def __init__(self, ltree = 0, rtree = 0, data = 0):
        self.ltree = ltree
        self.rtree = rtree
        self.data = data

class BinaryTree():
    def __init__(self, base = 0):
        self.base = base
    '''
    判断是否为空
    '''
    def _Empty(self):
        if self.base == 0:
            return True
        else:
            return False
    '''
    前序遍历
    '''
    def preOrder(self, tree_base):
        if tree_base == 0:
            return False
        print(tree_base.data, end='')
        self.preOrder(tree_base.ltree)
        self.preOrder(tree_base.rtree)
    '''
    中序遍历
    '''
    def inOrder(self, tree_base):
        if tree_base == 0:
            return False
        self.inOrder(tree_base.ltree)
        print(tree_base.data, end='')
        self.inOrder(tree_base.rtree)
    '''
    后序遍历
    '''
    def postOrder(self, tree_base):
        if tree_base == 0:
            return False
        self.postOrder(tree_base.ltree)
        self.postOrder(tree_base.rtree)
        print(tree_base.data, end='')


if __name__ == '__main__':
    tree1 = Tree(data=8)
    tree2 = Tree(data=9)
    tree3 = Tree(tree1, data=6)
    tree4 = Tree(tree2, 0, data=7)
    base = Tree(tree3, tree4, 5)
    btree = BinaryTree(base)
    print('前序遍历结果：')
    btree.preOrder(btree.base)
    print('\n中序遍历结果：')
    btree.inOrder(btree.base)
    print('\n后序遍历结果：')
    btree.postOrder(btree.base)
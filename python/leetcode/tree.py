# -*- coding: utf-8 -*-
# @time: 2020-05-11 10:56
# @file: tree.py

from python.tree import *


def maxDepth(root):
    if root is None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def minDepth(root):
    """
    leetcode 111. 二叉树的最小深度
    - 根节点到树叶节点
    :param root:
    :return:
    """
    if root is None:
        return 0
    if not root.left:
        return minDepth(root.right) + 1
    if not root.right:
        return minDepth(root.left) + 1
    return min(minDepth(root.left), minDepth(root.right)) + 1


def hasPathSum(root, _sum):
    """
    leetcode 112 路径和
    :param root:
    :param _sum:
    :return:
    """
    if root is None:
        return False
    if root.val == _sum and root.left is None and root.right is None:
        return True
    return hasPathSum(root.left, _sum-root.val) or hasPathSum(root.right, _sum-root.val)

if __name__ == '__main__':
    
    xtree = BinTree().list_to_tree(range(10))
    print(xtree)
    
    # print(tree_height(xtree))
    # print(tree_m_height(xtree))
    
    print(hasPathSum(xtree, 11))
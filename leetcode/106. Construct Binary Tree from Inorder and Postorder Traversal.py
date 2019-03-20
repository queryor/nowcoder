# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if postorder==[] or inorder==[]:
            return None
        for i in range(len(inorder)):
            if inorder[i]==postorder[-1]:
                break
        cur = TreeNode(postorder[-1])
        cur.left = self.buildTree(inorder[:i],postorder[:i])
        cur.right = self.buildTree(inorder[i+1:],postorder[i:-1])
        return cur
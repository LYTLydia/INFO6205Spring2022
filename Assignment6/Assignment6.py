# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Q1
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        def helper(root,sum):
            count = 0
            if not root:
                return 0
            if root.val==sum:
                count += 1

            count += helper(root.left, sum-root.val)
            count += helper(root.right,sum-root.val)
            return count

        return helper(root,targetSum)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)

#Q2
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root is p or root is q:
            return root

        root.left=self.lowestCommonAncestor(root.left,p,q)
        root.right=self.lowestCommonAncestor(root.right,p,q)

        if root.left and root.right:
            return root
        if not root.left:
            return root.right
        if not root.right:
            return root.left
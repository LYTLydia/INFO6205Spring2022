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

#Q3
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        count=0

        def helper(root):
            nonlocal count
            if not root:
                return 0

            l=0
            r=0

            left=helper(root.left)
            right=helper(root.right)

            if root.left:
                if root.left.val==root.val:
                    l=left+1
            if root.right:
                if root.right.val==root.val:
                    r=right+1

            count=max(count,l+r)
            return max(l,r)

        helper(root)
        return count

#Q4
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res=[]
        def helper(root):
            if not root:
                res.append("N")
                return

            res.append(str(root.val))
            helper(root.left)
            helper(root.right)
        helper(root)

        return ",".join(res)




    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        l=data.split(",")
        i=0

        def helper():
            nonlocal i
            if l[i]=="N":
                i+=1
                return None
            root = TreeNode(int(l[i]))
            i+=1
            root.left=helper()
            root.right=helper()
            return root
        return helper()

#Q5
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        values={}
        res=[]
        v=0
        h=0

        self.helper(root,h,v,values)

        for x in sorted(values.keys()):
            l=[i[1] for i in sorted(values[x])]
            res.append(l)
        return res

    def helper(self, root, h, v, values):
        if not root:
            return
        if h in values:
            values[h].append((v,root.val))
        else:
            values[h]=[(v,root.val)]

        self.helper(root.left,h-1,v+1,values)
        self.helper(root.right,h+1,v+1,values)

#Q6
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        res=[]

        def helper(root):
            if not root:
                return 0
            res.append(root.val)

            helper(root.left)
            helper(root.right)

        helper(root)

        return len(res)

#Q7
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        temp=[]

        def helper(root,cur):
            if not root:
                return 0
            cur+=str(root.val)

            if not root.left and not root. right:
                temp.append(cur)
            helper(root.left,cur)
            helper(root.right,cur)


        helper(root,"")

        return sum([int(i) for i in temp])

#Q8
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return

            if not root.left and not root.right and root.val == target:
                return None

            root.left = helper(root.left)
            root.right = helper(root.right)

            if not root.left and not root.right and root.val == target:
                return None

            return root

        return helper(root)
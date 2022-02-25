# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Q1
    #opt1
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if root ==None:
            return res

        q=deque([])
        q.append(root)
        temp=deque([])
        while len(q)>0:
            size=len(q)
            l=[]
            while size>0:
                cur=q.popleft()
                l.append(cur.val)
                if cur.left !=None:
                    q.append(cur.left)
                if cur.right !=None:
                    q.append(cur.right)
                size-=1
            temp.appendleft(l[:])
        res = list(temp)

        return res

    #opt2
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if root ==None:
            return res

        q=deque([])
        q.append(root)
        while len(q)>0:
            size=len(q)
            l=[]
            while size>0:
                cur=q.popleft()
                l.append(cur.val)
                if cur.left !=None:
                    q.append(cur.left)
                if cur.right !=None:
                    q.append(cur.right)
                size-=1
            res.append(l[:])
        res = res[::-1]

        return res

#Q2
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res=[]

        def helper(root):
            if root == None:
                return 0

            l=helper(root.left)
            r=helper(root.right)
            h=max(l,r)

            if len(res)==h:
                res.append([])
            res[h].append(root.val)
            return h+1
        helper(root)
        return res

#Q3
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque()
        iQ=deque()
        res=0

        if root==None:
            return 0

        q.append(root)
        iQ.append(1)

        while len(q)>0:
            levelSize=len(q)
            initialIndex=iQ[0]
            i=initialIndex
            while levelSize>0:
                cur=q.popleft()
                i=iQ.popleft()
                if cur != None:
                    if cur.left != None:
                        q.append(cur.left)
                        iQ.append(i*2)
                    if cur.right != None:
                        q.append(cur.right)
                        iQ.append(i*2+1)
                levelSize-=1

            w=i-initialIndex+1
            res=max(res,w)

        return res


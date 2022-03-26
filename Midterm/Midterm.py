#Q1
class Solution:
    def missingRanges(self, nums: List[int], a: int, b: int) -> List[str]:
        left, ans = a, []
        for right in nums + [b + 1]:
            if right - 1 > left:
                ans.append(str(left)+'->'+str(right-1))
            elif right - 1 == left:
                ans.append(str(left))
            left = right + 1
        return ans



#Q2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1=[]
        a2=[]
        while l1:
            a1.append(l1.val)
            l1=l1.next
        while l2:
            a2.append(l2.val)
            l2=l2.next
        a1_int=int("".join(map(str,a1[::-1])))
        a2_int=int("".join(map(str,a2[::-1])))

        arr_int=a1_int+a2_int
        arr=[int(a) for a in str(arr_int)]

        p=res=ListNode()
        for i in arr[::-1]:
            p.next=ListNode(i)
            p=p.next
        return res.next


#Q3
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        rootValue=preorder[0]
        root=TreeNode(rootValue)
        i=inorder.index(rootValue)

        root.left=self.buildTree(preorder[1:i+1],inorder[:i])
        root.right=self.buildTree(preorder[i+1:],inorder[i+1:])

        return root


#Q4
class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        res = []
        for i in l1:
            for j in l2:
                if i[0] > j[1] or i[1] < j[0]:
                    continue
                res.append([max(i[0], j[0]), min(i[1], j[1])])
        return res





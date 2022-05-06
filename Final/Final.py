#1
class Solution:
    def compress(self, res):
        if len(res) == 0:
            return res
        ans = []
        count = 1
        last = res[0]
        for c in res[1:]:
            if c == last:
                count += 1
            else:
                ans.append(last)
                ans.append("%s" % count)
                last = c
                count = 1

        ans.append(last)
        ans.append("%s" % count)

        if len(ans) < len(res):
            return ''.join(ans)
        else:
            return res


#2
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def helper(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                helper(i + 1, j)
                helper(i - 1, j)
                helper(i, j - 1)
                helper(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    helper(i, j)
        return res


#3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())

#4
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

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


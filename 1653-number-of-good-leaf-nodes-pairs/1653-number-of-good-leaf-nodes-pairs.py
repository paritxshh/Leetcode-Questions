# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root, count, i):
            if root is None or i >= distance:
                return
            if root.left is None and root.right is None:
                count[i] += 1
                return
            dfs(root.left, count, i + 1)
            dfs(root.right, count, i + 1)

        if root is None:
            return 0
        ans = self.countPairs(root.left, distance) + self.countPairs(root.right, distance)
        count1 = Counter()
        count2 = Counter()
        dfs(root.left, count1, 1)
        dfs(root.right, count2, 1)

        for k1, v1 in count1.items():
            for k2, v2 in count2.items():
                if k1 + k2 <= distance:
                    ans += v1 * v2
        
        return ans
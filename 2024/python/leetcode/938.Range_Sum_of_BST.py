# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        # sol_1 - dfs (브루트포스)
        if not root:
            return 0

        return (root.val if low <= root.val <= high else 0) + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        '''

        '''
        # sol_2 - dfs(가지치기)
        def dfs(node):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        return dfs(root)
        '''
        '''
        # sol_3 - 반복구조 dfs
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum
        '''

        # sol_4 - 반복구조 bfs
        stack, sum = [root], 0
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum


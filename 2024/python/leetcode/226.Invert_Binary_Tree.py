# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        # sol_1
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        '''

        '''
        # sol_2 - bfs
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left

                q.append(node.left)
                q.append(node.right)

        return root
        '''
        '''
        # sol_3 - dfs (전위 순회)
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)
        return root
        '''

        # sol_4 - dfs (후위 순회)
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left

        return root
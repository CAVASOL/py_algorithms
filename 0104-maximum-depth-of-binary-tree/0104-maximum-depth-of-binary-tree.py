# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        list = deque([root])
        node_level = 1
        depth = 0

        while list:
            node = list.popleft()

            if node.left:
                list.append(node.left)
            if node.right:
                list.append(node.right)
            
            node_level -= 1
            if node_level == 0:
                depth += 1
                node_level = len(list)

        return depth
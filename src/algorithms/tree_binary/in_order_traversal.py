
from typing import List, Optional

from tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root is None:
        #     return []

        # left = self.inorderTraversal(root.left)
        # right = self.inorderTraversal(root.right)
        # return [*left, root.val, *right]

        stack = []
        current = root
        result = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result
    
print(Solution().inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
        
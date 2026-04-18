from typing import List, Optional
from tree_node import TreeNode

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        https://leetcode.com/problems/binary-tree-right-side-view/
        '''

        results = []
        # def recurse(_root: Optional[TreeNode], depth: int):
        #     if _root is None:
        #         return

        #     if depth == len(results):
        #         results.append(_root.val)
            
        #     recurse(_root.right, depth+1)
        #     recurse(_root.left, depth+1)

        # recurse(root, 0)


        current = root
        depth = 0
        while current:
            if depth == len(results):
                results.append(current.val)

            depth += 1
            right_subtree = current.right
            while right_subtree:
                results.append(right_subtree.val)
                right_subtree = current.right
                depth += 1

            left_subtree = current.left
            while left_subtree:
                results.append(left_subtree.val)
                left_subtree = left_subtree.left
                depth += 1
                
        return results
    
print(Solution().rightSideView(
    TreeNode(1,
             TreeNode(2,
                      TreeNode(4,
                               TreeNode(5))), TreeNode(3))
)) # [1, 3, 4, 5]
from typing import Optional


class TreeNode:
    left: 'Optional[TreeNode]'
    right: 'Optional[TreeNode]'
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    # Lowest Common Ancestor Binary Tree
    # Level Order Traversal /Breadth First Search
    # Leetcode tree study guide
    
    # def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    #     pass
    max_path: int = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
    # def _maxDepthRecursive(self, node, current_depth, max_depth):
    #     if node == None:
    #         return max_depth
        
    #     max_depth = max(current_depth, max_depth)
    #     max_depth = max(self._maxDepthRecursive(node.left, current_depth+1, max_depth), max_depth)
    #     max_depth = max(self._maxDepthRecursive(node.right, current_depth+1, max_depth), max_depth)
    #     return max_depth
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return max(self.max_path, self._diameterOfBinaryTreeRecursive(root, 0))

    def _diameterOfBinaryTreeRecursive(self, root: Optional[TreeNode], depth) -> int:
        if root == None:
            return self.max_path
        
        left_depth = self._diameterOfBinaryTreeRecursive(root.left, depth)
        right_depth = self._diameterOfBinaryTreeRecursive(root.right, depth)
        self.max_path = max(self.max_path, left_depth + right_depth)
        return left_depth + right_depth + 1
    
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> list[int]:
        nums1 = []
        self.nodeToList(root1, nums1)
        nums2 = []
        self.nodeToList(root2, nums2)
        return sorted(nums1 + nums2)
    
    def getAllElements2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> list[int]:
        nums1 = []
        root1Gen = self.preorder_traversal(root1)
        root2Gen = self.preorder_traversal(root2)
        r1 = next(root1Gen)
        r2 = next(root2Gen)
        while r1 is not None and r2 is not None:
            if type(r1) is int and type(r2) is int:
                if r1 < r2:
                    nums1.append(r1)
                    try:
                        r1 = next(root1Gen)
                    except:
                        r1 = None
                else:
                    nums1.append(r2)
                    try:
                        r2 = next(root2Gen)
                    except:
                        r2 = None
            elif type(r1) is int:
                nums1.append(r1)
                try:
                    r1 = next(root1Gen)
                except:
                    r1 = None
            else:
                nums1.append(r2)
                try:
                    r2 = next(root2Gen)
                except:
                    r2 = None
            
        return nums1
    
    def nodeToList(self, root: Optional[TreeNode], nums: list[int]):
        if root == None:
            return
        
        nums.append(root.val)
        self.nodeToList(root.left, nums)
        self.nodeToList(root.right, nums)

    def preorder_traversal(self, root):
        if root is not None:
            yield from self.preorder_traversal(root.left) 
            yield root.val  # Yield the root value # Yield from left subtree
            yield from self.preorder_traversal(root.right)  # Yield from right subtree

# tree = TreeNode(3, 
#     TreeNode(9), TreeNode(20, 
#                 TreeNode(15), TreeNode(7)))
# print(Solution().maxDepth(tree))

# diameter_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
# print(Solution().diameterOfBinaryTree(diameter_tree))


# print(Solution().getAllElements2(TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(1, TreeNode(0), TreeNode(3))))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution2:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        fast = head
        slow = head
        while fast and fast.next:
            assert slow.next is not None
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)
        fast = head
        slow = head
        prev_slow: Optional[ListNode] = None
        while fast and fast.next:
            prev_slow = slow
            assert slow.next is not None
            slow = slow.next
            fast = fast.next.next
        
        tree = TreeNode(slow.val)

        # Disconnect here so the head will have a new end
        # that head can iterate through again
        assert prev_slow is not None
        prev_slow.next = None
        tree.left = self.sortedListToBST(head)
        tree.right = self.sortedListToBST(slow.next)
        return tree
    


def printTree(head: Optional[TreeNode]):
    if not head:
        return None
    
    printTree(head.left)
    print(head.val)
    printTree(head.right)
    
mylist = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
output = Solution2().sortedListToBST(mylist)
printTree(output)

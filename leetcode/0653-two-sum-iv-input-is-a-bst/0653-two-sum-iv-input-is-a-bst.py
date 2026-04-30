# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        result = []
    
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        left = 0
        right = len(result) - 1

        while left < right and left < len(result) and right < len(result):
            if result[left] + result[right] == k:
                return True
            elif result[left] + result[right] > k:
                right -= 1
            else:
                left += 1
        else:
            return False
            
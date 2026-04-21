# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(current):
            if not current:
                return [0,0]

            left_size , left_coins = dfs(current.left)
            right_size , right_coins = dfs(current.right)

            size = 1 + left_size + right_size
            coins = current.val + left_coins + right_coins

            self.result += abs(size - coins)

            return [size,coins]

        dfs(root)
        return self.result



            

        
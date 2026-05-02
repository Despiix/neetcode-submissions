# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.isSamee(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSamee(self, r, s):
        if not r and not s:
            return True
        if s and r and s.val == r.val:
            return (self.isSamee(r.left, s.left) and self.isSamee(r.right, s.right))
        
        return False
            
    
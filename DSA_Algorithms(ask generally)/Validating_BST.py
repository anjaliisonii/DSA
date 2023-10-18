# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        if root.left and not self.arrless(root.left,root.val):
            return False
        if root.right and not self.arrgreat(root.right,root.val):
            return False
        if self.isValidBST(root.left)==False:
            return False
        if self.isValidBST(root.right)==False:
            return False
        return True
    def arrless(self,root,val):
        if not root:
            return True
        if root.val>=val:
            return False
        return self.arrless(root.left,val) and self.arrless(root.right,val)
    def arrgreat(self,root,val):
        if not root:
            return True
        if root.val<=val:
            return False
        return self.arrgreat(root.left,val) and self.arrgreat(root.right,val)
        

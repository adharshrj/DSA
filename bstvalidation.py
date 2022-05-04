# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def isValidBST(self, root: Optional[TreeNode]) -> bool: 
            def isValid(root, minval , maxval):
                if root == None:
                    return True

                if root.val <= minval or root.val >= maxval:
                    return False

                if not isValid(root.left, minval , root.val):
                    return False

                if not isValid(root.right, root.val, maxval):
                    return False

                return True
            
            return isValid(root, float('-inf'), float('inf'))

##Recursion
class Solution:
        def isValidBST(self, root: Optional[TreeNode]) -> bool: 
            def isValid(root, minval , maxval):
                if root == None:
                    return True

                if root.val <= minval or root.val >= maxval:
                    return False

                return isValid(root.left, minval , root.val) and isValid(root.right, root.val, maxval)
            
            return isValid(root, float('-inf'), float('inf'))
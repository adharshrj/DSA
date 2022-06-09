def isSymmetric(root):
    def areSymmetric(root1, root2):
        if root1 is None and root2 is None:
            return True
        elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
            return False
        else:
            return areSymmetric(root1.left, root2.right) and areSymmetric(root1.right, root2.left)
    
    if root is None:
        return True
    return areSymmetric(root.left, root.right)

# def isSymmetricinv(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return True
#         def invertTree(self, root):
#             self.invertTree(root.left)
#             self.invertTree(root.right)
#             root.left, root.right = root.right, root.left
#             if ((root.left is None) != (root.right is None)) or root.left.val != root.right.val:
#                 return False
#         return root
#         if root == invertTree(root):
#             return True
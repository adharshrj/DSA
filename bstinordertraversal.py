class Solution:
    def __init__(self):
        self.ino = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.inorderTraversal(root.left)
        self.ino.append(root.val)
        self.inorderTraversal(root.right)
        
        return self.ino
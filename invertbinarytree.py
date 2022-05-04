class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root

#iterative
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        queue = [root]
        
        while queue:
            node = queue.pop()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                node.left, node.right = node.right, node.left
         
        return root
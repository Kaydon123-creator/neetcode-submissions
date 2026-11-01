# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            if not node:
                return "N$"
            return str(node.val)+"$"+dfs(node.left)+dfs(node.right)
        return dfs(root)
            

    # 1 2 N N 3 4 N N 5 N N 


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split("$")
        print(data)
        i = -1
        def buildTree():
            nonlocal i 
            i+=1
            if data[i] == "N":
                return None 
            root = TreeNode(data[i])
            root.left = buildTree()
            root.right = buildTree()
   
            return root
        return buildTree()


            

























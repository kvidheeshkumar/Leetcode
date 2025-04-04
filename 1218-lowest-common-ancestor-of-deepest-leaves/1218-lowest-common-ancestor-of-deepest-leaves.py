# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Helper function to perform depth first search on the tree
        def dfs(node):
            #Base case: If current node is None, depth is 0
            if node is None:
                return None,0
            #Recursively find the lowest common ancestor and depth of the left subtree
            left_lca, left_depth=dfs(node.left)
            #Recursively find the lowest common ancestor and depth of the right subtree
            right_lca, right_depth=dfs(node.right)

            #If left subtree is deeper, return the left_lca and its depth increased by 1
            if left_depth>right_depth:
                return left_lca,left_depth+1

            #If right subtree is deeper, return the right_lca and its depth increased by 1
            if right_depth>left_depth:
                return right_lca,right_depth+1
            
            #If both the subtrees have same depth, then it is the lowest common ancestor
            #return the current node and depth+1

            if left_depth==right_depth:
                return node,left_depth+1
        
        #Call the DFS helper function and return the lowest common ancestor. The second value of the tuple is ignored.
        return dfs(root)[0]
            


        
        
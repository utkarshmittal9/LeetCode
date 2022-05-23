# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def get_int_fromBinary(binary):
            binary1 = binary
            decimal, i, n = 0, 0, 0
            while(binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1
            return decimal   
                
        def inorder(root, prev):
            print("prev initial:",prev)
            if not root:return
            if not root.left and not root.right:
                prev = prev + str(root.val)
                self.sum = self.sum + get_int_fromBinary(int(prev))
                return
            inorder(root.left, prev+str(root.val))
            print("from middle", prev, root.val)
            inorder(root.right, prev+str(root.val))
        inorder(root,"")
        return self.sum
                
        
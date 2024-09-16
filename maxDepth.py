class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def maxDepth(self,root:TreeNode)->int:
        if not root:
            return 0
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        return max(l,r)+1
    
def listToTree(arr):
    if not arr:
        return False
    nodes=[None if val=='null' else TreeNode(val) for val in arr]

    for i in range(len(arr)):
        if nodes[i]:
            left_index=2*i+1
            right_index=2*i+2
            if left_index<len(arr):
                nodes[i].left=nodes[left_index]
            if right_index<len(arr):
                nodes[i].right=nodes[right_index]

    return nodes[0]
output=Solution()

root_list=[3,9,20,'null','null',15,7]
root=listToTree(root_list)
print(output.maxDepth(root))
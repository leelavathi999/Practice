class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def sameTree(self,p:TreeNode,q:TreeNode)->bool:
        if not p and not q :
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right))
    

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
pList=[1,2,3]
qlist=[1,2,3]
p=listToTree(pList)
q=listToTree(qlist)

print(output.sameTree(p,q))
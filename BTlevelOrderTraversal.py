from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def levelOrderTraversal(self,root:TreeNode)->list[list[int]]:
        res=[]
        q=deque()
        q.append(root)
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)
        return res
    

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
arr=[3,9,20,'null','null',15,7]
root=listToTree(arr)

output=Solution().levelOrderTraversal(root)
print(output)
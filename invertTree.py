
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) ->TreeNode:
        if not root:
            return None
        temp=root.left
        root.left=root.right
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    

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
def print_tree(root):
    if not root:
        return "None"
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append('null')
    # Remove trailing 'null' values
    while result and result[-1] == 'null':
        result.pop()
    return result
output=Solution()
arr=[4,2,7,1,3,6,9]
root=listToTree(arr)
invertTree=output.invertTree(root)
print(print_tree(invertTree))
Binary Tree:--

maximum Depth of Binary Tree :
      using DFS approach

same Tree or not :
      two trees are said to be same if they both are structurally identical and the nodes have same value

Invert Tree:
      when at root swapping the left and right nodes

Binary Tree Level Order Traversal:
      using queue to pop the element which entered first at each level and appending to the level and after each level append that level elements to the result

Remove Duplicates from Sorted list II:
      skipping the duplicates and updating the prev and head node accordingly
      
Heap:--

Kth Largest Element in Array:
      forming min heap with length less tha k given and the pop small element and push current element then after return min_heap[0] which is the smalles element that we are finding for kth largest

BackTracking:--

Permutations:
      pop the element call recursively permute func to get permutations for remaining elements and add that popped element to that permutations and add popped element to original list nums like this calll recursively for each element and extend the result list with obtained permutations

Stack:--

Valid Paranthesis:
      uses a stack to track opening brackets, ensuring each closing bracket matches the most recent opening one

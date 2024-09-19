import heapq
class Solution:
    def findkthLargest(self,nums:list[int],k:int)->int:
        minheap=[]
        for num in nums:
            if len(minheap)<k:
                heapq.heappush(minheap,num)
            else:
                heapq.heappushpop(minheap,num)
        return minheap[0]
    

arr=[3,2,3,1,2,4,5,5,6]
output=Solution().findkthLargest(arr,k=4)
print(output)

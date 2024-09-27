
# removes duplicates from sorted array then return new array and it's length
# using pointers to keep track of index of unique element
# time complexity : O(n)  and Space Complexity : O(1)

class Solution:
    def removeDuplicates(self,nums:list[int]):
        l=1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l +=1
        return "array :" , nums[:l] , "length :" , l
    
res=Solution()
array=[0,0,1,1,1,2,2,3,3,4]
print(res.removeDuplicates(array))
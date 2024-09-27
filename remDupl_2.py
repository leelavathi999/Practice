# remove duplicates from sorted array 
# element appears atmost twice
# now we need to remove the element which appears more then twice
# used two pointer approach
# time complexity : O(n)  and Space Complexity : O(1)
class Solution:
    def remDupli(self,nums:list[int]):
        ptr,cnt=0,1
        for i in range(1,len(nums)):
            if nums[i] == nums[ptr] and cnt < 2:
                ptr += 1
                cnt += 1
                nums[ptr],nums[i] = nums[i],nums[ptr]
            elif nums[i] != nums[ptr]:
                ptr += 1
                cnt = 1
                nums[ptr],nums[i] = nums[i],nums[ptr]
        return "array :" , nums[:ptr] , "length :" , ptr+1
    
res=Solution()
array=[0,0,1,1,1,2,3,3]
print(res.remDupli(array))
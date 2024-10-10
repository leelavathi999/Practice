# Contains Duplicate
#  Given an integer array nums, return true if any value appears at
#  least twice in the array, and return false if every element is
#  distinct.
#  Input: nums = [1,2,3,1]
#  Output: true


class Solution:
    # approach 1:Brute force 
    def contDupl(self,nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    # approach 2:Hashmap
    def cont_dupl(self,nums):
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    # approach 3:sorting
    def contDupli(self,nums):
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
output=Solution()
nums=[1,2,3,1]
res1=output.contDupl(nums)
res2=output.cont_dupl(nums)
res3=output.contDupli(nums)
print(res1,res2,res3)
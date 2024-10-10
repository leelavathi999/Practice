#  Given an array of integer nums and an integer target, return
#  indices of the two numbers such that they add up to the target.

#  Input: nums = [2,7,11,15], target = 9
#  Output: [0,1]
#  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

class Solution:
    # approach 1:Brute force method 
    # Time comp:O(n^2) Space comp:O(1)
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return
                
    # approach 2:Hashmap
    # Time comp:O(n) Space comp:O(n)
    def two_sum(self,nums,target):
        premap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in premap:
                return [premap[diff],i]
            premap[n]=i
        return

output=Solution()
nums=[2,7,11,15]
target=9
result1=output.twoSum(nums,target)
result2=output.two_sum(nums,target)
print(result1)
print(result2)
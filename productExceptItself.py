# Product of Array Except Self
#  Given an integer array nums, return an array res such that
#  res[i] is equal to the product of all the elements of nums
#  except nums[I].
#  Input: nums = [1,2,3,4]
#  Output: [24,12,8,6]

class Solution:
    # brute force method
    def prod(self,nums):
        n=len(nums)
        left=[1]*n
        right=[1]*n
        res=[0]*n
         # Calculate left array
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        # Calculate right array
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        # Calculate the res by multiplying left and right
        for i in range(n):
            res[i] = left[i] * right[i]

        return res
    def prodExcept(self,nums):
        res=[1]*len(nums)
        # prefix calculation
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix *= nums[i]
        # postfix calculation
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
    
output=Solution()
nums=[1,2,3,4]
result1=output.prod(nums)
result2=output.prodExcept(nums)

print(result1,result2)
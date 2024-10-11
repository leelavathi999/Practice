# Maximum Subarray
#  Given an integer array nums, find the subarray with the largest
#  sum, and return its sum.
#  Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#  Output: 6
#  Explanation: The subarray [4,-1,2,1] has the largest sum 6.


class Solution:
    # brute force approach
    def maxSubArray(self,nums):
        maxsum=float('-inf')
        n=len(nums)
        for i in range(n):
            csum=0
            for j in range(i,n):
                csum += nums[j]
                maxsum=max(maxsum,csum)
        return maxsum
    # kadane's Algorithm
    def maxSubarray(self,nums):
        msum=csum=nums[0]
        for i in range(1,len(nums)):
            csum=max(nums[i],csum+nums[i])
            msum=max(msum,csum)
        return msum
    
output=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
res1=output.maxSubArray(nums)
res2=output.maxSubarray(nums)
print(res1)
print(res2)
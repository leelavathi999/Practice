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
    
# code to return that subarray along with maxsum
def max_subArray(nums):
    maxsum = cursum = nums[0]
    start = end = s = 0  # Initialize indices for the subarray
    
    for i in range(1, len(nums)):
        # If cursum is negative, start a new subarray
        if cursum < 0:
            cursum = nums[i]
            s = i  # Update the start index of the new subarray
        else:
            cursum += nums[i]
        
        # Update maxsum and the start/end indices if a new max is found
        if cursum > maxsum:
            maxsum = cursum
            start = s  # Update the start index
            end = i    # Update the end index
    
    # Return the maximum sum and the corresponding subarray
    return maxsum, nums[start:end + 1]
output=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
res1=output.maxSubArray(nums)
res2=output.maxSubarray(nums)
res3=max_subArray(nums)
print(res3)
print(res1)
print(res2)
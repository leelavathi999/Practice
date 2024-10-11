# Maximum Product Subarray
#  Given an integer array nums, find a subarray that has the largest
#  product, and return the product.
#  Input: nums = [2,3,-2,4]
#  Output: 6
#  Explanation: [2,3] has the largest product 6.

# Brute force Approach
def approach_1(nums):
    maxprod=float('-inf')
    for i in range(len(nums)):
        prod=1
        for j in range(i,len(nums)):
            prod *= nums[j]
            maxprod = max(maxprod,prod)
    return maxprod

# Kadane's Approach
def approach_2(nums):
    res=max(nums)
    cmax,cmin=1,1
    for n in nums:
        if n==0:
            cmax,cmin=1,1
            continue
        tmp=cmax*n
        cmax=max(n*cmax,n*cmin,n)
        cmin=min(n*cmax,n*cmin,n)
        res=max(res,cmax,cmin)
    return res
nums=[2,3,-2,4]
res1=approach_1(nums)
print(res1)
res2=approach_2(nums)
print(res2)
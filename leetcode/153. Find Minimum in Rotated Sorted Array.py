# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution:
    def findMin(self, nums) -> int:
        if len(nums) < 3:
            return min(nums)
        if(nums[0] < nums[-1]):
            return nums[0]
        mid = (len(nums)-1) >> 1
        if nums[0] < nums[mid]:
            return self.findMin(nums[mid+1:])
        else:
            return self.findMin(nums[:mid+1])
    def findMin1(self,nums)->int:
        if len(nums)==0:
            return -1
        res = nums[0]
        for n in nums:
            res = min(n,res)
        return res
    def findmin2(self,nums)->int:
        return min(nums)
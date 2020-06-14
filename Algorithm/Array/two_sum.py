# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num],i]
            else:
                dic[num] = i







# class Solution(object):
#     def two_sum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if len(nums)==0:
#             return None
#         l, r = 0, len(nums)-1
#         while l <= r:
#             mid = (l+r)//2
#             if nums[l]+nums[r] == target:
#                 return [l,r]
#             elif nums[l]+nums[r] > target:
#                 r = mid-1
#             elif nums[l]+nums[r] < target:
#                 l = mid+1

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.
# Example 2:
#
# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
#
# It doesn't matter what values are set beyond the returned length.


class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_element = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[unique_element] = nums[i+1]
                unique_element += 1
        return unique_element


# this is not the ideal solution based on the description of the question
class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {value: index for index, value in enumerate(nums)}
        nums[:] = sorted(dic.keys())
        return len(dic.keys())
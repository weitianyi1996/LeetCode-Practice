# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0


class Solution1(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            for i in range(len(nums)-1):
                if nums[i] < target < nums[i+1]:
                    return i+1
            return len(nums)


# using python builtin index
class Solution2(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            nums.append(target)
            nums = sorted(nums)
        return nums.index(target)


class Solution3(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return len([i for i in nums if i<target ])


# binary search
class Solution4(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
        return l

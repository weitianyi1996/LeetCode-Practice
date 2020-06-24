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


# Hash Table
# link: http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/
# hash('10')
class Solution1(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, value in enumerate(nums):
            if target-value in dic:
                return [dic[target-value], index]
            else:
                dic[value] = index


# Two Pointer
# [3,2,4]
# [3,3]
# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
# sorted(student_tuples, key=lambda student: student[2])
class Solution2(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = enumerate(nums)
        sort_nums = sorted(nums, key= lambda x: x[1])
        l ,r = 0, len(sort_nums)-1
        while l<r:
            if sort_nums[l][1]+sort_nums[r][1] == target:
                return sort_nums[l][0],sort_nums[r][0]
            elif sort_nums[l][1]+sort_nums[r][1] > target:
                r -= 1
            elif sort_nums[l][1]+sort_nums[r][1] < target:
                l += 1







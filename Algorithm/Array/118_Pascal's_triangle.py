# 118. Pascal's Triangle
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],  d[2]
#   [1,3,3,1], d[3]
#  [1,4,6,4,1]
# ]


class Solution():
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        d = []
        last_time_list = [1, 1]

        for i in range(0, numRows):
            l = [1 for value in range(i+1)]
            if i >= 2:
                for x in range(1, len(l)-1):
                    l[x] = last_time_list[x-1]+last_time_list[x]
                last_time_list = l
            d.append(l)
        return d


s1 = Solution()
print(s1.generate(5))

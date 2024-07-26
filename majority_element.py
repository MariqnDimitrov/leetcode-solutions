from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        counted_dict = sorted(Counter(nums).items(), key=lambda x: -x[1])
        return counted_dict[0][0]





solution = Solution()
print(solution.majorityElement([3,2,3]))
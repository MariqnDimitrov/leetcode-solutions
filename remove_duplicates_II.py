class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums):
            count = nums.count(nums[i])
            if count > 2:
                nums.remove(nums[i])
            else:
                i += 1
        return nums

solution = Solution()
print(solution.removeDuplicates([1,1,1,2,2,3]))

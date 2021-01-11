class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        maxConsec = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0 or i == len(nums) - 1:
                if count > maxConsec:
                    maxConsec = count
                count = 0
        return maxConsec


solution = Solution()
print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))

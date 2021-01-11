class Solution:
    def findNumbers(self, nums) -> int:
        for num in nums:
            print(len(str(num)))


solution = Solution()
print(solution.findNumbers([12, 345, 2, 6, 7896]))

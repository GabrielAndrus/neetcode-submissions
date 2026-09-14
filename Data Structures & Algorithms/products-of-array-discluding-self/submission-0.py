class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        left = 1
        right = 1

        # Compute the left product 
        # Time complexity: O(n)
        for i in range(0, len(nums)):
            result[i] = left
            left *= nums[i]

        # Compute the right product
        # Time complexity: O(n)
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
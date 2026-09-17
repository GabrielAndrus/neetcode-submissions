class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length_hash = {}
        longest_length_so_far = 0
        for num in list(set(nums)):
            # Already existing sequence
            if num - 1 in num_set:
                pass
            # A new sequence
            else:
                new_length = 1
                current = num
                while current + 1 in num_set:
                        current += 1
                        new_length += 1
                if new_length > longest_length_so_far:
                    longest_length_so_far = new_length
                        
        return longest_length_so_far


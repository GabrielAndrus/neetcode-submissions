class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for element in nums:
            if element in hash_table:
                return True
            else:
                hash_table[element] = 1
        return False

        
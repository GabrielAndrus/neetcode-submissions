class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        as_int = int("".join(map(str, digits)))
        result_int = as_int + 1
        result = []
        for c in str(result_int):
            result.append(int(c))
        return result
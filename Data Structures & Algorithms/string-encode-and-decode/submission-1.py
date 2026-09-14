class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for str in strs:
            padded_len = f"{len(str):04d}"
            loop_str = f"{padded_len}{str}"
            final_str += loop_str
        return final_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i <= len(s):
            if i + 4 > len(s):
                break
            w_len = int(s[i:i+4])
            result.append(s[i+4:i+4+w_len])
            i += 4 + w_len
        return result

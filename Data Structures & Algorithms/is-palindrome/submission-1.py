class Solution:
    def isPalindrome(self, s: str) -> bool:
       return str.lower(re.sub(r'[^a-zA-Z0-9]', '', s)) == ''.join(reversed(str.lower(re.sub(r'[^a-zA-Z0-9]', '', s))))
    
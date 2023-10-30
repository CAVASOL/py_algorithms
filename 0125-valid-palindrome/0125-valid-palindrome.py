class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [t.lower() for t in s if t.isalnum()]

        return all (s[i] == s[~i] for i in range(len(s)//2))


            
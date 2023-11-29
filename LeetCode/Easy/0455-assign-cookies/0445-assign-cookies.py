class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        kid = cookie = 0
        kids = 0

        while kid < len(g) and cookie < len(s):
            if g[kid] <= s[cookie]:
                kids += 1
                kid += 1
            cookie += 1

        return kids
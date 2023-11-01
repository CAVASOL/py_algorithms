class Solution:
    def isValid(self, s: str) -> bool:
        cnt = []
      # brackets = {'(': ')', '[': ']', '{': '}'}
        brackets = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in brackets:
                prev = cnt.pop() if cnt else "#"
                if brackets[char] != prev:
                    return False
            else:
                cnt.append(char)
        
        return not cnt
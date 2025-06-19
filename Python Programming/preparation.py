class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        
        i = 0
        while i < len(s):
            c = s[i]
            if c in pairs:
                if len(stack) == 0:
                    return False
                top = stack[len(stack) - 1]
                if pairs[c] != top:
                    return False
                stack = stack[:len(stack) - 1]
            else:
                stack = stack + [c]
            i += 1
        
        return len(stack) == 0
    
#Example Usage
s = "()[]{}"
obj = Solution()
print(obj.isValid(s))

#Example Usage 2
s = "(]"
obj = Solution()
print(obj.isValid(s))
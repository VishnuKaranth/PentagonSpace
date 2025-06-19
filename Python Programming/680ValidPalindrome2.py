class Solution:
    def isPalindrome(self, s, i, j):
        i , j = 0, len(s) - 1
        #Remove at most one
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True
    
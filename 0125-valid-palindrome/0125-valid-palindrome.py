class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        y =  "".join([x for x in s if x.isalnum()])
        if y[::-1] ==  y:
            return True 
        else:
            return False 
        
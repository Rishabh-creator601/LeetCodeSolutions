class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        for x in s:
            if not  x.isalnum() :
                s =  s.replace(x,"")
        if s[::-1] ==  s:
            return True 
        else:
            return False  
        
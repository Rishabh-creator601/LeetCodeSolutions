class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_ =  str(x)
        value =  True if x_[::-1] ==  x_ else False 
        return value 
        
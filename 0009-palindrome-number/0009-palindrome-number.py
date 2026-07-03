class Solution:
    def isPalindrome(self, x):

        value =  True if str(x)[::-1] ==  str(x) else False 
        return value 
        
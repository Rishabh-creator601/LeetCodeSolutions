class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> str:

        a =  "".join((list(map(str,nums)))).split("0")
        return len(max(a))

        
        

        
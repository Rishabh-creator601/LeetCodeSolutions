class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        values = []
        a =  nums[:n]
        b =  nums[n:]
        
        for (i,j)  in zip(a,b):
            values.append(i)
            values.append(j)
        
        return values 
        
        
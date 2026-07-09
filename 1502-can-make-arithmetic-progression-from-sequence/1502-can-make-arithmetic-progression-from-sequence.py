class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        

        arr =  sorted(arr)
        flag=  True  
        d =  abs(arr[1] - arr[0])

        for i in range(0,len(arr)-1):
            if abs(arr[i+1] - arr[i]) != d :
                flag = False 

        return flag 
            
        
        
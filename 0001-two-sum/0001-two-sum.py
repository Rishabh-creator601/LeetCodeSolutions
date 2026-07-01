from itertools import combinations 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        indexes =  []
        key_value = {}

        for index in range(len(nums)):
            key_value[index] =  nums[index]
        

        all_possibles = combinations(key_value.keys(),2)
        for a,b in all_possibles:
            if nums[a]+nums[b] ==  target:
                indexes.extend([a,b])
                break 
        return indexes 



                

        
        
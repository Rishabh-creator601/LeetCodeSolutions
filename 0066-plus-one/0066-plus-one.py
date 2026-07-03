class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        digits_ = list(map(lambda x : str(x) , digits ))
        value =  list(str(int("".join(digits_)) +  1))
        value = list(map(lambda x : int(x) , value ))
        return value 


        
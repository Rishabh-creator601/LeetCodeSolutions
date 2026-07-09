class Solution:

    def smaller(self,x,arr):
        count =  0 
        for   v in arr :
            if v < x :
             count  +=1
        return count  

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:


        small_count = []

        for x in nums :

            small_count.append(self.smaller(x,nums))

        return small_count 
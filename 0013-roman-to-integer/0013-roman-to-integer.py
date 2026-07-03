class Solution:


    def add_replace(self,el,count):
        
        if el in self.s:
            self.s =  self.s.replace(el,"")
            self.sum += count 

    def romanToInt(self, s: str) -> int:

        self.s =  s

        values = {
            "I":1, 
            "V" : 5, 
            "X":10,
            "L":50 ,
            "C":100,
            "D":500,
            "M":1000
        }

        self.sum = 0
       
        self.add_replace("IV",4)
        self.add_replace("IX",9)
        self.add_replace("XL",40)
        self.add_replace("XC",90)
        self.add_replace("CD",400)
        self.add_replace("CM",900)

        s_ = list(self.s)

        for i in s_:
            self.sum += values[i]
        return self.sum 


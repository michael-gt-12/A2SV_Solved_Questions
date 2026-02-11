class Solution:
    def intToRoman(self, num: int) -> str:
        # mapping of all the possible symbol and their vaue
        symbol_list = [["I",1] , ["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]

        # varianle to store the result
        result = ""

        # finding the result logic
        for symbol,value in reversed(symbol_list):
            if num // value:
                count = num // value
                result += symbol * count
                num = num % value
        return result

                
        
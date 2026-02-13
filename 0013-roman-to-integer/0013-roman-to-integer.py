class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        number = 0
        i = 0
        while i < n:
            if i < n-1:
                if s[i] == "I":
                    if s[i+1] == "V":
                        number = number + 4
                        i = i+1
                    elif s[i+1] == "X":
                        number = number + 9
                        i = i+1
                    else:
                        number = number + 1
                elif s[i] == "V":
                    number = number + 5
                elif s[i] == "X":
                    if s[i+1] == "L":
                        number = number + 40
                        i = i+1
                    elif s[i+1] == "C":
                        number = number + 90
                        i = i+1
                    else:
                        number = number + 10
                elif s[i] == "L":
                    number = number + 50
                elif s[i] == "C":
                    if s[i+1] == "D":
                        number = number + 400
                        i = i+1
                    elif s[i+1] == "M":
                        number = number + 900
                        i = i+1
                    else:
                        number = number + 100
                elif s[i] == "D":
                    number = number + 500
                elif s[i] == "M":
                    number = number + 1000
            elif i == n-1:
                if s[i] == "I":
                    number = number + 1
                elif s[i] == "V":
                    number = number + 5
                elif s[i] == "X":
                    number = number + 10
                elif s[i] == "L":
                    number = number + 50
                elif s[i] == "C":
                    number = number + 100
                elif s[i] == "D":
                    number = number + 500
                elif s[i] == "M":
                    number = number + 1000
            i = i+1
        return number
                
       


            
            

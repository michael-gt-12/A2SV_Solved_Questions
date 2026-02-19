class Solution:
    def smallestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        if len(s) % 2 == 0:
            string = s[0:len(s)//2]
            string = "".join(sorted(string))
            return string+string[::-1]

        else:
            string = s[0:len(s)//2]
            center = s[len(s)//2]
            string = "".join(sorted(string))
            return string+center+string[::-1]


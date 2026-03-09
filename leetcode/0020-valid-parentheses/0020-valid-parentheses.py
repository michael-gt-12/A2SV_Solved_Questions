class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        pre = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        stack = []
        top = -1
        
        for char in s:
            if char in pre.keys():
                stack.append(char)
                top += 1
            else:
                if top == -1:
                    return False
                else:
                    if pre[stack[top]] == char:
                        stack.pop()
                        top -= 1
                    else:
                        return False

        if len(stack) == 0:
            return True
        else:
            return False


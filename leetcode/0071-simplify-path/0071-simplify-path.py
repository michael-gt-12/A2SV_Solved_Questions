class Solution:
    def simplifyPath(self, path: str) -> str:

        path_list = path.split("/")

        # for i in range(path_list.count("")):
        #     path_list.remove("")

        stack = ["/"]

        for i in path_list:
            if i == "." or i == "":
                continue

            elif i == "..":
                if len(stack) > 1:
                    stack.pop()
                    stack.pop()

            else:
                stack.append(i)
                stack.append("/")

        if stack[-1] =="/" and len(stack) > 1:
            stack.pop()

        return "".join(stack)
            




        
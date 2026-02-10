class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False
        buffer = ""

        for line in source:
            i = 0
            if not in_block:
                buffer = ""
            while i < len(line):
                if in_block:
                    if i + 1 < len(line) and line[i] == "*" and line[i+1] == "/":
                        in_block = False
                        i += 2
                    else:
                        i += 1
                else:
                    if i + 1 < len(line) and line[i] == "/" and line[i+1] == "/":
                        break
                    elif i + 1 < len(line) and line[i] == "/" and line[i+1] == "*":
                        in_block = True
                        i += 2
                    else:
                        buffer += line[i]
                        i += 1
            if buffer and not in_block:
                result.append(buffer)
        return result

        
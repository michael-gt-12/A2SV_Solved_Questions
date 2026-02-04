def swap_case(s):
    s_new = ""
    for i in s:
        if i.isupper():
            s_new += i.lower()
        else:
            s_new += i.upper()
    return s_new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

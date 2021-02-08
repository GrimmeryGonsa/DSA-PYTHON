def Replacer(s):
    if len(s) == 1 or len(s) == 0:
        return s
    if s[0] == 'p' and s[1] == 'i':
        smallOp = Replacer(s[2:])
        return "3.14" + smallOp
    else:
        smallOp = Replacer(s[1:])
        return s[0] + smallOp


print(Replacer("adlpiadl"))

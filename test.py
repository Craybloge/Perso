phrase = input("choisissez une phrase:").lower()
n = int(input("choisissez un nombre:"))%26
code = ""
for i in range(len(phrase)):
    if phrase[i] != " ":
        if ord(phrase[i])+n > 122:
            code += chr(ord(phrase[i])+n-26)
        else:
            code += chr(ord(phrase[i])+n)
    else:
        code += " "
print(code)

u = i = d = s = sp = 0

str_input = input("Enter string: ")
for x in str_input:
    if x.isupper():
        u += 1
    elif x.islower():
        i += 1
    elif x.isdigit():
        d += 1
    elif x.isspace():
        s += 1
    else:
        sp += 1

print("Total upper letters:", u)
print("Total lower letters:", i)
print("Total special characters:", sp)
print("Total spaces:", s)
print("Total digits:", d)

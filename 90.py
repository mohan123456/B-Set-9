a=input()
b=[]
for i in a:
    if i.isdigit():
        b.append(i)

print("".join(b))

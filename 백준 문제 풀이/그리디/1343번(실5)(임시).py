a  = "XX.XXXXXXXXXX..XXXXXXXX...XXXXXX"

b = a.split('.')
print("b :", b) ###
new_b = []

c = len(b)
print("c :", c) ###

for i in range(c):
    if b[i] != '':
        d = len(b[i])
        print("d :", d) ###
        if d % 4 == 0:
            b[i] = "A" * d
            
        elif d % 2 == 0:
            b[i] = "A" * (d - 2) + "BB"
        else:
            break

print(b)


for i in range(c):
    if b[i][0] == "X":
        print(-1)
        break
    else:
        b[i].replace("", ".")
        ret = "".join(b)
        print(ret)

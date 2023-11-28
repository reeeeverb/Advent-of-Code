sum = 0
f = open("input.txt","r")
lines = f.readlines()

for l in lines:
    size = len(l)//2
    first = l[:size]
    last = l[size:]
    for c in first:
        if c in last:
            if c.islower():
                sum += ord(c)-96
            else:
                sum += ord(c)-64+26
            break
print(sum)

sum = 0
f = open("input.txt","r")
lines = f.readlines()
i = 0

while i+2 < len(lines):
    f = lines[i]
    s = lines[i+1]
    t = lines[i+2]
    for c in f:
        if c in s:
            if c in t:
                if c.islower():
                   sum += ord(c)-96
                else:
                    sum += ord(c)-64+26
                break
    i+=3
print(sum)

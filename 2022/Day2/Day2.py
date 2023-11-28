f = open("input.txt","r")
lines = f.readlines()
sum = 0

for l in lines:
    opp = ord(l[0]) - 64
    mine = l[2]
    if mine == "X":
        if opp == 1:
            sum += 3
        else:
            sum += opp-1
    elif mine == "Y":
        sum += opp + 3
    else:
        sum += (opp%3)+1 + 6
print(sum)

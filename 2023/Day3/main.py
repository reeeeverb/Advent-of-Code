f = open("input.txt","r")
lines = f.readlines()

skip = ['.','1','2','3','4','5','6','7','8','9','0']

index = -1
line_index = -1
for l in lines:
    line_index+=1
    l = l.strip()
    size = len(l)
    for c in l:
        index += 1
        if c not in skip:
            print(l[index%size])
            front = 0
            if line_index > 0 and lines[line_index-1][index%size].isdigit():
                front = index%size
                back = index%size
                c = 1
                while index%size-c > -1 and lines[line_index-1][(index%size)-c].isdigit():
                    print("---" , lines[line_index-1][index%size - c])
                    front -= 1
                    c-=1
                c = 1
                while index%size+c < size and lines[line_index-1][(index%size)+c].isdigit():
                    print("---" , lines[line_index-1][index%size + c])
                    back += 1
                    c+=1
                print(lines[line_index-1][front:back+1])

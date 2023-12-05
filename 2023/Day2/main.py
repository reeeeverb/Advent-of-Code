f = open("input.txt","r")
lines = f.readlines()
colors = {"red":0,"green":0,"blue":0}
sum = 0
for l in lines:
    colors = {"red":0,"green":0,"blue":0}
    delimiters = [",", "|", ";"]
    for delimiter in delimiters:
        l = " ".join(l.split(delimiter))
    my_list = l.split()
    my_list = list(map(str.strip, my_list))

    for index in range(len(my_list)):
        if my_list[index] in colors and colors[my_list[index]] < int(my_list[index-1]):
            colors[my_list[index]] = int(my_list[index-1])
    
    sum += (colors["red"] * colors["green"] * colors["blue"])

print(sum)

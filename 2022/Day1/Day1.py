f = open("input.txt","r")
lines = f.readlines()
max_sum = [0,0,0]
current_sum = 0

for l in lines:
  if l!="\n":
    current_sum += int(l)
  else:
    if current_sum > max_sum[2]:
      if current_sum > max_sum[1]:
        if current_sum > max_sum[0]:
          max_sum[2] = max_sum[1]
          max_sum[1] = max_sum[0]
          max_sum[0] = current_sum;
        else:
          max_sum[2] = max_sum[1]
          max_sum[1] = current_sum
      else:
        max_sum[2] = current_sum
    current_sum = 0
print(sum(max_sum))

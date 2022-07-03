n = 1000000
l1 = []

for i in range(1, n+1):
  l2 = []
  while True:
    l2.append(i)
    if i == 1:
      break
    if i%2 == 0:
      i = i/2
    else:
      i = (3*i)+1
    
  if len(l2) > len(l1):
    l1 = l2

print(l1[0])

# ans 837799

l = []
for i in range(99, 1000):
  for j in range(99, 1000):
    if str(i*j) == str(i*j)[::-1]:
      l.append(i*j)
  
print(max(l))

#ans 906609

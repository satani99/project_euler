def divisible(n, lst):
  return all(map(lambda y: n%y == 0, lst))

a = 1
while True:
  if divisible(a, [20,19,18,17,16,15,14,13,12,11]):
    print(a)
    break
  a += 1
  

#  ans 232792560

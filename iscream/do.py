def iScream(f, s):
  x=f+s-1
  m=1
  d=1
  for i in range(1,s+1):
    m=m*x
    x=x-1
    d=d*i
  return m/d

print iScream(5,3)
print iScream(3,3)
print iScream(5,0)

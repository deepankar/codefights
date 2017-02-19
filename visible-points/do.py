import math
import bisect

def visiblePoints(points):
  angles=[]
  for p in points:
    if p[0] != 0:
 #     print "div " + str(p[1]) + "/"+ str(p[0]) + "=" + str(p[1]*1.0/p[0])
      ang = math.atan(p[1]*1.0/p[0])
      if p[0] < 0:
        ang += math.pi
      elif p[1] < 0:
        ang += 2*math.pi
      angles.append(ang)
    elif p[1] > 0:
      angles.append(math.pi/4)
    else:
      angles.append(3*math.pi/4)
  angles.sort()
  nump=len(angles)
  i=0
  d=math.pi/4 + 0.0000001
  j=bisect.bisect_right(angles, d+angles[0])
  if (j == len(angles)):
    return j
  for ex in xrange(1+j):
    angles.append(angles[ex] + 2*math.pi)
#  print angles
#  print j
  maxp = j-i
  for i in xrange(1,nump):
    while angles[j] - angles[i] <= d:
      j+=1
#    print "i=" + str(i) + "("+ str(angles[i]) + ") j="+ str(j) + "("+ str(angles[j]) + ")"
    if j - i > maxp:
      maxp = j-i

  return maxp

#points = [[1, 1], [3, 1], [3, 2], [3, 3], [1, 3], [2, 5], [1, 5], [-1], [-1, -2], [-2, -3], [-4, -4]]
points = [[1, 1], [3, 1], [3000000, 2000000], [3, 3], [1, 3], [2, 5], [1, 5], [-10000000, -10000000], [-1, -2], [-2, -3], [-4, -4]]
print visiblePoints(points)


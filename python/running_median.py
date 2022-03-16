import os
import heapq

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  a_count = int(input().strip())

  result = []
  minq = [] # max-heap
  maxq = [] # min-heap
  
  for _ in range(a_count):
    a_item = int(input().strip())
    
    if len(minq) == 0 or a_item < -minq[0]:
      heapq.heappush(minq, -a_item)
    else:
      heapq.heappush(maxq, a_item)
      
    big, bigsign = (maxq, 1) if len(maxq) > len(minq) else (minq, -1)
    sml, smlsign = (minq, -1) if len(maxq) > len(minq) else (maxq, 1)
    
    if len(big) - len(sml) >= 2:
      frombig = heapq.heappop(big)*bigsign
      heapq.heappush(sml, frombig*smlsign)
    
    median = big[0] * bigsign
    
    if len(big) == len(sml):
      frombig = big[0] * bigsign
      fromsml = sml[0] * smlsign
      median = (frombig+fromsml)/2
      
    result.append("{:.1f}".format(median))
    
  fptr.write('\n'.join(map(str, result)))
  fptr.write('\n')

  fptr.close()

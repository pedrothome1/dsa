# a and b are already sorted
def merge(a, b):
  c = []
  m = 0
  n = 0

  while m < len(a) and n < len(b):
    if a[m] < b[n]:
      c.append(a[m])
      m += 1
    else:
      c.append(b[n])
      n += 1

  while m < len(a):
    c.append(a[m])
    m += 1

  while n < len(b):
    c.append(b[n])
    n += 1

  return c

# [7,2,4,8,5,2,1,0]
def merge_sort(a):
  if len(a) <= 1:
    return a

  mid = int((len(a)-1)/2)
  left = merge_sort(a[:mid+1])
  right = merge_sort(a[mid+1:])

  return merge(left, right)

if __name__ == "__main__":
  # a = [2,4,6]
  # b = [1,7,11,12]
  # print(merge(a,b))
  # print(merge([7], [2]))
  print(merge_sort([7,2,4,8,5,2,1,0]))

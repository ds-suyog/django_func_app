


def fact(n):
  if (not isinstance(n,int)) or (n < 0):
    return("wrong input given!!")
  f = 1
  n1 = n
  if n == 0: return 1
  while n >= 1:
  	f = n * fact(n-1) 
  	return f

def fibo(n):
  st, nx, temp = 0, 1, 0
  result = []
  result.append(st)
  result.append(nx)

  for i in range(0,n-2):
    temp = nx
    nx = st + nx
    st = temp
    result.append(nx)
  return str(result)

def isarmstrong(n):
  'armstrong- sum of cubes of digits = number'
  if isinstance(n, int) == False or n < 0:
    return("invalid input!")
  n1=n
  r=0
  sum=0
  while n>0:
    r=(n%10)
    sum=sum+(r**3)  
    n=n//10 
  if n1 == sum:
    return "%d is armstrong" % (n1)  
  else:
    return "%d is not armstrong"% (n1) 

def ispalin(input):
  length = len(input)
  ctr = length//2
  left = 0
  right = length - 1
  flag = 1

  for i in range(1,ctr+1):        
    if input[left] != input[right]:
      flag = 0
      break
    left += 1
    right -= 1

  if flag == 1:
    return "%s is palindrome" % (input)
  else:
    return "%s is not palindrome" % (input)

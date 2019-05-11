
def isarmstrong(n):
  'armstrong- sum of cubes of digits = number'
  if isinstance(n, int) == False or n < 0:
    print("invalid input!")
    return

  n1=n
  r=0
  sum=0
  while n>0:
    r=(n%10)
    sum=sum+(r**3)  
    n=n//10 
  print("%d is armstrong" % (n1)) if n1 == sum else print("%d is not armstrong"% (n1)) 


def fact(n):
  if (not isinstance(n,int)) or (n < 0):
    return("wrong input given!!")
  f = 1
  n1 = n
  if n == 0: return 1
  while n >= 1:
  	f = n * fact(n-1) 
  	return f


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
    print("it is palindrome")
  else:
    print("it is not palindrome")


def generate(n):
  st, nx, temp = 0, 1, 0
  print(st,", ",nx,end="")

  for i in range(0,n-2):
    temp = nx
    nx = st + nx
    st = temp
    print(", ", nx, end="")
  print()

def guddu():
  import re
  name_list = ["kamlesh", "Ramesh", "Suresh", "Gita esh", "esh isha", "esh"] 
  print("original_set: %s" % (str(name_list)))
  name_list = [x for x in name_list if len(re.findall(r'^esh$' , x)) == 0]
  #name_list = filter(lambda x: len(re.findall(r'^esh$' , x)) == 0, name_list)
  print("filtered:     %s" % (str(name_list)))


  
def main():
    print("in main")
    #do stuff

main()
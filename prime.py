#find optimus

import math # need this for the sqrt function

number_max = int(input("Please enter a number: ")) 
my_list= [1, 2]

for n in range(3, number_max,2):
  top = int(math.sqrt(n)) + 1
  for x in range(3, top):
    if n % x == 0:
      #print(f"The number {n} is {x} * {n//x}. Not prime!")
      break
  else: my_list.append(n) # nice use of else in loops

print (f" This is the list of prime numbers between 1 and {number_max}:  {my_list}")

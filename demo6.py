
num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

def myfunc(n):
 
  return lambda a : a * n

mydoubler = myfunc(2)
mydoubler = myfunc(2)


print(mydoubler(11))



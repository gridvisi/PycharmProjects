'''
https://www.tutorialspoint.com/python/python_loop_control.htm#:~:text=The%20break%20statement%20in%20Python,both%20while%20and%20for%20loops.
'''

for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print('Current Letter :', letter)

var = 10  # Second Example
while var > 0:
    print ('Current variable value :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")


for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")


for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i #to calculate the second factor
         print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:        # else part of the loop
      print (num, 'is a prime number')


for letter in 'Python':
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")


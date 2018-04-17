'''
Created on 05-Apr-2018

@author: viky
'''

if __name__ == '__main__':
    pass
# This program adds two numbers

#number1 = int(input('Enter First number : '))
#number2 = int(input('Enter Second number : '))
#number3 = int(input('Enter Third number : '))
import Ref
import Smallest
import Dep 
import Largest         
import Fib             
      
Ref.greet("Viky") 
  
Smallest.smallest(12, 33, 23);

Largest.largest(24, 98, 67);

Dep.my_function()

Fib.fib(78)
 
num1 = 1.5
num2 = 6.3

# Add two numbers
sum = float(num1) + float(num2)

for x in range(0, 3):
    print ("We're on time %d" % (x))
    
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

#largest(number1, number2, number3)
#smallest(number1, number2, number3)

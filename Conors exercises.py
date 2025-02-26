# Loop exercise 

total = 0  # Initialising

for i in range(1, 11):  # Iterate from 1 to 10 (inclusive)
    total += i  # Add the loop variable to the total sum

print("The total sum is:", total)  # Print the final sum

#  While loop
x=10
while x>0:
    x-=1
    print(x)

# break 
x = 10  #initilisation 
while x>0:  #as long as x is greater than 0, print x minus 1 (it's a list from 10 subtracting 1 down to 1)
    print(x)
    x-=1

#challenge 
x=1
y=1
x is y #returns true because x and y point to the same object 

# defining functions
def my_function(a,b,/,c,d,*,e,f):
      return 0 
print('this is a function')

def my_func2(a, b, c=3, d=4):
      return 0 

def my_function(a, b=10, c=20):
    print(a, b, c)

# Usage
my_function(5)  # a is required, b and c will take default values
# Output: 5 10 20

first_value = 10
second_value = 10

my_dict = {'first key': first_value, 'second key': second_value}

#creating a list
my_list = list(range(0,10,2))
print(my_list)

#creating a list of even numbers using comprehension

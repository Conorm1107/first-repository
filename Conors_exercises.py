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
my_list2 = [x**2 for x in range(10) if x%2 ==0]
print(my_list2)
#for each value of x^2 in the range(10) include the value of x if the remainder when divided by 2 is 0 (e.g. an even number)

#accumulator in a comprehension
my_acc = 0 
[my_acc:= my_acc+x**2 for x in range(10) if x%2==0]
print(my_acc)

#making neater lists with comprehension 
my_list3 = []
for i in range(10):
     for j in range(10):
          if i%2==0:
               my_list3.append(i*j)
               print(my_list3)

#is the same as 
[i*j for i in range(10) for j in range(10) if i%2==0]

#tuple comprehension

#dictionary comprehension 
my_dict_2 = {x: x**2 for x in range(10)}
print(my_dict_2)

#printing arguments
def f(*args):
    for arg in args:
        print(arg)


#Suppose we have another function, g, and we want it to forward a variable number of arguments straight into f. How do you think this would be written?
def f(*args, **kwargs): #function designed to accept any number of positional arguments (*args) and keyword arguments (**kwargs)
    for arg in args: #args is a tuple that holds all the positional arguments passed to f, kwargs is a dictionary that holds all the keyword arguments passed to f
     print(arg)
    for key, value in kwargs.items():   #inside f it loops through the args tuple and prints each positional argument, then loops through the kwargs dictionary and prints the key-value pairs
     print(f"{key}:{value}")

def g(*args, **kwargs): #this function accepts any number of positional and keyword arguments, just like f
    f(*args, **kwargs)  #inside g, instead of doing any processing it simply forwards these arguments directly to f by calling f(*args, **kwargs)
# *args unpacks the positional arguments from g and forwards them to f as a tuple
# **kwargs unpacks the keyword arguments from g and forwards them to f as a dictionary
g(1,2,3, name='Alice', age=25)
# we call function g and pass it some positional arguments(1,2,3) and keyword arguments (name="Alice", age = 25)
# 1,2,3 are collected by *args in g as a tuple (1,2,3) and alice, 25 are collected by **kwargs in g as a dictionary

#What do you think will happen when you run this program?
def f(a,b,c):
    return a+b+c    #defines a function f, that takes 3 arguments and returns the sum of them 

def g(list_of_numbers):
    return f(*list_of_numbers)  #defines a function g, with a single argument list of numbers
#*list of numbers unpacks the list and passes its individual elements as positional arguments to the function f
#since f requires exactly 3 arguments (a,b and c), list_of_numbers must be a list with exactly 3 elements for the unpacking to work correctly

my_first_list = [10,20,30]  #expect the output here to be 60
my_second_list = [10, 20, 30, 40]   #expect an error here given f expects 3 arguments but this has 4

#print(g(my_second_list)) - gave error as expected

#Write a function which sums a variable number of arguments, and pass it an unpacked comprehension of the first 10 even squares (starting at 1).

def h(*args):
    return sum(args)

def i(*list_of_squares):
    return h(*list_of_squares)

my_squares_list = [i**2 for i in range(1,11)]
print(h(*my_squares_list))

#Write your own version of the zip function to work on a variable number of lists, using the techniques learned in the previous sections.
def my_zip(*args):
    for items in zip(*args):
     return items

result = list(my_zip([1,2,3],[4,5,6],[7,8,9]))
print(result)

#listing 61
def recip(x):
    try:
        y=1/x
    except:
        print("Warning: cannot take the reciprocal of zero!")
        y=0
    finally:
        return y
result = recip(0)
print(result)



#renaming
import os

os.rename('Conors exercises.py', 'Conors_exercises.py')

#linking scripts
def f(x):
    return x**2

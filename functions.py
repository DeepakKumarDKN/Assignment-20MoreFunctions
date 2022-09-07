#TODO: 1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

# def uniqueElements(a):
#   listOne = []
#   for i in a:
#     if i not in listOne:
#       listOne.append(i)
#   print(listOne)

# uniqueElements([10,20,30,10,20,10,30,40,70,80])

# TODO: 2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

# def checkPrime(n):
#   factor = 0
#   for i in range(1,n+1):
#     if n % i == 0:
#       factor+=1
      
#   if factor==2:
#     print('its a prime number')
#   else:
#     print('Its not a prime number')
    
# checkPrime(18)

#TODO: 3. Write a python program to create a function that prints the even numbers from a given list.

# def evenNumber(a):
#   for i in range(len(a)):
#     if a[i] %  2 ==0:
#       print(a[i])

# evenNumber([10,33,77,93,50])



# TODO: 4. Write a python program to create a function that checks whether a passed string is palindrome or not.

# def pallindrome(char):
#   if char[::-1] == char:
#     print('The number is pallindrome')
#   else:
#     print('The number is not pallindrome')
# pallindrome('momy')


# TODO: 5. Write a python program to create a function to find the Min of three numbers.

# def findMaximim(list):
#   result = max([list[i]  for i in range(len(list))])
#   print(result)
# findMaximim([10,20,30,40,100,90,10])

# def findMaximim(list):
#   maximum = 10 
#   for i in list:
#     if i > maximum:
#       maximum = i
#   print('The maximum number is:', maximum)
# findMaximim([10,20,30,40,100,90])

# def findMax(list):
#   max = 10
#   for i in range(len(list)):
#     if list[i]>max:
#       max = list[i]
#   print(max)

# findMax([10,20,30,40,90,100,250,467,80])

#TODO: 6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.

# def square(a):
#   squareNumbers=[]
#   for i in range(1,a+1):
#     squareNumbers.append(i*i)
#   print(squareNumbers)

# n = int(input('Enter the number:'))
# square(n)

# TODO: 7. Write a python program to access a function inside a function.

# def functionOne():
#   print('Hello i am from Function One')
#   def functionTwo():
#     functionOne()
#   return functionTwo
# a=functionOne()

# TODO: 8 Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.

# def lowerUpper(charcter):
#   lower = []
#   upper = []
#   for i in charcter: 
#     if i.isupper():
#       upper.append(i)
#     else:
#       lower.append(i)
#   print('The number of lower Characters are:',len(lower))
#   print('The number of upper Characters are:',len(upper))
# lowerUpper('MySirG')



# TODO: Write a python program to create a function to check whether a string is a pangram or not.

# def checkPanagram(str):
#   characters = 'abcdefghijklmnopqrstuvwxyz'
#   for i in characters:
#     if i not in str.lower():
#       return False

#   return True
  
# stringInput = input('Enter the string:')  
# if (checkPanagram(stringInput) == True):
#   print('Its a panagram')
# else:
#   print('Its not a panagram')




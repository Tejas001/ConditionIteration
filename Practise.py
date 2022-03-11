# n = int(input("Enter a number a random number between 1 and 2022: "))
# if n in range(1,2022+1):
#     print('YES')
# else:
#     print('NO')

# ch = int(input("Enter a single character: "))

# if ch >= 0 and ch <= 9:
#     print('The Entered digit between 0-9 i.e. ',ch)
# if ch >= 9 and ch <= 100:
#     print('Entered digit is beyond the range 0-9 i.e. ',ch)

# sales = int(input('Enter sales: '))
# if sales >=1000:
#     discount = sales * 0.10
#     print(f"Discount is {discount}")
# else:
#     discount = sales * 0.05
#     print(f"Discount is {discount}")

# mAxImUm NuMbEr
# x,y,z = 0,0,0
# x = int(input('Enter x value: '))
# y = int(input('Enter y value: '))
# z = int(input('Enter z value: '))

# max = x

# if y>max:
#     max = y
# elif z>max:
#     max = z
# print()

# Filter function
# def even(number):
#     if (number % 2) == 0:
#         return True
#     return False

# numbers = [1,2,3,4,5]
# even_numbers = filter(even, numbers)
# for i in even_numbers:
#     print(i)

# MaP FuNcTiOn
# def square(number):
#     return number*number

# numbers = [1,2,3,4,5]
# squared_numbers = map(square, numbers)
# print([i for i in squared_numbers])

# Area and perimeter of circle
# radius = int(input("Enter radius of circle: "))
# choice = int(input("Enter choice 1(area) or 0(perimeter): "))
# if choice == 1:
#     area = 3.14*radius*radius
#     print(area)
# else:
#     perimeter = 2*3.14*radius
#     print(perimeter)

# Program to read 2 num and print computed result
# n1 = int(input("Enter First Number: "))
# n2 = int(input("Enter First Number: "))
# op = input("Enter Arithmetic operator[+,-,*,/,%]: ")
# symbol = ['+','-','*','/','%']

# if op =='+':
#     print(n1+n2) 
# elif op =='-':
#     print(n1-n2)
# elif op =='*':
#     print(n1*n2)
# elif op =='/':
#     print(n1/n2)
# else:
#     print(n1%n2)

# if elif else
# choice = input("Enter sinlge character: ")
# if choice >= 'A' and choice <= 'Z':
#     print('UPPERCASE',choice)
# elif choice >= 'a' and choice <= 'z':
#     print('lowercase',choice)
# elif choice >= '0' and choice <= '9':
#     print('Digit',choice)
# else:
#     print('Special character',choice)

# Program to calculate factorial using for and while loop
# num = int(input("Enter a number: "))
# fact = 1
# for n in range(1,num+1):
#     fact *= n
# print("Factorial of ",num, ":", fact)
# a = 1
# while a <= num:
#     fact *= a
#     a += 1
# print(f"Factorial of {num} is {fact}")

# Program to print even and odd number using while
# num = int(input('Enter up to which number it should print: '))
# ctr = 1
# even_list = []
# odd_list = []
# even = odd = 0
# while ctr <= num:
#     if  ctr%2==0:
#         even_list.append(ctr)
#         even += ctr
#     else:
#         odd_list.append(ctr)
#         odd += ctr
#     ctr+=1
# print("Even number list: ",even_list,"Even number sum: ",even)
# print("Odd number list: ",odd_list,"odd number sum: ",odd)

# Program to Guess a number
# import random
# num = random.randint(10,50)
# chance = 1
# while chance <= 5:
#     guess = int(input('Enter number to be guessed: '))
#     if guess == num:
#         print('You Won')
#         break
#     else:
#         chance += 1
# if not chance<5:
#     print('You lost')

# Program to take input and sum the number 
# sum = 0
# ctr = 0
# num_list=[]
# ans = 'y'
# while ans == 'y':
#     num = int(input('Enter number: '))
#     if num <=0:
#         break
#     sum += num
#     ctr += 1
#     num_list.append(num)
#     ans = input('Want to enter more (y/n): ')
# else:
#     print(f"Entered number are {ctr}")
# print(f'Sum of entered number is: {sum}')
# print(f'List of entered number is = {num_list}')

# Program to read an integer > 1000 and reverse the number
# num = int(input('Enter a number > 1000: '))
# reverse = 0

# while num != 0:
#     digit = num%10
#     print('digit',digit)
#     reverse = reverse*10+digit
#     print('reverse',reverse)
#     num //= 10
# # print('original number:',num,'Reverse number is:',reverse)

# Rewrite code to save time
# a = int(input('Enter number: '))
# if a == 0:
#     print('Zero')
# elif a == 1:
#     print('One')
# elif a == 2:
#     print('Second')
# else:
#     print('Three')

# It prints water when temp < 212 and greater than 32

# Output produced by code is C, D

# error in code
# weather = 'raining'
# if weather == 'sunny':
#     print('Summer')
# elif weather == 'snow':
#     print('Winter')
# else:
#     print(weather)

# Output of code None of the above

# Find error in code if and else need to be indented properly
# n = int(input('Enter number: '))
# if n<1:
#     print('Less than one')
# else:
#     for i in range(1,n+1):
#         print(i*i, end=", ")

# Program to check o/p
# n = int(input('Enter number: '))
# if n>0:
#     for i in range(1,n+n):
#         print(i/(n/2))
#     else:
#         print('Quiting...')

# Rewrite code
n = 20
# while n>0:
#     print(n)
#     n -= 3

# print('##########')
# for i in range(20,0,-3):
#     print(i)

# while n > 0:
#     print(n%10)
#     n = n/10

# i = 0
# while i<4:
#     j=0
#     while j<5:
#         if i+1==j or j+1==4:
#             print('+', end=' ')
#         j+=1
#     else:
#         print('o', end=' ')
#     i+=1
# print()

# x = 45
# while x<50:
#     print(x)
#     x += 1

# for q in range(100,50,-10):
#     print(q)

# for i in range(500,100,10):
    # print('*',i) #print nothing

# for x in [1,2,3]:
#     for y in [4,5,6]:
#         print(x,y)

# x = 10
# y=5
# for i in range(x-y*2):
#     print('%',i) 

# for x in range(2):
#     for y in range(3):
#         print(x,y,x+y)

# c=0
# for x in range(10):
#     for y in range(5):
#         c+=1
# print(c) 

# Checking o/p
# a1 =1
# a2 = 2
# while True:
#     n = int(input('Enter num: '))
#     if n == a1:
#         continue
#     elif n == a2:
#         break
#     else:
#         print('What')

# print('ever')

# Checking output
# cntr = 0
# for i in range(4):
#     for j in range(5):
#         if i+1==j or j+i==4:
#             print('+',end=' ')
#             cntr +=1
#         else:
#             print('o',end=' ')
# print(cntr)


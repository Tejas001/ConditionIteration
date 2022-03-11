# Convert centimeter to inches
# centimeter = float(input('Enter a lenght in centimeter: '))
# if centimeter<0:
#     print('Invalid input')
# else:
#     CTI = centimeter/2.54
#     print(f'Length {centimeter} to inches {CTI}')

# Calculate Total cost
# item = int(input("Enter nno. of item bought: "))

# if item < 10:
#     total_cost = item*125   
# elif item >= 10 and item <= 99:
#     total_cost = item*100
# else:
#     total_cost = item*70
# print('Total Cost: ',total_cost)

# Leap year logic if ((year % 400==0 or year%100 !=0) or year % 4==0) 

# Program to input digit and print as words
# for i in range(0,9):
#     d = int(input('Enter a number: '))
#     if d == 0 :
#         print("Zero")
#     elif d == 1 :
#         print("One")
#     elif d == 2 :
#         print("Two")
#     elif d == 3 :
#         print("Three")
#     elif d == 4 :
#         print("Four")
#     elif d == 5 :
#         print("Five")
#     elif d == 6 :
#         print("Six")
#     elif d == 7 :
#         print("Seven")
#     elif d == 8 :
#         print("Eight")
#     elif d == 9 :
#         print("Nine")
#     else :
#         print("Invalid Digit")
#         break
# print('The End')

# Program to check sqrt of number is prime or not
# num = int(input('Enter a number: '))
# square_root = num*0.5
# flag = False
# if square_root >1:
#     for i in range(2,int(square_root+1)):
#         if (square_root%i)==0:
#             flag = True
#             break
# if flag:
#     print("Original no. is ",num," and it's SQRT is ",square_root," which not a prime number")
# else:
#     print("Original no. is ",num," and it's SQRT is ",square_root," which is a prime number")

# Program to print first n odd number in desc order
# num = int(input('Enter a number: '))

# for i in range(num,0,-1):
#     if i%2!=0:
#         print(f'{i} a odd number')

# print('Program ends')

# Program to print series
# for i in range(1,41,3):
#     print(i,end=" ")
# print()
# x = 1
# for i in range(1,41,3):
#     print(i * x,end=" ")
#     x *= -1

# Program to avg the input values
# sum = count = 0
# print('To quit enter (q/Q)')

# while True:
#     num = input()
#     if num == 'q' or num == 'Q':
#         break
#     else:
#         sum += int(num)
#         count += 1
# avg = sum/count
# print(f'Avg of entered number is: {avg}')

# Program  to print Tipsy Topsy
# n = int(input('Enter a num (>20) : '))
# if n<=20:
#     print('Invalid output')
# else:
#     for i in range(11,n+1):
#         if i%3==0 and i%7==0:
#             print('TipsyTopsy')
#         elif i%3==0:
#             print('Tipsy')
#         elif i%7==0:
#             print('Topsy')
# print('End....')

from itertools import chain, count
import sys
# Program to print max number
# max = input("Enter number: ")
# if max != 'q' or max != 'Q':
#     max = int(max)
#     while True:
#         n = input("Enter number: ")
#         if n == 'q' or n == 'Q':
#             break
#         n = int(n)
#         if n > max:
#             max = n
#     print('Largest number is: ',max)

import sys
# Program to print 2nd max number
# n = int(input('No. of inputs required:'))
# if n>1:
#     max1 = int(input("Enter number: "))
#     max2 = int(input("Enter number: "))
#     if max2 > max1:
#         temp = max2
#         max2 = max1
#         max1 = temp
#     for i in range(n-2):
#         inpt = int(input("Enter number: "))
#         if inpt > max1:
#             max2 = max1
#             max1 = inpt
#         elif inpt > max2:
#             max2 = inpt                     
#     print('Second Largest number is: ',max2)
# else:
#     print('Enter more numbers')

# Program to print input (1234) and output 41
# x = int(input("Enter an integer: "))
# temp = x
# count = 0
# digit = -1

# while temp != 0 :
#     digit = temp % 10
#     print(digit)
#     count += 1
#     print(count)
#     temp = temp // 10
#     print(temp)

# y = count * 10 + digit

# print("Y =", y)

# program to print count of employee in age bucket
# c1 = c2 = c3 = 0
# n = int(input('Enter no of age to be include: '))
# for i in range(1,n+1):
#     age = int(input('Enter age: '))
#     print('Age: ',age)
#     if 26 <= age <=35:
#         c1 += 1
#     elif 36 <= age <=45:
#         c2 += 1
#     elif 46 <= age <=55:
#         c3 += 1
# print('Age Count in between 26 <= age <=35: ',c1)
# print('Age Count in between 36 <= age <=45: ',c2)
# print('Age Count in between 46 <= age <=55: ',c3)

# Program to print rectangle 
# for i in range(6):
#     for j in range(20):
#         print('*',end='')
#     print()

# Program to print factorial
# fact = 1
# n=int(input('Enter number: '))
# for i in range(1,n+1):
#     fact *= i

# print(f'Factorial of number {n} is {fact}')

# Program to print *
n = 6
# for i in range(1,n+1):
#     print(str("*"*((2*i)-1)).center((2*n)-1))

# for i in range(1,n):
#     print(" "*(n-i),end='')
#     print("*"*((2*i)-1))    

# for i in range(n,0,-1):
#     print(" "*(n-i),end='')
#     print("*"*((2*i)-1))


# for i in range(1,n):
#     print("*"*i)
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print('*',end='') 
#     print()



# for i in range(1,n+1):
#     for j in range(0,i):
#         print('*',end='') 
#     print()
# for i in range(1,n):
#     print("*"*(n-i))

# for i in range(1,n+1):
#     print(" "*(n-i),end='')
#     print('*'*i)

# for i in range(1,n):
#     print(" "*(n-i),end='')
#     print('*'*n)

# for i in range(n,0,-1):
#     print("*"*(n))
#     print(' '*(n-i),end='')

# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     print('*'*(i))



# for i in range(n,0,-1):
#     print(' '*(n-i),end='')
#     print('*'*(i-1))

# for i in range(1,n):
#     print(' '*(n-i),end='')
#     print('*'*((2*i)-1))

# for i in range(1,n):
#     print(" "*(n-i),end='')
#     print("*"*((2*i)-1))    
# for i in range(n,0,-1):
#     print(" "*(n-i),end='')
#     print("*"*((2*i)-1))    

# for i in range(1,n):
#     print('*'*i)
# for i in range(n,0,-1):
#     print('*'*i)

# for i in range(1,n+1):
#     print('*'*i)
# for i in range(n,0,-1):
#     print('*'*i)
atoz=65
for i in range(1,n):
    print(chr((atoz+i)-1)*i)

# for i in range(1,n):
#     for j in range(i+1):
#         print(chr((atoz+1)-1),end='')
#     print()


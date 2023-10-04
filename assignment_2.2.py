"""
Problem 1: Print Even Numbers- Write a Python program that prints all even numbers
from 1 to a given positive integer 'n'. Use a for loop to iterate through the numbers and
print only the even ones.
"""
# n = int(input('Enter any positive number:'))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)
#         i+=1

"""
Problem 2: Calculate Average- Write a Python program that calculates the average of
a list of numbers. First, ask the user to input the number of values and then the values
themselves. Use a for loop to calculate the average.
"""
# n = int(input("Enter the number of values: "))
# print('Please input each value and press "Enter!"')
# sum=0
# for i in range(n):
#     value = float(input())
#     sum+=value
#     average = sum/n
# print('The average of the values is: ', average)

"""
Problem 3: Find Prime Numbers Write a Python program that finds and prints all
prime numbers within a given range (from start to end). Use a for loop to check
each number in the range for primality.
"""
start = int(input('Enter the start number:'))
end = int(input('Enter the end number: '))
print("The Prime numbers are:")

for num in range(start, end+1):
    if num>1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

#!/usr/bin/env python3

# 4.
print("#4.\nHello, World!")

# 5.
print(f"#5.\nResult of the 2+2 = {2+2}") 

# 6.
name = input("#6.\nInput your name : ")
print(f"Hello, {name}!")

# 7.
print("#7.")
for i in range(1, 11):
    print(i)

#8. 
age = input("#8.\nEnter your age: ")
print(f"You are {age} years old")

#9.
try:
    num1 = int(input("#9.\nEnter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Result of multiplication is {num1*num2}")
except ValueError:
    print(f"Invalid literal for int() with base 10")

#10.
word = input("#10.\nInput any word: ")
print(word[0])

#11.
try:
    number = int(input("#11.\nInput decimal number: "))
    print(f"Square of number is {number**2}")
except ValueError:
    print("Invalud literal for int() with base 10.")

#12.
print(f"#12.\n{[x*5 for x in range(1, 11)]}")

#13.
try:
    num_1 = int(input("#13.\nEnter first number: "))
    num_2 = int(input("Enter second number: "))
    arithm_mean=(num_1+num_2)/2
    print(f"Arithmetic mean is {arithm_mean}")
except ValueError:
    print(f"Invalid literal for int() with base 10")
from functools import reduce

'''i=1
list=[]
while i<=3:
	k=input("Enter movie name : ")
	list.append(k)
	i+=1
print(list)'''


# palindromic list

'''
list=[1,2,3,1]
le=len(list)
l=int(len(list)/2)
for i in range(l) :
	if(list[i]==list[le-i-1]):
		f=0
	else:
		f=1
if f==0 :
	print("palindrome")
else :
	print("no")
'''


# tuple program

# t=("A","B","A")
# print(t.count("A"))


# l=[1,2,2,2,3,4,5,5]
# s=list(set(l))
# print(s)



# Example: print each sublist in a list of lists
# list_of_lists = [[1, 2], [3, 4], [5, 6]]
# for sublist in list_of_lists:
# 	print(sublist)

# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))
# user_list = []
# for i in range(rows):
# 	row = []
# 	for j in range(cols):
# 		val = input(f"Enter value for row {i+1}, column {j+1}: ")
# 		row.append(val)
# 	user_list.append(row)

# for sublist in user_list:
# 	print(sublist)


# Example: format string using f-string
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello, {name}! You are {age} years old.")
# print("Hello, {}! You are {} years old.".format(name, age))
# print("Hello, %s! You are %d years old." % (name, age))

# Addition of two matrices using lists

# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# print("Enter elements for first matrix:")
# matrix1 = []
# for i in range(rows):
# 	row = []
# 	for j in range(cols):
# 		val = int(input(f"Element [{i+1}][{j+1}]: "))
# 		row.append(val)
# 	matrix1.append(row)

# print("Enter elements for second matrix:")
# matrix2 = []
# for i in range(rows):
# 	row = []
# 	for j in range(cols):
# 		val = int(input(f"Element [{i+1}][{j+1}]: "))
# 		row.append(val)
# 	matrix2.append(row)

# result = []
# for i in range(rows):
# 	row = []
# 	for j in range(cols):
# 		row.append(matrix1[i][j] + matrix2[i][j])
# 	result.append(row)

# print("Sum of matrices:")
# for row in result:
# 	print(row)

# Matrix multiplication taking input from user 

# rows1 = int(input("Enter number of rows for first matrix: "))
# cols1 = int(input("Enter number of columns for first matrix: "))
# print("Enter elements for first matrix:")
# matrix1 = []
# for i in range(rows1):
# 	row = []
# 	for j in range(cols1):
# 		val = int(input(f"Element [{i+1}][{j+1}]: "))
# 		row.append(val)
# 	matrix1.append(row)

# rows2 = int(input("Enter number of rows for second matrix: "))
# cols2 = int(input("Enter number of columns for second matrix: "))
# print("Enter elements for second matrix:")
# matrix2 = []
# for i in range(rows2):
# 	row = []
# 	for j in range(cols2):
# 		val = int(input(f"Element [{i+1}][{j+1}]: "))
# 		row.append(val)
# 	matrix2.append(row)

# if cols1 != rows2:
# 	print("Matrix multiplication not possible. Number of columns of first matrix must equal number of rows of second matrix.")
# else:
# 	result = []
# 	for i in range(rows1): 
# 		row = []
# 		for j in range(cols2):
# 			sum = 0
# 			for k in range(cols1):
# 				sum += matrix1[i][k] * matrix2[k][j]
# 			row.append(sum)
# 		result.append(row)
# 	print("Product of matrices:")
# 	for row in result:
# 		print(row)



# Example function: Check if a list is palindromic
# def is_palindrome(lst):
# 	return lst == lst[::-1]

#
# sample_list = [1, 2, 3, 2, 1]
# if is_palindrome(sample_list):
# 	print("The list is a palindrome.")
# else:
# 	print("The list is not a palindrome.")


# Example: Local and Global Variables using Function

# x = 10  # Global variable

# def local():
# 	x = 5  # Local variable
# 	print("local x =", x)

# local()
# print("global x =", x)



# Example: Using 'global' keyword to modify global variable inside a function
# x = 10  # Global variable

# def modify_global():
# 	global x
# 	x = 5  # Modify global variable
# 	print("Inside function, x =", x)

# modify_global()
# print("Outside function, x =", x)



# using * c becomes keyword argument 
# def add(a, b,*,c):
# 	return a + b + c
# print("* :",add(2,3,c=4))

# # using / a and b become positional arguments 
# def add(a, b,/,c=0):
# 	return a + b + c
# print("/ :",add(2,3,c=4))




# Calculator

# def add(x, y):
# 	return x + y

# def subtract(x, y):
# 	return x - y

# def multiply(x, y):
# 	return x * y

# def divide(x, y):
# 	if y == 0:
# 		return "Error: Division by zero"
# 	return x / y

# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter choice (1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1':
# 	print("Result:", add(num1, num2))
# elif choice == '2':
# 	print("Result:", subtract(num1, num2))
# elif choice == '3':
# 	print("Result:", multiply(num1, num2))
# elif choice == '4':
# 	print("Result:", divide(num1, num2))
# else:
# 	print("Invalid input")



# 	# Example: Using filter, map, and reduce


# 	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 	# filter: get even numbers
# 	evens = list(filter(lambda x: x % 2 == 0, numbers))
# 	print("Even numbers (filter):", evens)

# 	# map: square each number
# 	squares = list(map(lambda x: x ** 2, numbers))
# 	print("Squares (map):", squares)

# 	# reduce: sum all numbers
# 	total = reduce(lambda x, y: x + y, numbers)
# 	print("Sum (reduce):", total)




# Linear Search Program

def linear_search(arr, target):
	for i, value in enumerate(arr):
		if value == target:
			return i
	return -1

arr = [5, 3, 8, 4, 2]
arr.append(10)
target = int(input("Enter the number to search: "))
result = linear_search(arr, target)
if result != -1:
	print(f"{target} found at index {result}")
else:
	print(f"{target} not found in the list")
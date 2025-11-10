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
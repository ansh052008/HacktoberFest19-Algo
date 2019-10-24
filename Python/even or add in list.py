list1=[]
size=int(input("How many numbers you want to enter? "))
for i in range(size):
    x=int(input("Enter the number: "))
    list1.append(x)

even_num , odd_num = 0, 0

for num in list1:

	if num % 2 == 0:
		even_num += 1

	else:
		odd_num += 1

print("Even numbers in the list: ", even_num)
print("Odd numbers in the list: ", odd_num)

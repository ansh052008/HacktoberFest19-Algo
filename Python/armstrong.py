num = int(input("Enter a number: "))

if(num>0):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        if num == sum:
            print(num,"is an Armstrong number")
        else:
            print(num,"is not an Armstrong number")
if(num=0):
    print("Zero is not an amstrong number")
else:
    num=0-num
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        if num == sum:
            print(num,"is an Armstrong number")
        else:
            print(num,"is not an Armstrong number")

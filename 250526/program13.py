
#factorial of a number
num=int(input("enter num:"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"factorial of {num} is {factorial}")

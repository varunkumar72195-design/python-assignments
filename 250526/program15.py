    ##amstrong number
num=int(input("enter num:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print(f"{num} is an amstrong number")
else:
    print(f"{num} is not an amstrong number")

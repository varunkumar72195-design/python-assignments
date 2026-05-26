 #  ##Armstrong numbers in a range
lower=int(input("enter lower limit:"))
upper=int(input("enter upper limit:"))
print(f"Armstrong numbers between {lower} and {upper} are:")
for num in range(lower,upper+1):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if num==sum:
        print(num)

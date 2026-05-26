
##fabonacci series
n=int(input("enter n:"))
a=0
b=1
print("Fibonacci series:")
for i in range(n):
    print(a)
    a,b=b,a+b

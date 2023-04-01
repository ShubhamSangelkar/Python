#fibonacci Series using while 0,1,1,2,3,5,8,13

a,b,c=0,1,0
count=0

n=int(input("Enter your number of sequence: "))
if n==1:
    print("Fibonacci series of ",n,"is",a)
elif n<=0:
    print("Kindly enter positive number")
    breakpoint
else:
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1

#fibonacci Series using For 0,1,1,2,3,5,8,13

a,b,c=0,1,0
s=int(input("Ener your range: "))
if s==1:
    print("your series is: ",a)
elif s<0:
    print("please enter positive number")
    breakpoint
else:
    for i in range(s):
        print(a)
        c=a+b
        a=b
        b=c

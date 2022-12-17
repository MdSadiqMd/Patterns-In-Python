a=int(input("enter the number of steps"))
for i in range(0,a):
    for j in range(0,a-i-1):
        print(end=" ")
    for j in range(0,2*i+1):
        print("*",end=" ")
    print()
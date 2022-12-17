a=int(input("enter a number"))
for i in range(a,0,-1):
    for j in range(0,a-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
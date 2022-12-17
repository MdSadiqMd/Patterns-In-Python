a=int(input("enter number of steps"))
k=2
for row in range(1,a+1):
    for col in range(1,2*a):
        if col+row==a+1 or col-row==a-1:
            print("*",end="")
        elif row==a and col!=k:
            print("*",end="")
            k=k+2
        else:
            print(end=" ")
    print()
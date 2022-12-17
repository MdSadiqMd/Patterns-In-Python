a=int(input("enter number of steps:"))
for row in range(a,0,-1):
    for col in range(1,row+1):
        print(format(row,"<3"),end="")#format used for space in output
    print()
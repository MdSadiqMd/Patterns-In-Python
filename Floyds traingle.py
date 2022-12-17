a=int(input("enter number of steps of floyds traingle"))
num=1
for row in range(1,a+1):
    for col in range(1,row+1):
        print(format(num,"<3"),end=" ")#format specifier used for space
        num=num+1
    print()

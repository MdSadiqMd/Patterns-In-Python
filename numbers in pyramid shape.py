a=int(input("enter number of rows:"))
for i in range(1,a+1):
    for j in range(1,a-i+1):#printing space
        print(format(" ","<3"),end="")#format specifier used for space
    for j in range(i,0,-1):#print right angle traingle
        print(format(j,"<3"),end="")
    for j in range(2,i+1):#printing other half of right angle traingle to complete triangle
        print(format(j,"<3"),end="")
    print()

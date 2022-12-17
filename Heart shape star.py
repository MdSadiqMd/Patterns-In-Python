#we dont need star in the index row 0,3,6 so we writ modulus at first condition
for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or row-col==2 or col+row==8:
            print("*",end="")
        else:
            print(end=" ")
    print()
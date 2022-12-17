#sum of row and col index is 2 and some of same conditions for others
for row in range(5):
    for col in range(5):
        if row+col==2 or col-row==2 or row-col==2 or (col==3 and row==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
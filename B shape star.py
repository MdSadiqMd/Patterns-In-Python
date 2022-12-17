# in coloumn 0 and 3 we need star line ; in row 0,3,6 we need stars but not in row in the same olace the star in row printed so we write row>0<4 such that it will not print double stars in that place we dont wnat stars at last of row 0,3,6 so we write row!=0,3,6 otherwise it print box B 
for row in range(7):
    for col in range(5):
        if(col==0) or (col==3 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<3)):
            print("*",end="")
        else:
            print(end=" ")
    print()

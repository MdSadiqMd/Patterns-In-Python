for row in range(7):
    for col in range(5):
        if ((row==0 or row==3 or row==6)and (col>0 and col<4)) or ((row==1 or row==2 ) and (col==0)) or ((row==4 or row==5) and (col==4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
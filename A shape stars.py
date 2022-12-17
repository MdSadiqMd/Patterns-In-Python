#here the range numbers are given according to the size of a if condition gives ways to print star and else condition to print spaces insiide the A
for row in range(7):
    for col in range(5):
        if (col==0 or col==4) and row!=0 or (row==0 or row==3) and (col>0 or col<4):
            print("*",end="")
        else:
            print(end=" ")
    print()


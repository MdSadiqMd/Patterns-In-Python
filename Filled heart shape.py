#filled heart shape is divided into three parts two traingle in the top and one gaint inverted traingle in the bottom
a=int(input("enter number of steps"))
b=a//2
for i in range(b):
    for j in range(b-i-1):#printing space in traingle
        print(" ",end="")
    for j in range(i+1):#printing gaps in the traingle
        print("* ",end="")#giving gap in ""between star is for gap in shape
    if(a%2==0):#if the number of steps allocated is even
        for j in range(2*(b-i-1)):#printing space for second traingle as from reserence line double distance so 2*
            print(" ",end="")
    else:#if the input steps is odd then there will be an error in shape so we can directly add one to code
        for j in range(2*(b-i-1)+1):#printing space for second traingle as from reserence line double distance so 2*
            print(" ",end="")
    for j in range(i+1):#printing gps in second traingle
        print("* ",end="")

    print()

for i in range(a,0,-1):
    for j in range(a-i):#printing gaps in inverted traingle
        print(" ",end="")
    for j in range(i,0,-1):#printing stars of inverted traingle
        print("* ",end="")
    print()

a=int(input("enter number of steps"))
b=a//2
for i in range(b):
    print(" "*(b-i-1)+"* "*(i+1),end="")#this print space in (n-i-1) and * for (i+1)
    if(a%2==0):
        print(" "*(2*(b-i-1)),end="")
    else:
        print(" "*(2*(b-i-1)+1),end="")
    for j in range(i+1):
        print("* ",end="")
    print()
for i in range(a,0,-1):
    print(" "*(a-i)+"* "*(i))

print()

i=1
limit=10
while i<=limit:

    k=1
    while k<=(limit-i):
        print(" ",end=" ")
        k=k+1

    l = 1
    while l<=i:
        print("*",end="    ")
        l=l+1
    print()
    i=i+1
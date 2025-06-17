num=7
p=2
limit=int(num/2)
if num>1:
    while p<=limit:
        # print(p)
        if num%p==0:
            print("not prime")
            break
        p=p+1

    else:
        print("prime")
else:
    print("provide valid number")
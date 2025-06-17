lists=[]
count=0 
while True:
    n=int(input("ENTER THE NUMBERS : "))
    if n>=5 and n<=25:
      lists.append(n)
      count=count+1
    else:
        print("enter valid..")
    if count>=5:
        break
print(lists)
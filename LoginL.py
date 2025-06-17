username=['a','b','c','d','e']
password=['abc','xyz','mno','123','456']
user=input("ENTER YOUR USERNAME :")
if user in username:   
    pas=input("ENTER YOUR PASSWORD")
    index=username.index(user)
    if pas==password[index]:
        print("welcome",user)
    else:
        print("wrong password")
else:
    print("invalid user")
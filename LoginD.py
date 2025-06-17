dict={'ARAV':'123','SONU':'098','fredy':'456'}
user=input("Enter your username : ")
if user in dict.keys():
    passw=input("Enter your password:")
    if passw==dict[user]:
        print("welcome user",user)
    else:
      print("invalid password")
else:
    print("invalid username")

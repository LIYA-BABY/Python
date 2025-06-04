sea = input("Enter the string :")
level = 0
valley = 0
for i in sea:
    if (i == 'U'):
        level = level + 1
    elif (i == 'D'):
        level = level - 1
    else:
        print("Invalid Character")
    if level == 0 and i == 'U':
        valley += 1
print(valley)






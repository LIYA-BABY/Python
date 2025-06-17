
students={'manju':{'py':20,'so':30,'en':40},'rahul':{'py':30,'so':30,'en':90},'sam':{'py':70,'so':30,'en':50}}
for stud1,markdict in students.items():
    total=0
    for subm in markdict.values():
        total=total+subm
        avg=total/3
    print(f"{stud1} got the totalmarks {total} an average {avg} ")
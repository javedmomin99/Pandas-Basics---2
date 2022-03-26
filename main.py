import pandas as pd
dict1 = {
    "name" : ["harry","rohan","skillf","shubham"],
    "marks" : [92,87,96,90],
    "city":["Rampur","Kolakata","Bareilly","Antarctica"]
    }
df = pd.DataFrame(dict1)
#print(df)
df.to_csv("friends.csv",index=False)
head = df.head(2)
#Gives 1st 2 Values from Top
#print(head)
tail = df.tail(2)
#Gives Last 2 Values from Bottom
#print(tail)

describe = df.describe()
#describe fucntion does analysis automatically of entire data set
#print(describe)
friend = pd.read_csv("friends.csv")
#read csv
#print(javed)

#If I want to get all the names of students, it can be retrieved using the below:
name = friend["name"]
print(name)
#If I want to get only the 1st name of student or at a specific index, it can be retrieved using the below:
first_name = friend["name"][0]
print(first_name)

#If i want to change the value, then it can done using:
friend["name"][0] = "shafi"
print(friend)



#Index can also be understood as:
friend.index = ["first","second","third","fourth"]
friend.to_csv("changed_name.csv")

#data = { "name": [ "Alice", "Bob", "Charlie", "Dave" ], 
#         "age": [20, 18, 19, 20]}

data = {"name":[], "age":[]}

for i in range(3):
    nameVal = input("Name ")
    ageVal = input("Age ")
    data["name"].append(nameVal) 
    data["age"].append(ageVal) 

print(data)
"Read data structures and record for 2 minutes"
"""
Data structures are used to store data in an organised and accessible way. 
A list is a data structure.  Another example of a data structure is a record.  
You might have heard of the word record if you have ever created a database before. 


A record allows you to store a collection of attributes for a single entity.
Data structure: record: An entity can be any object, place, person, or thing. 
Attributes are properties or characteristics of that entity.  
Attributes are sometimes referred to as fields. 

"""


"To Do: Predict, then Run, and then Investigate"
# create a dictionary 
# syntax: dictionary = {"key":"some value"}
dict1 = {"fName":"James Smith", "age":23,"interests":"coding","gamer":True, "fName":"kriyes mahendra"}
# print(dict1)

"Using dictionary methods"
# D.items() -> a set-like object providing a view on D's items
dItems = dict1.items()
# print(dItems)

# D.keys() -> a set-like object providing a view on D's keys
dKeys = dict1.keys()
# print(dKeys)

# D.values() -> an object providing a view on D's values
dValues = dict1.values()
# print(dValues)

"To Do: Task 1: Refer to the example code above to create your own dictionary with key value pairs and explain the differences between the items(), keys() and values() dictionary methods"

# Loop through the keys ansd/values


# "To Do: Task 2: Modify"
# # Modify: The for loop block above to loop through your own the values 

# "To Do: Extension: Can you use the for loop with the items method to loop through the keys and values simultaneously"
# # Modify: The for loop block above to loop through the keys and the values and format your output

# # create a dictionary 
# dict2 = {2:"Python", 3:"HTML", 4:"CSS"}
# print(f"Dictionary 2 {dict2}")


# # Use of the Update method to merge two dictionaries
# ?.update(dict2)
# print(f"Updated dictionary 1\n{dict1}")

# "To Do: Task 2: Research: Look up Pop vs popItem explaind comment the code below to explain the difference"

# # Add comment here to explain the function of th pop() method.
# dict2.pop(3)
# print(dict2)

# # Add comment here to explain the function of th popItem() method.
# ?.popitem()
# print(dict1)


# "Delete key-value pair from dictionary:"
# # We can delete a key-value pair from a dictionary using the del keyword followed
# # by the key value to be deleted enclosed in [].

# del dict1[2]


# # update dictionary value using the key
# dict1[1] = "Emma Smith"
# user={"interests" :"coding"}

# print(user)
# user["interests"] = "Football"

# print(dict1)
# print(user)

print("dictionary with keys but no values")
userDetails1 = {"fname": "", "address": "", "interest":"", "age":""}
# udate dictioanry keys wih values
# userDetails1["fname"] = "Some Name"
# print(userDetails1)
 
# # # Use key to add values to dictionary
 
# userDetails1["fname"] = input("Enter your full name: ")
# userDetails1["address"] = input("Enter your address: ")
# userDetails1["interest"] = input("Enter your interests: ")
# userDetails1["age"] = int(input("Enter age: "))
# print(userDetails1)

# create a dictionary with no keys and no values
# print("dictionary with no keys and no values")
# userDetails2 = {}
# dict1Key = input("Enter a  key:")
# userDetails2[dict1Key] = input(f"Enter value for {dict1Key}: ")

userDetails3 = {}
numOfKeys = 3

for dictItems in range(numOfKeys):
  aKey = input("Enter key: ")
  aValue = input(f"Enter value for key {aKey}:")
  userDetails3[aKey]=aValue

print(userDetails3)

userDetails = {"fullName": "", "address": "", "interest":"", "age":""}

for key in userDetails:
  userDetails[key] = input

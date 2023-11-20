fname    = input("Enter you full name: ")
address   = input("Enter your address: ")
interest = input("Enter your interest: ")
age      =    int(input("Enter your age: "))

"Make"
"To Do: Task 1: Use the code above to ask for user input and then save it to a file called userDetails.txt"

with open('Pt7_FilesDictsCodeBase/1_FileHandling/userDetails.txt', 'a') as userData:
  "method 1"
  # userData.write(fname + " " + address + " " + interest + " " + str(age))

  "method 2"
  # userData.write(f"\n{fname} {address} {interest} {age}")
  
  "method 3"
  someData = f"\n{fname} {address} {interest} {age}"
  userData.write(someData)
  


"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp
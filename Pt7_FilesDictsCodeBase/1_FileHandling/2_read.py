
"To Do: Task 2:Modify the code below to:"
# Read the contents of your file (yourName.txt) by replacing the:
# 1. "w" mode after the file path with the "r"
# 2. the write() method with the read method()
# 3. Unlike the write mode, no argument is required within the parenthesis of the read mode.

"Syntax :  varName = openMethod('pathtofolder/parthtofile//fileName.txt', 'w')"
filePath1 = open('Pt7_FilesDictsCodeBase/1_FileHandling/file1.txt', 'r') # folder/folder/filename

"method 1"
# print(filePath1.read())
"method 2"
# readContents = filePath1.read()
# readContents = filePath1.readline()
# readContents = filePath1.readlines()
readContents = filePath1.readable()
print(readContents)

filePath1.close()


"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html
'''
Q. What is File Handling?
Ans. File handling is an important part of any web application.
	Python has several functions for creating, reading, updating, and deleting files.
	The key function for working with files in Python is the open() function.
	The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''


aruIntro = open("my_intro.json", "r")

print("Line 1: ",aruIntro.readline())
print("Line 2: ",aruIntro.readline())


print(aruIntro.read())



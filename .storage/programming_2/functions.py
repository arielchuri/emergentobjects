# Functions are blocks of code that we can reuse by calling its name.
# Here we are creating a function called "say_hello"
# We define a function with the "def" keyword.
def say_hello():
    # block belonging to the function
    print('hello world')
# End of function

# We can now use the function by "calling" it as below.

say_hello()  # call the function
say_hello()  # call the function again

# ----------------------------------------------

# We can create functions that accept "arguments".
# This function expects a value when it is called.
# Inside the function, it uses the variable "a" to hold the value it was sent.
def sayTheValue(a):
    print(a)

sayTheValue(42) # call the function with an argument.

# ---------------------------------------------

# Global and local variables

# print(a) # This command will not work even though we just printed "a"
# A variable that is inside a function can only be used in that function unless we declare in a "global" variable.

def printGlobalVariable(b):
    global fred
    fred = b
    print(b)

printGlobalVariable("nice")
print("Fred is " + fred +".")
# print(b) # This gives an error because "b" is local to the function.


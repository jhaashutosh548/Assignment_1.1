

# 1. What is the difference between a Mutable datatype and an Immutable data type?
# Mutable data types can be edited i.e., they can change at runtime. Eg – List, Dictionary, etc.
# Immutable data types can not be edited i.e., they can not change at runtime. Eg – String, Tuple, etc.

# 2. How are arguments passed by value or by reference in Python?
# Everything in Python is an object and all variables hold references to the objects. The reference values are according to the functions; as a result, you cannot change the value of the references. However, you can change the objects if it is mutable.

# 3. What is the difference between a Set and Dictionary?
# The set is an unordered collection of data types that is iterable, mutable and has no duplicate elements.
# A dictionary in Python is an unordered collection of data values, used to store data values like a map.

# 4. What is List Comprehension? Give an Example.
# List comprehension is a syntax construction to ease the creation of a list based on existing iterable.

# For Example:

# my_list = [i for i in range(1, 10)]
# 5. What is a lambda function?
# A lambda function is an anonymous function. This function can have any number of parameters but, can have just one statement. For Example:


# a = lambda x, y : x*y
# print(a(7, 19))
# 10. What is a pass in Python?
# Pass means performing no operation or in other words, it is a placeholder in the compound statement, where there should be a blank left and nothing has to be written there.

# 6. What is the difference between / and // in Python?
# // represents floor division whereas / represents precise division. For Example:

# 5//2 = 2
# 5/2 = 2.5
# 7. How is Exceptional handling done in Python?
# There are 3 main keywords i.e. try, except, and finally which are used to catch exceptions and handle the recovering mechanism accordingly. Try is the block of a code that is monitored for errors. Except block gets executed when an error occurs.

# The beauty of the final block is to execute the code after trying for an error. This block gets executed irrespective of whether an error occurred or not. Finally, block is used to do the required cleanup activities of objects/variables.

# 8. What is swapcase function in Python?
# It is a string’s function that converts all uppercase characters into lowercase and vice versa. It is used to alter the existing case of the string. This method creates a copy of the string which contains all the characters in the swap case. For Example:

# string = "GeeksforGeeks"
# string.swapcase() ---> "gEEKSFORgEEKS"
# 9. Difference between for loop and while loop in Python
# The “for” Loop is generally used to iterate through the elements of various collection types such as List, Tuple, Set, and Dictionary. Developers use a “for” loop where they have both the conditions start and the end. Whereas, the “while” loop is the actual looping feature that is used in any other programming language. Programmers use a Python while loop where they just have the end conditions.

# 10. Can we Pass a function as an argument in Python?
# Yes, Several arguments can be passed to a function, including objects, variables (of the same or distinct data types), and functions. Functions can be passed as parameters to other functions because they are objects. Higher-order functions are functions that can take other functions as arguments.

# To read more, refer to the article: Passing function as an argument in Python

# 11. What are *args and *kwargs?
# To pass a variable number of arguments to a function in Python, use the special syntax *args and **kwargs in the function specification. It is used to pass a variable-length, keyword-free argument list. By using the *, the variable we associate with the * becomes iterable, allowing you to do operations on it such as iterating over it and using higher-order operations like map and filter.

# 12. Is Indentation Required in Python?
# Yes, indentation is required in Python. A Python interpreter can be informed that a group of statements belongs to a specific block of code by using Python indentation. Indentations make the code easy to read for developers in all programming languages but in Python, it is very important to indent the code in a specific order.

# 13. What is Scope in Python?
# The location where we can find a variable and also access it if required is called the scope of a variable.

# Python Local variable: Local variables are those that are initialized within a function and are unique to that function. It cannot be accessed outside of the function.
# Python Global variables: Global variables are the ones that are defined and declared outside any function and are not specified to any function.
# Module-level scope: It refers to the global objects of the current module accessible in the program.
# Outermost scope: It refers to any built-in names that the program can call. The name referenced is located last among the objects in this scope.
# 14. What is docstring in Python?
# Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods.

# Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or “””triple double quotes””” just below the class, method, or function declaration. All functions should have a docstring.
# Accessing Docstrings: The docstrings can be accessed using the __doc__ method of the object or using the help function.
# 15. What is a dynamically typed language?
# Typed languages are the languages in which we define the type of data type and it will be known by the machine at the compile-time or at runtime. Typed languages can be classified into two categories:

# Statically typed languages: In this type of language, the data type of a variable is known at the compile time which means the programmer has to specify the data type of a variable at the time of its declaration. 
# Dynamically typed languages: These are the languages that do not require any pre-defined data type for any variable as it is interpreted at runtime by the machine itself. In these languages, interpreters assign the data type to a variable at runtime depending on its value.

# 16. What is a break, continue, and pass in Python? 
# The break statement is used to terminate the loop or statement in which it is present. After that, the control will pass to the statements that are present after the break statement, if available.

# Continue is also a loop control statement just like the break statement. continue statement is opposite to that of the break statement, instead of terminating the loop, it forces to execute the next iteration of the loop.

# Pass means performing no operation or in other words, it is a placeholder in the compound statement, where there should be a blank left and nothing has to be written there.

# 17. What are Built-in data types in Python?
# The following are the standard or built-in data types in Python:

# Numeric: The numeric data type in Python represents the data that has a numeric value. A numeric value can be an integer, a floating number, a Boolean, or even a complex number.
# Sequence Type: The sequence Data Type in Python is the ordered collection of similar or different data types. There are several sequence types in Python:
# Python String
# Python List
# Python Tuple
# Python range
# Mapping Types: In Python, hashable data can be mapped to random objects using a mapping object. There is currently only one common mapping type, the dictionary, and mapping objects are mutable.
# Python Dictionary
# Set Types: In Python, a Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.
# 18. How do you floor a number in Python?
# The Python math module includes a method that can be used to calculate the floor of a number. 

# floor() method in Python returns the floor of x i.e., the largest integer not greater than x. 
# Also, The method ceil(x) in Python returns a ceiling value of x i.e., the smallest integer greater than or equal to x.
 
# 19. What is the difference between xrange and range functions?
# range() and xrange() are two functions that could be used to iterate a certain number of times in for loops in Python. In Python 3, there is no xrange, but the range function behaves like xrange in Python 2.

# range() – This returns a list of numbers created using the range() function.
# xrange() – This function returns the generator object that can be used to display numbers only by looping. The only particular range is displayed on demand and hence called lazy evaluation.
# 20. What is Dictionary Comprehension? Give an Example
# Dictionary Comprehension is a syntax construction to ease the creation of a dictionary based on the existing iterable.

# For Example: my_dict = {i:1+7 for i in range(1, 10)}
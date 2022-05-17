# capitalize()	Converts the first character to upper case

x = 'rohan'
print(x.capitalize())

# casefold()	Converts string into lower case

x = 'ROHAN'
print(x.casefold())

# center()	Returns a centered string

x = 'ROHAN'
print(x.center(10))

# count()	Returns the number of times a specified value occurs in a string

x = 'ROHAN PARMAR'
print(x.count('A'))

# encode()	Returns an encoded version of the string

x = 'ROHAN PARMAR'
print(x.encode())

# endswith()	Returns true if the string ends with the specified value

x = 'ROHAN'
print(x.endswith('N'))

# expandtabs()	Sets the tab size of the string

x = 'R\tO\tH\tA\tN'
print(x.expandtabs(5))

# find()	Searches the string for a specified value and returns the position of where it was found

x = 'ROHAN'
print(x.find('H'))

# format()	Formats specified values in a string

x = 'Rohan: {er}'.format(er=44)
print(x)
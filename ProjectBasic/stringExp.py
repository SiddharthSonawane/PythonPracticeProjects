# changing case of string using string methods - title()

name = "siddharth sonawane"
print(name.title())          # this will change title of all words i.e first letter of all words to uppercase

name2 = "machine learning using python"
print(name2.title())

name3 = "hello programming world"
print(name3.title())

# changing words to lower and uppercase

nameLow = "SIDDHARTH SONAWANE"
print(nameLow.lower())
print(nameLow.upper())

# concate or combine strings
firstName = "Siddharth"
lastName = "Sonawane"
fullName = firstName + " " + lastName
print(fullName)

print("Hello," + fullName.title() + "!")
print("how are you " + firstName + "?")

# OR
msg = "Hello," + fullName.title() + "!"
print(msg)


# to add newline use \n and for tab \t

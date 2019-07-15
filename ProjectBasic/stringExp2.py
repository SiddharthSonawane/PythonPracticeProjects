# to remove whitespaces from strings

fav_lang = "python "  # here we have space after python word,which is useless
print(fav_lang)
print(fav_lang.rstrip())
print(len(fav_lang))  # whitespace cannot be seen in output so length is printed
print(len(fav_lang.rstrip()))
print(len(fav_lang))   # rstip method does not remove whitespace permanently
# to store stripped value ,we need to store stripped value again in string
# variable
fav_lang = fav_lang.rstrip()
print(len(fav_lang))
print(fav_lang)
# You can also strip whitespace from the left side of a string using the
# lstrip() method or strip whitespace from both sides at once using strip()

lang = " python "
print(lang.lstrip())
print(lang.strip())

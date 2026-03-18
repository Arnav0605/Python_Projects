my_string = "Hello"
result = my_string.isalpha()  # Returns True

my_string = "hello"
result = my_string.islower()  # Returns True

my_string = "HELLO"
result = my_string.isupper()  # Returns True

my_string = "Hello World"
result = my_string.istitle()  # Returns True

my_string = "   "
result = my_string.isspace()  # Returns True

my_string = "Hello"
result = my_string.isprintable()  # Returns True

my_string = "my_variable"
result = my_string.isidentifier()  # Returns True

my_string = "12345"
result = my_string.isdigit()  # Returns True

my_string = "12.34"
result = my_string.replace('.', '', 1).isdigit() and my_string.count('.') < 2  # Returns True only for valid decimals

my_string = "⅔"  # This includes fraction
result = my_string.isnumeric()  # Returns True

my_string = "Hello"
result = all(ord(char) < 128 for char in my_string)  # Returns True


my_string = "Hello123"
result = my_string.isalnum()  # Returns True
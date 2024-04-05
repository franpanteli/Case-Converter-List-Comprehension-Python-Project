"""
	-> This is the same function as in the first .py file for this project, 
        but just with a list comprehension (rather than a for loop)
	-> The argument to this function is the same as the previous one <- a 
        string in Pascal or Camel case 
	-> We want to convert this to Snake case (as per the name of the function)
	-> This .py file is doing this with list comprehension, rather than a for loop 
	-> The final def main() section of this code is the same as with the previous 
        .py file 
	-> The name of the first function is the same, but its content is different 
	-> This contains a list comprehension which constructs the same list as the for 
        loop in the previous function <- The other .py file as part of this project 
        (with-list-comprehension.py)
	-> Add _ and make the element lowercase if it's uppercase 
	-> 'Element' being character in the input string 
	-> Otherwise, leave it alone 
	-> Do this for each of the characters in the string which is in the argument of the 
        function 
	-> Return this, but without the underscores and in a string (rather than a list)
	-> Then execute the rest of the code in the same way as in the previous project .py 
        file
"""

def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))
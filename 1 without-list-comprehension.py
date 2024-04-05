"""
	-> This function is for the project, without using list comprehension 
	-> The argument is a string in camel or pascal case 
	-> We want to return this in snake case 
	-> So we first define an empty list for this 
	-> We are then iterating through each letter in the input string 
	-> If it's uppercase, then convert it to lowercase 
	-> Then add it to the snake_cased_char_list
	-> Otherwise, add the character to the snake_cased_char_list 
	-> In the 'otherwise' case, we don't need to do anything to the character - because it's already 
        lowercase
	-> Then we take the elements in the list we just created and make them into a string which we store 
        in the `snake_cased_string` variable, and strip the underscores from this in the 
        `clean_snake_cased_string` variable, which the function then returns  
	-> Then we call the function in the `main` section of the code <- provided that this .py file is the 
        main one (not a file which we are defining Python modules in)   
"""

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string
def main():
    print(convert_to_snake_case('aLongAndComplexString'))

if __name__ == '__main__':
    main()
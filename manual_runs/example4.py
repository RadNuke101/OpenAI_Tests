# Function to delete the first "/" and the next two numbers after
def delete_first_slash(input):
    # Get the index of the first "/" in the string
    first_slash_index = input.index("/")
    
    # Get the string after deleting the first "/"
    output = input[(first_slash_index + 1):]
    
    # Get the index of the first "/" after deleting the first "/"
    second_slash_index = output.index("/")
    
    # Get the string after deleting the next two numbers after the first "/"
    output = output[:second_slash_index - 2] + output[second_slash_index + 1:]
    
    return output
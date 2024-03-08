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

# Get inputs from user
input1 = input("Enter input 1: ")
input2 = input("Enter input 2: ")
input3 = input("Enter input 3: ")

# Call delete_first_slash function for each input and print the output
print(delete_first_slash(input1))
print(delete_first_slash(input2))
print(delete_first_slash(input3))
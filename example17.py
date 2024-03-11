# Define function to return letters after last "/"
def get_letters_after_last_slash(input_string):
    # Split input string by "/"
    split_string = input_string.split("/")
    # Get last element of split string
    last_element = split_string[-1]
    # Return letters after last "/"
    return last_element
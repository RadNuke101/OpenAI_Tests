# Define function to return text before last 3 numbers
def return_text(input):
    # Get index of last 3 numbers
    index = len(input) - 3
    # Return text before last 3 numbers
    return input[:index]
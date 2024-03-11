# Function to remove all instances of "<" and ">" from a string
def remove_tags(string):
    # Initialize an empty string to store the output
    output = ""
    # Loop through each character in the input string
    for char in string:
        # Check if the character is not "<" or ">"
        if char != "<" and char != ">":
            # Add the character to the output string
            output += char
    # Return the output string
    return output
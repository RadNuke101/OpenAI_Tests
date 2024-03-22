# Prompt: delete everything enclosed by a pair of "/"
# Input: ['This is a line. /delete words in the area /keep this part']
# Output: This is a line. keep this part

def delete_enclosed(input_str):
    output = ""
    within_slashes = False

    for char in input_str:
        if char == '/':
            within_slashes = not within_slashes
        elif not within_slashes:
            output += char

    return output

# Test cases
print(delete_enclosed('This is a line. /delete words in the area /keep this part'))  # Output: This is a line. keep this part
print(delete_enclosed('/delete words in the area /'))  # Output: 

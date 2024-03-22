# Prompt: delete everything enclosed by a pair of "/"
# Input: ['This is a line. /delete words in the area /keep this part']
# Output: This is a line. keep this part

def delete_enclosed(input_str):
    start = input_str.find('/')
    while start != -1:
        end = input_str.find('/', start + 1)
        if end != -1:
            input_str = input_str[:start] + input_str[end + 1:]
        start = input_str.find('/', start + 1)
    return input_str

# Test cases
print(delete_enclosed('This is a line. /delete words in the area /keep this part'))  # Output: This is a line. keep this part
print(delete_enclosed('/delete words in the area /'))  # Output: 

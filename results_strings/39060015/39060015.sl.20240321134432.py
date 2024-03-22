def delete_enclosed(input_str):
    start = input_str.find('/')
    end = input_str.find('/', start + 1)
    
    while start != -1 and end != -1:
        input_str = input_str[:start] + input_str[end + 1:]
        start = input_str.find('/')
        end = input_str.find('/', start + 1)
    
    return input_str

# Prompt: delete everything enclosed by a pair of "/"
# Input: ['This is a line. /delete words in the area /keep this part']
# Output: This is a line. keep this part

# Input: ['/delete words in the area /']
# Output: 

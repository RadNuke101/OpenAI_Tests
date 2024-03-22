def delete_enclosed(input_str):
    start = input_str.find('/')
    while start != -1:
        end = input_str.find('/', start + 1)
        if end != -1:
            input_str = input_str[:start] + input_str[end + 1:]
        start = input_str.find('/', start + 1)
    return input_str

# Prompt: delete everything enclosed by a pair of "/"
# Input: ['This is a line. /delete words in the area /keep this part']
# Output: This is a line. keep this part

# Input: ['/delete words in the area /']
# Output: 

input_str1 = 'This is a line. /delete words in the area /keep this part'
input_str2 = '/delete words in the area /'

output_str1 = delete_enclosed(input_str1)
output_str2 = delete_enclosed(input_str2)

print(output_str1)
print(output_str2)

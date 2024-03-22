# Prompt: return everything before the fifth occurance of "=" from the right of input
# Input: 'valentine day=1915=50==7.1=45'
# Output: 'valentine day'

def return_before_fifth_equal(input_str):
    count = 0
    index = len(input_str) - 1
    
    while index >= 0:
        if input_str[index] == '=':
            count += 1
            if count == 5:
                break
        index -= 1
    
    return input_str[:index]

# Test the function with the provided inputs
input1 = 'valentine day=1915=50==7.1=45'
output1 = return_before_fifth_equal(input1)
print(output1)  # Output: 'valentine day'

input2 = 'movie blah=2blahblah, The=1914=54==7.9=17'
output2 = return_before_fifth_equal(input2)
print(output2)  # Output: 'movie blah=2blahblah, The'

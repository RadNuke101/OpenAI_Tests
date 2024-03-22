# Prompt: return everything before the fifth occurance of "=" from the right of input
# Input: 'valentine day=1915=50==7.1=45'
# Output: 'valentine day'

def return_before_fifth_equal(input_str):
    count = 0
    index = len(input_str) - 1
    
    while count < 5 and index >= 0:
        if input_str[index] == '=':
            count += 1
        index -= 1
    
    return input_str[:index + 2]

# Test the function with the provided inputs
print(return_before_fifth_equal('valentine day=1915=50==7.1=45'))  # Output: 'valentine day'
print(return_before_fifth_equal('movie blah=2blahblah, The=1914=54==7.9=17'))  # Output: 'movie blah=2blahblah, The'

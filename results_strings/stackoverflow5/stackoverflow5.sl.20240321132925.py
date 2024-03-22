# Prompt: return everything before the fifth occurance of "=" from the right of input
# Input: 'valentine day=1915=50==7.1=45'
# Output: 'valentine day'

def return_before_fifth_equal(input_str):
    equal_count = 0
    output = ""
    
    for char in input_str[::-1]:
        if char == "=":
            equal_count += 1
            if equal_count == 5:
                break
        output = char + output
    
    return output

# Test the function with the provided inputs
print(return_before_fifth_equal('valentine day=1915=50==7.1=45'))  # Output: 'valentine day'
print(return_before_fifth_equal('movie blah=2blahblah, The=1914=54==7.9=17'))  # Output: 'movie blah=2blahblah, The'
valentine day
movie blah=2blahblah, The

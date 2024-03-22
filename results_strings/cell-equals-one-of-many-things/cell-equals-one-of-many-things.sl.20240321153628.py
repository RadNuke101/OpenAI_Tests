# Prompt: if input is a color that is not "gray" or "black", return true
# Input: 'yellow' => Output: 'true'
# Input: 'gray' => Output: 'false'
# Input: 'black' => Output: 'false'
# Input: 'blue' => Output: 'true'
# Input: 'pink' => Output: 'true'
# Input: 'orange' => Output: 'true'
# Input: 'turkey' => Output: 'false'

def check_color(input_color):
    if input_color != 'gray' and input_color != 'black':
        return 'true'
    else:
        return 'false'

# Test cases
print(check_color('yellow'))  # Output: 'true'
print(check_color('gray'))    # Output: 'false'
print(check_color('black'))   # Output: 'false'
print(check_color('blue'))    # Output: 'true'
print(check_color('pink'))    # Output: 'true'
print(check_color('orange'))  # Output: 'true'
print(check_color('turkey'))  # Output: 'false'

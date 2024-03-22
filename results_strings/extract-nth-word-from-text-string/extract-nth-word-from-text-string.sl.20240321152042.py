# Prompt: return the nth word in the inputted expression, with n being the second input
# Input: ['you can do anything but you cant do everything.', '4']
# Output: anything

def return_nth_word(input_list):
    input_str = input_list[0]
    n = int(input_list[1])
    
    words = input_str.split()
    
    if n <= len(words):
        return words[n-1]
    else:
        return "Invalid input"

# Test cases
print(return_nth_word(['you can do anything but you cant do everything.', '4']))  # Output: anything
print(return_nth_word(['you can do anything but you cant do everything.', '1']))  # Output: you
print(return_nth_word(['you can do anything but you cant do everything.', '2']))  # Output: can
print(return_nth_word(['you can do anything but you cant do everything.', '3']))  # Output: do

# Prompt: return the first word of the input followed by a space, and if there is a 1 in the input return "apple", if there is a 2 in the input return "bananas", if there is a 3 in the input return "strawberries", if there is a 4 in the input return "oranges"
# Input: ['one, 1']
# Output: one apple

def process_input(input_str):
    input_list = input_str.split(', ')
    first_word = input_list[0]
    number = int(input_list[1])

    if number == 1:
        return first_word + ' apple'
    elif number == 2:
        return first_word + ' bananas'
    elif number == 3:
        return first_word + ' strawberries'
    elif number == 4:
        return first_word + ' oranges'

# Test cases
print(process_input('one, 1'))  # Output: one apple
print(process_input('two, 2'))  # Output: two bananas
print(process_input('three, 3'))  # Output: three strawberries
print(process_input('four, 4'))  # Output: four oranges

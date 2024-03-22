# Input: ['one, 1']
# Output: one apple
def process_input(input):
    input_str = input[0]
    words = input_str.split(',')
    first_word = words[0]
    num = int(words[1].strip())
    
    if num == 1:
        return first_word + " apple"
    elif num == 2:
        return first_word + " bananas"
    elif num == 3:
        return first_word + " strawberries"
    elif num == 4:
        return first_word + " oranges"

# Test cases
print(process_input(['one, 1']))  # Output: one apple
print(process_input(['two, 2']))  # Output: two bananas
print(process_input(['three, 3']))  # Output: three strawberries
print(process_input(['four, 4']))  # Output: four oranges

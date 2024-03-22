def return_second_word(input_list):
    return [phrase[1] for phrase in input_list]

# Test the function with the provided input
input_list = [['Park Kim'], ['Lee Kim'], ['Kim Lee']]
output = return_second_word(input_list)
print(output)

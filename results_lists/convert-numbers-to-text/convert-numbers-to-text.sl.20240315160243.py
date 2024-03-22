def return_input(input_list):
    return [item[0] for item in input_list]

# Test the function with the provided input
input_list = [['101'], ['1002'], ['743']]
output = return_input(input_list)
print(output)

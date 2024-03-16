def return_last_word(input_list):
    return [item[0].split()[-1] for item in input_list]

# Test the function with the provided input
input_list = [['Sarah Jane Jones'], ['Bob Jane Smithfield']]
output = return_last_word(input_list)
print(output)

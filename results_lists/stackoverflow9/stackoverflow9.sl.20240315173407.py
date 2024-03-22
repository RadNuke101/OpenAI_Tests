def return_last_word(input_list):
    return [item[0].split()[-1] for item in input_list]

# Test the function
input_list = [['Sarah Jane Jones'], ['Bob Jane Smithfield']]
print(return_last_word(input_list))  # Output: ['Jones', 'Smithfield']

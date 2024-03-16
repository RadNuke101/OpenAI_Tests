def clean_phone_numbers(input_list):
    output_list = []
    for sublist in input_list:
        for phone_number in sublist:
            cleaned_number = ''.join(char for char in phone_number if char not in ['-', '<', '>', '.', ' '])
            output_list.append(cleaned_number)
    return output_list

# Test the function with the provided input
input_list = [['801-456-8765'], ['<978> 654-0299'], ['978.654.0299']]
output = clean_phone_numbers(input_list)
print(output)

def clean_phone_numbers(input_list):
    output_list = []
    for phone_number in input_list:
        clean_number = ''.join(char for char in phone_number[0] if char not in ['-', '<', '>', '.', ' '])
        output_list.append(clean_number)
    return output_list

input_list = [['801-456-8765'], ['<978> 654-0299'], ['978.654.0299']]
output = clean_phone_numbers(input_list)
print(output)

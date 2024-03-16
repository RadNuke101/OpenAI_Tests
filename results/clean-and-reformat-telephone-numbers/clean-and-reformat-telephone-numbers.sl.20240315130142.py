def clean_phone_numbers(input_list):
    output_list = []
    for sublist in input_list:
        phone_number = ''.join(filter(lambda x: x.isdigit(), sublist[0]))
        output_list.append(phone_number)
    return output_list

# Test the function with the provided input
input_list = [['801-456-8765'], ['<978> 654-0299'], ['978.654.0299']]
output = clean_phone_numbers(input_list)
print(output)

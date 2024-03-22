def extract_numbers(input_list):
    output_list = []
    for item in input_list:
        for word in item:
            for char in word:
                if char.isdigit():
                    output_list.append(''.join(filter(str.isdigit, char)))
    return output_list

input_list = [['100 apples'], ['the price is %500 dollars'], ['serial number %003399']]
output = extract_numbers(input_list)
print(output)

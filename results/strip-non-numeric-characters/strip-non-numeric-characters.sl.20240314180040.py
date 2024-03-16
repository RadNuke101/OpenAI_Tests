def return_number_from_input(input_list):
    output_list = []
    for item in input_list:
        for word in item[0].split():
            if word.isdigit():
                output_list.append(word)
            elif word.startswith('%') and word[1:].isdigit():
                output_list.append(word[1:])
    return output_list

# Test the function
input_list = [['100 apples'], ['the price is %500 dollars'], ['serial number %003399']]
print(return_number_from_input(input_list))

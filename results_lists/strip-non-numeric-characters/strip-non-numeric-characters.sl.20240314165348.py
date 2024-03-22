def extract_numbers(input_list):
    output = []
    for item in input_list:
        for word in item[0].split():
            if word.isdigit():
                output.append(word)
            elif word.startswith('%') and word[1:].isdigit():
                output.append(word[1:])
    return output

input_list = [['100 apples'], ['the price is %500 dollars'], ['serial number %003399']]
output = extract_numbers(input_list)
print(output)

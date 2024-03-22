def extract_numbers(input_list):
    output = []
    for item in input_list:
        for word in item:
            for char in word:
                if char.isdigit():
                    output.append(''.join(filter(str.isdigit, word)))
                    break
    return output

input_list = [['100 apples'], ['the price is %500 dollars'], ['serial number %003399']]
output = extract_numbers(input_list)
print(output)

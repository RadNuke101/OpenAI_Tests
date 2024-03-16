def extract_numbers(input_list):
    output = []
    for item in input_list:
        for word in item:
            for char in word:
                if char.isdigit():
                    output.append(word.split()[-1])
                    break
    return output

input_list = [['100 apples'], ['the price is %500 dollars'], ['serial number %003399']]
print(extract_numbers(input_list))

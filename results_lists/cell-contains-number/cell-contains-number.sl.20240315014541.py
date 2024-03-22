def check_number_presence(input_list):
    output = []
    for item in input_list:
        if any(char.isdigit() for char in item[0]):
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['A bird in the hand is worth 2 in the bush.'], ['A bird in the hand is worth two in the bush.'], ['The 15 shortcuts you simply must know']]
print(check_number_presence(input_list))

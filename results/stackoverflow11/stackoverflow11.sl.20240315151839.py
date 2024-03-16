def return_after_underscore(input_list):
    output_list = []
    for item in input_list:
        for string in item:
            index = string.find('_')
            if index != -1:
                output_list.append(string[index+1:])
    return output_list

input_list = [['2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'], ['44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'], ['PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA']]
output = return_after_underscore(input_list)
print(output)

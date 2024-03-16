def process_input(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].replace('<', ' ').replace('>', ' ').replace(',', ' '))
    return output_list

input_list = [['R/V<208,0,32>'], ['R/S<184,28,16>'], ['R/B<255,88,80>']]
output = process_input(input_list)
print(output)

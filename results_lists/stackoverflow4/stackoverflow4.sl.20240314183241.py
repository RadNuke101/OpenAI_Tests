def process_input(input_list):
    output_list = []
    for item in input_list:
        processed_item = item[0].replace('<', ' ').replace('>', ' ').replace(',', ' ')
        output_list.append(processed_item)
    return output_list

input_list = [['R/V<208,0,32>'], ['R/S<184,28,16>'], ['R/B<255,88,80>']]
print(process_input(input_list))

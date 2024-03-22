def process_input(input_list):
    output_list = []
    for item in input_list:
        processed_item = item[0].replace('+', '').replace('-', '.').replace(' ', '.')
        output_list.append(processed_item)
    return output_list

input_list = [['+106 769-858-438'], ['+83 973-757-831'], ['+62 647-787-775'], ['+172 027-507-632'], ['+72 001-050-856'], ['+95 310-537-401'], ['+6 775-969-238']]
output = process_input(input_list)
print(output)

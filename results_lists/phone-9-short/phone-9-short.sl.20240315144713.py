def process_input(input_data):
    output = []
    for item in input_data:
        num_str = item[0].replace('+', '').replace('-', '.').replace(' ', '')
        output.append(num_str)
    return output

input_data = [['+106 769-858-438'], ['+83 973-757-831'], ['+62 647-787-775'], ['+172 027-507-632'], ['+72 001-050-856'], ['+95 310-537-401'], ['+6 775-969-238']]
output = process_input(input_data)
print(output)

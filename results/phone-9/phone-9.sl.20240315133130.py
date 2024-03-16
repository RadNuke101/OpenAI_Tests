def process_phone_numbers(input_data):
    output = []
    for item in input_data:
        phone_number = item[0].replace("+", "").replace("-", ".").replace(" ", ".")
        output.append(phone_number)
    return output

input_data = [['+106 769-858-438'], ['+83 973-757-831'], ['+62 647-787-775'], ['+172 027-507-632'], ['+72 001-050-856'], ['+95 310-537-401'], ['+6 775-969-238']]
output = process_phone_numbers(input_data)
print(output)
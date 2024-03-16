def format_phone_numbers(input_list):
    output_list = []
    for item in input_list:
        phone_number = item[0]
        first_three_numbers = phone_number[:3]
        rest_of_number = phone_number[4:]
        formatted_number = f"{phone_number[0]} ({first_three_numbers}) {rest_of_number}"
        output_list.append(formatted_number)
    return output_list

input_list = [['+106 769-858-438'], ['+83 973-757-831'], ['+62 647-787-775'], ['+172 027-507-632'], ['+72 001-050-856'], ['+95 310-537-401'], ['+6 775-969-238']]
output = format_phone_numbers(input_list)
print(output)

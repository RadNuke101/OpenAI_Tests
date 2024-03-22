def format_phone_numbers(input_list):
    output_list = []
    for item in input_list:
        phone_number = item[0]
        first_dash_index = phone_number.index('-')
        formatted_number = phone_number[:first_dash_index].replace('-', ' ') + ' (' + phone_number[first_dash_index+1:first_dash_index+4] + ') ' + phone_number[first_dash_index+5:]
        output_list.append(formatted_number)
    return output_list

input_list = [['+106 769-858-438'], ['+83 973-757-831'], ['+62 647-787-775'], ['+172 027-507-632'], ['+72 001-050-856'], ['+95 310-537-401'], ['+6 775-969-238']]
output_list = format_phone_numbers(input_list)
print(output_list)

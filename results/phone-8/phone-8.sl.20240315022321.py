def return_last_three_numbers(input_list):
    output = []
    for sublist in input_list:
        number = sublist[0][-3:]
        output.append(number)
    return output

input_list = [['+106 769-858-438'], ['+83 973-757-831'], ['+62 647-787-775'], ['+172 027-507-632'], ['+72 001-050-856'], ['+95 310-537-401'], ['+6 775-969-238']]
output = return_last_three_numbers(input_list)
print(output)

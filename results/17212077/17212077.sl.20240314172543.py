def delete_numbers(input_list):
    output_list = []
    for date in input_list:
        date_str = date[0]
        slash_index = date_str.index('/')
        new_date = date_str[:slash_index] + date_str[slash_index+4:]
        output_list.append(new_date)
    return output_list

input_list = [['01/15/2013'], ['03/07/2011'], ['05/09/2009']]
print(delete_numbers(input_list))

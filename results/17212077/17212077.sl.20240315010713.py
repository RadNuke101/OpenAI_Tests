def delete_numbers(input_list):
    output_list = []
    for date in input_list:
        date_str = date[0]
        first_slash_index = date_str.index('/')
        new_date_str = date_str[:first_slash_index] + date_str[first_slash_index + 4:]
        output_list.append(new_date_str)
    return output_list

input_list = [['01/15/2013'], ['03/07/2011'], ['05/09/2009']]
print(delete_numbers(input_list))

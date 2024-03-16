def add_newline(input_list):
    output_list = []
    for entry in input_list:
        output_list.append('/n'.join(entry))
    return output_list

input_list = [['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607'], ['Mary Hannan', '1195 Amethyst Drive', 'Lansing, MI 48933'], ['Linda Thomas', '2479 North Bend Road', 'Allen, KY 41601']]
print(add_newline(input_list))

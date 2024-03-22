def add_newline(input_list):
    output_list = []
    for item in input_list:
        output_list.append('/n'.join(item))
    return output_list

input_list = [['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607'], ['Mary Hannan', '1195 Amethyst Drive', 'Lansing, MI 48933'], ['Linda Thomas', '2479 North Bend Road', 'Allen, KY 41601']]
output_list = add_newline(input_list)
print(output_list)

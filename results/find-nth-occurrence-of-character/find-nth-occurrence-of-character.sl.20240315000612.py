def find_position(input_list):
    output = []
    for item in input_list:
        text = item[0]
        num = int(item[1])
        if num == 1:
            output.append(str(text.index('_') + 1))
        elif num == 2:
            first_underscore = text.index('_')
            output.append(str(text.index('_', first_underscore + 1) + 1))
        elif num == 3:
            first_underscore = text.index('_')
            second_underscore = text.index('_', first_underscore + 1)
            output.append(str(text.index('_', second_underscore + 1) + 1))
    return output

input_list = [['replies to _aya, _tasisuke, and _chan', '1'], ['replies to _aya, _tasisuke, and _chan', '2'], ['replies to _aya, _tasisuke, and _chan', '3']]
print(find_position(input_list))

def find_position(input_list):
    output = []
    for item in input_list:
        sentence = item[0]
        position = int(item[1])
        if position == 1:
            output.append(str(sentence.find('_') + 1))
        elif position == 2:
            output.append(str(sentence.find('_', sentence.find('_') + 1) + 1))
        elif position == 3:
            output.append(str(sentence.rfind('_') + 1))
    return output

input_list = [['replies to _aya, _tasisuke, and _chan', '1'], ['replies to _aya, _tasisuke, and _chan', '2'], ['replies to _aya, _tasisuke, and _chan', '3']]
print(find_position(input_list))

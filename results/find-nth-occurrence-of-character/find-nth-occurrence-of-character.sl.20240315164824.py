def find_position(input_list):
    output = []
    for item in input_list:
        text = item[0]
        num = int(item[1])
        positions = [pos for pos, char in enumerate(text) if char == '_']
        if num <= len(positions):
            output.append(str(positions[num-1]))
    return output

input_list = [['replies to _aya, _tasisuke, and _chan', '1'], ['replies to _aya, _tasisuke, and _chan', '2'], ['replies to _aya, _tasisuke, and _chan', '3']]
print(find_position(input_list))

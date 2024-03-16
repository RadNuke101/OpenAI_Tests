def extract_text(input_list):
    output_list = []
    for item in input_list:
        text = item[0]
        start_index = text.find("<") + 1
        end_index = text.find(">")
        output_list.append(text[start_index:end_index])
    return output_list

input_list = [['Jones <60>'], ['Jones <57>'], ['Jones <55>']]
print(extract_text(input_list))

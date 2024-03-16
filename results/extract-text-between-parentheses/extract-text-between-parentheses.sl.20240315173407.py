def extract_text(input_list):
    output_list = []
    for item in input_list:
        text = item[0]
        start_index = text.find("<") + 1
        end_index = text.find(">")
        extracted_text = text[start_index:end_index]
        output_list.append(extracted_text)
    return output_list

input_list = [['Jones <60>'], ['Jones <57>'], ['Jones <55>']]
output = extract_text(input_list)
print(output)

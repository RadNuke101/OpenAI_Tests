def extract_text_between_brackets(input_list):
    output_list = []
    for item in input_list:
        text = item[0]
        start = text.find("<")
        end = text.find(">")
        output_list.append(text[start+1:end])
    return output_list

input_list = [['Jones <60>'], ['Jones <57>'], ['Jones <55>']]
output = extract_text_between_brackets(input_list)
print(output)

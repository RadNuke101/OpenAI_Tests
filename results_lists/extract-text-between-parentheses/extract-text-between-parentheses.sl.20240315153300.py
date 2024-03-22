def extract_text(input_list):
    output = []
    for item in input_list:
        text = item[0]
        start = text.find("<") + 1
        end = text.find(">")
        output.append(text[start:end])
    return output

input_list = [['Jones <60>'], ['Jones <57>'], ['Jones <55>']]
print(extract_text(input_list))

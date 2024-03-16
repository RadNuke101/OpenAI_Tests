def get_text_after_last_equal(input_list):
    output = []
    for item in input_list:
        text = item[0]
        output.append(text.split('=')[-1].strip())
    return output

input_list = [['Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'], ['Dec 2, 2014, 11=24 PM - +91 90000 80000= loren']]
print(get_text_after_last_equal(input_list))

def extract_date_time(input_list):
    output_list = []
    for item in input_list:
        date_time = item[0].split(' - ')[0]
        output_list.append(date_time)
    return output_list

input_list = [['Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'], ['Dec 2, 2014, 11=24 PM - +91 90000 80000= loren']]
output = extract_date_time(input_list)
print(output)

def extract_date_time(input_data):
    output = []
    for item in input_data:
        date_time = item[0].split(' - ')[0]
        output.append(date_time)
    return output

input_data = [['Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'], ['Dec 2, 2014, 11=24 PM - +91 90000 80000= loren']]
print(extract_date_time(input_data))

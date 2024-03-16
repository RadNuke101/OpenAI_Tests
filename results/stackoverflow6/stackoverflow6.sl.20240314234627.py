def get_last_after_equal(input):
    output = []
    for item in input:
        last_equal_index = item[0].rfind("=")
        output.append(item[0][last_equal_index+1:])
    return output

input = [['Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'], ['Dec 2, 2014, 11=24 PM - +91 90000 80000= loren']]
print(get_last_after_equal(input))

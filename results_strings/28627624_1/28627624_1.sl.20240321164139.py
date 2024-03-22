# Prompt: return date and time
# Input: 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
# Output: 'Dec 2, 2014, 11=23 PM'

def extract_date_time(input_str):
    parts = input_str.split(' - ')
    date_time = parts[0]
    return date_time

# Test cases
input1 = 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
output1 = extract_date_time(input1)
print(output1)  # Output: Dec 2, 2014, 11=23 PM

input2 = 'Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'
output2 = extract_date_time(input2)
print(output2)  # Output: Dec 2, 2014, 11=24 PM

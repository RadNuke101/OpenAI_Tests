# Prompt: return date and time
# Input: 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
# Output: 'Dec 2, 2014, 11=23 PM'

def extract_date_time(input_str):
    parts = input_str.split(' - ')
    date_time = parts[0]
    return date_time

# Test cases
print(extract_date_time('Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'))  # Output: 'Dec 2, 2014, 11=23 PM'
print(extract_date_time('Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'))  # Output: 'Dec 2, 2014, 11=24 PM'

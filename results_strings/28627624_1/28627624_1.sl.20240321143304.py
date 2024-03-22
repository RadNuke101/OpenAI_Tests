# Prompt: return date and time
# Input: 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
# Output: 'Dec 2, 2014, 11=23 PM'

def extract_date_time(input_str):
    # Split the input string by the delimiter '-'
    parts = input_str.split('-')
    
    # Extract the date and time from the first part
    date_time = parts[0].strip()
    
    return date_time

# Test cases
print(extract_date_time('Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'))  # Output: 'Dec 2, 2014, 11=23 PM'
print(extract_date_time('Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'))  # Output: 'Dec 2, 2014, 11=24 PM'

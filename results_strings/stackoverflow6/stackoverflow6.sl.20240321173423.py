# Prompt: return everything after the last "=" in input
# Input: 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
# Output: 'loren ipsum'

def get_text_after_last_equal(input_str):
    parts = input_str.split("=")
    if len(parts) > 1:
        return parts[-1]
    else:
        return ""

# Test cases
print(get_text_after_last_equal('Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'))  # Output: 'loren ipsum'
print(get_text_after_last_equal('Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'))  # Output: 'loren'

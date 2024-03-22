# Prompt: return the sequence of 4 numbers (excluding spaces) from input
# Input: ['April 1 1799'], Output: 1799
# Input: ['April 11 1867'], Output: 1867
# Input: ['February 12 1806'], Output: 1806

def extract_year(input_str):
    for word in input_str.split():
        if word.isdigit() and len(word) == 4:
            return word

# Test cases
print(extract_year('April 1 1799'))  # Output: 1799
print(extract_year('April 11 1867'))  # Output: 1867
print(extract_year('February 12 1806'))  # Output: 1806

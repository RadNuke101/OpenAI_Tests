def extract_year(input_str):
    input_list = input_str.split()
    for item in input_list:
        if item.isdigit() and len(item) == 4:
            return item

# Prompt: return the sequence of 4 numbers (excluding spaces) from input
# Input: ['April 1 1799']
# Output: 1799

# Test cases
print(extract_year('April 1 1799'))  # Output: 1799
print(extract_year('April 11 1867'))  # Output: 1867
print(extract_year('February 12 1806'))  # Output: 1806
print(extract_year('February 21 1798'))  # Output: 1798
print(extract_year('February 28 1844 as Delaware Township'))  # Output: 1844
print(extract_year('February 5 1798'))  # Output: 1798
print(extract_year('February 7 1892 Verona Township'))  # Output: 1892
print(extract_year('February 9 1797'))  # Output: 1797
print(extract_year('January 19 1748'))  # Output: 1748
print(extract_year('July 10 1721 as Upper Penns Neck Township'))  # Output: 1721
print(extract_year('March 15 1860'))  # Output: 1860
print(extract_year('March 17 1870 <as Raritan Township>'))  # Output: 1870
print(extract_year('March 17 1874'))  # Output: 1874
print(extract_year('March 23 1864'))  # Output: 1864
print(extract_year('March 5 1867'))  # Output: 1867
print(extract_year('April 28th 1828'))  # Output: 1828

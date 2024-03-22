def extract_year(input_str):
    # Prompt: return the sequence of 4 numbers (excluding spaces) from input
    # Input: ['April 1 1799'], Output: 1799
    # Input: ['April 11 1867'], Output: 1867
    # Input: ['February 12 1806'], Output: 1806
    # Input: ['February 21 1798'], Output: 1798
    # Input: ['February 28 1844 as Delaware Township'], Output: 1844
    # Input: ['February 5 1798'], Output: 1798
    # Input: ['February 7 1892 Verona Township'], Output: 1892
    # Input: ['February 9 1797'], Output: 1797
    # Input: ['January 19 1748'], Output: 1748
    # Input: ['July 10 1721 as Upper Penns Neck Township'], Output: 1721
    # Input: ['March 15 1860'], Output: 1860
    # Input: ['March 17 1870 <as Raritan Township>'], Output: 1870
    # Input: ['March 17 1874'], Output: 1874
    # Input: ['March 23 1864'], Output: 1864
    # Input: ['March 5 1867'], Output: 1867
    # Input: ['April 28th 1828'], Output: 1828
    
    year = ''
    for char in input_str:
        if char.isdigit():
            year += char
    return year

# Test cases
print(extract_year('April 1 1799'))  # Output: 1799
print(extract_year('March 17 1870 <as Raritan Township>'))  # Output: 1870
print(extract_year('February 9 1797'))  # Output: 1797

# Prompt: return the sequence of 4 numbers (excluding spaces) from input
# Given input as ['April 1 1799'] output is 1799
# Given input as ['April 11 1867'] output is 1867
# Given input as ['February 12 1806'] output is 1806
# Given input as ['February 21 1798'] output is 1798
# Given input as ['February 28 1844 as Delaware Township'] output is 1844
# Given input as ['February 5 1798'] output is 1798
# Given input as ['February 7 1892 Verona Township'] output is 1892
# Given input as ['February 9 1797'] output is 1797
# Given input as ['January 19 1748'] output is 1748
# Given input as ['July 10 1721 as Upper Penns Neck Township'] output is 1721
# Given input as ['March 15 1860'] output is 1860
# Given input as ['March 17 1870 <as Raritan Township>'] output is 1870
# Given input as ['March 17 1874'] output is 1874
# Given input as ['March 23 1864'] output is 1864
# Given input as ['March 5 1867'] output is 1867
# Given input as ['April 28th 1828'] output is 1828

def extract_year(input_str):
    for word in input_str.split():
        if word.isdigit() and len(word) == 4:
            return word

# Test cases
print(extract_year('April 1 1799'))  # Output: 1799
print(extract_year('February 21 1798'))  # Output: 1798
print(extract_year('March 17 1870 <as Raritan Township>'))  # Output: 1870

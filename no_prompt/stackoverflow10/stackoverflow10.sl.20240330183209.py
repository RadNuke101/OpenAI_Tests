# Start time: 2024-03-30 18:46:04.110826

# Content: Given that given input as ['April 1 1799'] output is 1799, given input as ['April 11 1867'] output is 1867, given input as ['February 12 1806'] output is 1806, given input as ['February 21 1798'] output is 1798, given input as ['February 28 1844 as Delaware Township'] output is 1844, given input as ['February 5 1798'] output is 1798, given input as ['February 7 1892 Verona Township'] output is 1892, given input as ['February 9 1797'] output is 1797, given input as ['January 19 1748'] output is 1748, given input as ['July 10 1721 as Upper Penns Neck Township'] output is 1721, given input as ['March 15 1860'] output is 1860, given input as ['March 17 1870 <as Raritan Township>'] output is 1870, given input as ['March 17 1874'] output is 1874, given input as ['March 23 1864'] output is 1864, given input as ['March 5 1867'] output is 1867, given input as ['April 28th 1828'] output is 1828, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_year(date_str):
    try:
        # Input: 'April 1 1799'
        # Output: '1799'
        
        # Input: 'April 11 1867'
        # Output: '1867'
        
        # Input: 'February 12 1806'
        # Output: '1806'
        
        # Input: 'February 21 1798'
        # Output: '1798'
        
        # Input: 'February 28 1844 as Delaware Township'
        # Output: '1844'
        
        # Input: 'February 5 1798'
        # Output: '1798'
        
        # Input: 'February 7 1892 Verona Township'
        # Output: '1892'
        
        # Input: 'February 9 1797'
        # Output: '1797'
        
        # Input: 'January 19 1748'
        # Output: '1748'
        
        # Input: 'July 10 1721 as Upper Penns Neck Township'
        # Output: '1721'
        
        # Input: 'March 15 1860'
        # Output: '1860'
        
        # Input: 'March 17 1870 <as Raritan Township>'
        # Output: '1870'
        
        # Input: 'March 17 1874'
        # Output: '1874'
        
        # Input: 'March 23 1864'
        # Output: '1864'
        
        # Input: 'March 5 1867'
        # Output: '1867'
        
        # Input: 'April 28th 1828'
        # Output: '1828'
        
        words = date_str.split()
        for word in words:
            if word.isdigit() and len(word) == 4:
                return word
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return None

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

# End time: 2024-03-30 18:46:19.901330
# Elapsed time in seconds: 15.790148621000071
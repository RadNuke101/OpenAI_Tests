
# Define function to count occurrences of specific word in expression
def count_occurrences(expression, word):
    
    # Split expression into list of words
    words = expression.split()
    
    # Initialize counter
    count = 0
    
    # Loop through each word in list
    for w in words:
        
        # Check if word is equal to input word
        if w == word:
            
            # If equal, increment counter
            count += 1
    
    # Return final count
    return count

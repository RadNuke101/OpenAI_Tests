# Function to check if the second, third, and fourth inputs are in the first input
def check_inputs(expression, word1, word2, word3):
    # Split the expression into a list of words
    words = expression.split()
    # Check if all three words are in the expression
    if word1 in words and word2 in words and word3 in words:
        return True
    else:
        return False
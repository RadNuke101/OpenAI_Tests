# Function to check if a number is present in the inputted expression
def check_number(expression):
    # Split the expression into individual words
    words = expression.split()
    # Loop through each word
    for word in words:
        # Check if the word is a number
        if word.isdigit():
            return True
    # If no number is found, return False
    return False
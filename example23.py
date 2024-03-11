# Function to check if "overhead" is in the expression
def check_overhead(expression):
    # Split the expression into individual words
    words = expression.split(",")
    # Check if "overhead" is in the list of words
    if "overhead" in words:
        return False
    else:
        return True
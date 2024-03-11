# Function to check if entered letter or phrase is in the expression
def check_input(expression, input):
    # Convert expression to lowercase for case-insensitive comparison
    expression = expression.lower()
    # Convert input to lowercase for case-insensitive comparison
    input = input.lower()
    # Check if input is in expression
    if input in expression:
        return True
    else:
        return False
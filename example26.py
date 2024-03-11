# Define function to return the three capitalized letters before the ">" in the expression
def get_capital_letters(expression):
    # Split the expression by the ">" symbol
    split_expression = expression.split(">")
    # Get the first part of the split expression
    first_part = split_expression[0]
    # Split the first part by the "." symbol
    split_first_part = first_part.split(".")
    # Get the last three characters of the first part
    last_three_chars = split_first_part[-1][-3:]
    # Capitalize the last three characters
    capitalized_letters = last_three_chars.upper()
    # Return the capitalized letters
    return capitalized_letters
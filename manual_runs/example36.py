
# Python program with a function that follows the prompt and returns the outputs when given the inputs

def check_inputs(input1, input2, input3, input4):
    # Split the first input into a list of words
    words = input1.split()

    # Check if any of the words in the first two columns are in the first two words of the first input
    if input2 in words[:2] or input3 in words[:2] or input4 in words[:2]:
        return True
    else:
        return False
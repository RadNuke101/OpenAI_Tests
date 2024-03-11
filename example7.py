# Code:

# Function to generate outputs given inputs
def generate_outputs(inputs):
  # Split the input string into a list of words
  words = inputs.split()
  # Get the first letter of the first word
  first_letter = words[0][0]
  # Get the second word
  second_word = words[1]
  # Generate the output string
  output = first_letter + " " + second_word
  # Return the output
  return output

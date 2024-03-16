
# Define function
def get_capitalized_letters(input_phrase):
    # Split input phrase into individual words
    words = input_phrase.split(" ")
    
    # Create an empty string to store capitalized letters
    capitalized_letters = ""
    
    # Loop through each word in the input phrase
    for word in words:
        # Check if the word has at least three characters
        if len(word) >= 3:
            # Get the first three characters from the word
            letters = word[:3]
            # Check if the letters are all uppercase
            if letters.isupper():
                # Add the letters to the output string
                capitalized_letters += letters + " "
    
    # Remove the last space from the output string and return it
    return capitalized_letters[:-1]
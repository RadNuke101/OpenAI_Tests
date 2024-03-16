# Define a function that takes in a phrase as input
def first_word(phrase):
    # Check if "ssp" is in the phrase
    if "ssp" in phrase:
        # Split the phrase into a list of words
        words = phrase.split()
        # Return the first two words
        return words[0] + " " + words[1]
    else:
        # Split the phrase into a list of words
        words = phrase.split()
        # Return the first word
        return words[0]
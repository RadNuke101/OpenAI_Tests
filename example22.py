# Function to delete everything enclosed by a pair of "/"
def delete_enclosed(text):
    # Find the index of the first "/" in the text
    first_index = text.find("/")
    # Find the index of the second "/" in the text
    second_index = text.find("/", first_index + 1)
    # Return the text with the enclosed part deleted
    return text[:first_index] + text[second_index + 1:]
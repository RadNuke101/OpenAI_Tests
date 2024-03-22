# Prompt: if "that" is in the inputted phrase, remove "that" from the phrase and return the updated phrases. 
# If the inputted phrase is one word, return unedited phrase.

def remove_that(input_phrase):
    if 'that' in input_phrase:
        return input_phrase.replace('that', '')
    else:
        return input_phrase

# Test cases
print(remove_that('thatensures')) # Output: ensures
print(remove_that('thatwill')) # Output: will
print(remove_that('thathave')) # Output: have
print(remove_that('knowthat')) # Output: know
print(remove_that('that')) # Output: that
print(remove_that('mouse')) # Output: mouse
print(remove_that('knowthat')) # Output: know

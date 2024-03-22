# Prompt: if "that" is in the inputted phrase, remove "that" from the phrase and return the updated phrases. If the inputted phrase is one word, return unedited phrase.
# Input: ['thatensures'] -> Output: ensures
# Input: ['thatwill'] -> Output: will
# Input: ['thathave'] -> Output: have
# Input: ['knowthat'] -> Output: know
# Input: ['that'] -> Output: that
# Input: ['mouse'] -> Output: mouse
# Input: ['knowthat'] -> Output: know

def remove_that(input_str):
    if 'that' in input_str:
        return input_str.replace('that', '')
    else:
        return input_str

# Test cases
print(remove_that('thatensures'))  # Output: ensures
print(remove_that('thatwill'))     # Output: will
print(remove_that('thathave'))     # Output: have
print(remove_that('knowthat'))     # Output: know
print(remove_that('that'))         # Output: that
print(remove_that('mouse'))        # Output: mouse
print(remove_that('knowthat'))     # Output: know

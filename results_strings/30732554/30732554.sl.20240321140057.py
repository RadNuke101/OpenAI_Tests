# Prompt: if "—" present, delete that and everything after "|"
# Input: ['TL-18273982| 10MM']
# Output: TL-18273982

def process_input(input_str):
    if "—" in input_str:
        input_str = input_str.split("—")[0]
    if "|" in input_str:
        input_str = input_str.split("|")[0]
    return input_str.strip()

# Test cases
print(process_input('TL-18273982| 10MM'))  # Output: TL-18273982
print(process_input('TL-288762| 76DK'))    # Output: TL-288762
print(process_input('CT-576'))              # Output: CT-576
print(process_input('N/A'))                 # Output: N/A

def process_input(input_str):
    input_list = input_str.split(', ')
    if 'New York' in input_list[1]:
        input_list[1] = 'NY'
    else:
        input_list.append('USA')
    return ', '.join(input_list)

# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
# Input: ['UCLA', 'Los Angeles, CA']
# Output: Los Angeles, CA, USA

# Test cases
print(process_input("University of Pennsylvania, Phialdelphia, PA, USA"))
print(process_input("UCLA, Los Angeles, CA"))
print(process_input("Cornell University, Ithaca, New York, USA"))
print(process_input("Penn, Philadelphia, PA, USA"))
print(process_input("University of Maryland College Park, College Park, MD"))
print(process_input("University of Michigan, Ann Arbor, MI, USA"))
print(process_input("UC Berkeley, Berkeley, CA"))
print(process_input("MIT, Cambridge, MA"))
print(process_input("Rice University, Houston, TX"))
print(process_input("Yale University, New Haven, CT, USA"))
print(process_input("Columbia University, New York, NY, USA"))
print(process_input("NYU, New York, New York, USA"))
print(process_input("UC Berkeley, Berkeley, CA"))
print(process_input("UIUC, Urbana, IL"))
print(process_input("Temple University, Philadelphia, PA"))
print(process_input("Harvard University, Cambridge, MA, USA"))
print(process_input("University of Connecticut, Storrs, CT, USA"))
print(process_input("Drexel University, Philadelphia, PA"))
print(process_input("New Haven University, New Haven, CT, USA"))
print(process_input("University of California, Santa Barbara, Santa Barbara, CA, USA"))

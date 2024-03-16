def format_universities(input_list):
    return [f"{item[0]}, {item[1]}" for item in input_list]

input_list = [['University of Pennsylvania', 'Phialdelphia, PA, USA'], ['Cornell University', 'Ithaca, New York, USA'], ['University of Maryland College Park', 'College Park, MD'], ['University of Michigan', 'Ann Arbor, MI, USA'], ['Yale University', 'New Haven, CT, USA'], ['Columbia University', 'New York, NY, USA']]
output = format_universities(input_list)
print(output)

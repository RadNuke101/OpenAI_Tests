def process_input(input_list):
    output_list = []
    for item in input_list:
        second_input = item[1]
        if "New York" in second_input:
            second_input = second_input.replace("New York", "NY")
        else:
            second_input += ", USA"
        output_list.append(second_input)
    
    return output_list

input_list = [['University of Pennsylvania', 'Phialdelphia, PA, USA'], ['UCLA', 'Los Angeles, CA'], ['Cornell University', 'Ithaca, New York, USA'], ['Penn', 'Philadelphia, PA, USA'], ['University of Maryland College Park', 'College Park, MD'], ['University of Michigan', 'Ann Arbor, MI, USA'], ['Columbia University', 'New York, NY, USA'], ['NYU', 'New York, New York, USA']]
output = process_input(input_list)
print(output)

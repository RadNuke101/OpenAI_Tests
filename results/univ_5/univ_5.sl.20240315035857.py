def process_input(input_list):
    output_list = []
    for item in input_list:
        if "New York" in item[1]:
            output_list.append(item[1].replace("New York", "NY"))
        elif "USA" not in item[1]:
            output_list.append(item[1] + ", USA")
        else:
            output_list.append(item[1])
    return output_list

input_list = [['University of Pennsylvania', 'Phialdelphia, PA, USA'], ['UCLA', 'Los Angeles, CA'], ['Cornell University', 'Ithaca, New York, USA'], ['Penn', 'Philadelphia, PA, USA'], ['University of Maryland College Park', 'College Park, MD'], ['University of Michigan', 'Ann Arbor, MI, USA'], ['Columbia University', 'New York, NY, USA'], ['NYU', 'New York, New York, USA']]
output = process_input(input_list)
print(output)

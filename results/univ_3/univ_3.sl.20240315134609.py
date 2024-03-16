def return_second_input(data):
    result = []
    for item in data:
        if len(item) > 1:
            second_input = item[1]
            if "USA" not in second_input:
                result.append(", USA")
            else:
                result.append(second_input)
    return result

input_data = [['University of Pennsylvania', 'Phialdelphia, PA, USA'], ['UCLA', 'Los Angeles, CA'], ['Cornell University', 'Ithaca, New York, USA'], ['Penn', 'Philadelphia, PA, USA'], ['University of Maryland College Park', 'College Park, MD'], ['University of Michigan', 'Ann Arbor, MI, USA']]
output_data = return_second_input(input_data)
print(output_data)

def return_second_input(data):
    result = []
    for item in data:
        if len(item) >= 2:
            second_input = item[1]
            if "USA" not in second_input:
                result.append(", USA")
            else:
                result.append(second_input)
    return result

input_data = [['University of Pennsylvania', 'Phialdelphia, PA, USA'], ['UCLA', 'Los Angeles, CA'], ['Cornell University', 'Ithaca, New York, USA'], ['Penn', 'Philadelphia, PA, USA'], ['University of Maryland College Park', 'College Park, MD'], ['University of Michigan', 'Ann Arbor, MI, USA'], ['UC Berkeley', 'Berkeley, CA'], ['MIT', 'Cambridge, MA'], ['Rice University', 'Houston, TX'], ['Yale University', 'New Haven, CT, USA'], ['Columbia University', 'New York, NY, USA'], ['NYU', 'New York, New York, USA'], ['UC Berkeley', 'Berkeley, CA'], ['UIUC', 'Urbana, IL'], ['Temple University', 'Philadelphia, PA'], ['Harvard University', 'Cambridge, MA, USA'], ['University of Connecticut', 'Storrs, CT, USA'], ['Drexel University', 'Philadelphia, PA'], ['New Haven University', 'New Haven, CT, USA'], ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']]

output_result = return_second_input(input_data)
print(output_result)

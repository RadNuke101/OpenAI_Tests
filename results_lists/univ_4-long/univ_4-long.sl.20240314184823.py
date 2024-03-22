def return_second_input(data):
    output = []
    for item in data:
        if 'USA' in item[1]:
            output.append(item[1])
        else:
            output.append(', USA')
    return output

input_data = [['University of Pennsylvania', 'Phialdelphia, PA, USA'], ['UCLA', 'Los Angeles, CA'], ['Cornell University', 'Ithaca, New York, USA'], ['Penn', 'Philadelphia, PA, USA'], ['University of Maryland College Park', 'College Park, MD'], ['University of Michigan', 'Ann Arbor, MI, USA'], ['UC Berkeley', 'Berkeley, CA'], ['MIT', 'Cambridge, MA'], ['Rice University', 'Houston, TX'], ['Yale University', 'New Haven, CT, USA'], ['Columbia University', 'New York, NY, USA'], ['NYU', 'New York, New York, USA'], ['UC Berkeley', 'Berkeley, CA'], ['UIUC', 'Urbana, IL'], ['Temple University', 'Philadelphia, PA'], ['Harvard University', 'Cambridge, MA, USA'], ['University of Connecticut', 'Storrs, CT, USA'], ['Drexel University', 'Philadelphia, PA'], ['New Haven University', 'New Haven, CT, USA'], ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']]

print(return_second_input(input_data))

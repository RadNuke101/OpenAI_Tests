def return_second_input(data):
    result = []
    for item in data:
        if 'USA' not in item[1]:
            result.append(item[1] + ', USA')
        else:
            result.append(item[1])
    return result

input_data = [['UC Berkeley', 'Berkeley, CA'], ['University of Pennsylvania', 'Phialdelphia, PA, USA'], ['Cornell University', 'Ithaca, New York, USA'], ['Penn', 'Philadelphia, PA, USA'], ['University of Michigan', 'Ann Arbor, MI, USA'], ['UC Berkeley', 'Berkeley, CA'], ['MIT', 'Cambridge, MA'], ['University of Pennsylvania', 'Phialdelphia, PA, USA'], ['UCLA', 'Los Angeles, CA'], ['University of Maryland College Park', 'College Park, MD'], ['University of Michigan', 'Ann Arbor, MI, USA'], ['UC Berkeley', 'Berkeley, CA'], ['MIT', 'Cambridge, MA'], ['Rice University', 'Houston, TX'], ['Yale University', 'New Haven, CT, USA'], ['Columbia University', 'New York, NY, USA'], ['NYU', 'New York, New York, USA'], ['Drexel University', 'Philadelphia, PA'], ['UC Berkeley', 'Berkeley, CA'], ['UIUC', 'Urbana, IL'], ['Temple University', 'Philadelphia, PA'], ['Harvard University', 'Cambridge, MA, USA'], ['University of Connecticut', 'Storrs, CT, USA'], ['Drexel University', 'Philadelphia, PA'], ['NYU', 'New York, New York, USA'], ['UIUC', 'Urbana, IL'], ['New Haven University', 'New Haven, CT, USA'], ['University of California, Santa Barbara', 'Santa Barbara, CA, USA'], ['University of Connecticut', 'Storrs, CT, USA']]
output_data = ['Berkeley, CA, USA', 'Phialdelphia, PA, USA', 'Ithaca, NY, USA', 'Philadelphia, PA, USA', 'Ann Arbor, MI, USA', 'Berkeley, CA, USA', 'Cambridge, MA, USA', 'Phialdelphia, PA, USA', 'Los Angeles, CA, USA', 'College Park, MD, USA', 'Ann Arbor, MI, USA', 'Berkeley, CA, USA', 'Cambridge, MA, USA', 'Houston, TX, USA', 'New Haven, CT, USA', 'New York, NY, USA', 'New York, NY, USA', 'Philadelphia, PA, USA', 'Berkeley, CA, USA', 'Urbana, IL, USA', 'Philadelphia, PA, USA', 'Cambridge, MA, USA', 'Storrs, CT, USA', 'Philadelphia, PA, USA', 'New York, NY, USA', 'Urbana, IL, USA', 'New Haven, CT, USA', 'Santa Barbara, CA, USA', 'Storrs, CT, USA']

print(return_second_input(input_data) == output_data)

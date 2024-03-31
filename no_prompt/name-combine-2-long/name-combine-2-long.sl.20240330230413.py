# Start time: 2024-03-30 23:15:22.967704

# Content: Given that given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., given input as ['Launa', 'Withers'] output is Launa W., given input as ['Lakenya', 'Edison'] output is Lakenya E., given input as ['Brendan', 'Hage'] output is Brendan H., given input as ['Bradford', 'Lango'] output is Bradford L., given input as ['Rudolf', 'Akiyama'] output is Rudolf A., given input as ['Lara', 'Constable'] output is Lara C., given input as ['Madelaine', 'Ghoston'] output is Madelaine G., given input as ['Salley', 'Hornak'] output is Salley H., given input as ['Micha', 'Junkin'] output is Micha J., given input as ['Teddy', 'Bobo'] output is Teddy B., given input as ['Coralee', 'Scalia'] output is Coralee S., given input as ['Jeff', 'Quashie'] output is Jeff Q., given input as ['Vena', 'Babiarz'] output is Vena B., given input as ['Karrie', 'Lain'] output is Karrie L., given input as ['Tobias', 'Dermody'] output is Tobias D., given input as ['Celsa', 'Hopkins'] output is Celsa H., given input as ['Kimberley', 'Halpern'] output is Kimberley H., given input as ['Phillip', 'Rowden'] output is Phillip R., given input as ['Elias', 'Neil'] output is Elias N., given input as ['Lashanda', 'Cortes'] output is Lashanda C., given input as ['Mackenzie', 'Spell'] output is Mackenzie S., given input as ['Kathlyn', 'Eccleston'] output is Kathlyn E., given input as ['Georgina', 'Brescia'] output is Georgina B., given input as ['Beata', 'Miah'] output is Beata M., given input as ['Desiree', 'Seamons'] output is Desiree S., given input as ['Jeanice', 'Soderstrom'] output is Jeanice S., given input as ['Mariel', 'Jurgens'] output is Mariel J., given input as ['Alida', 'Bogle'] output is Alida B., given input as ['Jacqualine', 'Olague'] output is Jacqualine O., given input as ['Joaquin', 'Clasen'] output is Joaquin C., given input as ['Samuel', 'Richert'] output is Samuel R., given input as ['Malissa', 'Marcus'] output is Malissa M., given input as ['Alaina', 'Partida'] output is Alaina P., given input as ['Trinidad', 'Mulloy'] output is Trinidad M., given input as ['Carlene', 'Garrard'] output is Carlene G., given input as ['Melodi', 'Chism'] output is Melodi C., given input as ['Bess', 'Chilcott'] output is Bess C., given input as ['Chong', 'Aylward'] output is Chong A., given input as ['Jani', 'Ramthun'] output is Jani R., given input as ['Jacquiline', 'Heintz'] output is Jacquiline H., given input as ['Hayley', 'Marquess'] output is Hayley M., given input as ['Andria', 'Spagnoli'] output is Andria S., given input as ['Irwin', 'Covelli'] output is Irwin C., given input as ['Gertude', 'Montiel'] output is Gertude M., given input as ['Stefany', 'Reily'] output is Stefany R., given input as ['Rae', 'Mcgaughey'] output is Rae M., given input as ['Cruz', 'Latimore'] output is Cruz L., given input as ['Maryann', 'Casler'] output is Maryann C., given input as ['Annalisa', 'Gregori'] output is Annalisa G., given input as ['Jenee', 'Pannell'] output is Jenee P., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(input_name):
    try:
        # Input: ['Nancy', 'FreeHafer'] Output: Nancy F.
        first_name, last_name = input_name.split()
        return f"{first_name} {last_name[0]}."
    except (ValueError, AttributeError) as e:
        print("Invalid input format. Please provide a valid input in the format ['First', 'Last'].")
        return None

# Test cases
print(format_name('Nancy FreeHafer'))
print(format_name('Andrew Cencici'))
print(format_name('Jan Kotas'))
print(format_name('Mariya Sergienko'))
print(format_name('Launa Withers'))
print(format_name('Lakenya Edison'))
print(format_name('Brendan Hage'))
print(format_name('Bradford Lango'))
print(format_name('Rudolf Akiyama'))
print(format_name('Lara Constable'))
print(format_name('Madelaine Ghoston'))
print(format_name('Salley Hornak'))
print(format_name('Micha Junkin'))
print(format_name('Teddy Bobo'))
print(format_name('Coralee Scalia'))
print(format_name('Jeff Quashie'))
print(format_name('Vena Babiarz'))
print(format_name('Karrie Lain'))
print(format_name('Tobias Dermody'))
print(format_name('Celsa Hopkins'))
print(format_name('Kimberley Halpern'))
print(format_name('Phillip Rowden'))
print(format_name('Elias Neil'))
print(format_name('Lashanda Cortes'))
print(format_name('Mackenzie Spell'))
print(format_name('Kathlyn Eccleston'))
print(format_name('Georgina Brescia'))
print(format_name('Beata Miah'))
print(format_name('Desiree Seamons'))
print(format_name('Jeanice Soderstrom'))
print(format_name('Mariel Jurgens'))
print(format_name('Alida Bogle'))
print(format_name('Jacqualine Olague'))
print(format_name('Joaquin Clasen'))
print(format_name('Samuel Richert'))
print(format_name('Malissa Marcus'))
print(format_name('Alaina Partida'))
print(format_name('Trinidad Mulloy'))
print(format_name('Carlene Garrard'))
print(format_name('Melodi Chism'))
print(format_name('Bess Chilcott'))
print(format_name('Chong Aylward'))
print(format_name('Jani Ramthun'))
print(format_name('Jacquiline Heintz'))
print(format_name('Hayley Marquess'))
print(format_name('Andria Spagnoli'))
print(format_name('Irwin Covelli'))
print(format_name('Gertude Montiel'))
print(format_name('Stefany Reily'))
print(format_name('Rae Mcgaughey'))
print(format_name('Cruz Latimore'))
print(format_name('Maryann Casler'))
print(format_name('Annalisa Gregori'))
print(format_name('Jenee Pannell'))

# End time: 2024-03-30 23:15:32.244511
# Elapsed time in seconds: 9.276576256997942
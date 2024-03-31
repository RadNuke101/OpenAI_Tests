# Start time: 2024-03-30 22:42:24.888001

# Content: Given that given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., given input as ['Launa', 'Withers'] output is Launa W., given input as ['Lakenya', 'Edison'] output is Lakenya E., given input as ['Brendan', 'Hage'] output is Brendan H., given input as ['Bradford', 'Lango'] output is Bradford L., given input as ['Rudolf', 'Akiyama'] output is Rudolf A., given input as ['Lara', 'Constable'] output is Lara C., given input as ['Madelaine', 'Ghoston'] output is Madelaine G., given input as ['Salley', 'Hornak'] output is Salley H., given input as ['Micha', 'Junkin'] output is Micha J., given input as ['Teddy', 'Bobo'] output is Teddy B., given input as ['Coralee', 'Scalia'] output is Coralee S., given input as ['Jeff', 'Quashie'] output is Jeff Q., given input as ['Vena', 'Babiarz'] output is Vena B., given input as ['Karrie', 'Lain'] output is Karrie L., given input as ['Tobias', 'Dermody'] output is Tobias D., given input as ['Celsa', 'Hopkins'] output is Celsa H., given input as ['Kimberley', 'Halpern'] output is Kimberley H., given input as ['Phillip', 'Rowden'] output is Phillip R., given input as ['Elias', 'Neil'] output is Elias N., given input as ['Lashanda', 'Cortes'] output is Lashanda C., given input as ['Mackenzie', 'Spell'] output is Mackenzie S., given input as ['Kathlyn', 'Eccleston'] output is Kathlyn E., given input as ['Georgina', 'Brescia'] output is Georgina B., given input as ['Beata', 'Miah'] output is Beata M., given input as ['Desiree', 'Seamons'] output is Desiree S., given input as ['Jeanice', 'Soderstrom'] output is Jeanice S., given input as ['Mariel', 'Jurgens'] output is Mariel J., given input as ['Alida', 'Bogle'] output is Alida B., given input as ['Jacqualine', 'Olague'] output is Jacqualine O., given input as ['Joaquin', 'Clasen'] output is Joaquin C., given input as ['Samuel', 'Richert'] output is Samuel R., given input as ['Malissa', 'Marcus'] output is Malissa M., given input as ['Alaina', 'Partida'] output is Alaina P., given input as ['Trinidad', 'Mulloy'] output is Trinidad M., given input as ['Carlene', 'Garrard'] output is Carlene G., given input as ['Melodi', 'Chism'] output is Melodi C., given input as ['Bess', 'Chilcott'] output is Bess C., given input as ['Chong', 'Aylward'] output is Chong A., given input as ['Jani', 'Ramthun'] output is Jani R., given input as ['Jacquiline', 'Heintz'] output is Jacquiline H., given input as ['Hayley', 'Marquess'] output is Hayley M., given input as ['Andria', 'Spagnoli'] output is Andria S., given input as ['Irwin', 'Covelli'] output is Irwin C., given input as ['Gertude', 'Montiel'] output is Gertude M., given input as ['Stefany', 'Reily'] output is Stefany R., given input as ['Rae', 'Mcgaughey'] output is Rae M., given input as ['Cruz', 'Latimore'] output is Cruz L., given input as ['Maryann', 'Casler'] output is Maryann C., given input as ['Annalisa', 'Gregori'] output is Annalisa G., given input as ['Jenee', 'Pannell'] output is Jenee P., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(input_name):
    try:
        # Input: ['Nancy', 'FreeHafer'] Output: Nancy F.
        first_name, last_name = input_name.split()
        return f"{first_name} {last_name[0]}."
    except ValueError:
        print("Input format is incorrect. Please provide first name and last name separated by a space.")

# Test cases
print(format_name('Nancy FreeHafer'))  # Output: Nancy F.
print(format_name('Andrew Cencici'))  # Output: Andrew C.
print(format_name('Jan Kotas'))  # Output: Jan K.
print(format_name('Mariya Sergienko'))  # Output: Mariya S.
print(format_name('Launa Withers'))  # Output: Launa W.
print(format_name('Lakenya Edison'))  # Output: Lakenya E.
print(format_name('Brendan Hage'))  # Output: Brendan H.
print(format_name('Bradford Lango'))  # Output: Bradford L.
print(format_name('Rudolf Akiyama'))  # Output: Rudolf A.
print(format_name('Lara Constable'))  # Output: Lara C.
print(format_name('Madelaine Ghoston'))  # Output: Madelaine G.
print(format_name('Salley Hornak'))  # Output: Salley H.
print(format_name('Micha Junkin'))  # Output: Micha J.
print(format_name('Teddy Bobo'))  # Output: Teddy B.
print(format_name('Coralee Scalia'))  # Output: Coralee S.
print(format_name('Jeff Quashie'))  # Output: Jeff Q.
print(format_name('Vena Babiarz'))  # Output: Vena B.
print(format_name('Karrie Lain'))  # Output: Karrie L.
print(format_name('Tobias Dermody'))  # Output: Tobias D.
print(format_name('Celsa Hopkins'))  # Output: Celsa H.
print(format_name('Kimberley Halpern'))  # Output: Kimberley H.
print(format_name('Phillip Rowden'))  # Output: Phillip R.
print(format_name('Elias Neil'))  # Output: Elias N.
print(format_name('Lashanda Cortes'))  # Output: Lashanda C.
print(format_name('Mackenzie Spell'))  # Output: Mackenzie S.
print(format_name('Kathlyn Eccleston'))  # Output: Kathlyn E.
print(format_name('Georgina Brescia'))  # Output: Georgina B.
print(format_name('Beata Miah'))  # Output: Beata M.
print(format_name('Desiree Seamons'))  # Output: Desiree S.
print(format_name('Jeanice Soderstrom'))  # Output: Jeanice S.
print(format_name('Mariel Jurgens'))  # Output: Mariel J.
print(format_name('Alida Bogle'))  # Output: Alida B.
print(format_name('Jacqualine Olague'))  # Output: Jacqualine O.
print(format_name('Joaquin Clasen'))  # Output: Joaquin C.
print(format_name('Samuel Richert'))  # Output: Samuel R.
print(format_name('Malissa Marcus'))  # Output: Malissa M.
print(format_name('Alaina Partida'))  # Output: Alaina P.
print(format_name('Trinidad Mulloy'))  # Output: Trinidad M.
print(format_name('Carlene Garrard'))  # Output: Carlene G.
print(format_name('Melodi Chism'))  # Output: Melodi C.
print(format_name('Bess Chilcott'))  # Output: Bess C.
print(format_name('Chong Aylward'))  # Output: Chong A.
print(format_name('Jani Ramthun'))  # Output: Jani R.
print(format_name('Jacquiline Heintz'))  # Output: Jacquiline H.
print(format_name('Hayley Marquess'))  # Output: Hayley M.
print(format_name('Andria Spagnoli'))  # Output: Andria S.
print(format_name('Irwin Covelli'))  # Output: Irwin C.
print(format_name('Gertude Montiel'))  # Output: Gertude M.
print(format_name('Stefany Reily'))  # Output: Stefany R.
print(format_name('Rae Mcgaughey'))  # Output: Rae M.
print(format_name('Cruz Latimore'))  # Output: Cruz L.
print(format_name('Maryann Casler'))  # Output: Maryann C.
print(format_name('Annalisa Gregori'))  # Output: Annalisa G.
print(format_name('Jenee Pannell'))  # Output: Jenee P.

# End time: 2024-03-30 22:42:38.833782
# Elapsed time in seconds: 13.945413055000245
# Start time: 2024-03-30 01:01:12.879092
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period, and given input as ['Launa', 'Withers'] output is Withers, L., given input as ['Lakenya', 'Edison'] output is Edison, L., given input as ['Brendan', 'Hage'] output is Hage, B., given input as ['Bradford', 'Lango'] output is Lango, B., given input as ['Rudolf', 'Akiyama'] output is Akiyama, R., given input as ['Lara', 'Constable'] output is Constable, L., given input as ['Madelaine', 'Ghoston'] output is Ghoston, M., given input as ['Salley', 'Hornak'] output is Hornak, S., given input as ['Micha', 'Junkin'] output is Junkin, M., given input as ['Teddy', 'Bobo'] output is Bobo, T., given input as ['Coralee', 'Scalia'] output is Scalia, C., given input as ['Jeff', 'Quashie'] output is Quashie, J., given input as ['Vena', 'Babiarz'] output is Babiarz, V., given input as ['Karrie', 'Lain'] output is Lain, K., given input as ['Tobias', 'Dermody'] output is Dermody, T., given input as ['Celsa', 'Hopkins'] output is Hopkins, C., given input as ['Kimberley', 'Halpern'] output is Halpern, K., given input as ['Phillip', 'Rowden'] output is Rowden, P., given input as ['Elias', 'Neil'] output is Neil, E., given input as ['Lashanda', 'Cortes'] output is Cortes, L., given input as ['Mackenzie', 'Spell'] output is Spell, M., given input as ['Kathlyn', 'Eccleston'] output is Eccleston, K., given input as ['Georgina', 'Brescia'] output is Brescia, G., given input as ['Beata', 'Miah'] output is Miah, B., given input as ['Desiree', 'Seamons'] output is Seamons, D., given input as ['Jeanice', 'Soderstrom'] output is Soderstrom, J., given input as ['Mariel', 'Jurgens'] output is Jurgens, M., given input as ['Alida', 'Bogle'] output is Bogle, A., given input as ['Jacqualine', 'Olague'] output is Olague, J., given input as ['Joaquin', 'Clasen'] output is Clasen, J., given input as ['Samuel', 'Richert'] output is Richert, S., given input as ['Malissa', 'Marcus'] output is Marcus, M., given input as ['Alaina', 'Partida'] output is Partida, A., given input as ['Trinidad', 'Mulloy'] output is Mulloy, T., given input as ['Carlene', 'Garrard'] output is Garrard, C., given input as ['Melodi', 'Chism'] output is Chism, M., given input as ['Bess', 'Chilcott'] output is Chilcott, B., given input as ['Chong', 'Aylward'] output is Aylward, C., given input as ['Jani', 'Ramthun'] output is Ramthun, J., given input as ['Jacquiline', 'Heintz'] output is Heintz, J., given input as ['Hayley', 'Marquess'] output is Marquess, H., given input as ['Andria', 'Spagnoli'] output is Spagnoli, A., given input as ['Irwin', 'Covelli'] output is Covelli, I., given input as ['Gertude', 'Montiel'] output is Montiel, G., given input as ['Stefany', 'Reily'] output is Reily, S., given input as ['Rae', 'Mcgaughey'] output is Mcgaughey, R., given input as ['Cruz', 'Latimore'] output is Latimore, C., given input as ['Maryann', 'Casler'] output is Casler, M., given input as ['Annalisa', 'Gregori'] output is Gregori, A., given input as ['Jenee', 'Pannell'] output is Pannell, J., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def format_names(input_str):
    try:
        input_list = input_str.split(', ')
        first_name = input_list[0]
        last_name = input_list[1]
        formatted_name = last_name + ', ' + first_name[0] + '.'
        return formatted_name
    except (IndexError, AttributeError) as e:
        return "Invalid input format. Please provide two names separated by a comma and a space."

# Input: "Launa, Withers"
# Output: "Withers, L."
# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period

# Testing the function with example inputs
print(format_names("Launa, Withers"))
print(format_names("Lakenya, Edison"))
print(format_names("Brendan, Hage"))
print(format_names("Bradford, Lango"))
print(format_names("Rudolf, Akiyama"))
print(format_names("Lara, Constable"))
print(format_names("Madelaine, Ghoston"))
print(format_names("Salley, Hornak"))
print(format_names("Micha, Junkin"))
print(format_names("Teddy, Bobo"))
print(format_names("Coralee, Scalia"))
print(format_names("Jeff, Quashie"))
print(format_names("Vena, Babiarz"))
print(format_names("Karrie, Lain"))
print(format_names("Tobias, Dermody"))
print(format_names("Celsa, Hopkins"))
print(format_names("Kimberley, Halpern"))
print(format_names("Phillip, Rowden"))
print(format_names("Elias, Neil"))
print(format_names("Lashanda, Cortes"))
print(format_names("Mackenzie, Spell"))
print(format_names("Kathlyn, Eccleston"))
print(format_names("Georgina, Brescia"))
print(format_names("Beata, Miah"))
print(format_names("Desiree, Seamons"))
print(format_names("Jeanice, Soderstrom"))
print(format_names("Mariel, Jurgens"))
print(format_names("Alida, Bogle"))
print(format_names("Jacqualine, Olague"))
print(format_names("Joaquin, Clasen"))
print(format_names("Samuel, Richert"))
print(format_names("Malissa, Marcus"))
print(format_names("Alaina, Partida"))
print(format_names("Trinidad, Mulloy"))
print(format_names("Carlene, Garrard"))
print(format_names("Melodi, Chism"))
print(format_names("Bess, Chilcott"))
print(format_names("Chong, Aylward"))
print(format_names("Jani, Ramthun"))
print(format_names("Jacquiline, Heintz"))
print(format_names("Hayley, Marquess"))
print(format_names("Andria, Spagnoli"))
print(format_names("Irwin, Covelli"))
print(format_names("Gertude, Montiel"))
print(format_names("Stefany, Reily"))
print(format_names("Rae, Mcgaughey"))
print(format_names("Cruz, Latimore"))
print(format_names("Maryann, Casler"))
print(format_names("Annalisa, Gregori"))
print(format_names("Jenee, Pannell"))

# End time: 2024-03-30 01:01:25.936827
# Elapsed time in seconds: 13.05736897800034
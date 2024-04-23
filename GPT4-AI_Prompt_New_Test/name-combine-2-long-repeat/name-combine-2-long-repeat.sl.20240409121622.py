# Start time: 2024-04-09 12:55:38.488986

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns, each containing personal names. The first column includes a variety of first names, while the second column contains last names. These names span a diverse range of cultural backgrounds, indicating a wide representation of individuals. The data set includes repetitions of certain name combinations, suggesting either a focus on specific individuals or a limited sample size that necessitates repeated entries for comprehensive analysis.

### Output Column Summary:

The output data is a transformation of the input names into a standardized format that combines the first name from the first column with the initial of the last name from the second column, followed by a period. This format provides a concise way to reference individuals while maintaining a level of privacy or anonymity by not disclosing full last names. It also standardizes the way names are presented, making it easier to manage and reference in a list or database.

### Relationship Between Input and Output:

The relationship between the input and output data is a process of formatting and partially anonymizing personal names. The transformation retains the full first name, ensuring that the individual's primary identifier is kept intact for personalization and recognition. By reducing the last name to only its initial and appending a period, the process creates a uniform, concise identifier that balances recognizability with a measure of privacy. This method is commonly used in formal and semi-formal contexts where full names are unnecessary or where privacy concerns are paramount. The consistent format across all entries suggests a systematic approach to handling personal data, likely aimed at simplifying record-keeping, enhancing readability, and maintaining a level of confidentiality., and input as ['Nancy', 'FreeHafer'] output is Nancy F., input as ['Andrew', 'Cencici'] output is Andrew C., input as ['Jan', 'Kotas'] output is Jan K., input as ['Mariya', 'Sergienko'] output is Mariya S., input as ['Launa', 'Withers'] output is Launa W., input as ['Launa', 'Withers'] output is Launa W., input as ['Launa', 'Withers'] output is Launa W., input as ['Lakenya', 'Edison'] output is Lakenya E., input as ['Lakenya', 'Edison'] output is Lakenya E., input as ['Lakenya', 'Edison'] output is Lakenya E., input as ['Brendan', 'Hage'] output is Brendan H., input as ['Brendan', 'Hage'] output is Brendan H., input as ['Brendan', 'Hage'] output is Brendan H., input as ['Bradford', 'Lango'] output is Bradford L., input as ['Bradford', 'Lango'] output is Bradford L., input as ['Bradford', 'Lango'] output is Bradford L., input as ['Rudolf', 'Akiyama'] output is Rudolf A., input as ['Rudolf', 'Akiyama'] output is Rudolf A., input as ['Rudolf', 'Akiyama'] output is Rudolf A., input as ['Lara', 'Constable'] output is Lara C., input as ['Lara', 'Constable'] output is Lara C., input as ['Lara', 'Constable'] output is Lara C., input as ['Madelaine', 'Ghoston'] output is Madelaine G., input as ['Madelaine', 'Ghoston'] output is Madelaine G., input as ['Madelaine', 'Ghoston'] output is Madelaine G., input as ['Salley', 'Hornak'] output is Salley H., input as ['Salley', 'Hornak'] output is Salley H., input as ['Salley', 'Hornak'] output is Salley H., input as ['Micha', 'Junkin'] output is Micha J., input as ['Micha', 'Junkin'] output is Micha J., input as ['Micha', 'Junkin'] output is Micha J., input as ['Teddy', 'Bobo'] output is Teddy B., input as ['Teddy', 'Bobo'] output is Teddy B., input as ['Teddy', 'Bobo'] output is Teddy B., input as ['Coralee', 'Scalia'] output is Coralee S., input as ['Coralee', 'Scalia'] output is Coralee S., input as ['Coralee', 'Scalia'] output is Coralee S., input as ['Jeff', 'Quashie'] output is Jeff Q., input as ['Jeff', 'Quashie'] output is Jeff Q., input as ['Jeff', 'Quashie'] output is Jeff Q., input as ['Vena', 'Babiarz'] output is Vena B., input as ['Vena', 'Babiarz'] output is Vena B., input as ['Vena', 'Babiarz'] output is Vena B., input as ['Karrie', 'Lain'] output is Karrie L., input as ['Karrie', 'Lain'] output is Karrie L., input as ['Karrie', 'Lain'] output is Karrie L., input as ['Tobias', 'Dermody'] output is Tobias D., input as ['Tobias', 'Dermody'] output is Tobias D., input as ['Tobias', 'Dermody'] output is Tobias D., input as ['Celsa', 'Hopkins'] output is Celsa H., input as ['Celsa', 'Hopkins'] output is Celsa H., input as ['Celsa', 'Hopkins'] output is Celsa H., input as ['Kimberley', 'Halpern'] output is Kimberley H., input as ['Kimberley', 'Halpern'] output is Kimberley H., input as ['Kimberley', 'Halpern'] output is Kimberley H., input as ['Phillip', 'Rowden'] output is Phillip R., input as ['Phillip', 'Rowden'] output is Phillip R., input as ['Phillip', 'Rowden'] output is Phillip R., input as ['Elias', 'Neil'] output is Elias N., input as ['Elias', 'Neil'] output is Elias N., input as ['Elias', 'Neil'] output is Elias N., input as ['Lashanda', 'Cortes'] output is Lashanda C., input as ['Lashanda', 'Cortes'] output is Lashanda C., input as ['Lashanda', 'Cortes'] output is Lashanda C., input as ['Mackenzie', 'Spell'] output is Mackenzie S., input as ['Mackenzie', 'Spell'] output is Mackenzie S., input as ['Mackenzie', 'Spell'] output is Mackenzie S., input as ['Kathlyn', 'Eccleston'] output is Kathlyn E., input as ['Kathlyn', 'Eccleston'] output is Kathlyn E., input as ['Kathlyn', 'Eccleston'] output is Kathlyn E., input as ['Georgina', 'Brescia'] output is Georgina B., input as ['Georgina', 'Brescia'] output is Georgina B., input as ['Georgina', 'Brescia'] output is Georgina B., input as ['Beata', 'Miah'] output is Beata M., input as ['Beata', 'Miah'] output is Beata M., input as ['Beata', 'Miah'] output is Beata M., input as ['Desiree', 'Seamons'] output is Desiree S., input as ['Desiree', 'Seamons'] output is Desiree S., input as ['Desiree', 'Seamons'] output is Desiree S., input as ['Jeanice', 'Soderstrom'] output is Jeanice S., input as ['Jeanice', 'Soderstrom'] output is Jeanice S., input as ['Jeanice', 'Soderstrom'] output is Jeanice S., input as ['Mariel', 'Jurgens'] output is Mariel J., input as ['Mariel', 'Jurgens'] output is Mariel J., input as ['Mariel', 'Jurgens'] output is Mariel J., input as ['Alida', 'Bogle'] output is Alida B., input as ['Alida', 'Bogle'] output is Alida B., input as ['Alida', 'Bogle'] output is Alida B., input as ['Jacqualine', 'Olague'] output is Jacqualine O., input as ['Jacqualine', 'Olague'] output is Jacqualine O., input as ['Jacqualine', 'Olague'] output is Jacqualine O., input as ['Joaquin', 'Clasen'] output is Joaquin C., input as ['Joaquin', 'Clasen'] output is Joaquin C., input as ['Joaquin', 'Clasen'] output is Joaquin C., input as ['Samuel', 'Richert'] output is Samuel R., input as ['Samuel', 'Richert'] output is Samuel R., input as ['Samuel', 'Richert'] output is Samuel R., input as ['Malissa', 'Marcus'] output is Malissa M., input as ['Malissa', 'Marcus'] output is Malissa M., input as ['Malissa', 'Marcus'] output is Malissa M., input as ['Alaina', 'Partida'] output is Alaina P., input as ['Alaina', 'Partida'] output is Alaina P., input as ['Alaina', 'Partida'] output is Alaina P., input as ['Trinidad', 'Mulloy'] output is Trinidad M., input as ['Trinidad', 'Mulloy'] output is Trinidad M., input as ['Trinidad', 'Mulloy'] output is Trinidad M., input as ['Carlene', 'Garrard'] output is Carlene G., input as ['Carlene', 'Garrard'] output is Carlene G., input as ['Carlene', 'Garrard'] output is Carlene G., input as ['Melodi', 'Chism'] output is Melodi C., input as ['Melodi', 'Chism'] output is Melodi C., input as ['Melodi', 'Chism'] output is Melodi C., input as ['Bess', 'Chilcott'] output is Bess C., input as ['Bess', 'Chilcott'] output is Bess C., input as ['Bess', 'Chilcott'] output is Bess C., input as ['Chong', 'Aylward'] output is Chong A., input as ['Chong', 'Aylward'] output is Chong A., input as ['Chong', 'Aylward'] output is Chong A., input as ['Jani', 'Ramthun'] output is Jani R., input as ['Jani', 'Ramthun'] output is Jani R., input as ['Jani', 'Ramthun'] output is Jani R., input as ['Jacquiline', 'Heintz'] output is Jacquiline H., input as ['Jacquiline', 'Heintz'] output is Jacquiline H., input as ['Jacquiline', 'Heintz'] output is Jacquiline H., input as ['Hayley', 'Marquess'] output is Hayley M., input as ['Hayley', 'Marquess'] output is Hayley M., input as ['Hayley', 'Marquess'] output is Hayley M., input as ['Andria', 'Spagnoli'] output is Andria S., input as ['Andria', 'Spagnoli'] output is Andria S., input as ['Andria', 'Spagnoli'] output is Andria S., input as ['Irwin', 'Covelli'] output is Irwin C., input as ['Irwin', 'Covelli'] output is Irwin C., input as ['Irwin', 'Covelli'] output is Irwin C., input as ['Gertude', 'Montiel'] output is Gertude M., input as ['Gertude', 'Montiel'] output is Gertude M., input as ['Gertude', 'Montiel'] output is Gertude M., input as ['Stefany', 'Reily'] output is Stefany R., input as ['Stefany', 'Reily'] output is Stefany R., input as ['Stefany', 'Reily'] output is Stefany R., input as ['Rae', 'Mcgaughey'] output is Rae M., input as ['Rae', 'Mcgaughey'] output is Rae M., input as ['Rae', 'Mcgaughey'] output is Rae M., input as ['Cruz', 'Latimore'] output is Cruz L., input as ['Cruz', 'Latimore'] output is Cruz L., input as ['Cruz', 'Latimore'] output is Cruz L., input as ['Maryann', 'Casler'] output is Maryann C., input as ['Maryann', 'Casler'] output is Maryann C., input as ['Maryann', 'Casler'] output is Maryann C., input as ['Annalisa', 'Gregori'] output is Annalisa G., input as ['Annalisa', 'Gregori'] output is Annalisa G., input as ['Annalisa', 'Gregori'] output is Annalisa G., input as ['Jenee', 'Pannell'] output is Jenee P., input as ['Jenee', 'Pannell'] output is Jenee P., input as ['Jenee', 'Pannell'] output is Jenee P., input as ['Launa', 'Withers'] output is Launa W., input as ['Lakenya', 'Edison'] output is Lakenya E., input as ['Brendan', 'Hage'] output is Brendan H., input as ['Bradford', 'Lango'] output is Bradford L., input as ['Rudolf', 'Akiyama'] output is Rudolf A., input as ['Lara', 'Constable'] output is Lara C., input as ['Madelaine', 'Ghoston'] output is Madelaine G., input as ['Salley', 'Hornak'] output is Salley H., input as ['Micha', 'Junkin'] output is Micha J., input as ['Teddy', 'Bobo'] output is Teddy B., input as ['Coralee', 'Scalia'] output is Coralee S., input as ['Jeff', 'Quashie'] output is Jeff Q., input as ['Vena', 'Babiarz'] output is Vena B., input as ['Karrie', 'Lain'] output is Karrie L., input as ['Tobias', 'Dermody'] output is Tobias D., input as ['Celsa', 'Hopkins'] output is Celsa H., input as ['Kimberley', 'Halpern'] output is Kimberley H., input as ['Phillip', 'Rowden'] output is Phillip R., input as ['Elias', 'Neil'] output is Elias N., input as ['Lashanda', 'Cortes'] output is Lashanda C., input as ['Mackenzie', 'Spell'] output is Mackenzie S., input as ['Kathlyn', 'Eccleston'] output is Kathlyn E., input as ['Georgina', 'Brescia'] output is Georgina B., input as ['Beata', 'Miah'] output is Beata M., input as ['Desiree', 'Seamons'] output is Desiree S., input as ['Jeanice', 'Soderstrom'] output is Jeanice S., input as ['Mariel', 'Jurgens'] output is Mariel J., input as ['Alida', 'Bogle'] output is Alida B., input as ['Jacqualine', 'Olague'] output is Jacqualine O., input as ['Joaquin', 'Clasen'] output is Joaquin C., input as ['Samuel', 'Richert'] output is Samuel R., input as ['Malissa', 'Marcus'] output is Malissa M., input as ['Alaina', 'Partida'] output is Alaina P., input as ['Trinidad', 'Mulloy'] output is Trinidad M., input as ['Carlene', 'Garrard'] output is Carlene G., input as ['Melodi', 'Chism'] output is Melodi C., input as ['Bess', 'Chilcott'] output is Bess C., input as ['Chong', 'Aylward'] output is Chong A., input as ['Jani', 'Ramthun'] output is Jani R., input as ['Jacquiline', 'Heintz'] output is Jacquiline H., input as ['Hayley', 'Marquess'] output is Hayley M., input as ['Andria', 'Spagnoli'] output is Andria S., input as ['Irwin', 'Covelli'] output is Irwin C., input as ['Gertude', 'Montiel'] output is Gertude M., input as ['Stefany', 'Reily'] output is Stefany R., input as ['Rae', 'Mcgaughey'] output is Rae M., input as ['Cruz', 'Latimore'] output is Cruz L., input as ['Maryann', 'Casler'] output is Maryann C., input as ['Annalisa', 'Gregori'] output is Annalisa G., input as ['Jenee', 'Pannell'] output is Jenee P., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    """
    This function takes a first name and a last name as inputs and returns a string
    that combines the first name with the initial of the last name followed by a period.
    """
    return f"{first_name} {last_name[0]}."

# Test cases
print(generated_function('Nancy', 'FreeHafer'))  # Expected output: Nancy F.
print(generated_function('Andrew', 'Cencici'))  # Expected output: Andrew C.
print(generated_function('Jan', 'Kotas'))  # Expected output: Jan K.
print(generated_function('Mariya', 'Sergienko'))  # Expected output: Mariya S.
print(generated_function('Launa', 'Withers'))  # Expected output: Launa W.
print(generated_function('Lakenya', 'Edison'))  # Expected output: Lakenya E.
print(generated_function('Brendan', 'Hage'))  # Expected output: Brendan H.
print(generated_function('Bradford', 'Lango'))  # Expected output: Bradford L.
print(generated_function('Rudolf', 'Akiyama'))  # Expected output: Rudolf A.
print(generated_function('Lara', 'Constable'))  # Expected output: Lara C.
# Additional test cases based on the provided input
print(generated_function('Madelaine', 'Ghoston'))  # Expected output: Madelaine G.
print(generated_function('Salley', 'Hornak'))  # Expected output: Salley H.
print(generated_function('Micha', 'Junkin'))  # Expected output: Micha J.
print(generated_function('Teddy', 'Bobo'))  # Expected output: Teddy B.
print(generated_function('Coralee', 'Scalia'))  # Expected output: Coralee S.
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.
print(generated_function("Launa", "Withers"))  ## Output: Launa W.
print(generated_function("Launa", "Withers"))  ## Output: Launa W.
print(generated_function("Launa", "Withers"))  ## Output: Launa W.
print(generated_function("Lakenya", "Edison"))  ## Output: Lakenya E.
print(generated_function("Lakenya", "Edison"))  ## Output: Lakenya E.
print(generated_function("Lakenya", "Edison"))  ## Output: Lakenya E.
print(generated_function("Brendan", "Hage"))  ## Output: Brendan H.
print(generated_function("Brendan", "Hage"))  ## Output: Brendan H.
print(generated_function("Brendan", "Hage"))  ## Output: Brendan H.
print(generated_function("Bradford", "Lango"))  ## Output: Bradford L.
print(generated_function("Bradford", "Lango"))  ## Output: Bradford L.
print(generated_function("Bradford", "Lango"))  ## Output: Bradford L.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Rudolf A.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Rudolf A.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Rudolf A.
print(generated_function("Lara", "Constable"))  ## Output: Lara C.
print(generated_function("Lara", "Constable"))  ## Output: Lara C.
print(generated_function("Lara", "Constable"))  ## Output: Lara C.
print(generated_function("Madelaine", "Ghoston"))  ## Output: Madelaine G.
print(generated_function("Madelaine", "Ghoston"))  ## Output: Madelaine G.
print(generated_function("Madelaine", "Ghoston"))  ## Output: Madelaine G.
print(generated_function("Salley", "Hornak"))  ## Output: Salley H.
print(generated_function("Salley", "Hornak"))  ## Output: Salley H.
print(generated_function("Salley", "Hornak"))  ## Output: Salley H.
print(generated_function("Micha", "Junkin"))  ## Output: Micha J.
print(generated_function("Micha", "Junkin"))  ## Output: Micha J.
print(generated_function("Micha", "Junkin"))  ## Output: Micha J.
print(generated_function("Teddy", "Bobo"))  ## Output: Teddy B.
print(generated_function("Teddy", "Bobo"))  ## Output: Teddy B.
print(generated_function("Teddy", "Bobo"))  ## Output: Teddy B.
print(generated_function("Coralee", "Scalia"))  ## Output: Coralee S.
print(generated_function("Coralee", "Scalia"))  ## Output: Coralee S.
print(generated_function("Coralee", "Scalia"))  ## Output: Coralee S.
print(generated_function("Jeff", "Quashie"))  ## Output: Jeff Q.
print(generated_function("Jeff", "Quashie"))  ## Output: Jeff Q.
print(generated_function("Jeff", "Quashie"))  ## Output: Jeff Q.
print(generated_function("Vena", "Babiarz"))  ## Output: Vena B.
print(generated_function("Vena", "Babiarz"))  ## Output: Vena B.
print(generated_function("Vena", "Babiarz"))  ## Output: Vena B.
print(generated_function("Karrie", "Lain"))  ## Output: Karrie L.
print(generated_function("Karrie", "Lain"))  ## Output: Karrie L.
print(generated_function("Karrie", "Lain"))  ## Output: Karrie L.
print(generated_function("Tobias", "Dermody"))  ## Output: Tobias D.
print(generated_function("Tobias", "Dermody"))  ## Output: Tobias D.
print(generated_function("Tobias", "Dermody"))  ## Output: Tobias D.
print(generated_function("Celsa", "Hopkins"))  ## Output: Celsa H.
print(generated_function("Celsa", "Hopkins"))  ## Output: Celsa H.
print(generated_function("Celsa", "Hopkins"))  ## Output: Celsa H.
print(generated_function("Kimberley", "Halpern"))  ## Output: Kimberley H.
print(generated_function("Kimberley", "Halpern"))  ## Output: Kimberley H.
print(generated_function("Kimberley", "Halpern"))  ## Output: Kimberley H.
print(generated_function("Phillip", "Rowden"))  ## Output: Phillip R.
print(generated_function("Phillip", "Rowden"))  ## Output: Phillip R.
print(generated_function("Phillip", "Rowden"))  ## Output: Phillip R.
print(generated_function("Elias", "Neil"))  ## Output: Elias N.
print(generated_function("Elias", "Neil"))  ## Output: Elias N.
print(generated_function("Elias", "Neil"))  ## Output: Elias N.
print(generated_function("Lashanda", "Cortes"))  ## Output: Lashanda C.
print(generated_function("Lashanda", "Cortes"))  ## Output: Lashanda C.
print(generated_function("Lashanda", "Cortes"))  ## Output: Lashanda C.
print(generated_function("Mackenzie", "Spell"))  ## Output: Mackenzie S.
print(generated_function("Mackenzie", "Spell"))  ## Output: Mackenzie S.
print(generated_function("Mackenzie", "Spell"))  ## Output: Mackenzie S.
print(generated_function("Kathlyn", "Eccleston"))  ## Output: Kathlyn E.
print(generated_function("Kathlyn", "Eccleston"))  ## Output: Kathlyn E.
print(generated_function("Kathlyn", "Eccleston"))  ## Output: Kathlyn E.
print(generated_function("Georgina", "Brescia"))  ## Output: Georgina B.
print(generated_function("Georgina", "Brescia"))  ## Output: Georgina B.
print(generated_function("Georgina", "Brescia"))  ## Output: Georgina B.
print(generated_function("Beata", "Miah"))  ## Output: Beata M.
print(generated_function("Beata", "Miah"))  ## Output: Beata M.
print(generated_function("Beata", "Miah"))  ## Output: Beata M.
print(generated_function("Desiree", "Seamons"))  ## Output: Desiree S.
print(generated_function("Desiree", "Seamons"))  ## Output: Desiree S.
print(generated_function("Desiree", "Seamons"))  ## Output: Desiree S.
print(generated_function("Jeanice", "Soderstrom"))  ## Output: Jeanice S.
print(generated_function("Jeanice", "Soderstrom"))  ## Output: Jeanice S.
print(generated_function("Jeanice", "Soderstrom"))  ## Output: Jeanice S.
print(generated_function("Mariel", "Jurgens"))  ## Output: Mariel J.
print(generated_function("Mariel", "Jurgens"))  ## Output: Mariel J.
print(generated_function("Mariel", "Jurgens"))  ## Output: Mariel J.
print(generated_function("Alida", "Bogle"))  ## Output: Alida B.
print(generated_function("Alida", "Bogle"))  ## Output: Alida B.
print(generated_function("Alida", "Bogle"))  ## Output: Alida B.
print(generated_function("Jacqualine", "Olague"))  ## Output: Jacqualine O.
print(generated_function("Jacqualine", "Olague"))  ## Output: Jacqualine O.
print(generated_function("Jacqualine", "Olague"))  ## Output: Jacqualine O.
print(generated_function("Joaquin", "Clasen"))  ## Output: Joaquin C.
print(generated_function("Joaquin", "Clasen"))  ## Output: Joaquin C.
print(generated_function("Joaquin", "Clasen"))  ## Output: Joaquin C.
print(generated_function("Samuel", "Richert"))  ## Output: Samuel R.
print(generated_function("Samuel", "Richert"))  ## Output: Samuel R.
print(generated_function("Samuel", "Richert"))  ## Output: Samuel R.
print(generated_function("Malissa", "Marcus"))  ## Output: Malissa M.
print(generated_function("Malissa", "Marcus"))  ## Output: Malissa M.
print(generated_function("Malissa", "Marcus"))  ## Output: Malissa M.
print(generated_function("Alaina", "Partida"))  ## Output: Alaina P.
print(generated_function("Alaina", "Partida"))  ## Output: Alaina P.
print(generated_function("Alaina", "Partida"))  ## Output: Alaina P.
print(generated_function("Trinidad", "Mulloy"))  ## Output: Trinidad M.
print(generated_function("Trinidad", "Mulloy"))  ## Output: Trinidad M.
print(generated_function("Trinidad", "Mulloy"))  ## Output: Trinidad M.
print(generated_function("Carlene", "Garrard"))  ## Output: Carlene G.
print(generated_function("Carlene", "Garrard"))  ## Output: Carlene G.
print(generated_function("Carlene", "Garrard"))  ## Output: Carlene G.
print(generated_function("Melodi", "Chism"))  ## Output: Melodi C.
print(generated_function("Melodi", "Chism"))  ## Output: Melodi C.
print(generated_function("Melodi", "Chism"))  ## Output: Melodi C.
print(generated_function("Bess", "Chilcott"))  ## Output: Bess C.
print(generated_function("Bess", "Chilcott"))  ## Output: Bess C.
print(generated_function("Bess", "Chilcott"))  ## Output: Bess C.
print(generated_function("Chong", "Aylward"))  ## Output: Chong A.
print(generated_function("Chong", "Aylward"))  ## Output: Chong A.
print(generated_function("Chong", "Aylward"))  ## Output: Chong A.
print(generated_function("Jani", "Ramthun"))  ## Output: Jani R.
print(generated_function("Jani", "Ramthun"))  ## Output: Jani R.
print(generated_function("Jani", "Ramthun"))  ## Output: Jani R.
print(generated_function("Jacquiline", "Heintz"))  ## Output: Jacquiline H.
print(generated_function("Jacquiline", "Heintz"))  ## Output: Jacquiline H.
print(generated_function("Jacquiline", "Heintz"))  ## Output: Jacquiline H.
print(generated_function("Hayley", "Marquess"))  ## Output: Hayley M.
print(generated_function("Hayley", "Marquess"))  ## Output: Hayley M.
print(generated_function("Hayley", "Marquess"))  ## Output: Hayley M.
print(generated_function("Andria", "Spagnoli"))  ## Output: Andria S.
print(generated_function("Andria", "Spagnoli"))  ## Output: Andria S.
print(generated_function("Andria", "Spagnoli"))  ## Output: Andria S.
print(generated_function("Irwin", "Covelli"))  ## Output: Irwin C.
print(generated_function("Irwin", "Covelli"))  ## Output: Irwin C.
print(generated_function("Irwin", "Covelli"))  ## Output: Irwin C.
print(generated_function("Gertude", "Montiel"))  ## Output: Gertude M.
print(generated_function("Gertude", "Montiel"))  ## Output: Gertude M.
print(generated_function("Gertude", "Montiel"))  ## Output: Gertude M.
print(generated_function("Stefany", "Reily"))  ## Output: Stefany R.
print(generated_function("Stefany", "Reily"))  ## Output: Stefany R.
print(generated_function("Stefany", "Reily"))  ## Output: Stefany R.
print(generated_function("Rae", "Mcgaughey"))  ## Output: Rae M.
print(generated_function("Rae", "Mcgaughey"))  ## Output: Rae M.
print(generated_function("Rae", "Mcgaughey"))  ## Output: Rae M.
print(generated_function("Cruz", "Latimore"))  ## Output: Cruz L.
print(generated_function("Cruz", "Latimore"))  ## Output: Cruz L.
print(generated_function("Cruz", "Latimore"))  ## Output: Cruz L.
print(generated_function("Maryann", "Casler"))  ## Output: Maryann C.
print(generated_function("Maryann", "Casler"))  ## Output: Maryann C.
print(generated_function("Maryann", "Casler"))  ## Output: Maryann C.
print(generated_function("Annalisa", "Gregori"))  ## Output: Annalisa G.
print(generated_function("Annalisa", "Gregori"))  ## Output: Annalisa G.
print(generated_function("Annalisa", "Gregori"))  ## Output: Annalisa G.
print(generated_function("Jenee", "Pannell"))  ## Output: Jenee P.
print(generated_function("Jenee", "Pannell"))  ## Output: Jenee P.
print(generated_function("Jenee", "Pannell"))  ## Output: Jenee P.
print(generated_function("Launa", "Withers"))  ## Output: Launa W.
print(generated_function("Lakenya", "Edison"))  ## Output: Lakenya E.
print(generated_function("Brendan", "Hage"))  ## Output: Brendan H.
print(generated_function("Bradford", "Lango"))  ## Output: Bradford L.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Rudolf A.
print(generated_function("Lara", "Constable"))  ## Output: Lara C.
print(generated_function("Madelaine", "Ghoston"))  ## Output: Madelaine G.
print(generated_function("Salley", "Hornak"))  ## Output: Salley H.
print(generated_function("Micha", "Junkin"))  ## Output: Micha J.
print(generated_function("Teddy", "Bobo"))  ## Output: Teddy B.
print(generated_function("Coralee", "Scalia"))  ## Output: Coralee S.
print(generated_function("Jeff", "Quashie"))  ## Output: Jeff Q.
print(generated_function("Vena", "Babiarz"))  ## Output: Vena B.
print(generated_function("Karrie", "Lain"))  ## Output: Karrie L.
print(generated_function("Tobias", "Dermody"))  ## Output: Tobias D.
print(generated_function("Celsa", "Hopkins"))  ## Output: Celsa H.
print(generated_function("Kimberley", "Halpern"))  ## Output: Kimberley H.
print(generated_function("Phillip", "Rowden"))  ## Output: Phillip R.
print(generated_function("Elias", "Neil"))  ## Output: Elias N.
print(generated_function("Lashanda", "Cortes"))  ## Output: Lashanda C.
print(generated_function("Mackenzie", "Spell"))  ## Output: Mackenzie S.
print(generated_function("Kathlyn", "Eccleston"))  ## Output: Kathlyn E.
print(generated_function("Georgina", "Brescia"))  ## Output: Georgina B.
print(generated_function("Beata", "Miah"))  ## Output: Beata M.
print(generated_function("Desiree", "Seamons"))  ## Output: Desiree S.
print(generated_function("Jeanice", "Soderstrom"))  ## Output: Jeanice S.
print(generated_function("Mariel", "Jurgens"))  ## Output: Mariel J.
print(generated_function("Alida", "Bogle"))  ## Output: Alida B.
print(generated_function("Jacqualine", "Olague"))  ## Output: Jacqualine O.
print(generated_function("Joaquin", "Clasen"))  ## Output: Joaquin C.
print(generated_function("Samuel", "Richert"))  ## Output: Samuel R.
print(generated_function("Malissa", "Marcus"))  ## Output: Malissa M.
print(generated_function("Alaina", "Partida"))  ## Output: Alaina P.
print(generated_function("Trinidad", "Mulloy"))  ## Output: Trinidad M.
print(generated_function("Carlene", "Garrard"))  ## Output: Carlene G.
print(generated_function("Melodi", "Chism"))  ## Output: Melodi C.
print(generated_function("Bess", "Chilcott"))  ## Output: Bess C.
print(generated_function("Chong", "Aylward"))  ## Output: Chong A.
print(generated_function("Jani", "Ramthun"))  ## Output: Jani R.
print(generated_function("Jacquiline", "Heintz"))  ## Output: Jacquiline H.
print(generated_function("Hayley", "Marquess"))  ## Output: Hayley M.
print(generated_function("Andria", "Spagnoli"))  ## Output: Andria S.
print(generated_function("Irwin", "Covelli"))  ## Output: Irwin C.
print(generated_function("Gertude", "Montiel"))  ## Output: Gertude M.
print(generated_function("Stefany", "Reily"))  ## Output: Stefany R.
print(generated_function("Rae", "Mcgaughey"))  ## Output: Rae M.
print(generated_function("Cruz", "Latimore"))  ## Output: Cruz L.
print(generated_function("Maryann", "Casler"))  ## Output: Maryann C.
print(generated_function("Annalisa", "Gregori"))  ## Output: Annalisa G.
print(generated_function("Jenee", "Pannell"))  ## Output: Jenee P.

# End time: 2024-04-09 12:55:57.711034
# Elapsed time in seconds: 19.22166807700023


# APPEND TEST SCRIPTS...
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.
print(generated_function("Launa", "Withers"))  ## Output: Launa W.
print(generated_function("Launa", "Withers"))  ## Output: Launa W.
print(generated_function("Launa", "Withers"))  ## Output: Launa W.
print(generated_function("Lakenya", "Edison"))  ## Output: Lakenya E.
print(generated_function("Lakenya", "Edison"))  ## Output: Lakenya E.
print(generated_function("Lakenya", "Edison"))  ## Output: Lakenya E.
print(generated_function("Brendan", "Hage"))  ## Output: Brendan H.
print(generated_function("Brendan", "Hage"))  ## Output: Brendan H.
print(generated_function("Brendan", "Hage"))  ## Output: Brendan H.
print(generated_function("Bradford", "Lango"))  ## Output: Bradford L.
print(generated_function("Bradford", "Lango"))  ## Output: Bradford L.
print(generated_function("Bradford", "Lango"))  ## Output: Bradford L.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Rudolf A.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Rudolf A.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Rudolf A.
print(generated_function("Lara", "Constable"))  ## Output: Lara C.
print(generated_function("Lara", "Constable"))  ## Output: Lara C.
print(generated_function("Lara", "Constable"))  ## Output: Lara C.
print(generated_function("Madelaine", "Ghoston"))  ## Output: Madelaine G.
print(generated_function("Madelaine", "Ghoston"))  ## Output: Madelaine G.
print(generated_function("Madelaine", "Ghoston"))  ## Output: Madelaine G.
print(generated_function("Salley", "Hornak"))  ## Output: Salley H.
print(generated_function("Salley", "Hornak"))  ## Output: Salley H.
print(generated_function("Salley", "Hornak"))  ## Output: Salley H.
print(generated_function("Micha", "Junkin"))  ## Output: Micha J.
print(generated_function("Micha", "Junkin"))  ## Output: Micha J.
print(generated_function("Micha", "Junkin"))  ## Output: Micha J.
print(generated_function("Teddy", "Bobo"))  ## Output: Teddy B.
print(generated_function("Teddy", "Bobo"))  ## Output: Teddy B.
print(generated_function("Teddy", "Bobo"))  ## Output: Teddy B.
print(generated_function("Coralee", "Scalia"))  ## Output: Coralee S.
print(generated_function("Coralee", "Scalia"))  ## Output: Coralee S.
print(generated_function("Coralee", "Scalia"))  ## Output: Coralee S.
print(generated_function("Jeff", "Quashie"))  ## Output: Jeff Q.
print(generated_function("Jeff", "Quashie"))  ## Output: Jeff Q.
print(generated_function("Jeff", "Quashie"))  ## Output: Jeff Q.
print(generated_function("Vena", "Babiarz"))  ## Output: Vena B.
print(generated_function("Vena", "Babiarz"))  ## Output: Vena B.
print(generated_function("Vena", "Babiarz"))  ## Output: Vena B.
print(generated_function("Karrie", "Lain"))  ## Output: Karrie L.
print(generated_function("Karrie", "Lain"))  ## Output: Karrie L.
print(generated_function("Karrie", "Lain"))  ## Output: Karrie L.
print(generated_function("Tobias", "Dermody"))  ## Output: Tobias D.
print(generated_function("Tobias", "Dermody"))  ## Output: Tobias D.
print(generated_function("Tobias", "Dermody"))  ## Output: Tobias D.
print(generated_function("Celsa", "Hopkins"))  ## Output: Celsa H.
print(generated_function("Celsa", "Hopkins"))  ## Output: Celsa H.
print(generated_function("Celsa", "Hopkins"))  ## Output: Celsa H.
print(generated_function("Kimberley", "Halpern"))  ## Output: Kimberley H.
print(generated_function("Kimberley", "Halpern"))  ## Output: Kimberley H.
print(generated_function("Kimberley", "Halpern"))  ## Output: Kimberley H.
print(generated_function("Phillip", "Rowden"))  ## Output: Phillip R.
print(generated_function("Phillip", "Rowden"))  ## Output: Phillip R.
print(generated_function("Phillip", "Rowden"))  ## Output: Phillip R.
print(generated_function("Elias", "Neil"))  ## Output: Elias N.
print(generated_function("Elias", "Neil"))  ## Output: Elias N.
print(generated_function("Elias", "Neil"))  ## Output: Elias N.
print(generated_function("Lashanda", "Cortes"))  ## Output: Lashanda C.
print(generated_function("Lashanda", "Cortes"))  ## Output: Lashanda C.
print(generated_function("Lashanda", "Cortes"))  ## Output: Lashanda C.
print(generated_function("Mackenzie", "Spell"))  ## Output: Mackenzie S.
print(generated_function("Mackenzie", "Spell"))  ## Output: Mackenzie S.
print(generated_function("Mackenzie", "Spell"))  ## Output: Mackenzie S.
print(generated_function("Kathlyn", "Eccleston"))  ## Output: Kathlyn E.
print(generated_function("Kathlyn", "Eccleston"))  ## Output: Kathlyn E.
print(generated_function("Kathlyn", "Eccleston"))  ## Output: Kathlyn E.
print(generated_function("Georgina", "Brescia"))  ## Output: Georgina B.
print(generated_function("Georgina", "Brescia"))  ## Output: Georgina B.
print(generated_function("Georgina", "Brescia"))  ## Output: Georgina B.
print(generated_function("Beata", "Miah"))  ## Output: Beata M.
print(generated_function("Beata", "Miah"))  ## Output: Beata M.
print(generated_function("Beata", "Miah"))  ## Output: Beata M.
print(generated_function("Desiree", "Seamons"))  ## Output: Desiree S.
print(generated_function("Desiree", "Seamons"))  ## Output: Desiree S.
print(generated_function("Desiree", "Seamons"))  ## Output: Desiree S.
print(generated_function("Jeanice", "Soderstrom"))  ## Output: Jeanice S.
print(generated_function("Jeanice", "Soderstrom"))  ## Output: Jeanice S.
print(generated_function("Jeanice", "Soderstrom"))  ## Output: Jeanice S.
print(generated_function("Mariel", "Jurgens"))  ## Output: Mariel J.
print(generated_function("Mariel", "Jurgens"))  ## Output: Mariel J.
print(generated_function("Mariel", "Jurgens"))  ## Output: Mariel J.
print(generated_function("Alida", "Bogle"))  ## Output: Alida B.
print(generated_function("Alida", "Bogle"))  ## Output: Alida B.
print(generated_function("Alida", "Bogle"))  ## Output: Alida B.
print(generated_function("Jacqualine", "Olague"))  ## Output: Jacqualine O.
print(generated_function("Jacqualine", "Olague"))  ## Output: Jacqualine O.
print(generated_function("Jacqualine", "Olague"))  ## Output: Jacqualine O.
print(generated_function("Joaquin", "Clasen"))  ## Output: Joaquin C.
print(generated_function("Joaquin", "Clasen"))  ## Output: Joaquin C.
print(generated_function("Joaquin", "Clasen"))  ## Output: Joaquin C.
print(generated_function("Samuel", "Richert"))  ## Output: Samuel R.
print(generated_function("Samuel", "Richert"))  ## Output: Samuel R.
print(generated_function("Samuel", "Richert"))  ## Output: Samuel R.
print(generated_function("Malissa", "Marcus"))  ## Output: Malissa M.
print(generated_function("Malissa", "Marcus"))  ## Output: Malissa M.
print(generated_function("Malissa", "Marcus"))  ## Output: Malissa M.
print(generated_function("Alaina", "Partida"))  ## Output: Alaina P.
print(generated_function("Alaina", "Partida"))  ## Output: Alaina P.
print(generated_function("Alaina", "Partida"))  ## Output: Alaina P.
print(generated_function("Trinidad", "Mulloy"))  ## Output: Trinidad M.
print(generated_function("Trinidad", "Mulloy"))  ## Output: Trinidad M.
print(generated_function("Trinidad", "Mulloy"))  ## Output: Trinidad M.
print(generated_function("Carlene", "Garrard"))  ## Output: Carlene G.
print(generated_function("Carlene", "Garrard"))  ## Output: Carlene G.
print(generated_function("Carlene", "Garrard"))  ## Output: Carlene G.
print(generated_function("Melodi", "Chism"))  ## Output: Melodi C.
print(generated_function("Melodi", "Chism"))  ## Output: Melodi C.
print(generated_function("Melodi", "Chism"))  ## Output: Melodi C.
print(generated_function("Bess", "Chilcott"))  ## Output: Bess C.
print(generated_function("Bess", "Chilcott"))  ## Output: Bess C.
print(generated_function("Bess", "Chilcott"))  ## Output: Bess C.
print(generated_function("Chong", "Aylward"))  ## Output: Chong A.
print(generated_function("Chong", "Aylward"))  ## Output: Chong A.
print(generated_function("Chong", "Aylward"))  ## Output: Chong A.
print(generated_function("Jani", "Ramthun"))  ## Output: Jani R.
print(generated_function("Jani", "Ramthun"))  ## Output: Jani R.
print(generated_function("Jani", "Ramthun"))  ## Output: Jani R.
print(generated_function("Jacquiline", "Heintz"))  ## Output: Jacquiline H.
print(generated_function("Jacquiline", "Heintz"))  ## Output: Jacquiline H.
print(generated_function("Jacquiline", "Heintz"))  ## Output: Jacquiline H.
print(generated_function("Hayley", "Marquess"))  ## Output: Hayley M.
print(generated_function("Hayley", "Marquess"))  ## Output: Hayley M.
print(generated_function("Hayley", "Marquess"))  ## Output: Hayley M.
print(generated_function("Andria", "Spagnoli"))  ## Output: Andria S.
print(generated_function("Andria", "Spagnoli"))  ## Output: Andria S.
print(generated_function("Andria", "Spagnoli"))  ## Output: Andria S.
print(generated_function("Irwin", "Covelli"))  ## Output: Irwin C.
print(generated_function("Irwin", "Covelli"))  ## Output: Irwin C.
print(generated_function("Irwin", "Covelli"))  ## Output: Irwin C.
print(generated_function("Gertude", "Montiel"))  ## Output: Gertude M.
print(generated_function("Gertude", "Montiel"))  ## Output: Gertude M.
print(generated_function("Gertude", "Montiel"))  ## Output: Gertude M.
print(generated_function("Stefany", "Reily"))  ## Output: Stefany R.
print(generated_function("Stefany", "Reily"))  ## Output: Stefany R.
print(generated_function("Stefany", "Reily"))  ## Output: Stefany R.
print(generated_function("Rae", "Mcgaughey"))  ## Output: Rae M.
print(generated_function("Rae", "Mcgaughey"))  ## Output: Rae M.
print(generated_function("Rae", "Mcgaughey"))  ## Output: Rae M.
print(generated_function("Cruz", "Latimore"))  ## Output: Cruz L.
print(generated_function("Cruz", "Latimore"))  ## Output: Cruz L.
print(generated_function("Cruz", "Latimore"))  ## Output: Cruz L.
print(generated_function("Maryann", "Casler"))  ## Output: Maryann C.
print(generated_function("Maryann", "Casler"))  ## Output: Maryann C.
print(generated_function("Maryann", "Casler"))  ## Output: Maryann C.
print(generated_function("Annalisa", "Gregori"))  ## Output: Annalisa G.
print(generated_function("Annalisa", "Gregori"))  ## Output: Annalisa G.
print(generated_function("Annalisa", "Gregori"))  ## Output: Annalisa G.
print(generated_function("Jenee", "Pannell"))  ## Output: Jenee P.
print(generated_function("Jenee", "Pannell"))  ## Output: Jenee P.
print(generated_function("Jenee", "Pannell"))  ## Output: Jenee P.
print(generated_function("Launa", "Withers"))  ## Output: Launa W.
print(generated_function("Lakenya", "Edison"))  ## Output: Lakenya E.
print(generated_function("Brendan", "Hage"))  ## Output: Brendan H.
print(generated_function("Bradford", "Lango"))  ## Output: Bradford L.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Rudolf A.
print(generated_function("Lara", "Constable"))  ## Output: Lara C.
print(generated_function("Madelaine", "Ghoston"))  ## Output: Madelaine G.
print(generated_function("Salley", "Hornak"))  ## Output: Salley H.
print(generated_function("Micha", "Junkin"))  ## Output: Micha J.
print(generated_function("Teddy", "Bobo"))  ## Output: Teddy B.
print(generated_function("Coralee", "Scalia"))  ## Output: Coralee S.
print(generated_function("Jeff", "Quashie"))  ## Output: Jeff Q.
print(generated_function("Vena", "Babiarz"))  ## Output: Vena B.
print(generated_function("Karrie", "Lain"))  ## Output: Karrie L.
print(generated_function("Tobias", "Dermody"))  ## Output: Tobias D.
print(generated_function("Celsa", "Hopkins"))  ## Output: Celsa H.
print(generated_function("Kimberley", "Halpern"))  ## Output: Kimberley H.
print(generated_function("Phillip", "Rowden"))  ## Output: Phillip R.
print(generated_function("Elias", "Neil"))  ## Output: Elias N.
print(generated_function("Lashanda", "Cortes"))  ## Output: Lashanda C.
print(generated_function("Mackenzie", "Spell"))  ## Output: Mackenzie S.
print(generated_function("Kathlyn", "Eccleston"))  ## Output: Kathlyn E.
print(generated_function("Georgina", "Brescia"))  ## Output: Georgina B.
print(generated_function("Beata", "Miah"))  ## Output: Beata M.
print(generated_function("Desiree", "Seamons"))  ## Output: Desiree S.
print(generated_function("Jeanice", "Soderstrom"))  ## Output: Jeanice S.
print(generated_function("Mariel", "Jurgens"))  ## Output: Mariel J.
print(generated_function("Alida", "Bogle"))  ## Output: Alida B.
print(generated_function("Jacqualine", "Olague"))  ## Output: Jacqualine O.
print(generated_function("Joaquin", "Clasen"))  ## Output: Joaquin C.
print(generated_function("Samuel", "Richert"))  ## Output: Samuel R.
print(generated_function("Malissa", "Marcus"))  ## Output: Malissa M.
print(generated_function("Alaina", "Partida"))  ## Output: Alaina P.
print(generated_function("Trinidad", "Mulloy"))  ## Output: Trinidad M.
print(generated_function("Carlene", "Garrard"))  ## Output: Carlene G.
print(generated_function("Melodi", "Chism"))  ## Output: Melodi C.
print(generated_function("Bess", "Chilcott"))  ## Output: Bess C.
print(generated_function("Chong", "Aylward"))  ## Output: Chong A.
print(generated_function("Jani", "Ramthun"))  ## Output: Jani R.
print(generated_function("Jacquiline", "Heintz"))  ## Output: Jacquiline H.
print(generated_function("Hayley", "Marquess"))  ## Output: Hayley M.
print(generated_function("Andria", "Spagnoli"))  ## Output: Andria S.
print(generated_function("Irwin", "Covelli"))  ## Output: Irwin C.
print(generated_function("Gertude", "Montiel"))  ## Output: Gertude M.
print(generated_function("Stefany", "Reily"))  ## Output: Stefany R.
print(generated_function("Rae", "Mcgaughey"))  ## Output: Rae M.
print(generated_function("Cruz", "Latimore"))  ## Output: Cruz L.
print(generated_function("Maryann", "Casler"))  ## Output: Maryann C.
print(generated_function("Annalisa", "Gregori"))  ## Output: Annalisa G.
print(generated_function("Jenee", "Pannell"))  ## Output: Jenee P.


print(generated_function("Ava", "Bennett"))  ### Output: Ava B.
print(generated_function("Lily", "Anderson"))  ### Output: Lily A.
print(generated_function("Samuel", "Wright"))  ### Output: Samuel W.
print(generated_function("Harper", "Taylor"))  ### Output: Harper T.
print(generated_function("Nolan", "Cooper"))  ### Output: Nolan C.
print(generated_function("Liam", "Carter"))  ### Output: Liam C.
print(generated_function("Logan", "Smith"))  ### Output: Logan S.
print(generated_function("Caleb", "Mitchell"))  ### Output: Caleb M.
print(generated_function("Olivia", "Parker"))  ### Output: Olivia P.
print(generated_function("Aiden", "Clark"))  ### Output: Aiden C.
print(generated_function("Sophia", "Coleman"))  ### Output: Sophia C.
print(generated_function("Owen", "Morgan"))  ### Output: Owen M.
print(generated_function("Zoey", "Turner"))  ### Output: Zoey T.
print(generated_function("Madison", "Foster"))  ### Output: Madison F.
print(generated_function("Gabriel", "Hayes"))  ### Output: Gabriel H.
print(generated_function("Grace", "Harrison"))  ### Output: Grace H.
print(generated_function("Emma", "Reynolds"))  ### Output: Emma R.
print(generated_function("Carter", "Edwards"))  ### Output: Carter E.
print(generated_function("Chloe", "Adams"))  ### Output: Chloe A.
print(generated_function("Jackson", "Turner"))  ### Output: Jackson T.
print(generated_function("Elijah", "Foster"))  ### Output: Elijah F.
print(generated_function("Scarlett", "Walker"))  ### Output: Scarlett W.
print(generated_function("Caleb", "Johnson"))  ### Output: Caleb J.
print(generated_function("Wyatt", "Davis"))  ### Output: Wyatt D.
print(generated_function("Hannah", "Martin"))  ### Output: Hannah M.
print(generated_function("Isabella", "Brooks"))  ### Output: Isabella B.
print(generated_function("Benjamin", "Hayes"))  ### Output: Benjamin H.
print(generated_function("Mason", "Thompson"))  ### Output: Mason T.
print(generated_function("Amelia", "Nelson"))  ### Output: Amelia N.
print(generated_function("Abigail", "Cooper"))  ### Output: Abigail C.

# TEST SCRIPTS APPENDED!


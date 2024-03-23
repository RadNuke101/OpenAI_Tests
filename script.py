import csv, glob, os, pandas, marko
from datetime import datetime
from openai import OpenAI
os.chdir(r"/Users/HALAdmin/StudioProjects/Pranav/table/")
client = OpenAI(api_key="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")

current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
str_current_datetime = str(current_datetime)
print("DATE", str_current_datetime)

####################################################
dict = {}
workbook = pandas.read_excel(r"/Users/HALAdmin/StudioProjects/Pranav/Purdue Research Table Notes.xlsx", usecols="B,C", index_col=0)
# print(workbook)
workbook = workbook.where(pandas.notnull(workbook), None)
# print (workbook.to_dict()["Human Prompt"])
dict = workbook.to_dict()["Human Prompt"]
# for key in dict:
#     print ("KEY:", key)
#     print ("VALUE:", dict[key])
####################################################

for input_file in glob.glob("*.sl"):
    d = '∎'
    f = open(input_file,'r')

    reader = csv.reader(f,delimiter=d)
    ncol = len(next(reader)) # Read first line and count columns
    '''
    print("========================================================")
    print ("FILE NAME:", input_file)
    print ("NCOL:", ncol)
    print ("PROMPT:", dict[input_file])
    print("========================================================")
    print("========================================================")
    '''
    # r = 0

    input = []
    output = []
    input_output_string = ""

    f.seek(0)              # go back to beginning of file
    for row in reader:
        # print("FULL ROW:", row)
        # for c in range(ncol):
        #     print(" COL:", c, ":", row[c])
        try:
            str_temp = ""

            last_column = row[ncol-1]
            output.append(last_column)
            # print("INPUT ROW ORIGINAL:", row)

            input.append(row[0:ncol-1])

            str_temp = "given input as " + str(row[0:ncol-1]) + " output is " + str(last_column) + ", "
            input_output_string = input_output_string + str_temp

            print("INPUT ROW:" + str_temp)

            '''
            print("INPUT ROW AFTER SLICING:", row[0:ncol-1])
            print("OUTPUT ROW:", last_column)
            print("INPUT ARRAY:", input)
            print("OUTPUT ARRAY:", output)
            '''
        except IndexError:
            print("IndexError:", input_file)
        # finally:
        #    print("IndexError:finally")

        # print("==============================:", r)
        # r = r + 1

    '''
    print("INPUT FINAL:", input)
    print("OUTPUT FINAL:", output)
    '''
    print("INPUT FINAL :" + input_output_string)

    content = ""
    try:
        if dict[input_file] is None or str(input) is None or str(output) is None:
            None
        else:
            content = "Given that the input and output is " + input_output_string + \
                ", generate summary for every input column data " \
                    "(one summary per entire column, not per row) and " \
                        "one summary for output column (one summary for the entire output column, not by row)."

            # content = "The prompt describes the relationship between the inputs and outputs. Given that the prompt is: " \
            #     + dict[input_file] + ", and " + input_output_string + ", generate a python function that returns the output when given the input, " \
            #             "treating the input and output as strings, not lists. Add the input, output, " \
            #                 "and prompt to the comment section of the python code."

            # content = "The prompt describes the relationship between the inputs and outputs. Given that the prompt is: " \
            #     + dict[input_file] + ", and the input is: " + str(input) + ", and the output is " \
            #         + str(output) + ", generate a python function that returns the output when given the input, " \
            #             "treating the input and output as strings, not lists. Add the input, output, " \
            #                 "and prompt to the comment section of the python code."

            print ("PROMPT CONTENT:", content)

        # content = "Given the input as : " + str(input) + ", and the output as " \
        #          + str(output) + ", generate a prompt that will return the output when given the input, taking into account the grammar. " \
        #             "The prompt should describe the relationship between the inputs and outputs."

        # content = "The prompt describes the relationship between the inputs and outputs. Given that the prompt is: " \
        #      + dict[input_file] + ", and the input is: " + str(input) + ", and the output is " \
        #          + str(output) + ", generate a python function that returns the output when given the input, with no extra test code to validate the function."

    # except NoneType:
    #     print("NoneType:", input_file)
    except KeyError:
        print("KeyError:", input_file)
    # finally:
    #        print("KeyError: finally")
    # print("CONTENT:", content)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.2,
        max_tokens=3000,
        messages=[
            {"role": "user", "content": content},
            {"role": "system", "content": "You are a helpful assistant."},
        ]
    )

    input = []
    output = []
    res = response.choices[0].message.content
    # Parse the Markdown response
    doc = marko.parse(res)
    #print(doc)
    # Extract Python code from the Markdown AST
    python_code = ''.join(''.join(raw.children) for node in doc.children if isinstance(node, marko.block.FencedCode) for raw in node.children)
    # Write the extracted Python code to another file
    # print("PYTHON CODE:", python_code)

    # Gets current working directory
    file_path = os.getcwd()
    # Joins the folder that we wanted to create
    file_path = os.path.join(file_path, "txt_" + input_file.replace(".sl",""))
    # file_path = os.path.join(file_path, input_file.replace(".sl",""))
    # print("DIRECTORY:", file_path)

    isExist = os.path.exists(file_path)
    if not isExist:
        os.makedirs(file_path)
        # print("The new directory is created!" + file_path)

    output_file = input_file + "." + str_current_datetime + ".txt"
    # print("OUTPUT FILE NAME:", output_file)
    with open(os.path.join(file_path, output_file), 'w') as temp_file:
        temp_file.write(res)
        # temp_file.write(python_code)
    temp_file.close()


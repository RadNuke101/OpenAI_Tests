import csv, glob, os, pandas, marko, time
from datetime import datetime
from openai import OpenAI

os.chdir(r"/Users/HALAdmin/StudioProjects/Pranav/table/")
# client = OpenAI(api_key="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")
client = OpenAI(api_key="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")

final_output_dict = {}
current_datetime2 = datetime.now().strftime("%Y%m%d%H%M")
str_current_datetime2 = str(current_datetime2)
print("DATE NO SECONDS:", str_current_datetime2)

# Create empty dictionary with all the sl files as keys
for in_file in glob.glob("*.sl"):
    final_output_dict[in_file] = []

# Enter of number of times to repeat in the range below
for x in range (20):
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")

    str_current_datetime = str(current_datetime)
    print("DATE:", str_current_datetime)

    ####################################################
    dict = {}
    cc = 0
    workbook = pandas.read_excel(r"/Users/HALAdmin/StudioProjects/Pranav/Purdue Research Table Notes.xlsx", usecols="B,C", index_col=0)
    # print(workbook)
    workbook = workbook.where(pandas.notnull(workbook), None)
    # print (workbook.to_dict()["Human Prompt"])
    dict = workbook.to_dict()["Human Prompt"]
    # for key in dict:
    #     print ("KEY:", key)
    #     print ("VALUE:", dict[key])
    ####################################################

    # with open("/Users/HALAdmin/StudioProjects/Pranav/final_output_" + str_current_datetime + ".output", 'w') as final_out_file:
    #     final_out_file.write("FINAL OUTPUT:\n")
    # final_out_file.close()

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
            except Exception as e:
                print("Exception while reading the input and output from the sl file:", e)

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
                # content = "Given that the input and output is " + input_output_string + \
                #     ", generate summary for every input column data " \
                #         "(one summary per entire column, not per row) and " \
                #             "one summary for output column (one summary for the entire output column, not by row)."

                content = "Given that " + input_output_string + ", generate a python function that matches the given input and output above, " \
                    "treating the input and output as strings, not lists. Add the input and output statements to the comment section " \
                        "of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types " \
                            "of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. " \
                                "Do not include the output of the test code in the python program. " \
                                    "Generated python code should have only executable statements and comments, nothng else."
                
                # content = "The prompt describes the relationship between the inputs and outputs. Given that the prompt is: " \
                #     + dict[input_file] + ", and " + input_output_string + ", generate a python function that matches the input and output, " \
                #         "treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section " \
                #             "of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types " \
                #                 "of input exceptions. The code should be clean to run at a command prompt without any noncode"

                # content = "The prompt describes the relationship between the inputs and outputs. Given that the prompt is: " \
                #     + dict[input_file] + ", and the input is: " + str(input) + ", and the output is " \
                #         + str(output) + ", generate a python function that returns the output when given the input, " \
                #             "treating the input and output as strings, not lists. Add the input, output, " \
                #                 "and prompt to the comment section of the python code."

            # content = "Given the input as : " + str(input) + ", and the output as " \
            #          + str(output) + ", generate a prompt that will return the output when given the input, taking into account the grammar. " \
            #             "The prompt should describe the relationship between the inputs and outputs."

            # content = "The prompt describes the relationship between the inputs and outputs. Given that the prompt is: " \
            #      + dict[input_file] + ", and the input is: " + str(input) + ", and the output is " \
            #          + str(output) + ", generate a python function that returns the output when given the input, with no extra test code to validate the function."

                print ("PROMPT CONTENT:", content)

        # except NoneType:
        #     print("NoneType:", input_file)
        except KeyError:
            print("KeyError:", input_file)
        except Exception as e:
            print("Exception while building the cintent string:", e)

        start = datetime.now()
        start_time = time.perf_counter()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.2,
            max_tokens=3000,
            messages=[
                {"role": "user", "content": content},
                {"role": "system", "content": "You are a helpful assistant."},
            ]
        )

        res = response.choices[0].message.content
        # Parse the Markdown response
        doc = marko.parse(res)
        # Extract Python code from the Markdown AST
        python_code = ''.join(''.join(raw.children) for node in doc.children if isinstance(node, marko.block.FencedCode) for raw in node.children)
        # print("PYTHON CODE:", python_code)

        # Gets current working directory
        file_path = os.getcwd()
        # Joins the folder that we wanted to create
        file_path = os.path.join(file_path, "" + input_file.replace(".sl",""))
        # file_path = os.path.join(file_path, input_file.replace(".sl",""))
        # print("DIRECTORY:", file_path)

        isExist = os.path.exists(file_path)
        if not isExist:
            os.makedirs(file_path)
            # print("The new directory is created!" + file_path)

        output_file = input_file + "." + str_current_datetime + ".py"
        # print("OUTPUT FILE NAME:", output_file)

        with open(os.path.join(file_path, output_file), 'w') as py_file:
            # temp_file.write(res)
            py_file.write("# Start time: " + str(start))
            py_file.write("\n\n")
            py_file.write("# Content: " + content)
            py_file.write("\n\n")
            py_file.write(python_code)

            # calculate the elapsed time and print to the file
            end = datetime.now()
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            py_file.write("\n# End time: " + str(end))

            elapsed_time_string = "\n# Elapsed time in seconds: " + str(elapsed_time)
            print(elapsed_time_string)
            py_file.write(elapsed_time_string)
        py_file.close()

        # Execute python file
        try:
            os.system(f'/usr/local/bin/python3 {file_path}/{output_file} -> {file_path}/{output_file}.out')
        except FileNotFoundError:
            print(f"Error: The file '{output_file}' does not exist.")
        except Exception as e:
            print("exception while executing the python file:", e)

        diff = ()
        matched = False
        with open(os.path.join(file_path, output_file + ".out"), 'r') as temp_out_file:
            file_contents = temp_out_file.readlines()
            file_contents = [x.strip() for x in file_contents]
            # Convert the list to a set for faster lookups.
            file_contents_set = set(file_contents)
            output_set = set(output)
            # Find the items in the file that are not in the list.
            diff = set(file_contents) - output_set
            matched = file_contents_set.issubset(output_set)
            print("DIFFFFFFF:" + "".join(diff))
        temp_out_file.close()

        # final_output_dict[in_file] = []
        final_output_dict[input_file].append(input_file)
        final_output_dict[input_file].append(output_file)
        final_output_dict[input_file].append(str(matched))
        # final_output_dict[input_file].append("".join(diff))

        # comment this section for now
        try:
            with open("/Users/HALAdmin/StudioProjects/Pranav/output_" + str_current_datetime + ".log", 'a') as final_out_file2:
                # Write to the final output file
                final_out_file2.write(output_file + "\t" + str(matched) + "\t" + "".join(diff) + "\n")
            final_out_file2.close()
        except Exception as e:
            print("final output file:", e)

        # Write the original output
        try:
            with open(os.path.join(file_path, output_file + ".out"), 'a') as temp_out_file1:
                temp_out_file1.write("\n")
                temp_out_file1.write("ORIGINAL OUTPUT:\n")
                temp_out_file1.write("\n".join(output))
            temp_out_file1.close()
        except Exception as e:
            print("write the inputted output into python output file:", e)

    # Testing purpose only
        # cc = cc + 1
        # if cc > 5:
        #     break

# Final output in tab delimitted format
print ("FINAL DICT:", final_output_dict)
with open("/Users/HALAdmin/StudioProjects/Pranav/final_output_" + str_current_datetime2 + ".txt", 'a') as final_output_dict_file:
    # Write to the final output file
    try:
        for i in final_output_dict:
            row_string = "\t".join(final_output_dict[i]) + "\n"
            print("FINAL DICT ROWS:", "\t", row_string)
            final_output_dict_file.write(row_string)
    except Exception as e:
        print("final tab delimitted output file: ", e)
final_output_dict_file.close()


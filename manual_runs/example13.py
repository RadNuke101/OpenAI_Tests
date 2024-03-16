def remove_words(input_string):
  word_list = ["Inc", "Company", "Corporation", "Enterprises"]
  output_string = input_string
  for word in word_list:
    output_string = output_string.replace(word, "").strip()
  return output_string
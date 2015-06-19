import os


def edit_file(file_name, to_file_name, delimiter="\t", replacement_value="", exact_values=[], near_values=[]):
	"""takes a file with delimiter (default ",") and replaces values specified and writes a new file"""

	def replace_empty(in_question):
		if in_question.lower().strip() in exact_values or 	any(in_question.lower().strip() in near for near in near_values):
			return replacement_value
		else:
			return in_question

	def make_csv_line(line):
	    """reads a line and replaces exact_values then produces csv line"""
	    line_list=[item.replace(",", "\",\"") for item in get_line(line, delimiter)]
	    return str(line_list)[1:][:-1].replace("'","")

	def get_line(line, delimiter):
		"""replaces exact_values with appropriate value"""
		return [replace_empty(col).strip() for col in line.split(delimiter)]

	with open(file_name, 'r') as f:
		with open(to_file_name, 'w') as t:
			for line in f:
				to_line=make_csv_line(line)
				t.write(to_line + '\n')
	return "Done"

exact_values=["none","nan", "na",".","null", "n/a"]


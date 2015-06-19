import os


def edit_file(file_name, to_file_name, delimiter, replacement_value, exact_values=[], near_values=[]):
	"""takes a file with delimiter (default ",") and replaces values specified and writes a new file"""

	def replace_empty(in_question):
		if in_question.lower().strip().strip("\"") in exact_values or any(in_question.lower().strip() in near for near in near_values):
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
	return "Done."


def edit_all_files(direc, to_direc,file_type, delimiter, replacement_value, exact_values=[], near_values=[]):
    """moves recursively through a directory and returns the list of files within it all subdirectories"""
    file_list=[]
    for element in os.listdir(direc):
    	if os.path.isdir(element):
    		edit_all_files(os.path.join(direc, element), os.path.join(to_direc, element),delimiter, replacement_value, exact_values, near_values)
    	elif os.path.splitext(element)[1]==file_type:
    		edit_file(os.path.join(direc,element),os.path.join(to_direc,element),delimiter, replacement_value, exact_values, near_values)
    return "All done."



exact_values=["none","nan", "na",".","\"n/a\"", "\"\"", "null", "n/a"]


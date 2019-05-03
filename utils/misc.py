
import os
import ntpath


def delim(p):
	if not p.endswith('/'):
		return '/'
	return ''


def get_paths_and_names(path):
	if os.path.isdir(path):
		return list(zip(
			[path + delim(path) + file for file in os.listdir(path)],
			[file.replace('.csv', '') for file in os.listdir(path)]))
	else:
		return list(zip([path], [ntpath.basename(path).replace('.csv', '')]))


def indent(text, spaces=4):
	spaces = ' ' * spaces
	return '\n'.join(spaces + line if line.strip() != '' else line for line in text.split('\n'))


def is_xor(*args):
	return [bool(a) for a in args].count(True) == 1


def listget(li, index, fallback=None):
	try:
		return li[index]
	except IndexError:
		return fallback


def sort_column_labels(labels):
	first = [labels.pop(labels.index('method_name'))]
	labels.sort()

	return first + labels


def write_df_to_csv(dir, df, name):
	if not os.path.exists(dir):
		os.makedirs(dir)

	df.to_csv(dir + '/' + name + ".csv")

import os
import sys
import javalang as jl
import pandas as pd
from utils.misc import indent


def find_god_classes(source=None):
	print('\n> Looking for god classes in "%s"...' % os.path.abspath(source))
	# creates new dataframe
	df = pd.DataFrame(columns=['class_name', 'method_num', 'path_to_source'])

	# goes through the project content
	for root, dirs, files in os.walk(source, topdown=False):
		for name in files:
			# mathces only java sources
			if name.endswith('.java'):
				with(open(root + '/' + name, 'r')) as jsc:

					# creates the AST
					tree = jl.parse.parse(jsc.read())

					# iterates through the AST (first filtering all the non-class declarations)
					for path, node in tree.filter(jl.parser.tree.ClassDeclaration):
						# adds the new class to the data frame (as well as the class details)
						df = df.append({
							'class_name': node.name,
							'path_to_source': root + '/' + node.name + '.java',
							'method_num': len(node.methods)
						}, ignore_index=True, sort=-1)
	# Filters the dataframe getting only the god classes
	god_classes = filter_all_classes(df)
	print('> Found the following god classes:\n'+indent(god_classes.to_string()))

	return god_classes


def filter_all_classes(all_classes):
	all_classes.sort_values('method_num', ascending=False, inplace=True)
	all_classes.reset_index(drop=True, inplace=True)

	cond = all_classes.method_num.mean() + 6 * all_classes.method_num.std()

	return all_classes.query('method_num > %s' % cond)


def find_god_classes_argparse(args):
	if args.source is None or not os.path.exists(args.source):
		print('Enter a valid path to a source code...')
		sys.exit(0)

	find_god_classes(source=args.source)

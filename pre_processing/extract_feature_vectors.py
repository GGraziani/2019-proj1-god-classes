import os
import sys
import datetime
import numpy as np
import javalang as jl

from pre_processing.find_god_classes import find_god_classes
from utils.feature_vector_utils import get_fields_accessed_by_method, get_methods_accessed_by_method, fv_dict_to_df
from utils.misc import write_df_to_csv

DEF_FVS_DIR = "./res/feature_vectors"
FV_DIR = DEF_FVS_DIR + '/' + str(int(datetime.datetime.now().timestamp()*1000))


def extract_feature_vectors(god_classes):
	print('\n> Starting feature vector extraction...')
	class_names = god_classes.class_name.tolist()
	all_feat_vectors = {}
	for src_path in god_classes.path_to_source.tolist():
		with(open(src_path, 'r')) as jsc:
			tree = jl.parse.parse(jsc.read())

			for path, node in tree.filter(jl.parser.tree.ClassDeclaration):
				if node.name in class_names:
					all_feat_vectors[node.name] = generate_all(node)
					write_df_to_csv(FV_DIR, all_feat_vectors[node.name], node.name)

	fv_dir = os.path.abspath(FV_DIR)
	print('> Feature vector/s has/ve been written to folder "%s"' % fv_dir)

	return fv_dir


def generate_all(node):
	fields = get_fields(node)
	methods = get_methods(node)

	fv_dict = {}

	for method in node.methods:
		fv = generate_feat_vector(method, fields, methods)
		add_vector(fv, fv_dict)

	df = fv_dict_to_df(fv_dict)

	return df


def get_fields(node):
	return [field.declarators[len(field.declarators) - 1].name for field in node.fields]


def get_methods(node):
	return np.unique([method.name for method in node.methods])


def generate_feat_vector(method, fields, methods):
	row = {'method_name': method.name}

	acc_fields = get_fields_accessed_by_method(method, fields)
	acc_methods = get_methods_accessed_by_method(method, methods)

	for field in list(acc_fields)+list(acc_methods):
		row[field] = 1

	return row


def add_vector(fv, fv_dict):
	if fv['method_name'] in fv_dict:
		fv_dict[fv['method_name']].update(fv)
	else:
		fv_dict[fv['method_name']] = fv


def extract_feature_vectors_argparse(args):
	if args.source is None or not os.path.exists(args.source):
		print("Enter a valid path to a source code...")
		sys.exit(0)

	god_classes = find_god_classes(source=args.source)
	extract_feature_vectors(god_classes)

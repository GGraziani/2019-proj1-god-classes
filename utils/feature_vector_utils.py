import javalang as jl
import numpy as np
import pandas as pd

from utils.misc import sort_column_labels


def get_fv_values(csv_path):
	return pd.read_csv(csv_path, index_col=0).sort_values('method_name').drop(['method_name'], axis=1).values


def get_fv_methods(csv_path):
	return pd.read_csv(csv_path, index_col=0).sort_values('method_name')['method_name'].tolist()


def get_fv_names_n_values(csv_path):
	df = pd.read_csv(csv_path, index_col=0)

	return df['method_name'].values, df.drop(['method_name'], axis=1).values


def get_fields_accessed_by_method(method, fields):
	return get_method_accesses(method, fields, jl.parser.tree.MemberReference)


def get_methods_accessed_by_method(method, methods):
	return get_method_accesses(method, methods, jl.parser.tree.MethodInvocation)


def get_method_accesses(method, arr, tree_filter):
	return np.unique([node.member for path, node in method.filter(tree_filter) if node.member in arr])


def fv_dict_to_df(vec_dict):
	df = pd.DataFrame([vec_dict.get(k) for k in vec_dict.keys()])
	df = df.reindex(columns=sort_column_labels(df.columns.tolist()))
	df = df.fillna(0)
	df[[col for col in df.columns if col != 'method_name']] = df[
		[col for col in df.columns if col != 'method_name']].astype('int')

	return df

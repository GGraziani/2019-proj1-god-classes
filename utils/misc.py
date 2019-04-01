import os
import ntpath
import pandas as pd


def get_paths_and_names(path):
	if os.path.isdir(path):
		return list(zip([path + delim(path) + file for file in os.listdir(path)], [file.replace('.csv', '') for file in os.listdir(path)]))
	else:
		return list(zip([path], [ntpath.basename(path).replace('.csv', '')]))


def delim(p):
	if not p.endswith('/'):
		return '/'
	return ''


def get_fv_values(fv_path):
	return pd.read_csv(fv_path, index_col=0).sort_values('method_name').drop(['method_name'], axis=1).values


def get_fv_methods(fv_path):
	return pd.read_csv(fv_path, index_col=0).sort_values('method_name')['method_name'].tolist()


def get_fv_names_n_values(df):
	return df['method_name'].values, df.drop(['method_name'], axis=1).values


def write_df_to_csv(dir, df, name):
	if not os.path.exists(dir):
		os.makedirs(dir)

	df.to_csv(dir + '/' + name + ".csv")


def sort_column_labels(labels):
	first = [labels.pop(labels.index('method_name'))]
	labels.sort()

	return first + labels

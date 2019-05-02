import pandas as pd
from utils.misc import get_paths_and_names, write_df_to_csv

DEF_CLS_DIR = "./res/clusters"


def do_all_cluster_from_path(path, target, f, k):

	paths_and_names = get_paths_and_names(path)

	for el in paths_and_names:
		df = f(el[0], k)

		write_df_to_csv(target, df, el[1])


def cluster_to_df(ids, methods):
	data = [{'cluster_id': k, 'method_name': v} for k, v in zip(ids, methods)]

	df = pd.DataFrame(data, columns=['cluster_id', 'method_name'])
	df.sort_values(['cluster_id', 'method_name'], inplace=True, ascending=True)
	df.set_index('method_name', inplace=True)

	return df


def read_cl_to_df(cl_path, sort_field):
	return pd.read_csv(cl_path, index_col=0).sort_values(sort_field).cluster_id.values

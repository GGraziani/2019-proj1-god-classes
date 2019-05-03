import datetime
import pandas as pd
from utils.misc import get_paths_and_names, write_df_to_csv

R = 10
CL_DIR = './res/clusters/'


def cluster_to_df(ids, methods):
	data = [{'cluster_id': k, 'method_name': v} for k, v in zip(ids, methods)]

	df = pd.DataFrame(data, columns=['cluster_id', 'method_name'])
	df.sort_values(['cluster_id', 'method_name'], inplace=True, ascending=True)
	df.set_index('method_name', inplace=True)

	return df


def read_cl_to_df(cl_path, sort_field):
	return pd.read_csv(cl_path, index_col=0).sort_values(sort_field).cluster_id.values


def get_target_dir(sub_dir):
	return CL_DIR + sub_dir + '-' + str(int(datetime.datetime.now().timestamp() * 1000))


def do_all_cluster_from_path(
			path=None,
			target=None,
			f=None,
			n=5):

	print(path)
	print(target)
	print(f)
	print(n)

	paths_and_names = get_paths_and_names(path)

	for el in paths_and_names:
		df = f(el[0], n)

		write_df_to_csv(target, df, el[1])

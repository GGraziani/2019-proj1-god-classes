import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import datetime
import pandas as pd

from utils.misc import sort_column_labels, write_df_to_csv, get_paths_and_names
from utils.feature_vector_utils import get_fv_methods

DEF_GT_DIR = "./res/ground_truths"
GT_DIR = DEF_GT_DIR + '/' + str(int(datetime.datetime.now().timestamp()*1000))


def get_keywords(file):
	content = open(file).readlines()
	return list(map(lambda x: str(x).replace("\n", ""), content))


def do_ground_truth_all(files, kws):
	for p, n in files:
		methods = get_fv_methods(p)
		ground_truth = do_ground_truth(methods, kws)

		write_df_to_csv(GT_DIR, gt_to_df(ground_truth, kws), n)


def do_ground_truth(methods, keywords):
	gt = {}
	for m in methods:
		k = find_match(m, keywords)

		if k in gt:
			gt[k] = gt[k] + [m]
		else:
			gt[k] = [m]

	return gt


def find_match(name, kws):
	for k in kws:
		if k in name.lower():
			return k
	return "none"


def gt_to_df(gt, kws):
	df = pd.DataFrame(columns=['method_name'] + kws)
	for key, value in gt.items():
		for v in value:
			df = df.append({'method_name': v, key: 1}, ignore_index=True, sort=-1)

	df = df.reindex(columns=sort_column_labels(df.columns.tolist()))
	df = df.fillna(0)
	df[[col for col in df.columns if col != 'method_name']] = df[
		[col for col in df.columns if col != 'method_name']].astype('int')

	return df


if __name__ == '__main__':
	if len(sys.argv) < 3 or not os.path.exists(sys.argv[1]):
		print("Enter a the path to a cluster file and the path to the 'keywords.txt' file...")
		sys.exit(0)

	do_ground_truth_all(get_paths_and_names(sys.argv[1]), get_keywords(sys.argv[2]))

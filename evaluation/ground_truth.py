import os
import sys
import datetime
import pandas as pd
from utils.misc import sort_column_labels, write_df_to_csv, get_paths_and_names
from utils.feature_vector_utils import get_fv_methods

DEF_GT_DIR = "./res/ground_truths"
GT_DIR = DEF_GT_DIR + '/' + str(int(datetime.datetime.now().timestamp() * 1000))


def do_ground_truth(methods, keywords):
	gt = {}
	for m in methods:
		k = find_match(m, keywords)

		if k in gt:
			gt[k] = gt[k] + [m]
		else:
			gt[k] = [m]

	return gt


def do_ground_truth_all(
			files=None,
			kws=None):

	print('\n> Defining ground truth for feature vector/s:')
	[print("\t"+os.path.relpath(file[0])) for file in files]

	for p, n in files:
		methods = get_fv_methods(p)
		ground_truth = do_ground_truth(methods, kws)

		write_df_to_csv(GT_DIR, gt_to_df(ground_truth, kws), n)

	print('> Ground truth/s has/ve been written to folder "%s"' % os.path.abspath(GT_DIR))

	return GT_DIR


def find_match(name, kws):
	for k in kws:
		if k in name.lower():
			return k
	return "none"


def get_keywords(file):
	content = open(file).readlines()
	return list(map(lambda x: str(x).replace("\n", ""), content))


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


def ground_truth_argparse(args):
	if args.f_vector is None:
		print("Enter a path to a cluster (or a folder containing clusters).")
		sys.exit(0)
	elif not os.path.exists(args.f_vector):
		print(
			'%s is not a valid path, please enter a path to a valid feature vector (or a folder containing feature vectors)' % args.f_vector)
		sys.exit(0)
	elif not os.path.exists(args.keywords):
		print(
			'%s is not a valid path, please enter a path to a valid keyword file' % args.keywords)
		sys.exit(0)

	do_ground_truth_all(
		files=get_paths_and_names(args.f_vector),
		kws=get_keywords(args.keywords))

import os
import sys
import pandas as pd
from utils.misc import get_paths_and_names


def get_gt(gt_path):
	df = pd.read_csv(gt_path, index_col=0)
	cols = [el for el in df.columns.tolist() if el != 'method_name']
	gt = []

	for c in cols:
		v = df[df[c] == 1].method_name.tolist()
		if v:
			gt.append(v)
	return gt


def get_cl_dict(cl_path):
	df = pd.read_csv(cl_path, index_col=0)

	clusters = []
	for c in df.cluster_id.unique():
		v = df[df.cluster_id == c]
		clusters.append(v.index.values.tolist())
	return clusters


def get_all_i_pairs(lstlst):
	return [j for i in lstlst for j in get_i_pairs(i)]


def get_i_pairs(lst):
	return [(i, j) for i in lst for j in lst if i != j]


def merge_paths_and_names_lists(aa, bb):

	cc = {}
	for a in aa:
		for b in bb:
			if a[1] == b[1]:
				cc[a[1]] = [a[0], b[0]]
	return cc


def compute_precision_n_recall_all(cls, gts):

	for k, v in merge_paths_and_names_lists(cls, gts).items():

		cl = get_cl_dict(v[0])
		gt = get_gt(v[1])

		dk = set(get_all_i_pairs(cl))
		g = set(get_all_i_pairs(gt))

		p, r = compute_precision_n_recall(dk, g)

		print(k+": p="+str(p)+", r="+str(r))


def compute_precision_n_recall(ip_dk, ip_g):
	interception = ip_dk.intersection(ip_g)
	return round(len(interception)/len(ip_dk), 2), round(len(interception)/len(ip_g), 2)


def prec_recall_argparse(args):

	if args.cluster is None:
		print("Enter a path to a cluster (or a folder containing clusters).")
		sys.exit(0)
	elif not os.path.exists(args.cluster):
		print(
			'%s is not a valid path, please enter a path to a valid cluster (or a folder containing clusters)' % args.cluster)
		sys.exit(0)

	if args.g_truth is None:
		print("Enter a path to a ground truth (or a folder containing ground truths).")
		sys.exit(0)
	elif not os.path.exists(args.g_truth):
		print(
			'%s is not a valid path, please enter a path to a valid ground truth (or a folder containing ground truths)' % args.g_truth)
		sys.exit(0)

	cl_files = get_paths_and_names(args.cluster)
	gt_files = get_paths_and_names(args.g_truth)

	compute_precision_n_recall_all(cl_files, gt_files)

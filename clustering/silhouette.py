import sys
import os
from sklearn.metrics import silhouette_score
from utils.cluster_utils import read_cl_to_df
from clustering.k_means import k_means
from clustering.hierarchical import h_agglomerative
from utils.misc import get_paths_and_names, is_xor, indent
from utils.feature_vector_utils import get_fv_values

MAX_k = 40


def do_silhouette_all(fvs, cls):

	for path, name in fvs:
		X = get_fv_values(path)
		cl = get_cluster_by_name(cls, name)
		if cl:
			labels = read_cl_to_df(cl, 'method_name')
			print(name+' -->', silhouette_score(X, labels))


def find_best_k_all(fvs, n=MAX_k):
	for path, name in fvs:
		print('\n> Filename: %s\n' % name)
		print(indent('cluster\tK-Means\t Agglomerative'))
		[print(indent('\t\t'.join(m))) for m in find_best_k(get_fv_values(path), n)]


def find_best_k(fv, n):
	metrics = []
	for i in range(2, n):
		metrics.append((
			str(i),
			str(round(silhouette_score(fv, k_means(fv, i)), 2)),
			str(round(silhouette_score(fv, h_agglomerative(fv, i)), 2))
		))
	return metrics


def get_cluster_by_name(clusters, name):
	for p, n in clusters:
		if n == name:
			return p

	return None


def main(
		  fv=None,
		  cl=None,
		  n=None):

	fv_files = get_paths_and_names(fv)

	if cl:
		cl_files = get_paths_and_names(cl)
		do_silhouette_all(fv_files, cl_files)
	else:
		find_best_k_all(fv_files, int(n))


def silhouette_argparse(args):
	if args.f_vector is None:
		print("Enter a path to a feature vector (or a folder containing feature vectors).")
		sys.exit(0)
	elif not os.path.exists(args.f_vector):
		print('%s is not a valid path, please enter a path to a valid feature vector (or a folder containing feature vectors)' % args.f_vector)
		sys.exit(0)

	# Checks whether not both (cluster and n) are entered by the user.
	elif not is_xor(args.cluster, args.n):
		print('Silhouette does not support both inputs, cluster and n, to be entered together. '+
				'Please check out documentation and pick one of the available options.')
		sys.exit(0)

	if bool(args.cluster) and not os.path.exists(args.f_vector):
		print('%s is not a valid path, please enter a path to a valid cluster (or a folder containing clusters)' % args.cluster)
	elif bool(args.n) and not (str(args.n).isdigit() and int(args.n) > 2):
		print("%s is not a valid digit, please enter a positive integer greater that 1" % args.n)
		sys.exit(0)

	main(
		fv=args.f_vector,
		cl=args.cluster,
		n=args.n)

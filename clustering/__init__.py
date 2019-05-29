import sys
import os

from clustering.k_means import *
from clustering.hierarchical import *
from utils.cluster_utils import do_all_cluster_from_path, get_target_dir

ALGORITHMS = {
	'k-means': do_k_means,
	'hierarchical': do_h_agglomerative
}


def clustering_argparse(args):
	if args.f_vector is None:
		print("Enter a path to a feature vector (or a folder containing feature vectors).")
		sys.exit(0)
	elif not os.path.exists(args.f_vector):
		print('"%s" is not a valid path, please enter a path to a valid feature vector (or a folder containing feature vectors)' % args.f_vector)
		sys.exit(0)
	elif args.algorithm not in ALGORITHMS:
		print("%s is not a valid algorithm, please pick one between {k-means, hierarchical}" % args.algorithm)
		sys.exit(0)
	elif not str(args.n).isdigit() or int(args.n) < 2:
		print("%s is not a valid digit, please enter a positive integer greater that 1" % args.n)
		sys.exit(0)

	return do_all_cluster_from_path(
		path=args.f_vector,
		target=get_target_dir(args.algorithm),
		f=ALGORITHMS.get(args.algorithm),
		n=int(args.n)
	)


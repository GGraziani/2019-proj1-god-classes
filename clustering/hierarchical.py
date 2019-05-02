import os, sys, datetime
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

from sklearn.cluster import hierarchical

from utils.cluster_utils import *
from utils.feature_vector_utils import get_fv_names_n_values

CL_DIR = DEF_CLS_DIR + '/' + 'hierarchical-' + str(int(datetime.datetime.now().timestamp()*1000))


def h_agglomerative(values, n):
	return hierarchical.AgglomerativeClustering(n_clusters=n).fit_predict(values)


def do_h_agglomerative(csv_path, n):
	m, v = get_fv_names_n_values(csv_path)
	cluster_ids = h_agglomerative(v, n)
	return cluster_to_df(cluster_ids, m)


if __name__ == '__main__':
	if len(sys.argv) < 3 or not os.path.exists(sys.argv[1]):
		print("Enter a the path to a feature vector (or a folder containing feature vectors) and the number of clusters...")
		sys.exit(0)

	do_all_cluster_from_path(sys.argv[1], CL_DIR, do_h_agglomerative, int(sys.argv[2]))

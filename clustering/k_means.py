import os, sys, datetime
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

from sklearn.cluster import KMeans

from utils.cluster_utils import *
from utils.misc import *

R = 10
CL_DIR = DEF_CLS_DIR + '/' + 'kmeans-' + str(int(datetime.datetime.now().timestamp()*1000))


def k_means(values, n):
	return KMeans(n_clusters=n, random_state=R).fit_predict(values)


def do_k_means(df, n):
	m, v = get_fv_names_n_values(df)
	cluster_ids = k_means(v, n)
	return cluster_to_df(cluster_ids, m)


if __name__ == '__main__':
	if len(sys.argv) < 3 or not os.path.exists(sys.argv[1]):
		print("Enter a the path to a feature vector (or a folder containing feature vectors) and the number of clusters...")
		sys.exit(0)

	do_all_cluster_from_path(sys.argv[1], CL_DIR, do_k_means, int(sys.argv[2]))

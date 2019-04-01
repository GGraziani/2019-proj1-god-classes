import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
from sklearn.metrics import silhouette_score

from utils.cluster_utils import read_cl_to_df
from clustering.k_means import k_means
from clustering.hierarchical import h_agglomerative
from utils.misc import get_fv_values, get_paths_and_names


MAX_k = 40


def do_silhouette_all(fvs, cls):

	for path, name in fvs:
		X = get_fv_values(path)
		cl = get_cluster_by_name(cls, name)
		if cl:
			labels = read_cl_to_df(cl, 'method_name')
			print(name+' -->', silhouette_score(X, labels))


def find_best_k_all(fvs):
	for path, name in fvs:
		print('\nFilename: '+name)
		agglomerative, kmeans = find_best_k(get_fv_values(path))
		print("Agglomerative")
		[print(str(x[0]) + ", " + str(x[1])) for x in agglomerative]
		print("\nK-means")
		[print(str(x[0]) + ", " + str(x[1])) for x in kmeans]


def find_best_k(fv):
	aggl = []
	kmeans = []
	for i in range(2, MAX_k):
		aggl.append([i, round(silhouette_score(fv, h_agglomerative(fv, i)), 2)])
		kmeans.append([i, round(silhouette_score(fv, k_means(fv, i)), 2)])

	return aggl, kmeans


def get_cluster_by_name(clusters, name):
	for p, n in clusters:
		if n == name:
			return p

	return None


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Enter a the path to a feature vector or a folder containing feature vectors...")
		sys.exit(0)

	fv_files = get_paths_and_names(sys.argv[1])

	if len(sys.argv) == 3:
		cl_files = get_paths_and_names(sys.argv[2])
		do_silhouette_all(fv_files, cl_files)

	else:
		find_best_k_all(fv_files)

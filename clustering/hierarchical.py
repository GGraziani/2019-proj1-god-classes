from utils.feature_vector_utils import get_fv_names_n_values
from sklearn.cluster import hierarchical
from utils.cluster_utils import cluster_to_df


def h_agglomerative(values, n):
	return hierarchical.AgglomerativeClustering(n_clusters=n).fit_predict(values)


def do_h_agglomerative(csv_path, n):
	m, v = get_fv_names_n_values(csv_path)
	cluster_ids = h_agglomerative(v, n)
	return cluster_to_df(cluster_ids, m)


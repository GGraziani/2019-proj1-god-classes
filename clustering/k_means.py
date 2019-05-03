from utils.feature_vector_utils import get_fv_names_n_values
from sklearn.cluster import KMeans
from utils.cluster_utils import cluster_to_df


def k_means(values, n):
	return KMeans(n_clusters=n, random_state=R).fit_predict(values)


def do_k_means(csv_path, n):
	m, v = get_fv_names_n_values(csv_path)
	cluster_ids = k_means(v, n)
	return cluster_to_df(cluster_ids, m)

from utils.misc import indent

DOCSTRING = '''
2019-proj1-god-classes
by Gustavo Graziani

Commands:
{find_god_classes}
{extract_feature_vectors}
{clustering}
{silhouette}
{ground_truth}
{prec_recall}

TO SEE DETAILS ON EACH COMMAND, RUN
> python3 god_classes.py <command>
'''

MODULE_DOCSTRINGS = {
    'find_god_classes': '''
find_god_classes:
    Given a source code, computes and returns a list of god classes.

    Example usage:
        $ python3 god_classes.py find_god_classes -s <path-to-src>

    flags:
    -s <path-to-src> | --source <path-to-src>:
        The path to the source code.
''',
    'extract_feature_vectors': '''
extract_feature_vectors:
    For each god class found on the given source code, it computes and writes to csv the respective feature vector.

    Example usage:
        $ python3 god_classes.py extract_feature_vectors -s <path-to-src>

    flags:
    -s <path-to-src> | --source <path-to-src>:
        The path to the source code.
''',
    'clustering': '''
clustering:
    For each feature vector it generates n clusters (using the given algorithm) and writes the result/s to csv.

    Example usage:
        $ python3 god_classes.py clustering -a k_means -fv <path-to-feature_vector-or-folder> -n <number-of-clusters>

    flags:
    -a <algorithm-name> | --algorithm <algorithm-name>:
        The algorithm to use for generating the clusters.
        Available algorithms are "k_means" and "hierarchical"

    -fv <path-to-feature_vector-or-folder> | --feature_vector <path-to-feature_vector-or-folder>:
        The path to the feature vector/s.

    -n <positive-integer> | --number_of_clusters <positive-integer>:
       The number of clusters (1 < n).
''',
    'silhouette': '''
silhouette:
    - 1° case (with clustering file): for each pair of feature vector and respective cluster, it computes the silhouette 
    score and prints it to the stdout.
    - 2° case (without clustering file): for each feature vector it computes the silhouette metrics for both algorithms 
    with k ranging from 2 to n (default n=40).

    Example usage:
        1) $ python3 god_classes.py silhouette -fv <path-to-feature-vector-or-folder> -cl <path-to-cluster-or-folder>
        2) $ python3 god_classes.py silhouette -fv <path-to-feature-vector-or-folder> -n <num-of-clusters>

    flags:
    -fv <path-to-feature_vector-or-folder> | --feature_vector <path-to-feature_vector-or-folder>:
        The path to the feature vector/s.

    -cl <path-to-cluster-or-folder> | --cluster <path-to-cluster-or-folder>:
        The path to the cluster/s.
    
    -n <positive-integer> | --number_of_clusters <positive-integer>:
       The number of clusters (1 < n).
''',
    'ground_truth': '''
ground_truth:
    For each feature vector it computes the respective ground truth (based on the keywords) and writes it to a csv file.

    Example usage:
        $ python3 god_classes.py ground_truth -fv <path-to-feature-vector-or-folder> -k <path-to-keywords>

    flags:
    -fv <path-to-feature_vector-or-folder> | --feature_vector <path-to-feature_vector-or-folder>:
        The path to the feature vector/s.

    -k <path-to-keywords> | --keywords <path-to-keywords>:
       The path to the a text file containing keywords (e.g "./res/keywords.txt")
''',
    'prec_recall': '''
prec_recall:
    For each pair of cluster and respective ground truth, it computes precision and recall and prints it to the stdout.

    Example usage:
        $ python3 god_classes.py prec_recall -cl <path-to-cluster> -fv <path-to-feature-vector-or-folder>

    flags:
    -cl <path-to-cluster-or-folder> | --cluster <path-to-cluster-or-folder>:
        The path to the cluster/s.

    -gt <path-to-ground_truth-or-folder> | --ground_truth <path-to-ground_truth-or-folder>:
        The path to the a file containing the ground truth.
''',
    'run_all': '''
run_all:
    Run the whole analysis from the god classes detection to the results evaluation.

    Example usage:
        $ python3 god_classes.py run_all -cl <path-to-cluster> -fv <path-to-feature-vector-or-folder>

    flags:
    -s
'''
}


def docstring_preview(text):
    return text.split('\n\n')[0]


docstring_headers = {
    key: indent(docstring_preview(value))
    for (key, value) in MODULE_DOCSTRINGS.items()
}

DOCSTRING = DOCSTRING.format(**docstring_headers)




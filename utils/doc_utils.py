from utils.misc import indent

DOCSTRING = '''
2019-proj1-god-classes
by Gustavo Graziani

Commands:
{find_god_classes}
{extract_feature_vectors}
{clustering}
{silhouette}

TO SEE DETAILS ON EACH COMMAND, RUN
> python3 god_classes.py <command>
'''

MODULE_DOCSTRINGS = {
    'find_god_classes': '''
find_god_classes:
    Given a source code, computes and returns a list of god classes.

    Example usage:
        $ python3 god_classes.py find_god_classes -s <path-to-src>
''',

    'extract_feature_vectors': '''
extract_feature_vectors:
    For each god class found on the given source code, it computes and writes to csv the respective feature vector.

    Example usage:
        $ python3 god_classes.py extract_feature_vectors -s <path-to-src>
''',

    'clustering': '''
clustering:
    For each feature vector it generates n clusters (using the given algorithm) and writes the result/s to csv.

    Example usage:
        $ python3 god_classes.py clustering -a k_means -fv <path-to-feature_vector-or-folder> -n <number-of-clusters>
''',

    'silhouette': '''
silhouette:
    1° case (with clustering file): for each pair of feature vector and respective cluster, it computes the silhouette 
    score and prints it to the stdout.
    2° case (without clustering file): for each feature vector it computes the silhouette metrics for both algorithms 
    with k ranging from 2 to n (default n=40).

    Example usage:
        1) $ python3 god_classes.py silhouette -fv <path-to-feature-vector-or-folder> -cl <path-to-cluster-or-folder>
        2) $ python3 god_classes.py silhouette -fv <path-to-feature-vector-or-folder> -n <num-of-clusters>
'''
}


def docstring_preview(text):
    return text.split('\n\n')[0]


docstring_headers = {
    key: indent(docstring_preview(value))
    for (key, value) in MODULE_DOCSTRINGS.items()
}

DOCSTRING = DOCSTRING.format(**docstring_headers)




import sys
import argparse
from utils.doc_utils import *
from utils.misc import listget


# add one gateway function for each functionality
def find_god_classes_gateway(args):
    from pre_processing import find_god_classes
    find_god_classes.find_god_classes_argparse(args)


def extract_feature_vectors_gateway(args):
    from pre_processing import extract_feature_vectors
    extract_feature_vectors.extract_feature_vectors_argparse(args)


def clustering_gateway(args):
    import clustering
    clustering.clustering_argparse(args)


def silhouette_gateway(args):
    from clustering import silhouette
    silhouette.silhouette_argparse(args)


def ground_truth_gateway(args):
    from evaluation import ground_truth
    ground_truth.ground_truth_argparse(args)


def prec_recall_gateway(args):
    from evaluation import prec_recall
    prec_recall.prec_recall_argparse(args)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# add subparser for find_god_classes
p_find_god_classes = subparsers.add_parser('find_god_classes')
p_find_god_classes.add_argument('-s', '-src', '--source', dest='source', default=None)
p_find_god_classes.set_defaults(func=find_god_classes_gateway)

# add subparser for extract_feature_vectors
p_extract_feature_vectors = subparsers.add_parser('extract_feature_vectors')
p_extract_feature_vectors.add_argument('-s', '-src', '--source', dest='source', default=None)
p_extract_feature_vectors.set_defaults(func=extract_feature_vectors_gateway)

# add subparser for clustering
p_clustering = subparsers.add_parser('clustering')
p_clustering.add_argument('-a', '--algorithm', dest='algorithm', default='k-means')
p_clustering.add_argument('-fv', '--feature_vector', dest='f_vector', default=None)
p_clustering.add_argument('-n', '--number_of_clusters', dest='n', default=5)
p_clustering.set_defaults(func=clustering_gateway)

# add subparser for silhouette
p_silhouette = subparsers.add_parser('silhouette')
p_silhouette.add_argument('-fv', '--feature_vector', dest='f_vector', default=None)
p_silhouette.add_argument('-cl', '--cluster', dest='cluster', default=None)
p_silhouette.add_argument('-n', '--number_of_clusters', dest='n', default=None)
p_silhouette.set_defaults(func=silhouette_gateway)

# add subparser for ground_truth
p_ground_truth = subparsers.add_parser('ground_truth')
p_ground_truth.add_argument('-fv', '--feature_vector', dest='f_vector', default=None)
p_ground_truth.add_argument('-k', '--keywords', dest='keywords', default='res/keywords.txt')
p_ground_truth.set_defaults(func=ground_truth_gateway)

# add subparser for prec_recall
p_prec_recall = subparsers.add_parser('prec_recall')
p_prec_recall.add_argument('-cl', '--cluster', dest='cluster', default=None)
p_prec_recall.add_argument('-gt', '--ground_truth', dest="g_truth", default=None)
p_prec_recall.set_defaults(func=prec_recall_gateway)


def main(argv):

    helpstrings = {'', '-h', '--help'}

    command = listget(argv, 0, '').lower()

    # The user did not enter a command, or the entered command is not recognized.
    if command not in MODULE_DOCSTRINGS:
        print(DOCSTRING)
        if command == '':
            print('You are seeing the default help text because you did not choose a command.')
        elif command not in helpstrings:
            print('You are seeing the default help text because "%s" was not recognized' % command)
        return 1

    # The user entered a command, but no further arguments, or just help.
    argument = listget(argv, 1, '').lower()
    if argument in helpstrings:
        print(MODULE_DOCSTRINGS[command])
        return 1

    args = parser.parse_args(argv)
    args.func(args)

    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))

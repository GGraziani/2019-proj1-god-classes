# How to run
## Via command line

1. **Pre-processing**
    - find_god_classes.py:
        - *$ python3 pre_processing/find_god_classes.py <path-to-source-code>*
        - Outcome: prints to the stdout a dataframe containing god classes name and number of methods  
    - extract_feature_vectors.py:
        - *$ python3 pre_processing/extract_feature_vectors.py ../res/xerces2-j/src*
        - Outcome: for each god class it computes and writes to csv the respective feature vector 
2. **Clustering**
    - k_means.py/hierarchical.py:
        - *$ python3 clustering/<algorithm-type>.py <path-to-feature vector-or-folder> <number-of-clusters>*
        - Outcome: given a number it computes for each feature vector the clusters (using the given algorithm) 
        and writes the result/s to csv
    - silhouette.py:
        - 1st case (with clustering file)
            - *$ python3 clustering/silhouette.py <path-to-feature-vector-or-folder> <path-to-cluster-or-folder>*
            - Outcome: for each pair of feature vector and respective cluster, it computes the silhouette 
            score and prints it to the stdout.
        - 2st case (without clustering file)
            - *$ python3 clustering/silhouette.py <path-to-feature-vector-or-folder>*
            -  Outcome: for each feature vector it computes the silhouette metrics for both algorithms 
            with k ranging from 2 to 40
3. *Evaluation*
    - ground_truth.py:
        - *$ python3 evaluation/ground_truth.py <path-to-cluster-or-folder> <path-to-keywords.txt>*
        - Outcome: for each feature vector it computes the respective ground truth and writes it to
        a csv file.
    - prec_recall.py:
        - *$ python3 evaluation/prec_recall.py <path-to-cluster-or-folder> <path-to-ground-truth-or-folder>*
        - Outcome: for each pair of cluster and respective ground truth, it computes precision and recall and 
        prints it to the stdout.
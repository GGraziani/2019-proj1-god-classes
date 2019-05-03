# How to run
1. **Pre-processing**
    - find_god_classes.py:
        - ```$ python3 god_classes.py find_god_classes -s <path-to-source>```
        - Outcome: prints to the stdout a dataframe containing god classes name and number of methods  
    - extract_feature_vectors.py:
        - ```$ python3 god_classes.py extract_feature_vectors -s <path-to-source>```
        - Outcome: for each god class it computes and writes to csv the respective feature vector 
2. **Clustering**
    - k_means.py/hierarchical.py:
        - ```$ python3 god_classes.py {hierarchical,k_means} <path-to-feature_vector-or-folder> <n°-of-clusters>```
        - Outcome: given a number it computes for each feature vector the clusters (using the given algorithm) 
        and writes the result/s to csv
    - silhouette.py:
        - 1st case (with clustering file)
            - ```$ python3 god_classes.py silhouette -fv <path-to-feature-vector-or-folder> -cl <path-to-cluster-or-folder>```
            - Outcome: for each pair of feature vector and respective cluster, it computes the silhouette 
            score and prints it to the stdout.
        - 2st case (without clustering file)
            - ```$ python3 god_classes.py silhouette -fv <path-to-feature-vector-or-folder> -n <number-of-clusters>```
            - Outcome: for each feature vector it computes the silhouette metrics for both algorithms 
            with k ranging from 2 to n (default n=40)
3. **Evaluation**
    - ground_truth.py:
        - ```$ python3 god_classes.py ground_truth -fv <path-to-feature_vector-or-folder> -k <path-to-keywords>```
        - Outcome: for each feature vector it computes the respective ground truth and writes it to
        a csv file.
    - prec_recall.py:
        - ```$ python3 god_classes.py prec_recall -cl <path-to-cluster-or-folder> -gt <path-to-ground-truth-or-folder>```
        - Outcome: for each pair of cluster and respective ground truth, it computes precision and recall and 
        prints it to the stdout.

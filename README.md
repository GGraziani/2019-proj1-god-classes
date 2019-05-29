## Project 1 - God Classes

### Documentation
 
For the general documentation run:

    python3 god_classes.py

For details about each command and instruction on "how to run", run:

    python3 god_classes.py <command>
    
To launch the whole analysis at once run:
    
    python3 god_classes.py run_all -s <path-to-src> -a <algorithm-name> (i.e. k-means or hierarchical)

### Examples usage:
The following are some example of commands:
1. **Pre-processing**
    - find_god_classes:
        - ```$ python3 god_classes.py find_god_classes -s ../res/xerces2-j/src```
    - extract_feature_vectors:
        - ```$ python3 god_classes.py extract_feature_vectors -s ../res/xerces2-j/src```
2. **Clustering**
    - k_means.py/hierarchical:
        - ```$ python3 god_classes.py clustering -a k-means -fv res/feature_vectors/1559157308733 -n 10``` or 
        - ```$ python3 god_classes.py clustering -a hierarchical -fv res/feature_vectors/1559157308733 -n 10```
    - silhouette.py:
        - 1st case (with clustering file)
            - ```$ python3 god_classes.py silhouette -fv res/feature_vectors/1559157308733 -cl res/clusters/k-means-1559157521766```
        - 2st case (without clustering file)
            - ```$ python3 god_classes.py silhouette -fv res/feature_vectors/1559157308733 -n 10```
3. **Evaluation**
    - ground_truth.py:
        - ```$ python3 god_classes.py ground_truth -fv res/feature_vectors/1559157308733 -k res/keywords.txt```
    - prec_recall.py:
        - ```$ python3 god_classes.py prec_recall -cl res/clusters/k-means-1559157521766 -gt res/ground_truths/1559157739490```

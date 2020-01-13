#import scipy.cluster.hierarchy as shc
from sklearn.cluster import DBSCAN
import numpy as np

"""
    Author : Alen Struklec
    Perform DBSCAN to cluster data
"""
class DBSCANClustering():
    def __init__(self):
        self.algorithm = DBSCAN(eps=0.05, min_samples=10, metric="precomputed")

    """
        Fit data to clustering algorithm
    """
    def fit(self, distance_matrix):
        self.cluster = self.algorithm.fit(distance_matrix)

    """
        Calculate centroids from data after DBSCAN clustering
    """
    def centorids(self, data, distance_matrix):
        #Create cluster dictionary based on data labels after clusting
        cluster_dict = {}
        for i in range(len(self.cluster.labels_)):
            label = self.cluster.labels_[i]
            if label not in cluster_dict:
                cluster_dict[label] = []
            cluster_dict[label].append((i,data[i]))

        #Calculate centroids
        centorids = []
        for label in cluster_dict:
            if label == -1: #Skip noisy data
                continue
            cluster = cluster_dict[label]
            print(f"Cluster {label}, length: {len(cluster)}")
            #Generate distance matrix between cluster data 
            distances = []
            for b, i in enumerate(cluster):
                distances.append([])
                for j in cluster:
                    x = i[0]
                    y = j[0]
                    distances[b].append(distance_matrix[x][y])

            distances = np.asarray(distances)
            index = distances.sum(axis=1).argmin() #Center is at minimum distance 
            centorids.append(cluster[index][1])
        return centorids
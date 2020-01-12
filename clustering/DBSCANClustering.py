#import scipy.cluster.hierarchy as shc
from sklearn.cluster import DBSCAN
import numpy as np

class DBSCANClustering():
    def __init__(self):
        self.algorithm = DBSCAN(eps=0.05, min_samples=10, metric="precomputed")

    def fit(self, distance_matrix):
        self.cluster = self.algorithm.fit(distance_matrix)

    def centorids(self, data, distance_matrix):
        cluster_dict = {}
        for i in range(len(self.cluster.labels_)):
            label = self.cluster.labels_[i]
            if label not in cluster_dict:
                cluster_dict[label] = []
            cluster_dict[label].append((i,data[i]))

        beta = 1
        centorids = []
        for label in cluster_dict:
            if label == -1:
                continue
            cluster = cluster_dict[label]
            print(f"Cluster {label}, length: {len(cluster)}")
            distances = []
            for b, i in enumerate(cluster):
                distances.append([])
                for j in cluster:
                    x = i[0]
                    y = j[0]
                    distances[b].append(distance_matrix[x][y])

            distances = np.asarray(distances)
            index = distances.sum(axis=1).argmin()
            centorids.append(cluster[index][1])
        return centorids
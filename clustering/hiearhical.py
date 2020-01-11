#import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
import numpy as np

class HierarchicalClustering():
    def __init__(self):
        self.algorithm = AgglomerativeClustering(n_clusters=3, affinity='precomputed', linkage='single')

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
            index = np.exp(-beta*distances / (distances.std() + 0.00000001)).sum(axis=1).argmax()
            centorids.append(cluster[index][1])
        return centorids

    def get_labels(self):
        return self.cluster.labels_
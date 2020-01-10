#import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

class HierarchicalClustering():
    def __init__(self):
        self.algorithm = AgglomerativeClustering(n_clusters=3, affinity='precomputed', linkage='single')

    def fit(self, distance_matrix):
        self.cluster = self.algorithm.fit(distance_matrix)

    def get_labels(self):
        return self.cluster.labels_
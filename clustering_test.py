import pickle
import numpy as np
from clustering import hiearhical
from sklearn.preprocessing import normalize
import time
import sys
import file_handler as fh
from sklearn.preprocessing import MinMaxScaler

input_file = sys.argv[1]
data_fasta = fh.read(input_file)

alg = hiearhical.HierarchicalClustering()

filename = "matrix.pickle"
with open(filename, 'rb') as handle:
    data = pickle.load(handle)['matrix']

#data = np.asarray(data)
print(data.shape)
print(data)
max_el = data.max()
data = np.array([i/max_el for i in data])

#data = data / np.linalg.norm(data)
data = 1/data

data = - np.log(data)
data = abs(data)
#min_max_scaler = MinMaxScaler()
#data = min_max_scaler.fit_transform(data)
print(data)

start = time.time()
alg.fit(data)
end = time.time()
print(f"time: {(end-start)/1000} ms")

start = time.time()
centorids = alg.centorids(data_fasta, data)
end = time.time()
print(f"time: {(end-start)/1000} ms")

print(centorids)
import pickle
import numpy as np
from clustering import DBSCANClustering
from sklearn.preprocessing import normalize
import time
import sys
import file_handler as fh
from sklearn.preprocessing import MinMaxScaler

input_file = sys.argv[1]
data_fasta = fh.read(input_file)

hist = {}
for d in data_fasta:
    key = len(d['seq'])
    if key not in hist:
        hist[key] = []
    hist[key].append(d)

p = {}
for key in hist:
    p[key] = len(hist[key])

sorted_hist = sorted(p.items(), key = 
             lambda kv:(kv[1], kv[0]))
max_len = sorted_hist[-1][0]

data_extrude = [p[0] for p in sorted_hist if abs(p[0]-max_len) <= 5]
data_fasta = []
for i in data_extrude:
    d = hist[i]
    for e in d:
        data_fasta.append(e)



alg = DBSCANClustering.DBSCANClustering()

filename = "matrix_"+input_file.split('\\')[-1].split('.')[0]+".pickle"
with open(filename, 'rb') as handle:
    data = pickle.load(handle)['matrix']

#data = np.asarray(data)
print(data.shape)
print(data)
max_el = data.max()
#data = np.array([i/max_el for i in data])

#data = abs(data)
#data = data / np.linalg.norm(data)
#data = 1/data

##data = - np.log(data)

min_max_scaler = MinMaxScaler()
data = min_max_scaler.fit_transform(data)
data = 1-data
print(data)

start = time.time()
alg.fit(data)
end = time.time()
print(f"time: {(end-start)/1000} ms")

start = time.time()
centorids = alg.centorids(data_fasta, data)
end = time.time()
print(f"time: {(end-start)/1000} ms")

#centorids = [x[0]['seq'] for x in centorids]
print(centorids)
print(f"Number of clusters: {len(centorids)}")
for c in centorids:
    print(f"Consensus ({len(c['seq'])})\n{c['seq']}\n")
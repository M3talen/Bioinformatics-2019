import file_handler as fh 
from clustering import DBSCANClustering
import alignment

import time
import sys
import numpy as np
import itertools
import pickle
from tqdm import tqdm
from sklearn.preprocessing import MinMaxScaler

input_file = sys.argv[1]
data = fh.read(input_file)
print(f"data length: {len(data)}")

start = time.time()
hist = {}
for d in data:
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
data = []
for i in data_extrude:
    d = hist[i]
    for e in d:
        data.append(e)

end = time.time()
print(f'Execution time (hist): {(end - start)} s')
print(f"data length(after): {len(data)}")

N = len(data)
distance_matrix = []
for i in range(len(data[0:N])):
    distance_matrix.append([None] * N)

start = time.time()
for i,j in tqdm(itertools.product(range(len(data[0:N])), range(len(data[0:N]))), total=N*N):
    if(distance_matrix[j][i] != None):
        distance_matrix[i][j] = distance_matrix[j][i]
    else:
        score = alignment.py_global(str.encode(data[i]['seq']), str.encode(data[j]['seq']))
        distance_matrix[i][j] = score

end = time.time()
print(f'Execution time (distance matrix): {(end - start)} s')

distance_matrix = np.array(distance_matrix)
distance_matrix = MinMaxScaler().fit_transform(distance_matrix)
distance_matrix = 1 - distance_matrix
for i,j in itertools.product(range(len(data[0:N])), range(len(data[0:N]))):
    if(abs(distance_matrix[i][j]) < 0.000000001):
        distance_matrix[i][j] = 0



print(f"shape: ({len(distance_matrix)},{len(distance_matrix[0])})")

clustering = DBSCANClustering.DBSCANClustering()
start = time.time()
clustering.fit(distance_matrix)
end = time.time()
print(f'Execution time (cluster fit): {(end - start)} s')

centorids = clustering.centorids(data, distance_matrix)
print(f"Number of clusters: {len(centorids)}")
for c in centorids:
    print(f"Consensus ({len(c['seq'])})\n{c['seq']}\n")

fh.write(centorids, 'output.fasta')
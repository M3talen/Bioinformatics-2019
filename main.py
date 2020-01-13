"""
        Authors : Zvonimir Kučiš, Zlatko Verk, Alen Štruklec
"""
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

# Load FASTA/FASTQ data 
input_file = sys.argv[1]
data = fh.read(input_file)
print(f"Data length: {len(data)}")

# Data cleanup
hist = {}
for d in data:
    key = len(d['seq'])
    if key not in hist:
        hist[key] = []
    hist[key].append(d)

p = {}
for key in hist:
    p[key] = len(hist[key])

sorted_hist = sorted(p.items(), key = lambda kv:(kv[1], kv[0]))
max_len = sorted_hist[-1][0]

data_extrude = [p[0] for p in sorted_hist if abs(p[0]-max_len) <= 5] # Add only data whose lenght is +/-5 from most freaquent data lenght
data = []
for i in data_extrude:
    d = hist[i]
    for e in d:
        data.append(e)
print(f"Data length(after): {len(data)}")

#Initialize similarity matrix
N = len(data)
similarity_matrix = []
for i in range(len(data[0:N])):
    similarity_matrix.append([None] * N)

#Calculate similarity matrix
for i,j in tqdm(itertools.product(range(len(data[0:N])), range(len(data[0:N]))), total=N*N):
    if(similarity_matrix[j][i] != None):
        similarity_matrix[i][j] = similarity_matrix[j][i]
    else:
        score = alignment.py_global(str.encode(data[i]['seq']), str.encode(data[j]['seq']))
        similarity_matrix[i][j] = score

#Transform similarity matrix to distance matrix
distance_matrix = np.array(similarity_matrix)
distance_matrix = MinMaxScaler().fit_transform(distance_matrix)
distance_matrix = 1 - distance_matrix
#Set all small distances to zero
for i,j in itertools.product(range(len(data[0:N])), range(len(data[0:N]))):
    if(abs(distance_matrix[i][j]) < 0.000000001):
        distance_matrix[i][j] = 0

#Cluster data
clustering = DBSCANClustering.DBSCANClustering()
clustering.fit(distance_matrix)

#Calculate centroids
centorids = clustering.centorids(data, distance_matrix)

print(f"Number of clusters: {len(centorids)}")
for c in centorids:
    print(f"Consensus ({len(c['seq'])})\n{c['seq']}\n")

#Save to file
fh.write(centorids, 'output.fasta')
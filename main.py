import file_handler as fh 
#from algorithms import global_aligment as globalAlg
from clustering import hiearhical

import time
import sys
import numpy as np
import itertools
import alignment
import pickle

input_file = sys.argv[1]


data = fh.read(input_file)
#alg = globalAlg.NeedlemanWunsch()
print(f"data length: {len(data)}")

N = len(data)
distance_matrix = []
for i in range(len(data[0:N])):
    distance_matrix.append([None] * N)

start = time.time()
for i,j in itertools.product(range(len(data[0:N])), range(len(data[0:N]))):
    if(distance_matrix[j][i] != None):
        distance_matrix[i][j] = distance_matrix[j][i]
    else:
        score = alignment.py_local(str.encode(data[i]['seq']), str.encode(data[j]['seq']))
        distance_matrix[i][j] = score
#for i, seqA in enumerate(data[0:N]):
#    for j, seqB in enumerate(data[0:N]):
#        if(distance_matrix[j][i] != None):
#            distance_matrix[i][j] = distance_matrix[j][i]
#        else:
#            score = alg.run(seqA['seq'], seqB['seq'])
#            distance_matrix[i][j] = score
end = time.time()
print(f'Execution time (distance matrix): {(end - start)} s')

#print('\nDistance matrix:')
#for i in range(len(distance_matrix)):
#    print('\t[', end = '')
#    for j in range(len(distance_matrix[i])):
#        d = distance_matrix[i][j]
#        if(d == None):
#            d = 0
#        print("%5d"%(d), end = '')
#    print(']')

distance_matrix = np.array(distance_matrix)
filename = "matrix.pickle"
#with open(filename, 'wb') as handle:
#    pickle.dump({'matrix' : distance_matrix}, handle, protocol=pickle.HIGHEST_PROTOCOL)

print(f"shape: ({len(distance_matrix)},{len(distance_matrix[0])})")

clustering = hiearhical.HierarchicalClustering()
start = time.time()
clustering.fit(distance_matrix)
end = time.time()
print(f'Execution time (cluster fit): {(end - start)} s')
#print(clustering.get_labels())
cluster_labels = clustering.get_labels()

start = time.time()
cluster_dict = {}
for i in range(len(cluster_labels)):
    label = cluster_labels[i]
    if label not in cluster_dict:
        cluster_dict[label] = []
    cluster_dict[label].append((i,data[i]))
end = time.time()
print(f'Execution time (grouping clusters): {(end - start)} s')
#print(cluster_dict)
beta = 1
centorids = []
start = time.time()
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
end = time.time()
print(f'Execution time (calcualting centorids): {(end - start)} s')
print("\nCentroids:")
print(centorids)

fh.write(centorids, 'output.fasta')
import file_handler as fh 
from algorithms import global_aligment as globalAlg

import time
import sys

input_file = sys.argv[1]


data = fh.read(input_file)
alg = globalAlg.NeedlemanWunsch()
print(f"data length: {len(data)}")

N = 50
distance_matrix = []
for i in range(len(data[0:N])):
    distance_matrix.append([None] * N)

start = time.time()
for i, seqA in enumerate(data[0:N]):
    for j, seqB in enumerate(data[0:N]):
        if(distance_matrix[j][i] != None):
            distance_matrix[i][j] = distance_matrix[j][i]
        else:
            score = alg.run(seqA['seq'], seqB['seq'])
            distance_matrix[i][j] = score
end = time.time()
print(f'Execution time: {(end - start)} s')

print('\nDistance matrix:')
for i in range(len(distance_matrix)):
    print('\t[', end = '')
    for j in range(len(distance_matrix[i])):
        d = distance_matrix[i][j]
        if(d == None):
            d = 0
        print("%5d"%(d), end = '')
    print(']')

print(f"shape: ({len(distance_matrix)},{len(distance_matrix[0])})")
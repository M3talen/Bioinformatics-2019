import file_handler as fh 
from algorithms import global_aligment as globalAlg

import time
import sys

input_file = sys.argv[1]

data = fh.read(input_file)
alg = globalAlg.NeedlemanWunsch()
print(len(data))
distance_matrix = []

start = time.time()
for i, seqA in enumerate(data[0:40]):
    distance_matrix.append([])
    for seqB in data[0:40]:
        score = alg.run(seqA['seq'], seqB['seq'])
        distance_matrix[i].append(score)
end = time.time()
print(f'Execution time: {(end - start)} s')

print('\nDistance matrix:')
for i in range(len(distance_matrix)):
    #print('\n')
    print('\t[', end = '')
    for j in range(len(distance_matrix)):
        d = distance_matrix[i][j]
        print("%5d"%(d), end = '')
    print(']')


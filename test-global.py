import file_handler as fh 
from algorithms import global_aligment as globalAlg

import time
import sys

input_file = sys.argv[1]

data = fh.read(input_file)
alg = globalAlg.NeedlemanWunsch()

start = time.time()
for i, seqA in enumerate(data[0:40]):
    for seqB in data[i+1:40]:
        _ = alg.run(seqA['seq'], seqB['seq'])
end = time.time()
print(f'Execution time: {(end - start)} s')
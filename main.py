import file_handler as fh 
from algorithms import local_aligment as local

import time
import sys

input_file = sys.argv[1]

data = fh.read(input_file)

alg = local.SmithWaterman(2, -1, -2)

start = time.time()
for seqA in data:
    for seqB in data[::-1]:
        _ = alg.score(seqA['seq'], seqB['seq'])
end = time.time()
print(f'Execution time: {(end - start)} s')
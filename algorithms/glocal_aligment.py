import time
from local_aligment import SmithWaterman

seqA = 'GAGATACATCTATAACCGGGAAGAGTACGTG'
seqB = 'CGCTTCGACAGCGACTGGGGCGAGTACCGGGCGGTGACAGAGCTGGGGC'
alg = SmithWaterman(2, -1, -2)

start = time.time()
score = alg.score(seqA, seqB, 'glocal')
end = time.time()
print(f'Aligment time: {(end - start) * 1000} ms')
print(score)

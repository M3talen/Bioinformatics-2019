#Smith-Waterman algorithm
# author zkucis
import itertools
import numpy as np 

class SmithWaterman():
    def __init__(self, match, insert, delete):
        self.match = match
        self.insert = insert
        self.delete = delete

    def score(self, seqA, seqB, alignment='local'):
        if(len(seqA) > len(seqB)):
            seqB, seqA = seqA, seqB
        H = np.zeros((len(seqA) + 1, len(seqB) + 1), np.int)

        for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):
            match = H[i - 1, j - 1] + (self.match if seqA[i - 1] == seqB[j - 1] else - self.match)
            delete = H[i - 1, j] + self.delete
            insert = H[i, j - 1] + self.insert
            H[i, j] = max(match, delete, insert, 0) if alignment == 'local' else max(match, delete, insert)

        return H.max() if alignment == 'local' else H[len(seqA), ].max()

if __name__ == '__main__':
    import time
    seqA = 'ACTGAGAGATAGAGTCAGCTACGTCGATCGACTAGCTACGATCGACTGAGAGATAGAGTCAGCTACG'
    seqB = 'ACGCTAGCATCGATCGATCGATCGATCGATCAGTCAGCTACGATCGATCGATCGCTGCTAGCTACGATCGA'
    alg = SmithWaterman(3 , -2, -3)

    start = time.time()
    score = alg.score(seqA, seqB)
    end = time.time()
    print(f'Aligment time: {(end - start) * 1000} ms')
    print(score)